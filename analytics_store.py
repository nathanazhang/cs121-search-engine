"""
Robust analytics storage with automatic field repair.
"""

import json
from pathlib import Path

ANALYTICS_PATH = Path("analytics.json")

DEFAULT_ANALYTICS = {
    "indexing": {
        "num_documents": 0,
        "num_unique_tokens": 0,
        "index_size_kb": 0,
        "num_duplicates": 0,
        "num_near_duplicates": 0,
    },
    "search": {
        "total_queries": 0,
        "avg_query_time_ms": 0.0,
        "max_query_time_ms": 0.0,
        "min_query_time_ms": None,
    }
}

def load_analytics():
    if ANALYTICS_PATH.exists():
        with ANALYTICS_PATH.open("r", encoding="utf-8") as f:
            data = json.load(f)
    else:
        return DEFAULT_ANALYTICS.copy()

    return data

def save_analytics(data):
    with ANALYTICS_PATH.open("w", encoding="utf-8") as f:
        json.dump(data, f, indent=2)

def record_indexing_stats(num_docs, num_tokens, index_size_kb, num_dups, num_near_dups):
    data = load_analytics()
    idx = data["indexing"]

    idx["num_documents"] = num_docs
    idx["num_unique_tokens"] = num_tokens
    idx["index_size_kb"] = index_size_kb
    idx["num_duplicates"] = num_dups
    idx["num_near_duplicates"] = num_near_dups

    save_analytics(data)

def record_query_time(elapsed_ms):
    data = load_analytics()
    s = data["search"]

    s["total_queries"] += 1

    n = s["total_queries"]
    old_avg = s["avg_query_time_ms"]
    s["avg_query_time_ms"] = ((old_avg * (n - 1)) + elapsed_ms) / n

    if s["min_query_time_ms"] is None or elapsed_ms < s["min_query_time_ms"]:
        s["min_query_time_ms"] = elapsed_ms

    if elapsed_ms > s["max_query_time_ms"]:
        s["max_query_time_ms"] = elapsed_ms

    save_analytics(data)
