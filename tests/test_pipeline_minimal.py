from opinion_lab.analysis import build_minimal_metrics
from opinion_lab.ingestion import load_mock_posts
from opinion_lab.preprocessing import preprocess_posts


def test_pipeline_metrics_schema() -> None:
    raw_records = load_mock_posts()
    clean_records = preprocess_posts(raw_records)
    metrics_rows = build_minimal_metrics(clean_records)

    assert set(metrics_rows[0].keys()) == {
        "total_posts",
        "unique_authors",
        "avg_engagement",
    }
    assert metrics_rows[0]["total_posts"] == 3.0
    assert metrics_rows[0]["unique_authors"] == 2.0
