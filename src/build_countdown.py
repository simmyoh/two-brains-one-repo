from pathlib import Path

TARGET_ISO_UTC = "2026-01-13T02:38:00Z"

template = Path("countdown_template.html").read_text(encoding="utf-8")
html = template.replace("__TARGET__", TARGET_ISO_UTC)

Path("countdown.html").write_text(html, encoding="utf-8")
print("Wrote countdown.html")
