"""
Business logic for Study Entry Submission using the Strategy pattern.
"""
from typing import Dict, List, Optional

class SubmissionStrategy:
    def evaluate(self, input_data: Dict, existing_titles: List[str], date: str) -> Dict:
        """Evaluate the submission. Must be implemented by concrete strategies."""
        raise NotImplementedError

class ValidSubmissionStrategy(SubmissionStrategy):
    def evaluate(self, input_data: Dict, existing_titles: List[str], date: str) -> Dict:
        normalized_title = input_data['title'].strip().lower()
        if normalized_title in existing_titles:
            return {
                "status": "rejected",
                "reason": "duplicate_entry"
            }
        return {
            "status": "accepted",
            "normalized_entry": {
                "title": normalized_title,
                "content": input_data['content'].strip(),
                "date": date
            },
            "reason": None
        }

class InvalidSubmissionStrategy(SubmissionStrategy):
    def evaluate(self, input_data: Dict, existing_titles: List[str], date: str) -> Dict:
        errors = {}
        if not input_data.get('title', '').strip():
            errors['title'] = 'Title is required.'
        if not input_data.get('content', '').strip():
            errors['content'] = 'Content is required.'
        return {
            "status": "rejected",
            "errors": errors,
            "reason": "validation_failed"
        }

class SubmissionContext:
    def __init__(self, strategy: SubmissionStrategy):
        self.strategy = strategy

    def set_strategy(self, strategy: SubmissionStrategy):
        self.strategy = strategy

    def evaluate(self, input_data: Dict, existing_titles: List[str], date: str) -> Dict:
        return self.strategy.evaluate(input_data, existing_titles, date)

def evaluate_entry_submission(input_data: Dict, existing_titles: List[str], date: str) -> Dict:
    """
    Pure function: evaluates a study entry submission using the Strategy pattern.
    Returns a decision dict (no side effects).
    """
    if not input_data.get('title', '').strip() or not input_data.get('content', '').strip():
        context = SubmissionContext(InvalidSubmissionStrategy())
    else:
        context = SubmissionContext(ValidSubmissionStrategy())
    return context.evaluate(input_data, existing_titles, date)
