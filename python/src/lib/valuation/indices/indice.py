from abc import ABC, abstractmethod


class Indice(ABC):
    def __init__(self, nome):
        super().__init__()
        self.nome = nome

    @abstractmethod
    def get_valor(self):
        pass

    def __str__(self):
        lines = [
            'Nome: {}',
            'Valor: {}'
        ]

        repr = '\n\t'.join(lines).format(
            self.nome,
            self.get_valor()
        )

        repr += self.str_comp()
        return repr

    @abstractmethod
    def str_comp(self):
        pass
