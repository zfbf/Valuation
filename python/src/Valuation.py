import src.lib.utils as utils


class Valuation:

    def __init__(self):
        super().__init__()

    def show_random_int(self):
        random_int = utils.generate_random_int(10, 1000)
        print('random_int: %s' % random_int)

    def __str__(self):
        return 'Valuation'

    def analise_horizontal_to_csv(self):
        data = ['cel1', 'cel2', 'cel3']
        csv = '\t'.join(data)
        return csv



if __name__ == '__main__':
    import sys

    sys.path.append(r'/home/zenon/dev/PycharmProjects/Valuation')
    sys.path.append(r'/home/zenon/dev/PycharmProjects/Valuation/lib')


    # ----------------- [ Criacao e uso] ----------------------------

    valuation = Valuation()
    print(valuation.analise_horizontal_to_csv())

    # ----------------------------------------------------------------
