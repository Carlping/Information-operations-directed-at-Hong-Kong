"""Privacy helpers for sanitizing free text and structured records."""

from __future__ import annotations

import re
from typing import Any, Iterable

EMAIL_PATTERN = re.compile(r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}\b")
PHONE_PATTERN = re.compile(r"\b(?:\+?\d{1,3}[\s.-]?)?(?:\(?\d{2,4}\)?[\s.-]?){2,4}\d{2,4}\b")
ID_PATTERN = re.compile(r"\b[A-Za-z]{1,2}\d{6,10}|\d{8,18}\b")


def sanitize_text(text: Any) -> Any:
    """Mask common sensitive snippets (email, phone, and ID-like tokens).

    Non-string values are returned unchanged.
    """

    if not isinstance(text, str):
        return text

    sanitized = EMAIL_PATTERN.sub("[REDACTED_EMAIL]", text)
    sanitized = PHONE_PATTERN.sub("[REDACTED_PHONE]", sanitized)
    sanitized = ID_PATTERN.sub("[REDACTED_ID]", sanitized)
    return sanitized


def drop_sensitive_fields(records: Any, blacklist: Iterable[str]):
    """Drop sensitive fields from list[dict] or pandas.DataFrame.

    Args:
        records: list of dictionaries or pandas DataFrame.
        blacklist: field names to remove.
    """

    blacklist_set = set(blacklist)

    if hasattr(records, "drop") and hasattr(records, "columns"):
        return records.drop(columns=[col for col in blacklist_set if col in records.columns])

    if isinstance(records, list):
        cleaned_records = []
        for item in records:
            if not isinstance(item, dict):
                raise TypeError("All items in records list must be dict.")
            cleaned_records.append({k: v for k, v in item.items() if k not in blacklist_set})
        return cleaned_records

    raise TypeError("records must be a list of dict or a pandas DataFrame.")
