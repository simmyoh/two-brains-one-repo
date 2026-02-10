from pathlib import Path

TARGET_ISO_UTC = "2026-02-16T02:36:00Z"
TARGET2_ISO_UTC = "2026-02-16T05:05:00Z"
TARGET3_ISO_UTC = "2026-02-16T05:05:00Z"

# Resolve repo-relative paths safely
ROOT = Path(__file__).resolve().parents[1]
TEMPLATES = ROOT / "templates"
DOCS = ROOT / "docs"

template_path = TEMPLATES / "multiple_countdown_template.html"
output_path = DOCS / "multiple_countdown.html"

template = template_path.read_text(encoding="utf-8")
html = template.replace("__TARGET__", TARGET_ISO_UTC)
html = template.replace("__TARGET2__", TARGET2_ISO_UTC)
html = template.replace("__TARGET3__", TARGET3_ISO_UTC)

output_path.write_text(html, encoding="utf-8")

print(f"Wrote {output_path}")
