# -*- coding: utf-8 -*-
"""
Builds a single self-contained index.html for GitHub Pages from the
architect-certs-12week course files. No Claude account, no backend,
no build step needed at serve time -- just a static file.
"""
import json
import os

SRC = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "architect-certs-12week")
OUT_DIR = os.path.dirname(os.path.abspath(__file__))

# Same metadata as the Medallion tracker, for 1:1 consistency between the two.
WEEKS = [
    {"n": 1, "title": "Lakehouse & Claude Foundations", "days": [
        {"key": "mon", "label": "Mon", "topic": "Databricks Lakehouse Platform Overview", "file": "01-mon-databricks-lakehouse-platform-overview.md", "ext": True},
        {"key": "tue", "label": "Tue", "topic": "Claude API Basics", "file": "02-tue-claude-api-basics.md"},
        {"key": "wed", "label": "Wed", "topic": "Delta Lake Fundamentals", "file": "03-wed-delta-lake-fundamentals.md"},
        {"key": "thu", "label": "Thu", "topic": "Prompt Engineering Fundamentals", "file": "04-thu-prompt-engineering-fundamentals.md"},
        {"key": "fri", "label": "Fri", "topic": "Unity Catalog Basics", "file": "05-fri-unity-catalog-basics.md"},
        {"key": "weekend", "label": "Weekend", "topic": "Map exam blueprints + build your tracker", "file": "06-weekend.md"},
    ]},
    {"n": 2, "title": "Spark Core & Agentic Concepts", "days": [
        {"key": "mon", "label": "Mon", "topic": "Spark SQL & DataFrame Fundamentals", "file": "01-mon-spark-sql-dataframe-fundamentals.md", "ext": True},
        {"key": "tue", "label": "Tue", "topic": "The Claude Agentic Loop", "file": "02-tue-the-claude-agentic-loop.md"},
        {"key": "wed", "label": "Wed", "topic": "Complex Types & User-Defined Functions", "file": "03-wed-complex-types-user-defined-functions.md"},
        {"key": "thu", "label": "Thu", "topic": "Agents vs. Workflows vs. Simple Prompting", "file": "04-thu-agents-vs-workflows-vs-simple-prompting.md"},
        {"key": "fri", "label": "Fri", "topic": "Auto Loader & Incremental Ingestion", "file": "05-fri-auto-loader-incremental-ingestion.md", "ext": True},
        {"key": "weekend", "label": "Weekend", "topic": "Topic-check quiz (Weeks 1-2)", "file": "06-weekend.md"},
    ]},
    {"n": 3, "title": "Ingestion, Transformation & MCP Basics", "days": [
        {"key": "mon", "label": "Mon", "topic": "Schema Evolution Strategies", "file": "01-mon-schema-evolution-strategies.md"},
        {"key": "tue", "label": "Tue", "topic": "Model Context Protocol (MCP) Basics", "file": "02-tue-model-context-protocol-mcp-basics.md"},
        {"key": "wed", "label": "Wed", "topic": "Silver-Layer Transformations & Data Quality", "file": "03-wed-silver-layer-transformations-data-quality.md"},
        {"key": "thu", "label": "Thu", "topic": "Connecting an MCP Server to Claude", "file": "04-thu-connecting-an-mcp-server-to-claude.md"},
        {"key": "fri", "label": "Fri", "topic": "Window Functions, Joins & Partitioning", "file": "05-fri-window-functions-joins-partitioning.md", "ext": True},
        {"key": "weekend", "label": "Weekend", "topic": "Databricks practice exam", "file": "06-weekend.md", "milestone": True},
    ]},
    {"n": 4, "title": "Orchestration & Tool Design", "days": [
        {"key": "mon", "label": "Mon", "topic": "Databricks Jobs & Workflows", "file": "01-mon-databricks-jobs-workflows.md"},
        {"key": "tue", "label": "Tue", "topic": "Tool Design Principles for Claude", "file": "02-tue-tool-design-principles-for-claude.md"},
        {"key": "wed", "label": "Wed", "topic": "Databricks Repos & CI/CD Basics", "file": "03-wed-databricks-repos-ci-cd-basics.md", "ext": True},
        {"key": "thu", "label": "Thu", "topic": "Structured Output from Claude", "file": "04-thu-structured-output-from-claude.md"},
        {"key": "fri", "label": "Fri", "topic": "Gold-Layer Aggregation & Visualization", "file": "05-fri-gold-layer-aggregation-visualization.md", "ext": True},
        {"key": "weekend", "label": "Weekend", "topic": "CCA-F practice exam (weighted review)", "file": "06-weekend.md", "milestone": True},
    ]},
    {"n": 5, "title": "Security, Governance & Multi-Tool Agents", "days": [
        {"key": "mon", "label": "Mon", "topic": "Unity Catalog Governance in Depth", "file": "01-mon-unity-catalog-governance-in-depth.md", "ext": True},
        {"key": "tue", "label": "Tue", "topic": "Chaining Multiple Tools in One Agent Run", "file": "02-tue-chaining-multiple-tools-in-one-agent-run.md"},
        {"key": "wed", "label": "Wed", "topic": "Databricks Asset Bundles: Deploying as Code", "file": "03-wed-databricks-asset-bundles-deploying-as-code.md"},
        {"key": "thu", "label": "Thu", "topic": "Error Handling & Retries in Agent Loops", "file": "04-thu-error-handling-retries-in-agent-loops.md"},
        {"key": "fri", "label": "Fri", "topic": "Full Pipeline Review", "file": "05-fri-full-pipeline-review.md"},
        {"key": "weekend", "label": "Weekend", "topic": "Databricks Data Engineer Associate exam", "file": "06-weekend.md", "milestone": True, "real": True},
    ]},
    {"n": 6, "title": "Diagnostic Checkpoint", "days": [
        {"key": "mon", "label": "Mon", "topic": "Review Databricks Milestone Results", "file": "01-mon-review-databricks-milestone-results.md"},
        {"key": "tue", "label": "Tue", "topic": "Full-Length CCA-F Practice Exam", "file": "02-tue-full-length-cca-f-practice-exam.md", "milestone": True},
        {"key": "wed", "label": "Wed", "topic": "Score Review & Domain Ranking", "file": "03-wed-score-review-domain-ranking.md"},
        {"key": "thu", "label": "Thu", "topic": "Deep-Dive: Weakest Domain #1", "file": "04-thu-deep-dive-weakest-domain-1.md"},
        {"key": "fri", "label": "Fri", "topic": "Deep-Dive: Weakest Domain #2", "file": "05-fri-deep-dive-weakest-domain-2.md"},
        {"key": "weekend", "label": "Weekend", "topic": "Build consolidated cheat-sheet", "file": "06-weekend.md"},
    ]},
    {"n": 7, "title": "Claude Certified Architect Push (Part 1)", "days": [
        {"key": "mon", "label": "Mon", "topic": "Claude Code Configuration Deep Dive", "file": "01-mon-claude-code-configuration-deep-dive.md"},
        {"key": "tue", "label": "Tue", "topic": "Claude Code Workflows in a Real Pipeline", "file": "02-tue-claude-code-workflows-in-a-real-pipeline.md"},
        {"key": "wed", "label": "Wed", "topic": "Advanced Prompting & Structured Output", "file": "03-wed-advanced-prompting-structured-output.md"},
        {"key": "thu", "label": "Thu", "topic": "Context Management Strategies", "file": "04-thu-context-management-strategies.md"},
        {"key": "fri", "label": "Fri", "topic": "Reliability & Evaluation Techniques", "file": "05-fri-reliability-evaluation-techniques.md"},
        {"key": "weekend", "label": "Weekend", "topic": "CCA-F practice exam #3", "file": "06-weekend.md", "milestone": True},
    ]},
    {"n": 8, "title": "Claude Certified Architect Push (Part 2) + Exam", "days": [
        {"key": "mon", "label": "Mon", "topic": "Targeted Review from Practice Exam #3", "file": "01-mon-targeted-review-from-practice-exam-3.md"},
        {"key": "tue", "label": "Tue", "topic": "Full Agent Project Polish", "file": "02-tue-full-agent-project-polish.md"},
        {"key": "wed", "label": "Wed", "topic": "Practice Exam #4 — Exam Conditions", "file": "03-wed-practice-exam-4-exam-conditions.md", "milestone": True},
        {"key": "thu", "label": "Thu", "topic": "Light Review Only", "file": "04-thu-light-review-only.md"},
        {"key": "fri", "label": "Fri", "topic": "Logistics & Rest", "file": "05-fri-logistics-rest.md"},
        {"key": "weekend", "label": "Weekend", "topic": "SIT THE CCA-F EXAM", "file": "06-weekend.md", "milestone": True, "real": True},
    ]},
    {"n": 9, "title": "Databricks Professional Depth", "days": [
        {"key": "mon", "label": "Mon", "topic": "Delta Lake Internals & Optimization", "file": "01-mon-delta-lake-internals-optimization.md"},
        {"key": "tue", "label": "Tue", "topic": "Change Data Capture (CDC) Patterns", "file": "02-tue-change-data-capture-cdc-patterns.md"},
        {"key": "wed", "label": "Wed", "topic": "Performance Tuning", "file": "03-wed-performance-tuning.md"},
        {"key": "thu", "label": "Thu", "topic": "Monitoring & Observability", "file": "04-thu-monitoring-observability.md", "ext": True},
        {"key": "fri", "label": "Fri", "topic": "Cost Optimization Strategies", "file": "05-fri-cost-optimization-strategies.md"},
        {"key": "weekend", "label": "Weekend", "topic": "DE Professional practice exam", "file": "06-weekend.md", "milestone": True},
    ]},
    {"n": 10, "title": "Azure Platform Architect Focus", "days": [
        {"key": "mon", "label": "Mon", "topic": "Azure Databricks Deployment Architecture", "file": "01-mon-azure-databricks-deployment-architecture.md"},
        {"key": "tue", "label": "Tue", "topic": "Networking: VNet Injection & Private Endpoints", "file": "02-tue-networking-vnet-injection-private-endpoints.md"},
        {"key": "wed", "label": "Wed", "topic": "Identity: Entra ID & Unity Catalog", "file": "03-wed-identity-entra-id-unity-catalog.md"},
        {"key": "thu", "label": "Thu", "topic": "Azure Integrations", "file": "04-thu-azure-integrations.md"},
        {"key": "fri", "label": "Fri", "topic": "Security Best Practices Review", "file": "05-fri-security-best-practices-review.md"},
        {"key": "weekend", "label": "Weekend", "topic": "SIT AZURE PLATFORM ARCHITECT ACCREDITATION", "file": "06-weekend.md", "milestone": True, "real": True},
    ]},
    {"n": 11, "title": "Integration & Final Depth", "days": [
        {"key": "mon", "label": "Mon", "topic": "Production Pipeline Design Patterns", "file": "01-mon-production-pipeline-design-patterns.md"},
        {"key": "tue", "label": "Tue", "topic": "Governance at Scale", "file": "02-tue-governance-at-scale.md"},
        {"key": "wed", "label": "Wed", "topic": "Project Polish: Professional-Level Practices", "file": "03-wed-project-polish-professional-level-practices.md", "ext": True},
        {"key": "thu", "label": "Thu", "topic": "Practice Exam #2 — Data Engineer Professional", "file": "04-thu-practice-exam-2-data-engineer-professional.md", "milestone": True},
        {"key": "fri", "label": "Fri", "topic": "Targeted Review", "file": "05-fri-targeted-review.md"},
        {"key": "weekend", "label": "Weekend", "topic": "Full mock DE Professional exam", "file": "06-weekend.md", "milestone": True},
    ]},
    {"n": 12, "title": "Final Review & Exam", "days": [
        {"key": "mon", "label": "Mon", "topic": "Final Cheat-Sheet Review", "file": "01-mon-final-cheat-sheet-review.md"},
        {"key": "tue", "label": "Tue", "topic": "Final Practice Exam", "file": "02-tue-final-practice-exam.md", "milestone": True},
        {"key": "wed", "label": "Wed", "topic": "Light Review Day", "file": "03-wed-light-review-day.md"},
        {"key": "thu", "label": "Thu", "topic": "Logistics & Rest", "file": "04-thu-logistics-rest.md"},
        {"key": "fri", "label": "Fri", "topic": "Rest", "file": "05-fri-rest.md"},
        {"key": "weekend", "label": "Weekend", "topic": "SIT DE PROFESSIONAL EXAM — Done!", "file": "06-weekend.md", "milestone": True, "real": True},
    ]},
]


