from typing import List

from presenter.cli_presenter import CliPresenter
from presenter.exceptions import UnsupportedPresentationType
from repositories.repository import Repository

PRESENTERS = {
    "cli": CliPresenter
}


class PresentationManager:
    def __init__(self, presentation_type: str):
        self.presentation_type = presentation_type
        self.presenter = self._get_presenter_according_to_type(presentation_type)

    def _get_presenter_according_to_type(self, presentation_type):
        if presentation_type.lower() not in PRESENTERS.keys():
            raise UnsupportedPresentationType("Unsupported type of presentation, we currently only supports the "
                                              "following types: {}".format(", ".join(PRESENTERS.keys())))
        return PRESENTERS.get(presentation_type)()

    def present(self, repos: List[Repository]):
        self.presenter.present(repos)
