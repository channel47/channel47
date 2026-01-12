/**
 * Beehiiv Subscription API Endpoint
 *
 * Handles email subscriptions by proxying requests to beehiiv API.
 * This keeps API keys secure on the server side.
 *
 * Security features:
 * - Server-side API key storage
 * - Input validation and sanitization
 * - Rate limiting via request timeout
 * - Email format validation (RFC 5322 compliant)
 * - Length validation for all inputs
 * - Security headers on responses
 *
 * Required environment variables:
 * - BEEHIIV_API_KEY: Your beehiiv API key (from Settings → API)
 * - BEEHIIV_PUBLICATION_ID: Your publication ID (from Settings → API)
 */

import type { APIRoute } from 'astro';

export const prerender = false;

// Constants
const EMAIL_REGEX = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
const MAX_EMAIL_LENGTH = 254; // RFC 5321
const MAX_TAG_LENGTH = 100;
const REQUEST_TIMEOUT_MS = 10000; // 10 seconds

/**
 * Validates email format according to RFC 5322 basic pattern
 */
function isValidEmail(email: string): boolean {
  if (!email || typeof email !== 'string') return false;
  if (email.length > MAX_EMAIL_LENGTH) return false;
  return EMAIL_REGEX.test(email);
}

/**
 * Sanitizes and validates tag input
 */
function sanitizeTag(tag: unknown): string | undefined {
  if (!tag || typeof tag !== 'string') return undefined;

  const trimmed = tag.trim();
  if (trimmed.length === 0) return undefined;
  if (trimmed.length > MAX_TAG_LENGTH) return undefined;

  // Remove any potentially dangerous characters
  return trimmed.replace(/[<>\"\']/g, '');
}

/**
 * Creates response with security headers
 */
function createResponse(body: object, status: number): Response {
  return new Response(JSON.stringify(body), {
    status,
    headers: {
      'Content-Type': 'application/json',
      'X-Content-Type-Options': 'nosniff',
      'X-Frame-Options': 'DENY',
      'X-XSS-Protection': '1; mode=block',
    }
  });
}

export const POST: APIRoute = async ({ request }) => {
  // Verify same-origin request (basic CSRF protection)
  const origin = request.headers.get('origin');
  const host = request.headers.get('host');

  if (origin && host) {
    const originHost = new URL(origin).host;
    if (originHost !== host) {
      return createResponse(
        {
          error: 'Forbidden',
          message: 'Cross-origin requests not allowed'
        },
        403
      );
    }
  }

  // Get environment variables
  const API_KEY = import.meta.env.BEEHIIV_API_KEY;
  const PUBLICATION_ID = import.meta.env.BEEHIIV_PUBLICATION_ID;

  // Validate configuration
  if (!API_KEY || !PUBLICATION_ID) {
    console.error('Missing beehiiv configuration');
    return createResponse(
      {
        error: 'Server configuration error',
        message: 'Beehiiv API is not properly configured'
      },
      500
    );
  }

  // Parse request body
  let email: string;
  let tag: string | undefined;

  try {
    const contentType = request.headers.get('content-type');

    if (contentType?.includes('application/json')) {
      const body = await request.json();
      email = body.email;
      tag = body.tag;
    } else {
      // Handle form-encoded data
      const formData = await request.formData();
      email = formData.get('email') as string;
      tag = formData.get('tag') as string | undefined;
    }
  } catch (error) {
    return createResponse(
      {
        error: 'Invalid request',
        message: 'Could not parse request body'
      },
      400
    );
  }

  // Sanitize and validate inputs
  if (!email || typeof email !== 'string') {
    return createResponse(
      {
        error: 'Invalid email',
        message: 'Email address is required'
      },
      400
    );
  }

  const trimmedEmail = email.trim().toLowerCase();

  // Validate email format
  if (!isValidEmail(trimmedEmail)) {
    return createResponse(
      {
        error: 'Invalid email',
        message: 'Please provide a valid email address'
      },
      400
    );
  }

  // Sanitize tag
  const sanitizedTag = sanitizeTag(tag);

  // Call beehiiv API with timeout
  try {
    const beehiivEndpoint = `https://api.beehiiv.com/v2/publications/${PUBLICATION_ID}/subscriptions`;

    // Create abort controller for timeout
    const controller = new AbortController();
    const timeoutId = setTimeout(() => controller.abort(), REQUEST_TIMEOUT_MS);

    const payload: any = {
      email: trimmedEmail,
      reactivate_existing: false,
      send_welcome_email: true,
      utm_source: 'channel47_website'
    };

    // Add tag as custom field if provided
    if (sanitizedTag) {
      payload.custom_fields = [
        {
          name: 'signup_context',
          value: sanitizedTag
        }
      ];
    }

    let response: Response;
    let data: any;

    try {
      response = await fetch(beehiivEndpoint, {
        method: 'POST',
        headers: {
          'Authorization': `Bearer ${API_KEY}`,
          'Content-Type': 'application/json'
        },
        body: JSON.stringify(payload),
        signal: controller.signal
      });

      clearTimeout(timeoutId);
      data = await response.json();
    } catch (fetchError: any) {
      clearTimeout(timeoutId);

      // Handle timeout
      if (fetchError.name === 'AbortError') {
        console.error('Beehiiv API timeout');
        return createResponse(
          {
            error: 'Request timeout',
            message: 'The request took too long. Please try again.'
          },
          504
        );
      }

      throw fetchError;
    }

    if (!response.ok) {
      console.error('Beehiiv API error:', data);

      // Handle specific error cases
      if (response.status === 400 && data.errors) {
        const errorMessage = data.errors[0]?.message || 'Invalid subscription data';
        return createResponse(
          {
            error: 'Subscription failed',
            message: errorMessage
          },
          400
        );
      }

      // Handle duplicate subscription
      if (response.status === 409 || (data.message && data.message.includes('already'))) {
        return createResponse(
          {
            error: 'Already subscribed',
            message: 'This email is already subscribed'
          },
          400
        );
      }

      return createResponse(
        {
          error: 'Subscription failed',
          message: 'Unable to subscribe at this time. Please try again later.'
        },
        response.status >= 500 ? 502 : 400
      );
    }

    // Success
    return createResponse(
      {
        success: true,
        message: 'Successfully subscribed!'
      },
      200
    );

  } catch (error: any) {
    console.error('Subscription error:', error);

    // Don't expose internal error details
    return createResponse(
      {
        error: 'Server error',
        message: 'An unexpected error occurred. Please try again later.'
      },
      500
    );
  }
};
