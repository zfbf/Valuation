from abc import ABC, abstractmethod
from ..valuation import Valuation

#
# Nice explanation about optional arguments:
# https://realpython.com/python-optional-arguments/
#
class Reporter(ABC):
    def __init__(self, nome):
        super().__init__()
        self.nome = nome

    @abstractmethod
    def execute(self, **kwargs):
        pass
