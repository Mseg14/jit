from typing import List

from repositories.repository import Repository
from risk_evaluators.exceptions import UnsupportedLanguage
from risk_evaluators.risk_evaluator import RiskEvaluator

SUPPORTED_LANGUAGES = {"python"}


class RiskEvaluatorManager:
    def __init__(self, risk_evaluators: List[RiskEvaluator]):
        self.risk_evaluators = risk_evaluators

    def evaluate(self, repo: Repository):
        if repo.language.lower() not in SUPPORTED_LANGUAGES:
            raise UnsupportedLanguage("Risk evaluator only supports repositories of the following languages: {}".
                                      format(", ".join(SUPPORTED_LANGUAGES)))

        for evaluator in self.risk_evaluators:
            if evaluator.should_evaluate(repo):
                return evaluator.evaluate(repo)
