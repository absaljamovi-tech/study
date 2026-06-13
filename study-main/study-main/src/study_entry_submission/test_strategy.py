"""
Unit tests for Study Entry Submission Strategy module.
"""
from strategy import evaluate_entry_submission

def test_valid_submission():
    input_data = {"title": "Math HW", "content": "Solved problems 1-5."}
    existing_titles = ["biology hw"]
    date = "2026-05-16"
    result = evaluate_entry_submission(input_data, existing_titles, date)
    assert result["status"] == "accepted"
    assert result["normalized_entry"]["title"] == "math hw"
    assert result["normalized_entry"]["content"] == "Solved problems 1-5."
    assert result["normalized_entry"]["date"] == date
    assert result["reason"] is None

def test_missing_title():
    input_data = {"title": "", "content": "Some content"}
    existing_titles = []
    date = "2026-05-16"
    result = evaluate_entry_submission(input_data, existing_titles, date)
    assert result["status"] == "rejected"
    assert result["reason"] == "validation_failed"
    assert "title" in result["errors"]

def test_duplicate_title():
    input_data = {"title": "Math HW", "content": "New content"}
    existing_titles = ["math hw"]
    date = "2026-05-16"
    result = evaluate_entry_submission(input_data, existing_titles, date)
    assert result["status"] == "rejected"
    assert result["reason"] == "duplicate_entry"
