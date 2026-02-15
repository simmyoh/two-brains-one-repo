from pathlib import Path

# Add as many targets as necessary
TARGET_ISO_UTC = "2026-02-16T02:36:00Z"
TARGET_2_ISO_UTC = "2026-02-16T05:05:00Z"
TARGET_3_ISO_UTC = "2026-02-17T06:00:00Z"

# Resolve repo-relative paths safely
ROOT = Path(__file__).resolve().parents[1]
TEMPLATES = ROOT / "templates"
DOCS = ROOT / "docs"

template_path = TEMPLATES / "countdowns_template.html"
output_path = DOCS / "countdowns.html"

# Add as many targets as necessary
template = template_path.read_text(encoding="utf-8")
html = template.replace("__TARGET__", TARGET_ISO_UTC)
html = template.replace("__TARGET_2__", TARGET_2_ISO_UTC)
html = template.replace("__TARGET_3__", TARGET_3_ISO_UTC)

output_path.write_text(html, encoding="utf-8")

print(f"Wrote {output_path}")
