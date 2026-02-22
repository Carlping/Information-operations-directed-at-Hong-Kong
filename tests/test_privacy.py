import pytest

from src.opinion_lab.privacy import drop_sensitive_fields, sanitize_text


def test_sanitize_text_masks_email_phone_and_id():
    text = "Contact me at test.user@example.com or +852 9123 4567, ID A123456789"
    masked = sanitize_text(text)

    assert "test.user@example.com" not in masked
    assert "+852 9123 4567" not in masked
    assert "A123456789" not in masked
    assert "[REDACTED_EMAIL]" in masked
    assert "[REDACTED_PHONE]" in masked
    assert "[REDACTED_ID]" in masked


def test_sanitize_text_returns_non_string_unchanged():
    payload = {"a": 1}
    assert sanitize_text(payload) is payload


def test_drop_sensitive_fields_with_list_of_dicts():
    records = [
        {"user": "alice", "email": "alice@example.com", "text": "hello"},
        {"user": "bob", "phone": "12345678", "text": "world"},
    ]

    result = drop_sensitive_fields(records, blacklist=["email", "phone"])

    assert result == [
        {"user": "alice", "text": "hello"},
        {"user": "bob", "text": "world"},
    ]


def test_drop_sensitive_fields_with_dataframe():
    pd = pytest.importorskip("pandas")

    df = pd.DataFrame(
        [
            {"user": "alice", "email": "alice@example.com", "text": "hello"},
            {"user": "bob", "phone": "12345678", "text": "world"},
        ]
    )

    result = drop_sensitive_fields(df, blacklist=["email", "phone"])

    assert list(result.columns) == ["user", "text"]


def test_drop_sensitive_fields_raises_for_unsupported_type():
    with pytest.raises(TypeError):
        drop_sensitive_fields("bad", blacklist=["email"])
