from abc import ABC, abstractmethod
from ..valuation import Valuation


class Reporter(ABC):
    def __init__(self):
        super().__init__()

    @abstractmethod
    def execute(self, valuation):
        pass
