from __future__ import annotations

import argparse
from pathlib import Path

from opinion_lab.analysis import build_minimal_metrics
from opinion_lab.ingestion import load_mock_posts
from opinion_lab.preprocessing import preprocess_posts
from opinion_lab.visualization import export_metrics


def run_minimal_pipeline(output: str = "data/processed/minimal_metrics.csv") -> Path:
    """Run the end-to-end minimal pipeline."""
    raw_records = load_mock_posts()
    clean_records = preprocess_posts(raw_records)
    metrics_rows = build_minimal_metrics(clean_records)
    return export_metrics(metrics_rows, output)


def main() -> None:
    parser = argparse.ArgumentParser(description="opinion-lab CLI")
    subparsers = parser.add_subparsers(dest="command", required=True)

    run_parser = subparsers.add_parser(
        "run-minimal-pipeline", help="Run minimal opinion observation pipeline"
    )
    run_parser.add_argument(
        "--output",
        default="data/processed/minimal_metrics.csv",
        help="Path to output CSV file",
    )

    args = parser.parse_args()

    if args.command == "run-minimal-pipeline":
        output_path = run_minimal_pipeline(output=args.output)
        print(f"Pipeline completed. Output saved to: {output_path}")
