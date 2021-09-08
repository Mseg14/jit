from repositories.repository import Repository


class RiskEvaluator:
    def should_evaluate(self, repo: Repository) -> bool:
        raise NotImplementedError

    def evaluate(self, repo: Repository) -> float:
        raise NotImplementedError
