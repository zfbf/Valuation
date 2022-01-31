from .valuation import Valuation


class ValuationDefault(Valuation):
    def __init__(self, empresa):
        super().__init__(empresa)

    def init(self):
        pass
