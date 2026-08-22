from __future__ import annotations

import json
import sys
from pathlib import Path

source = Path(sys.argv[1])
data = json.loads(source.read_text())

if "error" in data:
    print("API error:", data["error"].get("message", "Unknown error"))
    raise SystemExit(1)

lighthouse = data.get("lighthouseResult", {})
categories = lighthouse.get("categories", {})
audits = lighthouse.get("audits", {})

print("--- PageSpeed / Lighthouse summary ---")
for key in ("performance", "accessibility", "best-practices", "seo"):
    score = categories.get(key, {}).get("score")
    print(f"{key}: {'n/a' if score is None else round(score * 100)}")

for key in ("first-contentful-paint", "largest-contentful-paint", "total-blocking-time", "cumulative-layout-shift", "speed-index", "interactive"):
    audit = audits.get(key, {})
    print(f"{key}: {audit.get('displayValue', 'n/a')} (score={audit.get('score', 'n/a')})")

loading_experience = data.get("loadingExperience", {}).get("metrics", {})
origin_experience = data.get("originLoadingExperience", {}).get("metrics", {})
print("--- CrUX page data ---")
for key in ("LARGEST_CONTENTFUL_PAINT_MS", "CUMULATIVE_LAYOUT_SHIFT_SCORE", "INTERACTION_TO_NEXT_PAINT", "FIRST_CONTENTFUL_PAINT_MS"):
    metric = loading_experience.get(key, {})
    if metric:
        print(f"{key}: {metric.get('category', 'n/a')} ({metric.get('percentile', 'n/a')})")
print("--- CrUX origin data ---")
for key in ("LARGEST_CONTENTFUL_PAINT_MS", "CUMULATIVE_LAYOUT_SHIFT_SCORE", "INTERACTION_TO_NEXT_PAINT", "FIRST_CONTENTFUL_PAINT_MS"):
    metric = origin_experience.get(key, {})
    if metric:
        print(f"{key}: {metric.get('category', 'n/a')} ({metric.get('percentile', 'n/a')})")
