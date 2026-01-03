from pathlib import Path

TARGET_ISO_UTC = "2026-01-13T02:38:00Z"

# Resolve repo-relative paths safely
ROOT = Path(__file__).resolve().parents[1]
TEMPLATES = ROOT / "templates"
DOCS = ROOT / "docs"

template_path = TEMPLATES / "countdown_template.html"
output_path = DOCS / "countdown.html"

template = template_path.read_text(encoding="utf-8")
html = template.replace("__TARGET__", TARGET_ISO_UTC)

output_path.write_text(html, encoding="utf-8")

print(f"Wrote {output_path}")
