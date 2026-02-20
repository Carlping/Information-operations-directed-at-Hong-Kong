from __future__ import annotations

from pathlib import Path


def load_config_text(config_path: str | Path) -> str:
    """Load config file as plain text (minimal implementation)."""
    path = Path(config_path)
    return path.read_text(encoding="utf-8")
