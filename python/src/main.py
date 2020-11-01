if __name__ == '__main__' and __package__ is None:
    import sys
    from lib.contabilidade.conta import Conta

    print('#main')
    print('__name__: {}'.format(__name__))
    print('__package__: {}'.format(__package__))
    print('sys.path: {}'.format(sys.path))

    conta = Conta('caixa', 'caixa')
    print('conta: {}'.format(conta))
