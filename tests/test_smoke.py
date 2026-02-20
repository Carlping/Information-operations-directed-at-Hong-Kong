from pathlib import Path

from opinion_lab.cli import run_minimal_pipeline


def test_minimal_pipeline_creates_output(tmp_path: Path) -> None:
    output = tmp_path / "metrics.csv"
    result = run_minimal_pipeline(output=str(output))

    assert result.exists()
    assert result.name == "metrics.csv"
