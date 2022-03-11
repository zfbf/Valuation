from lib.empresa import Empresa

class Dummy(Empresa):
    def __init__(self):
        super().__init__('Dummy')
