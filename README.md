# Waypoint — Databricks + Claude Architect training site

A static, self-contained reader for the 12-week Databricks (Azure) Architect + Claude Certified Architect (CCA-F) training programme. No login, no backend, no build step — `index.html` is the entire site.

## Publish it on GitHub Pages (~5 minutes, no installs)

1. Go to **github.com** → **+** (top right) → **New repository**. Name it anything (e.g. `architect-training`). Keep it **Public** (Pages needs a public repo on a free account). Don't add a README/gitignore — leave it empty. Create it.
2. On the new repo's page, click **uploading an existing file**.
3. Drag in `index.html` and `.nojekyll` from this folder (yes, the dot-file too — show hidden files in your file explorer if you don't see it). Commit.
4. Go to **Settings** → **Pages** (left sidebar). Under **Build and deployment**, set **Source** to **Deploy from a branch**, branch **main**, folder **/ (root)**. Save.
5. Wait ~1 minute, then refresh that Settings → Pages screen — it'll show your live URL: `https://<your-username>.github.io/<repo-name>/`.

That URL works from anywhere, on any account, with no Claude login — including your office machine.

## Updating it later

If the course content changes, regenerate with:

```bash
python build_site.py
```

(reads from `../architect-certs-12week/`, writes a fresh `index.html`), then re-upload that one file to the same repo (**Add file → Upload files** on the repo page) and commit — Pages redeploys automatically in about a minute.

## What's in here

- `index.html` — the whole site (~1 MB, all 85 course files embedded)
- `build_site.py` — regenerates `index.html` from the course markdown
- `.nojekyll` — tells GitHub Pages to serve the file as-is, no Jekyll processing
