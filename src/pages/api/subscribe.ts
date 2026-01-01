// src/pages/api/subscribe.ts
import type { APIRoute } from 'astro';
import { Resend } from 'resend';

// Simple in-memory store for demo - replace with database in production
const subscribers: Set<string> = new Set();

export const POST: APIRoute = async ({ request }) => {
  try {
    const { email, source } = await request.json();

    if (!email || !email.includes('@')) {
      return new Response(JSON.stringify({ error: 'Valid email required' }), {
        status: 400,
        headers: { 'Content-Type': 'application/json' },
      });
    }

    // Check if already subscribed
    if (subscribers.has(email)) {
      return new Response(JSON.stringify({ message: 'Already subscribed' }), {
        status: 200,
        headers: { 'Content-Type': 'application/json' },
      });
    }

    // Add to subscribers
    subscribers.add(email);

    // Lazy initialization - only create client when API is called
    const apiKey = import.meta.env.RESEND_API_KEY;
    if (!apiKey) {
      return new Response(JSON.stringify({ error: 'Email service not configured' }), {
        status: 503,
        headers: { 'Content-Type': 'application/json' },
      });
    }

    const resend = new Resend(apiKey);

    // Send welcome email
    await resend.emails.send({
      from: 'Channel 47 <hello@channel47.dev>',
      to: email,
      subject: 'Welcome to Channel 47',
      html: `
        <h1>Welcome to Channel 47!</h1>
        <p>Thanks for subscribing. You'll be the first to know about new tools and content.</p>
        <p>- Channel 47</p>
      `,
    });

    return new Response(JSON.stringify({ success: true }), {
      status: 200,
      headers: { 'Content-Type': 'application/json' },
    });
  } catch {
    return new Response(JSON.stringify({ error: 'Subscription failed' }), {
      status: 500,
      headers: { 'Content-Type': 'application/json' },
    });
  }
};
