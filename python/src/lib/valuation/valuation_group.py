from .valuation import Valuation


class ValuationGroup:
    def __init__(self):
        super().__init__()
        self.valuations = []

    def append_valuation(self, valuation):
        self.valuations.append(valuation)
