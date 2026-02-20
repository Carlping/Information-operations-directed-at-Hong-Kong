from __future__ import annotations

import csv
from pathlib import Path


def export_metrics(metrics_rows: list[dict[str, float]], output_path: str | Path) -> Path:
    """Export metrics table to CSV as a minimal reporting output."""
    destination = Path(output_path)
    destination.parent.mkdir(parents=True, exist_ok=True)
    fieldnames = ["total_posts", "unique_authors", "avg_engagement"]
    with destination.open("w", newline="", encoding="utf-8") as csv_file:
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(metrics_rows)
    return destination
