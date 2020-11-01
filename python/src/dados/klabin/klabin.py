from src.lib.empresa import Empresa
from src.lib.contabilidade.relatorios_contabeis.balanco_patrimonial import BalancoPatrimonial
from src.lib.contabilidade.grupo_contas import GrupoContas


def get_empresa():
    sys.path.append(r'/home/zenon/PycharmProjects/Teste')
    sys.path.append(r'/home/zenon/PycharmProjects/Teste/front')
    sys.path.append(r'/home/zenon/PycharmProjects/Teste/front/library')

    klabin = Empresa('Klabin')

    for ano in range(2014, 2020):
        klabin.add_balanco_patrimonial(BalancoPatrimonial(ano))

    feed_ativo_circulante(klabin)
    feed_ativo_nao_circulante(klabin)
    return klabin


def feed_ativo_circulante(klabin):
    nomes = [
        'Caixa e equivalentes de caixa',
        'Títulos e valores mobiliários',
        'Contas a receber de clientes',
        'Perdas estimadas com créditos de liquidação duvidosa',
        'Estoques',
        'Tributos a recuperar',
        'Outros ativos'
    ]

    atv_circ_2019_valores = [
        8340386,
        1390529,
        1908974,
        -49469,
        1332244,
        505411,
        245869
    ]

    bp_2019 = klabin.get_balanco_patrimonial(2019)
    bp_2019.ativo.circulante.valor = 13673944
    bp_2019.add_ativo_circulante(nomes, nomes, atv_circ_2019_valores)
    print('Validação {} - {} - {} {}: {}'.format(klabin.nome,
                                                 bp_2019.ano,
                                                 bp_2019.ativo.nome,
                                                 bp_2019.ativo.circulante.nome,
                                                 bp_2019.ativo.circulante.validate))

    atv_circ_2018_valores = [
        5733854,
        1313350,
        2086325,
        -45394,
        1206353,
        269728,
        297718
    ]

    bp_2018 = klabin.get_balanco_patrimonial(2018)
    bp_2018.ativo.circulante.valor = 10861934
    bp_2018.add_ativo_circulante(nomes, nomes, atv_circ_2018_valores)
    print('Validação {} - {} - {} {}: {}'.format(klabin.nome,
                                                 bp_2018.ano,
                                                 bp_2018.ativo.nome,
                                                 bp_2018.ativo.circulante.nome,
                                                 bp_2018.ativo.circulante.validate))

    atv_circ_2017_valores = [
        7028422,
        1243173,
        1794196,
        -40133,
        933161,
        567079,
        277691
    ]

    bp_2017 = klabin.get_balanco_patrimonial(2017)
    bp_2017.ativo.circulante.valor = 11803589
    bp_2017.add_ativo_circulante(nomes, nomes, atv_circ_2017_valores)
    print('Validação {} - {} - {} {}: {}'.format(klabin.nome,
                                                 bp_2017.ano,
                                                 bp_2017.ativo.nome,
                                                 bp_2017.ativo.circulante.nome,
                                                 bp_2017.ativo.circulante.validate))

    atv_circ_2016_valores = [
        5872720,
        591303,
        1666626,
        -41246,
        876915,
        803355,
        190362
    ]

    bp_2016 = klabin.get_balanco_patrimonial(2016)
    bp_2016.ativo.circulante.valor = 9960035
    bp_2016.add_ativo_circulante(nomes, nomes, atv_circ_2016_valores)
    print('Validação {} - {} - {} {}: {}'.format(klabin.nome,
                                                 bp_2016.ano,
                                                 bp_2016.ativo.nome,
                                                 bp_2016.ativo.circulante.nome,
                                                 bp_2016.ativo.circulante.validate))

    nomes = [
        'Caixa e equivalentes de caixa',
        'Títulos e valores mobiliários',
        'Contas a receber de clientes',
        'Perdas estimadas com créditos de liquidação duvidosa',
        'Estoques',
        'Tributos a recuperar',
        'Despesas antecipadas - partes relacionadas',
        'Despesas antecipadas - terceiros',
        'Outros ativos'
    ]

    klabin.set_layout_contas_ativo_circulante(nomes)

    atv_circ_2015_valores = [
        5053723,
        557143,
        1539071,
        -37972,
        701126,
        736501,
        1081,
        9723,
        115348
    ]

    bp_2015 = klabin.get_balanco_patrimonial(2015)
    bp_2015.ativo.circulante.valor = 8675744
    bp_2015.add_ativo_circulante(nomes, nomes, atv_circ_2015_valores)
    print('Validação {} - {} - {} {}: {}'.format(klabin.nome,
                                                 bp_2015.ano,
                                                 bp_2015.ativo.nome,
                                                 bp_2015.ativo.circulante.nome,
                                                 bp_2015.ativo.circulante.validate))

    atv_circ_2014_valores = [
        5245833,
        497604,
        1193921,
        -45245,
        563709,
        331968,
        2613,
        25207,
        84066
    ]

    bp_2014 = klabin.get_balanco_patrimonial(2014)
    bp_2014.ativo.circulante.valor = 7899676
    bp_2014.add_ativo_circulante(nomes, nomes, atv_circ_2014_valores)
    print('Validação {} - {} - {} {}: {}'.format(klabin.nome,
                                                 bp_2014.ano,
                                                 bp_2014.ativo.nome,
                                                 bp_2014.ativo.circulante.nome,
                                                 bp_2014.ativo.circulante.validate))


