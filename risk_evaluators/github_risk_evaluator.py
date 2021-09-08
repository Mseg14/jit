import shutil

from repositories.github_repository import GithubRepository
from repositories.repository import Repository
from risk_evaluators.risk_evaluator import RiskEvaluator
from git import Repo
import subprocess


class GithubPythonUnusedReqsRiskEvaluator(RiskEvaluator):
    def should_evaluate(self, repo: Repository) -> bool:
        return repo.source.lower() == "github" and repo.language.lower() == "python"

    def evaluate(self, repo: GithubRepository) -> float:
        Repo.clone_from(repo.url, "../temp_repos")
        try:
            process = subprocess.Popen(["pip-extra-reqs", "."], cwd="../temp_repos", stdout=subprocess.PIPE,
                                       stderr=subprocess.PIPE)
            stdout, stderr = process.communicate()
            subprocess.Popen(["ls"], cwd="../jit", stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            if "Traceback" in stderr.decode('utf-8'):
                risk = -1
            else:
                risk = len(list(filter(lambda x: x.endswith('.txt'), stderr.decode('utf-8').split("\n"))))
        except Exception:
            risk = -1
        shutil.rmtree("../temp_repos")
        return risk
