# Aayan Cotton Industries — Company Website

**[Live demo →](https://aayansheraz.github.io/aayan-cotton/)**

![Aayan Cotton Industries screenshot](.github/screenshot.png)

Marketing website for Aayan Cotton Industries (Okara, Punjab, Pakistan) — a manufacturer of medical/surgical cotton products (gauze, bandages, scrub suits, patient gowns, and related items).

Static HTML site, no build step required.

## Run locally

Just open `index.html` in a browser, or serve the folder with any static server, e.g.:

```bash
npx serve .
```

## Structure

- `index.html` — the entire site (single-page).
- `media/` — product photos, certification logos, and promotional videos.
- `.htaccess` — Apache caching/compression config (for Apache-based hosting).
- `_headers` — security headers and cache rules (for Netlify/Cloudflare Pages-style static hosts).

## Deploying

The whole site is static files, so it can be hosted on any static host (Netlify, Cloudflare Pages, GitHub Pages, or traditional shared hosting via `.htaccess`).