def feed_ativo_nao_circulante(klabin):
    codigos_grupo_rlp= [
        'anc_rlp_depositos_judiciais',
        'anc_rlp_tributos_a_recuperar',
        'anc_rlp_outros_ativos'
    ]

    nomes_grupo_rlp = [
        'Depósitos judiciais',
        'Tributos a recuperar',
        'Outros ativos'
    ]

    valores_grupo_rlp_2019 = [
        117179,
        1944656,
        270817
    ]

    rlp_2019 = GrupoContas('realizavel_a_longo_prazo', 'Realizável a Longo Prazo')
    rlp_2019.valor = 2332652
    rlp_2019.add_nomes_valores(codigos_grupo_rlp, nomes_grupo_rlp, valores_grupo_rlp_2019)
    bp_2019 = klabin.get_balanco_patrimonial(2019)
    bp_2019.ativo.nao_circulante.add_conta(rlp_2019)

    investimentos_2019 = GrupoContas('anc_investimentos', 'Investimentos')

    codigos_grupo_investimentos = [
        'participacao_em_controladas',
        'outros'
    ]

    nomes_grupo_investimentos = [
        'Participação em controladas',
        'Outros'
    ]

    valores_grupo_investimentos_2019 = [
        160970,
        9687
    ]

    investimentos_2019.add_nomes_valores(codigos_grupo_investimentos,
                                         nomes_grupo_investimentos,
                                         valores_grupo_investimentos_2019)
    bp_2019.ativo.nao_circulante.add_conta(investimentos_2019)

    print('#1 - investimentos_2019')
    print(investimentos_2019)

    print('#1 - bp_2019.ativo.nao_circulante')
    print(bp_2019.ativo.nao_circulante)

    codigos_contas = [
        'imobilizado',
        'ativos_biologicos',
        'direito_de_uso_de_ativos',
        'intangiveis'
    ]

    nomes_contas = [
        'Imobilizado',
        'Ativos biológicos',
        'Direito de uso de ativos',
        'Intangíveis'
    ]

    valores_contas_2019 = [
        13241181,
        4712381,
        494399,
        77868
    ]

    bp_2019.ativo.nao_circulante.add_nomes_valores(codigos_contas, nomes_contas, valores_contas_2019)

    valores_grupo_rlp_2018 = [
        86658,
        1280811,
        300757
    ]

    rlp_2018 = GrupoContas('realizavel_a_longo_prazo', 'Realizável a Longo Prazo')
    rlp_2018.valor = 1668226
    rlp_2018.add_nomes_valores(codigos_grupo_rlp, nomes_grupo_rlp, valores_grupo_rlp_2018)
    bp_2018 = klabin.get_balanco_patrimonial(2018)
    bp_2018.ativo.nao_circulante.add_conta(rlp_2018)

    investimentos_2018 = GrupoContas('anc_investimentos', 'Investimentos')

    valores_grupo_investimentos_2018 = [
        166652,
        7607
    ]

    investimentos_2018.add_nomes_valores(codigos_grupo_investimentos,
                                         nomes_grupo_investimentos,
                                         valores_grupo_investimentos_2018)
    bp_2018.ativo.nao_circulante.add_conta(investimentos_2018)

    codigos_contas = [
        'imobilizado',
        'ativos_biologicos',
        'intangiveis'
    ]

    nomes_contas = [
        'Imobilizado',
        'Ativos biológicos',
        'Intangíveis'
    ]

    valores_contas_2018 = [
        12262472,
        4582631,
        85221
    ]

    bp_2018.ativo.nao_circulante.add_nomes_valores(codigos_contas, nomes_contas, valores_contas_2018)

    valores_grupo_rlp_2017 = [
        83381,
        1287669,
        344233
    ]

    rlp_2017 = GrupoContas('realizavel_a_longo_prazo', 'Realizável a Longo Prazo')
    rlp_2017.valor = 1715283
    rlp_2017.add_nomes_valores(codigos_grupo_rlp, nomes_grupo_rlp, valores_grupo_rlp_2017)
    bp_2017 = klabin.get_balanco_patrimonial(2017)
    bp_2017.ativo.nao_circulante.add_conta(rlp_2017)

    investimentos_2017 = GrupoContas('anc_investimentos', 'Investimentos')

    valores_grupo_investimentos_2017 = [
        171673,
        1773
    ]

    investimentos_2017.add_nomes_valores(codigos_grupo_investimentos,
                                         nomes_grupo_investimentos,
                                         valores_grupo_investimentos_2017)
    bp_2017.ativo.nao_circulante.add_conta(investimentos_2017)

    valores_contas_2017 = [
        12619495,
        4147779,
        89949
    ]

    bp_2017.ativo.nao_circulante.add_nomes_valores(codigos_contas, nomes_contas, valores_contas_2017)

    valores_grupo_rlp_2016 = [
        85704,
        1554672,
        385706
    ]

    rlp_2016 = GrupoContas('realizavel_a_longo_prazo', 'Realizável a Longo Prazo')
    rlp_2016.valor = 2026082
    rlp_2016.add_nomes_valores(codigos_grupo_rlp, nomes_grupo_rlp, valores_grupo_rlp_2016)
    bp_2016 = klabin.get_balanco_patrimonial(2016)
    bp_2016.ativo.nao_circulante.add_conta(rlp_2016)

    investimentos_2016 = GrupoContas('anc_investimentos', 'Investimentos')

    valores_grupo_investimentos_2016 = [
        544402,
        10943
    ]

    investimentos_2016.add_nomes_valores(codigos_grupo_investimentos,
                                         nomes_grupo_investimentos,
                                         valores_grupo_investimentos_2016)
    bp_2016.ativo.nao_circulante.add_conta(investimentos_2016)

    valores_contas_2016 = [
        13030184,
        3656596,
        85487
    ]

    bp_2016.ativo.nao_circulante.add_nomes_valores(codigos_contas, nomes_contas, valores_contas_2016)

    valores_grupo_rlp_2015 = [
        77391,
        1159638,
        219820
    ]

    rlp_2015 = GrupoContas('realizavel_a_longo_prazo', 'Realizável a Longo Prazo')
    rlp_2015.valor = 1456849
    rlp_2015.add_nomes_valores(codigos_grupo_rlp, nomes_grupo_rlp, valores_grupo_rlp_2015)
    bp_2015 = klabin.get_balanco_patrimonial(2015)
    bp_2015.ativo.nao_circulante.add_conta(rlp_2015)

    investimentos_2015 = GrupoContas('anc_investimentos', 'Investimentos')

    valores_grupo_investimentos_2015 = [
        495839,
        11436
    ]

    investimentos_2015.add_nomes_valores(codigos_grupo_investimentos,
                                         nomes_grupo_investimentos,
                                         valores_grupo_investimentos_2015)
    bp_2015.ativo.nao_circulante.add_conta(investimentos_2015)

    valores_contas_2015 = [
        12009146,
        3606389,
        12777
    ]

    bp_2015.ativo.nao_circulante.add_nomes_valores(codigos_contas, nomes_contas, valores_contas_2015)

    valores_grupo_rlp_2014 = [
        84689,
        428884,
        236050
    ]

    rlp_2014 = GrupoContas('realizavel_a_longo_prazo', 'Realizável a Longo Prazo')
    rlp_2014.valor = 749623
    rlp_2014.add_nomes_valores(codigos_grupo_rlp, nomes_grupo_rlp, valores_grupo_rlp_2014)
    bp_2014 = klabin.get_balanco_patrimonial(2014)
    bp_2014.ativo.nao_circulante.add_conta(rlp_2014)

    investimentos_2014 = GrupoContas('anc_investimentos', 'Investimentos')

    valores_grupo_investimentos_2014 = [
        483205,
        11542
    ]

    investimentos_2014.add_nomes_valores(codigos_grupo_investimentos,
                                         nomes_grupo_investimentos,
                                         valores_grupo_investimentos_2014)
    bp_2014.ativo.nao_circulante.add_conta(investimentos_2014)

    valores_contas_2014 = [
        8351387,
        3667085,
        11337
    ]

    bp_2014.ativo.nao_circulante.add_nomes_valores(codigos_contas, nomes_contas, valores_contas_2014)




    layout = [
        'blank Realizável a longo prazo',
        'anc_rlp_depositos_judiciais',
        'anc_rlp_tributos_a_recuperar',
        'anc_rlp_outros_ativos',
        'blank Investimentos',
        'participacao_em_controladas',
        'outros',
        'imobilizado',
        'ativos_biologicos',
        'direito_de_uso_de_ativos',
        'intangiveis'
    ]

    print('bp_2019.ativo.nao_circulante')
    print(bp_2019.ativo.nao_circulante)

    klabin.set_layout_contas_ativo_nao_circulante(layout)





