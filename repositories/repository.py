from datetime import datetime


class Repository:
    def __init__(self, source: str, language: str):
        self.source = source
        self.language = language

    def represent(self):
        raise NotImplementedError
