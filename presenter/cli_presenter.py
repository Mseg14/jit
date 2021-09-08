from typing import List

from presenter.presenter import Presenter
from repositories.repository import Repository
import json


class CliPresenter(Presenter):
    def present(self, repos: List[Repository]):
        for repo in repos:
            print(json.dumps(repo.__dict__, sort_keys=True, indent=4))
