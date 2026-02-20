from __future__ import annotations


def load_mock_posts() -> list[dict[str, object]]:
    """Return a tiny mock dataset for the minimal runnable pipeline."""
    return [
        {
            "post_id": "p1",
            "author_id": "u1",
            "text": "sample opinion A",
            "created_at": "2024-01-01T10:00:00Z",
            "engagement": 15,
        },
        {
            "post_id": "p2",
            "author_id": "u2",
            "text": "sample opinion B",
            "created_at": "2024-01-01T11:00:00Z",
            "engagement": 8,
        },
        {
            "post_id": "p3",
            "author_id": "u1",
            "text": "sample opinion C",
            "created_at": "2024-01-01T12:00:00Z",
            "engagement": 30,
        },
    ]
