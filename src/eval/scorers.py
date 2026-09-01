"""
Scoring strategies for the answer-quality rubric. harness.py calls .score(row)
and doesn't care which strategy is behind it.
"""
from abc import ABC, abstractmethod

RUBRIC_FIELDS = ["relevance", "groundedness", "correctness", "uncertainty_handling", "citation"]


class AnswerScorer(ABC):
    @abstractmethod
    def score(self, row: dict) -> dict:
        """Return a dict with exactly RUBRIC_FIELDS as keys."""
        ...


class ManualScorer(AnswerScorer):
    """Leaves rubric fields blank for a human to fill in via the CSV round-trip."""

    def score(self, row: dict) -> dict:
        return {field: None for field in RUBRIC_FIELDS}


# TODO: class LLMJudgeScorer(AnswerScorer)
#   def __init__(self, provider): self.provider = provider
#   def score(self, row): prompt the provider with the rubric + question +
#     gold_answer + model_answer, parse its response into RUBRIC_FIELDS.
#   Swap-in only — change the scorer instance passed to run_eval(), nothing else moves.