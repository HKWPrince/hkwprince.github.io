# Portfolio — CLAUDE.md

Personal portfolio site for **Huang Kuo-Wei**, hosted on GitHub Pages.
Single-page, no build step, no framework — pure HTML + CSS + JS.

---

## File structure

```
myWeb/
├── index.html   — all markup; edit content here
├── styles.css   — design tokens, layout, components, dark mode
├── script.js    — theme, navbar, scroll-fade, panel toggle, photo upload, form
├── resume.pdf   — drop your PDF here (not committed; add to .gitignore)
└── CLAUDE.md    — this file
```

---

## Before publishing — three TODOs

| What | Where | Value to set |
|---|---|---|
| LinkedIn URL | `index.html` → search `your-profile` (3 places) | Your real LinkedIn URL |
| Formspree ID | `index.html` → `<form action=…>` | Sign up at formspree.io → replace `yourFormId` |
| Resume PDF | Drop `resume.pdf` in this folder | Your actual PDF file |

Until Formspree is configured the contact form falls back to `mailto:` automatically (handled in `script.js`).

---

## Design system

**Fonts** (loaded from Google Fonts CDN):
- `--font-display`: Newsreader — editorial serif, used for h1/h2/project titles
- `--font-sans`:    Inter — body text, nav, buttons, labels
- `--font-mono`:    JetBrains Mono — tags, terminal, timestamps, code

**Key color tokens** (defined in `:root` in `styles.css`):
- `--accent` / `--accent-press`: rose pink `#d77a9b` / `#ba5d7e`
- `--bg-page` / `--bg-soft`: cream `#faf9f5` / warm off-white `#f5f0e8`
- `--surface-card`: `#efe9de` (light) · `#252320` (dark)
- `--text-heading/body/muted/faint`: four ink weights

Dark mode is toggled by adding `data-theme="dark"` to `<html>`. The override block is in `styles.css` under `[data-theme="dark"]`. Theme preference is persisted in `localStorage` under key `myweb-theme`.

---

## Scroll-fade (progressive enhancement)

Sections below the fold use class `.sf` for a fade-up-on-scroll effect.

- `html.ready .sf` — hides elements *only* after JS confirms it loaded (inline `<script>` in `<head>` sets `html.ready`). If JS is blocked, all content stays visible.
- `.sf.on` — reveals the element (added by `IntersectionObserver` in `script.js`).
- Observer uses `{ threshold: 0, rootMargin: '0px 0px 80px 0px' }` — fires 80 px before the element enters the viewport.

Hero columns (`.hero-l`, `.hero-r`) use a direct CSS `@keyframes fadeUp` so they animate even without JS.

---

## Right-side hero panel toggle

The right column of the hero has two faces stacked in the same CSS grid cell:

| ID | Default | Description |
|---|---|---|
| `#rp-terminal` | visible | Dark terminal mockup |
| `#rp-photo-panel` | hidden | Photo upload area |

Toggle is controlled by `#btn-terminal` / `#btn-photo` pill buttons.
`switchRightPanel(which)` in `script.js` flips the `.active` class.

---

## Photo upload

Both photo slots (left circle `#photo-slot` + right panel `#photo-slot-lg`) trigger the same hidden `<input type="file" id="photo-file">`. Uploading via either slot updates both through the shared `setPhoto(src)` function. The data-URL is persisted in `localStorage` under `myweb-photo` and restored on page load.

---

## Adding / editing content

- **Work experience** — `index.html`, inside `<div class="tl">`. Copy a `.tl-row.sf` block.
- **Projects** — `index.html`, inside `<div class="proj-grid">`. Copy a `.proj-card` block; use `.proj-card-plain` for cards with embedded media (no hover lift).
- **Skills** — `index.html`, inside `<div class="toolbox">`. Copy a `.skill-row` block.
- **Education** — `index.html`, inside `<div class="edu-grid">`. Copy a `.edu-card` block.

---

## Deployment (GitHub Pages)

1. Create a repo named `<username>.github.io` (or any repo with Pages enabled).
2. Push this folder's contents to `main` (or configure the Pages source branch).
3. Drop `resume.pdf` in the root before pushing (or after — it won't 404 during build).
4. GitHub Pages serves `index.html` automatically at the root.

No `package.json`, no build pipeline, no Jekyll — just static files.

---

## Common tasks for Claude

- **Add a new job**: copy a `.tl-row.sf` block in `index.html`; dates, company, role, bullets, and tags are all plain HTML.
- **Change accent color**: update `--accent` and `--accent-press` in the `:root` block of `styles.css` (two values; search for `d77a9b`).
- **Add a section**: create a `<section id="…">` in `index.html`, add a nav link in both `.nav-links` and `.mob-menu`, and add a `scroll-margin-top: 80px` rule in `styles.css`.
- **Embed a new video**: use the `.video-wrap` + `<iframe>` pattern from the Face8uy card. Set `loading="lazy"` on the iframe.
