def escaloes(rendimento_coletavel):
    if rendimento_coletavel <= 7479:
        taxa = 0.145
        parcela_abater = 0
        taxa_media = 0.145
        escalao = 1
    elif rendimento_coletavel > 7479 and rendimento_coletavel <= 11284:
        taxa = 0.21
        parcela_abater = 486.14
        taxa_media = 0.1669
        escalao = 2
    elif rendimento_coletavel > 11284 and rendimento_coletavel <= 15992:
        taxa = 0.265
        parcela_abater = 1106.73
        escalao = 3
        taxa_media = 0.1958
    elif rendimento_coletavel > 15992 and rendimento_coletavel <= 20700:
        taxa = 0.285
        parcela_abater = 1426.65
        escalao = 4
        taxa_media = 0.2161
    elif rendimento_coletavel > 20700 and rendimento_coletavel <= 26335:
        taxa = 0.35
        parcela_abater = 2772.14
        escalao = 5
        taxa_media = 0.2448
    elif rendimento_coletavel > 26335 and rendimento_coletavel <= 38632:
        taxa = 0.37
        parcela_abater = 3299.12
        escalao = 6
        taxa_media = 0.2846
    elif rendimento_coletavel > 38632 and rendimento_coletavel <= 50483:
        taxa = 0.435
        parcela_abater = 5810.25
        escalao = 7
        taxa_media = 0.3199
    elif rendimento_coletavel > 50483 and rendimento_coletavel <= 78834:
        taxa = 0.45
        parcela_abater = 6567.33
        escalao = 8
        taxa_media = 0.3667
    else:
        taxa = 0.48
        parcela_abater = 8932.68
        escalao = 9
    return taxa, parcela_abater, escalao, taxa_media


def irs(gerais_familiares, valor_ss1, valor_ss2, quociente_familiar, dependentes, rendimento_anual_a, rendimento_anual_b, saude, educacao, habitacao, lares, automoveis, motociclos, restauracao, cabeleireiros, veterinarios, transportes, ginasios, jornais,retencoes_fonte_a, retencoes_fonte_b):
    limite_adicional = 0
    rendimento_conjunto = rendimento_anual_a + rendimento_anual_b

    retencoes_fonte = retencoes_fonte_a + retencoes_fonte_b


    if valor_ss1 <= 4104:
        deducao1 = 4104
    else:
        deducao1 = valor_ss1

    if valor_ss2 <= 4104:
        deducao2 = 4104
    else:
        deducao2 = valor_ss2

    rendimento_coletavel = ((rendimento_conjunto - (deducao1+deducao2))/2)

    taxa, parcela_abater, escalao, taxa_media = escaloes(rendimento_coletavel)
    importancia_apurada = rendimento_coletavel*taxa

    coleta_total = (importancia_apurada - parcela_abater) * quociente_familiar


    if escalao == 1:
        limite = 0
    else:
        if dependentes >= 3:
            limite = 1000+((2500-1000)*78834-rendimento_coletavel)/(78834-7479)
            limite_adicional = limite * (0.05*dependentes)
            limite = limite + limite_adicional
        else:
            limite = 1000 + ((2500 - 1000) * 78834 - rendimento_coletavel / (78834 - 7479))

    deducoes_coleta_com_limite = saude + educacao + habitacao + lares + automoveis + motociclos + restauracao + cabeleireiros + veterinarios + transportes + ginasios + jornais
    if deducoes_coleta_com_limite > limite:
        deducoes_coleta = limite
    else:
        deducoes_coleta = deducoes_coleta_com_limite
    deducoes_dependentes = 600 * dependentes

    deducoes_coleta = deducoes_coleta + deducoes_dependentes + gerais_familiares

    coleta_liquida = coleta_total - deducoes_coleta

    coleta_final = coleta_liquida - retencoes_fonte

    return  coleta_final, rendimento_conjunto, deducoes_coleta


