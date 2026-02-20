# web_gui.py
from flask import Flask, request, render_template_string
import time

from search_engine import compute_scores, load_metadata, doc_meta
from analytics_store import record_query_time

app = Flask(__name__)

HTML_TEMPLATE = """
<!doctype html>
<html>
<head>
  <title>ICS Search Engine</title>
</head>
<body>
  <h1>ICS Search Engine</h1>
  <form method="GET">
    <input type="text" name="q" value="{{ query|e }}" style="width: 400px;" />
    <button type="submit">Search</button>
  </form>

  {% if query %}
    <h2>Results for "{{ query|e }}"</h2>

    {% if query_time_ms is not none %}
      <p>Query time: {{ query_time_ms }} ms</p>
    {% endif %}

    <ol>
    {% for r in results %}
      <li>
        <a href="{{ r.url }}" target="_blank">{{ r.url }}</a>
        <div>Score: {{ "%.4f"|format(r.score) }}</div>
      </li>
    {% endfor %}
    </ol>
  {% endif %}
</body>
</html>
"""

@app.route("/", methods=["GET"])
def search_page():
    q = request.args.get("q", "").strip()
    results_view = []
    query_time_ms = None

    if q:
        start = time.perf_counter()
        ranked = compute_scores(q)
        elapsed_ms = (time.perf_counter() - start) * 1000
        query_time_ms = round(elapsed_ms, 2)

        record_query_time(elapsed_ms)

        for doc_id, score in ranked:
            meta = doc_meta[str(doc_id)]
            results_view.append({"url": meta["url"], "score": score})

    return render_template_string(
        HTML_TEMPLATE,
        query=q,
        results=results_view,
        query_time_ms=query_time_ms
    )

if __name__ == "__main__":
    load_metadata()
    app.run(host="127.0.0.1", port=5000, debug=False)
