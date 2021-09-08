from typing import List
from datetime import datetime
import requests
import json

from info_fetchers.fetcher import Fetcher
from repositories.github_repository import GithubRepository, GITHUB_DATETIME_FORMAT

FETCHING_QUERY = 'https://api.github.com/search/repositories?q=language:{}&sort=stars&order=desc&per_page={}&page=1'


class GithubFetcher(Fetcher):
    def fetch(self, number_of_repos: int, language_of_projects: str) -> List[GithubRepository]:
        query_result = requests.get(FETCHING_QUERY.format(language_of_projects, number_of_repos))
        res = []
        for item in json.loads(query_result.content).get('items'):
            res.append(GithubRepository(
                source="github",
                repo_id=item.get('id', -1),
                name=item.get('name'),
                private=item.get('private'),
                owner_id=item.get('owner', {}).get('id'),
                description=item.get('description'),
                url=item.get('html_url'),
                created_at=str(datetime.strptime(item.get('created_at'), GITHUB_DATETIME_FORMAT)),
                updated_at=str(datetime.strptime(item.get('updated_at'), GITHUB_DATETIME_FORMAT)),
                size=item.get('size'),
                stargazers_count=item.get('stargazers_count'),
                watchers_count=item.get('watchers_count'),
                language=item.get('language')
            ))
        return res
