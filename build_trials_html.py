"""Build index.html (single standalone view) from trials_template.html + trials.json."""
import json, pathlib
d = pathlib.Path(__file__).parent
data = json.loads((d / "trials.json").read_text(encoding="utf8"))
html = (d / "trials_template.html").read_text(encoding="utf8").replace("__DATA__", json.dumps(data, separators=(",", ":")))
(d / "index.html").write_text(html, encoding="utf8")
print("wrote index.html", len(html))
