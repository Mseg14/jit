from typing import List

from repositories.repository import Repository


class Fetcher:
    def fetch(self, number_of_repos: int, language_of_projects: str) -> List[Repository]:
        raise NotImplementedError
