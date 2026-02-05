# channel47.dev — Site Brief

## Positioning

**One-liner:** Media buyer building an open-source AI agent to manage Google Ads autonomously. Documenting the whole thing.

**Voice:** Jackson. First person. Direct, honest, non-corporate. A builder showing his work — not a brand performing authority.

---

## Site Structure

### `/` — Home (Landing Page)

Single page. No nav bar clutter. Just the essentials:

1. **Headline + sub-line.** The positioning statement. Who you are, what you're building, why someone should care.
2. **"What I'm building" block.** 2-3 sentences max on the always-on Google Ads agent — open source, built in public, designed to learn and self-improve over time. Update this as the project evolves.
3. **Email capture.** One field, one button. "Follow the build" or similar. Pipe to Substack or a lightweight provider (Buttondown, ConvertKit). This is the primary CTA.
4. **Link row.** Icons/text links to:
   - X (real-time updates)
   - Substack (long-form writing)
   - GitHub (open-source repo, once live)
   - LinkedIn (optional, lower priority)
5. **Footer.** Minimal. Name, year, maybe a one-liner.

No blog on the site itself. No portfolio. No "about" page. Substack handles long-form. X handles short-form. This page is a funnel, not a destination.

### `/skills` — Workshop Landing Page

Purpose: CTA page for Vibe Marketers workshop attendees.

1. **Brief intro.** What skills are, why they matter, one sentence.
2. **Skill cards.** 3-5 featured skills with name, short description, and "Add to Claude" install button/link.
3. **Link to Vibe Marketers / School community.** Secondary CTA — include it, don't feature it.
4. **Email capture.** Same list as homepage. "Want more skills like these?"

This page can evolve into a broader skills directory post-workshop, or be archived. Keep it modular.

---

## Design Direction

- **Aesthetic:** Clean, utilitarian, slightly editorial. Think personal site of someone who builds things — not a SaaS landing page. Monospaced or semi-monospaced type for headings. Readable serif or clean sans for body.
- **Color:** Dark background preferred (you're a builder, not a lifestyle brand). One accent color for CTAs and links.
- **Layout:** Single column, generous whitespace, no grid tricks. Content-first. Mobile-native.
- **Motion:** Minimal. A subtle fade-in on load is fine. Nothing that delays the reader from getting to the point.
- **No stock images, no AI-generated hero art.** If there's a visual, it's a screenshot of real work — the agent output, a terminal, the Gamma deck.

---

## Technical Approach

Keep it dead simple. Options ranked by speed-to-ship:

1. **Static HTML/CSS + deployed via Vercel or Netlify.** Fastest. One file. Push to GitHub, auto-deploys. Email capture via embedded Substack form or third-party.
2. **Astro or Next.js static site.** Slightly more structure if you want `/skills` as a proper route. Still deploys to Vercel in minutes.
3. **Framer or Carrd.** No-code fallback if you want to get it live in 30 minutes and don't care about owning the code.

Domain: channel47.dev (already owned). Point DNS to whatever hosts it.

---

## Content Needed Before Launch

- [ ] Headline + sub-line (final copy)
- [ ] "What I'm building" paragraph (2-3 sentences)
- [ ] Email capture integration (Substack embed or equivalent)
- [ ] Social links (X, Substack, GitHub URLs)
- [ ] Skills page content: 3-5 skill names, descriptions, install links

---

## Timeline

- **Wed 2/5:** Homepage live with positioning, email capture, social links
- **Thu 2/6 (before workshop):** `/skills` page live with install links
- **Fri 2/7:** Post-workshop — publish workshop recap on Substack, link from site

---

## What This Is Not

This is not a portfolio. Not a blog. Not a SaaS marketing site. It's a signpost that says "here's who I am, here's what I'm building, here's how to follow along." Everything else lives on the platforms where people already are. The site just ties them together and captures emails from people who want to stay close.
