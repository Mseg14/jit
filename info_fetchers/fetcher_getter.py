from typing import Optional, Type

from info_fetchers.exceptions import NoFetcherWasFound
from info_fetchers.fetcher import Fetcher
from info_fetchers.github_fetcher import GithubFetcher

FETCHERS = {
    'github': GithubFetcher
}


class FetcherGetter:
    def __init__(self):
        self.fetchers = FETCHERS

    def get_fetcher(self, source: str) -> Optional[Fetcher]:
        source_lower = source.lower()
        fetcher = self.fetchers.get(source_lower)
        if fetcher:
            return fetcher()
        raise NoFetcherWasFound("Repositories information is only fetched from the following sources: {}, you tried "
                                "to fetch information from the source: {}"
                                .format(', '.join(FETCHERS.keys()), source))
