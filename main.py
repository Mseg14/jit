from typing import List

from info_fetchers.exceptions import NoFetcherWasFound
from info_fetchers.fetcher import Fetcher
from info_fetchers.fetcher_getter import FetcherGetter
from presenter.exceptions import UnsupportedPresentationType
from presenter.presentation_manager import PresentationManager
from repositories.repository import Repository
from risk_evaluators.github_risk_evaluator import GithubPythonUnusedReqsRiskEvaluator
from risk_evaluators.risk_evaluator_manager import RiskEvaluatorManager
import sys


def get_info_fetcher(source: str):
    return FetcherGetter().get_fetcher(source)


def calculate_risk(repos: List[Repository], risk_evaluator_manager: RiskEvaluatorManager):
    for repo in repos:
        repo.risk_score = risk_evaluator_manager.evaluate(repo)


def get_n_most_trending_repos(number_of_repos: int, data_fetcher: Fetcher, language: str) -> List[Repository]:
    return data_fetcher.fetch(number_of_repos, language)


def verify_input():
    if len(sys.argv) != 2:
        print('Please enter script name followed by number of required repos')
        sys.exit()

    if type(sys.argv[1]) == str and sys.argv[1].isdigit():
        n = int(sys.argv[1])
    else:
        print("Please enter a whole number between 1-100 (inclusive)")
        sys.exit()

    if n < 1 or 100 < n:
        print("Please enter a number between 1-100 (inclusive)")
        sys.exit()

    return n


if __name__ == '__main__':
    number = verify_input()
    repo_source = "Github"
    programming_language = "Python"
    try:
        single_source_data_fetcher = FetcherGetter().get_fetcher(repo_source)
        presentation_manager = PresentationManager("cli")
    except (NoFetcherWasFound, UnsupportedPresentationType) as e:
        print(e)
        sys.exit()
    risk_manager = RiskEvaluatorManager([GithubPythonUnusedReqsRiskEvaluator()])

    fetched_repos = get_n_most_trending_repos(number, single_source_data_fetcher, programming_language)
    calculate_risk(fetched_repos, risk_manager)
    presentation_manager.present(fetched_repos)
