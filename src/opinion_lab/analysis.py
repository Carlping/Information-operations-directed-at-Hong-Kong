from __future__ import annotations


def build_minimal_metrics(records: list[dict[str, object]]) -> list[dict[str, float]]:
    """Build minimal, publication-friendly aggregate metrics."""
    total_posts = len({str(item["post_id"]) for item in records})
    unique_authors = len({str(item["author_id"]) for item in records})
    avg_engagement = (
        sum(float(item.get("engagement", 0.0)) for item in records) / len(records)
        if records
        else 0.0
    )
    return [
        {
            "total_posts": float(total_posts),
            "unique_authors": float(unique_authors),
            "avg_engagement": avg_engagement,
        }
    ]
