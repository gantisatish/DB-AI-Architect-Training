# Waypoint — Databricks + Claude Architect training site

A static, self-contained reader for the 12-week Databricks (Azure) Architect + Claude Certified Architect (CCA-F) training programme. No login, no backend, no build step — `index.html` is the entire site.

## 🔗 Live site

**https://gantisatish.github.io/DB-AI-Architect-Training/**

Works from anywhere, on any account, with no Claude login — including your office machine. Bookmark it.

## Updating it later

If the course content changes, regenerate and push:

```bash
python build_site.py     # reads ../architect-certs-12week/, writes a fresh index.html
git add index.html
git commit -m "Update course content"
git push
```

Pages redeploys automatically in about a minute — refresh the live link above once it's done.

<details>
<summary>First-time setup steps (already done for this repo — kept here for reference)</summary>

1. Create a new **public** GitHub repo.
2. Upload `index.html` and `.nojekyll` (the dot-file too — show hidden files in your file explorer if you don't see it).
3. **Settings → Pages** → Source: **Deploy from a branch**, branch **main**, folder **/ (root)**. Save.
4. Wait ~1 minute — the live URL appears on that same Settings → Pages screen.

</details>

## What's in here

- `index.html` — the whole site (~1 MB, all 85 course files embedded)
- `build_site.py` — regenerates `index.html` from the course markdown
- `.nojekyll` — tells GitHub Pages to serve the file as-is, no Jekyll processing
