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
    def execute(self, to_export=False, **kwargs):
        pass

    def get_dados_dir(self):
        output_dir = os.environ['VALUATION_OUTPUT_DIR']
        return output_dir
