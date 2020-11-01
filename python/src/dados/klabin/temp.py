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