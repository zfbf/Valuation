from abc import ABC, abstractmethod
from ..valuation import Valuation

#
# Nice explanation about optional arguments:
# https://realpython.com/python-optional-arguments/
#
class Reporter(ABC):
    def __init__(self):
        super().__init__()

    @abstractmethod
    def execute(self, valuation, **kwargs):
        pass
