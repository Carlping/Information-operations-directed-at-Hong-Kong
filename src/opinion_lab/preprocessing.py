from __future__ import annotations

from datetime import datetime

REQUIRED_COLUMNS = ["post_id", "author_id", "text", "created_at", "engagement"]


def preprocess_posts(records: list[dict[str, object]]) -> list[dict[str, object]]:
    """Apply minimal cleaning and normalization for downstream analysis."""
    seen_post_ids: set[str] = set()
    cleaned: list[dict[str, object]] = []

    for record in records:
        normalized = {key: record.get(key) for key in REQUIRED_COLUMNS}
        if not normalized["post_id"] or not normalized["author_id"] or not normalized["text"]:
            continue

        post_id = str(normalized["post_id"])
        if post_id in seen_post_ids:
            continue
        seen_post_ids.add(post_id)

        try:
            datetime.fromisoformat(str(normalized["created_at"]).replace("Z", "+00:00"))
        except (TypeError, ValueError):
            normalized["created_at"] = None

        try:
            normalized["engagement"] = float(normalized["engagement"] or 0)
        except (TypeError, ValueError):
            normalized["engagement"] = 0.0

        cleaned.append(normalized)

    return cleaned