if __name__ == '__main__':
    import sys

    sys.path.append(r'/home/zenon/dev/PycharmProjects/Valuation/src/dados')

    klabin = get_empresa()

    balancos_patrimoniais = []

    # for ano in range(2019, 2013, -1):
    #     balancos_patrimoniais.append(klabin.get_balanco_patrimonial(ano))
    #
    # for balanco_patrimonial in balancos_patrimoniais:
    #
    # for conta in klabin.get_balanco_patrimonial(2018).ativo.circulante.contas:
    #     print('{}'.format(conta.valor))

    # print('-x-x-x')
    # nome_da_conta = 'Caixa e equivalentes de caixa'
    # anos = [2019, 2018, 2017]
    # valores = klabin.get_valores_conta_ativo_circulante(range(2019, 2015, -1), nome_da_conta)
    # print('valores: {}'.format(valores))
    # print('Fim.')

    analise_horizotal = klabin.ativo_circulante_to_analise_horizontal(2019, 6)
    print()
    print(analise_horizotal)
    print('Ativo Circulante:')

    for nome_da_conta in analise_horizotal:
        valores = analise_horizotal[nome_da_conta]

        for valor in valores:
            print('{}\t\t\t\t'.format(valor or ''), end='')

        print()

    analise_horizotal = klabin.ativo_nao_circulante_to_analise_horizontal(2019, 6)
    print()
    print(analise_horizotal)
    print('Ativo não Circulante:')

    for nome_da_conta in analise_horizotal:
        valores = analise_horizotal[nome_da_conta]

        for valor in valores:
            print('{}\t\t\t\t'.format(valor or ''), end='')

        print()
