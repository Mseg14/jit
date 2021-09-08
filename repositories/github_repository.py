from datetime import datetime
from repositories.repository import Repository

GITHUB_DATETIME_FORMAT = "%Y-%m-%dT%H:%M:%SZ"


class GithubRepository(Repository):
    def __init__(self, source: str, repo_id: int, name: str, private: bool, owner_id: int, description: str,
                 url: str, created_at: str, updated_at: str, size: int, stargazers_count: int,
                 watchers_count: int, language: str):
        super().__init__(source=source, language=language)
        self.repo_id = repo_id
        self.name = name
        self.private = private
        self.owner_id = owner_id
        self.description = description
        self.url = url
        self.created_at = created_at
        self.updated_at = updated_at
        self.size = size
        self.stargazers_count = stargazers_count
        self.watchers_count = watchers_count

    def represent(self):
        raise NotImplementedError
