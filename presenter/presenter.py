from typing import List

from repositories.repository import Repository


class Presenter:
    def present(self, repos: List[Repository]):
        raise NotImplementedError
