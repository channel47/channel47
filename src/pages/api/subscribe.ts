// src/pages/api/subscribe.ts
import type { APIRoute } from 'astro';
import { Resend } from 'resend';

const resend = new Resend(import.meta.env.RESEND_API_KEY);

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

    console.log(`New subscriber: ${email} (source: ${source})`);

    return new Response(JSON.stringify({ success: true }), {
      status: 200,
      headers: { 'Content-Type': 'application/json' },
    });
  } catch (error) {
    console.error('Subscribe error:', error);
    return new Response(JSON.stringify({ error: 'Subscription failed' }), {
      status: 500,
      headers: { 'Content-Type': 'application/json' },
    });
  }
};