def read(path):
    with open(path, "r", encoding="utf-8") as f:
        return f.read()


def build_data():
    top_readme = read(os.path.join(SRC, "README.md"))
    weeks_out = []
    for w in WEEKS:
        week_dir = os.path.join(SRC, "week-%02d" % w["n"])
        readme = read(os.path.join(week_dir, "README.md"))
        days_out = []
        for d in w["days"]:
            content = read(os.path.join(week_dir, d["file"]))
            days_out.append({
                "key": d["key"], "label": d["label"], "topic": d["topic"],
                "file": d["file"], "ext": d.get("ext", False),
                "milestone": d.get("milestone", False), "real": d.get("real", False),
                "content": content,
            })
        weeks_out.append({"n": w["n"], "title": w["title"], "readme": readme, "days": days_out})
    return {"topReadme": top_readme, "weeks": weeks_out}


TEMPLATE = r"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Waypoint — Databricks + Claude Architect Programme</title>
<meta name="description" content="Self-hosted reader for the 12-week Databricks (Azure) Architect + Claude Certified Architect training programme.">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Archivo:wght@600;700;800&family=IBM+Plex+Sans:wght@400;500;600&family=IBM+Plex+Mono:wght@400;500;600&display=swap">
<script src="https://cdnjs.cloudflare.com/ajax/libs/marked/9.1.6/marked.min.js"></script>
<style>
:root{
  --bg:#EEF2F1; --surface:#FFFFFF; --surface-2:#E4E9E7; --border:#D3DBD8;
  --ink:#1E2A2E; --muted:#5E6E72; --accent:#1F6F78; --bronze:#B5772E;
  --good:#3F7D53; --milestone:#8B3A42; --milestone-bg:#F3E4E5;
  --code-bg:#1E2A2E; --code-ink:#E7EEEC;
  --shadow:0 1px 2px rgba(15,30,32,.06), 0 4px 14px rgba(15,30,32,.05);
}
@media (prefers-color-scheme: dark){
  :root:not([data-theme="light"]){
    --bg:#111A1D; --surface:#182426; --surface-2:#20302F; --border:#2C3E3D;
    --ink:#E7EEEC; --muted:#93A5A5; --accent:#57BFC4; --bronze:#E0A45C;
    --good:#79C793; --milestone:#E38C93; --milestone-bg:#3A2226;
    --code-bg:#0C1315; --code-ink:#D9E4E2;
    --shadow:0 1px 2px rgba(0,0,0,.3), 0 6px 20px rgba(0,0,0,.35);
  }
}
:root[data-theme="dark"]{
  --bg:#111A1D; --surface:#182426; --surface-2:#20302F; --border:#2C3E3D;
  --ink:#E7EEEC; --muted:#93A5A5; --accent:#57BFC4; --bronze:#E0A45C;
  --good:#79C793; --milestone:#E38C93; --milestone-bg:#3A2226;
  --code-bg:#0C1315; --code-ink:#D9E4E2;
  --shadow:0 1px 2px rgba(0,0,0,.3), 0 6px 20px rgba(0,0,0,.35);
}
*{box-sizing:border-box;}
html{color-scheme:light dark;}
body{margin:0; background:var(--bg); color:var(--ink); font-family:'IBM Plex Sans',system-ui,sans-serif; line-height:1.6; -webkit-font-smoothing:antialiased;}
h1,h2,h3,h4{font-family:'Archivo',system-ui,sans-serif; text-wrap:balance;}
code,pre,kbd{font-family:'IBM Plex Mono',ui-monospace,monospace;}
a{color:var(--accent);}
::selection{background:var(--accent); color:#fff;}
:focus-visible{outline:2px solid var(--accent); outline-offset:2px;}
button{font-family:inherit; cursor:pointer;}

.shell{display:flex; min-height:100vh;}

/* ---- Sidebar ---- */
.sidebar{
  width:300px; flex-shrink:0; background:var(--surface); border-right:1px solid var(--border);
  height:100vh; position:sticky; top:0; overflow-y:auto; padding:18px 0 40px;
}
.sidebar-head{padding:0 16px 14px; border-bottom:1px solid var(--border); margin-bottom:8px;}
.brand{font-size:1.2rem; font-weight:800; letter-spacing:-0.01em;}
.brand-sub{font-size:.72rem; color:var(--muted); margin-top:2px;}
.theme-toggle{
  margin-top:10px; font-size:.72rem; padding:5px 10px; border-radius:999px; border:1px solid var(--border);
  background:var(--surface-2); color:var(--muted);
}
.search-box{
  margin:10px 16px 6px; padding:7px 10px; border-radius:8px; border:1px solid var(--border);
  background:var(--surface-2); color:var(--ink); font-size:.85rem; width:calc(100% - 32px);
}
.nav-week{margin-top:4px;}
.nav-week-head{
  width:100%; display:flex; align-items:center; gap:8px; padding:9px 16px; background:none; border:none;
  color:var(--ink); font-size:.86rem; font-weight:700; text-align:left;
}
.nav-week-head .wn{font-family:'IBM Plex Mono',monospace; color:var(--muted); font-size:.75rem; width:1.4em;}
.nav-week-head .chev{margin-left:auto; color:var(--muted); font-size:.7rem; transition:transform .15s;}
.nav-week.collapsed .chev{transform:rotate(-90deg);}
.nav-week.collapsed .nav-days{display:none;}
.nav-days{padding-bottom:4px;}
.nav-day{
  display:flex; align-items:center; gap:8px; padding:6px 16px 6px 40px; font-size:.82rem; color:var(--muted);
  text-decoration:none; border-left:2px solid transparent;
}
.nav-day:hover{background:var(--surface-2); color:var(--ink);}
.nav-day.active{background:var(--surface-2); color:var(--accent); border-left-color:var(--accent); font-weight:600;}
.nav-day .dlabel{font-family:'IBM Plex Mono',monospace; font-size:.68rem; width:2.6em; flex-shrink:0; opacity:.8;}
.nav-day .dot-badge{width:6px; height:6px; border-radius:50%; flex-shrink:0;}
.nav-day .dot-badge.ext{background:var(--bronze);}
.nav-day .dot-badge.milestone{background:var(--milestone);}
.nav-home{display:block; padding:8px 16px; font-size:.85rem; color:var(--ink); font-weight:600; text-decoration:none; border-bottom:1px solid var(--border); margin-bottom:4px;}
.nav-home:hover{background:var(--surface-2);}
.no-match{padding:10px 16px; font-size:.8rem; color:var(--muted); display:none;}

/* ---- Main ---- */
.main{flex:1; min-width:0;}
.topbar{
  position:sticky; top:0; z-index:5; background:var(--bg); border-bottom:1px solid var(--border);
  padding:10px 32px; display:none; align-items:center; gap:10px;
}
.topbar.show{display:flex;}
.menu-btn{background:var(--surface); border:1px solid var(--border); border-radius:8px; padding:6px 10px; color:var(--ink);}
.content-wrap{max-width:760px; margin:0 auto; padding:40px 32px 90px;}
.crumb{font-size:.78rem; color:var(--muted); margin-bottom:6px;}
.crumb a{color:var(--muted); text-decoration:none;}
.crumb a:hover{color:var(--accent);}
.doc h1{font-size:1.9rem; font-weight:800; margin:6px 0 2px; letter-spacing:-0.01em;}
.doc h2{font-size:1.4rem; font-weight:700; margin:38px 0 12px; padding-top:6px; border-top:1px solid var(--border);}
.doc h2:first-of-type{border-top:none; margin-top:18px;}
.doc h3{font-size:1.12rem; font-weight:700; margin:26px 0 10px;}
.doc h4{font-size:.98rem; font-weight:600; margin:20px 0 8px; color:var(--accent);}
.doc p{margin:0 0 14px; max-width:70ch;}
.doc ul,.doc ol{margin:0 0 14px; padding-left:1.3em; max-width:70ch;}
.doc li{margin-bottom:5px;}
.doc strong{font-weight:600;}
.doc a{text-underline-offset:2px;}
.doc code{background:var(--surface-2); padding:.15em .4em; border-radius:5px; font-size:.88em;}
.doc pre{
  background:var(--code-bg); color:var(--code-ink); padding:16px 18px; border-radius:10px;
  overflow-x:auto; margin:0 0 18px; box-shadow:var(--shadow);
}
.doc pre code{background:none; padding:0; font-size:.85rem; color:inherit; line-height:1.55;}
.doc table{border-collapse:collapse; width:100%; margin:0 0 18px; font-size:.88rem; display:block; overflow-x:auto;}
.doc th,.doc td{border:1px solid var(--border); padding:7px 11px; text-align:left;}
.doc th{background:var(--surface-2); font-weight:600;}
.doc blockquote{margin:0 0 14px; padding:2px 16px; border-left:3px solid var(--accent); color:var(--muted);}
.doc hr{border:none; border-top:1px solid var(--border); margin:32px 0;}
.doc details{
  background:var(--surface-2); border:1px solid var(--border); border-radius:10px; padding:10px 16px; margin:0 0 16px;
}
.doc details[open]{padding-bottom:14px;}
.doc summary{cursor:pointer; font-weight:600; color:var(--accent); padding:4px 0;}
.doc summary::marker{color:var(--accent);}

.day-meta{display:flex; gap:8px; margin:10px 0 22px; flex-wrap:wrap;}
.badge{font-size:.7rem; font-weight:600; padding:3px 9px; border-radius:999px;}
.badge-ext{background:var(--bronze); color:#fff;}
.badge-milestone{background:var(--milestone); color:#fff;}

.pager{display:flex; justify-content:space-between; gap:12px; margin-top:44px; padding-top:20px; border-top:1px solid var(--border);}
.pager a{
  flex:1; text-decoration:none; color:var(--ink); background:var(--surface); border:1px solid var(--border);
  border-radius:10px; padding:12px 16px; font-size:.85rem; box-shadow:var(--shadow);
}
.pager a:hover{border-color:var(--accent);}
.pager .plabel{display:block; color:var(--muted); font-size:.72rem; text-transform:uppercase; letter-spacing:.05em; margin-bottom:3px;}
.pager .pnext{text-align:right;}

.landing h1{font-size:2rem; margin-bottom:6px;}
.landing .lede{color:var(--muted); max-width:60ch; margin-bottom:26px;}
.week-grid{display:grid; grid-template-columns:repeat(auto-fill,minmax(230px,1fr)); gap:12px;}
.week-card{
  display:block; text-decoration:none; color:var(--ink); background:var(--surface); border:1px solid var(--border);
  border-radius:12px; padding:16px; box-shadow:var(--shadow);
}
.week-card:hover{border-color:var(--accent);}
.week-card .wn{font-family:'IBM Plex Mono',monospace; color:var(--muted); font-size:.75rem;}
.week-card h3{font-size:1rem; margin:4px 0 0;}

@media (max-width:880px){
  .sidebar{position:fixed; left:0; top:0; z-index:20; transform:translateX(-100%); transition:transform .2s ease; box-shadow:0 0 0 100vmax rgba(0,0,0,0); width:82vw; max-width:320px;}
  .sidebar.open{transform:translateX(0); box-shadow:0 0 0 100vmax rgba(0,0,0,.35);}
  .topbar{display:flex;}
  .content-wrap{padding:28px 20px 70px;}
}
</style>
</head>
<body>
<div class="shell">
  <aside class="sidebar" id="sidebar">
    <div class="sidebar-head">
      <div class="brand">Waypoint</div>
      <div class="brand-sub">Databricks (Azure) Architect + Claude Certified Architect</div>
      <button class="theme-toggle" id="theme-toggle" type="button">Toggle theme</button>
    </div>
    <input class="search-box" id="search" type="search" placeholder="Search topics…" aria-label="Search topics">
    <a class="nav-home" href="#/">Home</a>
    <div id="nav-tree"></div>
    <p class="no-match" id="no-match">No matching sessions.</p>
  </aside>

  <div class="main">
    <div class="topbar" id="topbar">
      <button class="menu-btn" id="menu-btn" type="button" aria-label="Open menu">☰ Menu</button>
    </div>
    <div class="content-wrap">
      <div id="content"></div>
    </div>
  </div>
</div>

<script id="site-data" type="application/json">__DATA__</script>
<script>
(function(){
  "use strict";
  var DATA = JSON.parse(document.getElementById("site-data").textContent);
  var WEEKS = DATA.weeks;

  function esc(s){
    return String(s==null?"":s).replace(/[&<>"']/g, function(c){
      return {"&":"&amp;","<":"&lt;",">":"&gt;","\"":"&quot;","'":"&#39;"}[c];
    });
  }

  function findDay(wn, key){
    var w = WEEKS.find(function(x){ return x.n === wn; });
    if (!w) return null;
    var d = w.days.find(function(x){ return x.key === key; });
    return d ? {week:w, day:d} : null;
  }

  function flatOrder(){
    var out = [];
    WEEKS.forEach(function(w){ w.days.forEach(function(d){ out.push({wn:w.n, key:d.key}); }); });
    return out;
  }
  var ORDER = flatOrder();

  function neighbor(wn, key, dir){
    var idx = ORDER.findIndex(function(o){ return o.wn===wn && o.key===key; });
    var n = ORDER[idx+dir];
    if (!n) return null;
    var found = findDay(n.wn, n.key);
    return found ? {wn:n.wn, key:n.key, topic: found.day.topic, weekTitle: found.week.title} : null;
  }

  function renderNav(activeWn, activeKey, filter){
    var tree = document.getElementById("nav-tree");
    var q = (filter||"").trim().toLowerCase();
    var anyMatch = false;
    var html = WEEKS.map(function(w){
      var dayMatches = w.days.filter(function(d){
        return !q || d.topic.toLowerCase().indexOf(q) !== -1 || w.title.toLowerCase().indexOf(q) !== -1;
      });
      if (q && dayMatches.length === 0) return "";
      anyMatch = true;
      var isActiveWeek = w.n === activeWn;
      var collapsed = q ? false : !isActiveWeek;
      var daysToShow = q ? dayMatches : w.days;
      var days = daysToShow.map(function(d){
        var active = (w.n===activeWn && d.key===activeKey);
        var badges = "";
        if (d.ext) badges += '<span class="dot-badge ext" title="Extended deep dive"></span>';
        if (d.milestone) badges += '<span class="dot-badge milestone" title="Milestone/exam"></span>';
        return '<a class="nav-day' + (active?' active':'') + '" href="#/w' + w.n + '/' + d.key + '">' +
          '<span class="dlabel">' + d.label + '</span><span>' + esc(d.topic) + '</span>' + badges + '</a>';
      }).join("");
      return (
        '<div class="nav-week' + (collapsed?' collapsed':'') + '" data-week="' + w.n + '">' +
          '<button type="button" class="nav-week-head" data-action="toggle-week" data-week="' + w.n + '">' +
            '<span class="wn">' + String(w.n).padStart(2,"0") + '</span><span>' + esc(w.title) + '</span>' +
            '<span class="chev">▾</span>' +
          '</button>' +
          '<div class="nav-days">' + days + '</div>' +
        '</div>'
      );
    }).join("");
    tree.innerHTML = html;
    document.getElementById("no-match").style.display = (q && !anyMatch) ? "block" : "none";

    tree.querySelectorAll('[data-action="toggle-week"]').forEach(function(btn){
      btn.addEventListener("click", function(){
        btn.closest(".nav-week").classList.toggle("collapsed");
      });
    });
  }

  function renderLanding(){
    document.title = "Waypoint — Databricks + Claude Architect Programme";
    var html = marked.parse(DATA.topReadme);
    document.getElementById("content").innerHTML =
      '<div class="doc landing">' + html + '</div>';
  }

  function renderDay(wn, key){
    var found = findDay(wn, key);
    if (!found){ renderLanding(); return; }
    var w = found.week, d = found.day;
    document.title = d.topic + " — Week " + wn + " — Waypoint";

    var badges = "";
    if (d.ext) badges += '<span class="badge badge-ext">🔬 extended deep dive</span>';
    if (d.milestone) badges += '<span class="badge badge-milestone">' + (d.real ? "real exam" : "practice exam") + '</span>';

    var body = marked.parse(d.content);

    var prev = neighbor(wn, key, -1);
    var next = neighbor(wn, key, 1);
    var pager = '<div class="pager">';
    pager += prev
      ? '<a href="#/w' + prev.wn + '/' + prev.key + '"><span class="plabel">&larr; previous</span>' + esc(prev.topic) + '</a>'
      : '<span></span>';
    pager += next
      ? '<a class="pnext" href="#/w' + next.wn + '/' + next.key + '"><span class="plabel">next &rarr;</span>' + esc(next.topic) + '</a>'
      : '<span></span>';
    pager += '</div>';

    document.getElementById("content").innerHTML =
      '<p class="crumb"><a href="#/">Home</a> / <a href="#/w' + wn + '">Week ' + wn + ': ' + esc(w.title) + '</a> / ' + d.label + '</p>' +
      '<div class="day-meta">' + badges + '</div>' +
      '<div class="doc">' + body + '</div>' +
      pager;
  }

  function renderWeekIndex(wn){
    var w = WEEKS.find(function(x){ return x.n === wn; });
    if (!w){ renderLanding(); return; }
    document.title = "Week " + wn + ": " + w.title + " — Waypoint";
    var body = marked.parse(w.readme);
    document.getElementById("content").innerHTML =
      '<p class="crumb"><a href="#/">Home</a> / Week ' + wn + '</p>' +
      '<div class="doc">' + body + '</div>';
  }

  function route(){
    var hash = location.hash.replace(/^#\/?/, "");
    var parts = hash.split("/").filter(Boolean);
    var activeWn = null, activeKey = null;
    if (parts.length === 0){
      renderLanding();
    } else {
      var m = parts[0].match(/^w(\d+)$/);
      if (m){
        activeWn = parseInt(m[1], 10);
        if (parts[1]){
          activeKey = parts[1];
          renderDay(activeWn, activeKey);
        } else {
          renderWeekIndex(activeWn);
        }
      } else {
        renderLanding();
      }
    }
    renderNav(activeWn, activeKey, document.getElementById("search").value);
    document.getElementById("sidebar").classList.remove("open");
    window.scrollTo(0,0);
  }

  window.addEventListener("hashchange", route);
  document.getElementById("search").addEventListener("input", function(e){
    var hash = location.hash.replace(/^#\/?/, "");
    var parts = hash.split("/").filter(Boolean);
    var m = parts[0] && parts[0].match(/^w(\d+)$/);
    renderNav(m?parseInt(m[1],10):null, parts[1]||null, e.target.value);
  });
  document.getElementById("menu-btn").addEventListener("click", function(){
    document.getElementById("sidebar").classList.toggle("open");
  });

  var themeKey = "waypoint-theme";
  function applyTheme(t){
    if (t) document.documentElement.setAttribute("data-theme", t);
    else document.documentElement.removeAttribute("data-theme");
  }
  applyTheme(localStorage.getItem(themeKey));
  document.getElementById("theme-toggle").addEventListener("click", function(){
    var cur = document.documentElement.getAttribute("data-theme");
    var next = cur === "dark" ? "light" : (cur === "light" ? null : "dark");
    if (next) localStorage.setItem(themeKey, next); else localStorage.removeItem(themeKey);
    applyTheme(next);
  });

  route();
})();
</script>
</body>
</html>
"""


def main():
    data = build_data()
    html = TEMPLATE.replace("__DATA__", json.dumps(data).replace("</script", "<\\/script"))
    out_path = os.path.join(OUT_DIR, "index.html")
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(html)
    print("Wrote", out_path, "(%d bytes)" % os.path.getsize(out_path))


if __name__ == "__main__":
    main()
