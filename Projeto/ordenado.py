parcela_dependente=0
def ordenado_dependente_solteiro(dependentes, renumeracao):
    if dependentes == 0:
        if renumeracao <= 762:
            renumeracao_liquida = renumeracao
        elif renumeracao > 762 and renumeracao <= 886.57:
            taxa = 0.145
            parcela_abater = taxa * 2.3 * (1091.31 - renumeracao)
            parcela_dependente = 0

        elif renumeracao > 886.57 and renumeracao <= 932.14:
            taxa = 0.210
            parcela_abater = taxa * 1.3 * (1350.22 - renumeracao)
            parcela_dependente = 0

        elif renumeracao > 932.14 and renumeracao <= 999.14:
            taxa = 0.210
            parcela_abater = 114.14
            parcela_dependente = 0

        elif renumeracao > 999.14 and renumeracao <= 1106.36:
            taxa = 0.265
            parcela_abater = 169.09
            parcela_dependente = 0

        elif renumeracao > 1106.36 and renumeracao <= 1600.36:
            taxa = 0.285
            parcela_abater = 191.23
            parcela_dependente = 0

        elif renumeracao > 1600.36 and renumeracao <= 1961.36:
            taxa = 0.350
            parcela_abater = 295.26
            parcela_dependente = 0

        elif renumeracao > 1961.36 and renumeracao <= 2529.05:
            taxa = 0.371
            parcela_abater = 334.48
            parcela_dependente = 0

        elif renumeracao > 2529.05 and renumeracao <= 3694.46:
            taxa = 0.3872
            parcela_abater = 377.86
            parcela_dependente = 0

        elif renumeracao > 3694.46 and renumeracao <= 5469.90:
            taxa = 0.4005
            parcela_abater = 427.18
            parcela_dependente = 0

        elif renumeracao > 5469.90 and renumeracao <= 6420.55:
            taxa = 0.4272
            parcela_abater = 573.22
            parcela_dependente = 0

        elif renumeracao > 6420.55 and renumeracao <= 20064.21:
            taxa = 0.4495
            parcela_abater = 716.08
            parcela_dependente = 0

        else:
            taxa = 0.4717
            parcela_abater = 1162.51
            parcela_dependente = 0
    else:
        if renumeracao <= 762:
            renumeracao_liquida = renumeracao
        elif renumeracao > 762 and renumeracao <= 886.57:
            taxa = 0.145
            parcela_abater = taxa * 2.3 * (1114.17 - renumeracao)
            parcela_dependente = 34.29
        elif renumeracao > 886.57 and renumeracao <= 932.14:
            taxa = 0.21
            parcela_abater = taxa * 1.3 * (1376.37 - renumeracao)
            parcela_dependente = 34.29
        elif renumeracao > 932.14 and renumeracao <= 999.14:
            taxa = 0.210
            parcela_abater = 121.28
            parcela_dependente = 34.29
        elif renumeracao > 999.14 and renumeracao <= 1106.93:
            taxa = 0.265
            parcela_abater = 176.23
            parcela_dependente = 34.29
        elif renumeracao > 1106.93 and renumeracao <= 1600.36:
            taxa = 0.285
            parcela_abater = 198.37
            parcela_dependente = 34.29
        elif renumeracao > 1600.36 and renumeracao <= 1961.36:
            taxa = 0.350
            parcela_abater = 302.39
            parcela_dependente = 34.29
        elif renumeracao > 1961.36 and renumeracao <= 2529.05:
            taxa = 0.370
            parcela_abater = 341.62
            parcela_dependente = 34.29
        elif renumeracao > 2529.05 and renumeracao <= 3694.46:
            taxa = 0.3872
            parcela_abater = 384.99
            parcela_dependente = 34.29
        elif renumeracao > 3694.46 and renumeracao <= 5469.90:
            taxa = 0.4005
            parcela_abater = 434.32
            parcela_dependente = 34.29
        elif renumeracao > 5469.90 and renumeracao <= 6420.55:
            taxa = 0.4272
            parcela_abater = 580.36
            parcela_dependente = 34.29
        elif renumeracao > 6420.55 and renumeracao <= 20064.21:
            taxa = 0.4495
            parcela_abater = 723.22
            parcela_dependente = 34.29
        else:
            taxa = 0.4717
            parcela_abater = 1169.65
            parcela_dependente = 34.29

    valor_dependente = dependentes * parcela_dependente
    valor_irs = (renumeracao * taxa) - parcela_abater - valor_dependente
    renumeracao_liquida = renumeracao - valor_irs
    return valor_irs, parcela_abater, taxa, renumeracao_liquida, parcela_dependente

def ordenado_casado_1t (dependentes, renumeracao):
    if dependentes == 0:
        if renumeracao <= 762:
            renumeracao_liquida = renumeracao
            parcela_dependente = 0
        elif renumeracao > 762 and renumeracao <= 886.57:
            taxa = 0.145
            parcela_abater = taxa * 2.3 * (1153.28 - renumeracao)
            parcela_dependente = 0
        elif renumeracao > 886.57 and renumeracao <= 932.14:
            taxa = 0.145
            parcela_abater = taxa * 1.883 * (1212.39 - renumeracao)
            parcela_dependente = 0
        if renumeracao > 932.14 and renumeracao <= 1027.71:
            taxa = 0.145
            parcela_abater = 76.51
            parcela_dependente = 0
        elif renumeracao > 1278.36 and renumeracao <= 1700.36:
            taxa = 0.1593
            parcela_abater = 91.20
            parcela_dependente = 0
        elif renumeracao > 1700.36 and renumeracao <= 1961.36:
            taxa = 0.2468
            parcela_abater = 218.66
            parcela_dependente = 0

        elif renumeracao > 1961.36 and renumeracao <= 2529.05:
            taxa = 0.2758
            parcela_abater = 275.52
            parcela_dependente = 0

        elif renumeracao > 2529.05 and renumeracao <= 3694.46:
            taxa = 0.2980
            parcela_abater = 331.54
            parcela_dependente = 0

        elif renumeracao > 3694.46 and renumeracao <= 6327.05:
            taxa = 0.3311
            parcela_abater = 453.94
            parcela_dependente = 0
        elif renumeracao > 6327.05 and renumeracao <= 6420.55:
            taxa = 0.3872
            parcela_abater = 808.52
            parcela_dependente = 0
        elif renumeracao > 6420.55 and renumeracao <= 20064.21:
            taxa = 0.4251
            parcela_abater = 1052.40
            parcela_dependente = 0

        else:
            taxa = 0.4717
            parcela_abater = 1986.71
            parcela_dependente = 0
    else:
        if renumeracao <= 762:
            renumeracao_liquida = renumeracao
            parcela_dependente = 0
        elif renumeracao > 762 and renumeracao <= 886.57:
            taxa = 0.145
            parcela_abater = taxa * 2.3 * (1146.84 - renumeracao)
            parcela_dependente = 42.86
        elif renumeracao > 886.57 and renumeracao <= 932.14:
            taxa = 0.145
            parcela_abater = taxa * 1.883 * (1204.55 - renumeracao)
            parcela_dependente = 42.86
        if renumeracao > 932.14 and renumeracao <= 999.14:
            taxa = 0.145
            parcela_abater = 74.37
            parcela_dependente = 42.86
        elif renumeracao > 999.14 and renumeracao <= 1106.93:
            taxa = 0.1593
            parcela_abater = 88.64
            parcela_dependente = 42.86
        elif renumeracao > 1106.93 and renumeracao <= 1600.36:
            taxa = 0.21
            parcela_abater = 144.78
            parcela_dependente = 42.86
        elif renumeracao > 1600.36 and renumeracao <= 1961.36:
            taxa = 0.2468
            parcela_abater = 203.73
            parcela_dependente = 42.86

        elif renumeracao > 1961.36 and renumeracao <= 2529.05:
            taxa = 0.2758
            parcela_abater = 260.59
            parcela_dependente = 42.86

        elif renumeracao > 2529.05 and renumeracao <= 3694.46:
            taxa = 0.2980
            parcela_abater = 316.61
            parcela_dependente = 42.86
        elif renumeracao > 3694.46 and renumeracao <= 5469.90:
            taxa = 0.3311
            parcela_abater = 439.01
            parcela_dependente = 42.86
        elif renumeracao > 5469.90 and renumeracao <= 6420.55:
            taxa = 0.3872
            parcela_abater = 745.55
            parcela_dependente = 42.86

        elif renumeracao > 6420.55 and renumeracao <=20064.21:
            taxa = 0.4251
            parcela_abater = 989.43
            parcela_dependente = 42.86
        else:
            taxa = 0.4717
            parcela_abater = 1923.74
            parcela_dependente = 42.86

    valor_dependente = dependentes * parcela_dependente
    valor_irs = (renumeracao * taxa) - parcela_abater - valor_dependente
    renumeracao_liquida = renumeracao - valor_irs
    return valor_irs, parcela_abater, taxa, renumeracao_liquida, parcela_dependente

def casados_2t(dependentes, renumeracao):
    if dependentes == 0:
        if renumeracao <= 762:
            renumeracao_liquida = renumeracao
        elif renumeracao > 762 and renumeracao <= 886.57:
            taxa = 0.145
            parcela_abater = taxa * 2.3 * (1091.31 - renumeracao)
            parcela_dependente = 0
        elif renumeracao > 886.57 and renumeracao <= 932.14:
            taxa = 0.210
            parcela_abater = taxa * 1.3 * (1350.22 - renumeracao)
            parcela_dependente = 0
        elif renumeracao > 932.14 and renumeracao <= 999.14:
            taxa = 0.210
            parcela_abater = 114.14
            parcela_dependente = 0
        elif renumeracao > 999.14 and renumeracao <= 1106.36:
            taxa = 0.265
            parcela_abater = 169.09
            parcela_dependente = 0
        elif renumeracao > 1106.36 and renumeracao <= 1600.36:
            taxa = 0.285
            parcela_abater = 191.23
            parcela_dependente = 0

        elif renumeracao > 1600.36 and renumeracao <= 1961.36:
            taxa = 0.350
            parcela_abater = 295.26
            parcela_dependente = 0

        elif renumeracao > 1961.36 and renumeracao <= 2529.05:
            taxa = 0.371
            parcela_abater = 334.48
            parcela_dependente = 0

        elif renumeracao > 2529.05 and renumeracao <= 3694.46:
            taxa = 0.3872
            parcela_abater = 377.86
            parcela_dependente = 0

        elif renumeracao > 3694.46 and renumeracao <= 5469.90:
            taxa = 0.4005
            parcela_abater = 427.18
            parcela_dependente = 0

        elif renumeracao > 5469.90 and renumeracao <= 6420.55:
            taxa = 0.4272
            parcela_abater = 573.22
            parcela_dependente = 0

        elif renumeracao > 6420.55 and renumeracao <= 20064.21:
            taxa = 0.4495
            parcela_abater = 716.08
            parcela_dependente = 0

        else:
            taxa = 0.4717
            parcela_abater = 1162.51
            parcela_dependente = 0
    else:
        if renumeracao <= 762:
            renumeracao_liquida = renumeracao
        elif renumeracao > 762 and renumeracao <= 886.57:
            taxa = 0.145
            parcela_abater = taxa * 2.3 * (1093.30 - renumeracao)
            parcela_dependente = 21.43
        elif renumeracao > 886.57 and renumeracao <= 932.14:
            taxa = 0.21
            parcela_abater = taxa * 1.3 * (1350.21 - renumeracao)
            parcela_dependente = 21.43
        elif renumeracao > 932.14 and renumeracao <= 999.14:
            taxa = 0.21
            parcela_abater = 114.14
            parcela_dependente = 21.43
        elif renumeracao > 999.14 and renumeracao <= 1106.36:
            taxa = 0.265
            parcela_abater = 169.09
            parcela_dependente = 21.43
        elif renumeracao > 1106.93 and renumeracao <= 1600.36:
            taxa = 0.285
            parcela_abater = 191.23
            parcela_dependente = 21.43
        elif renumeracao > 1600.36 and renumeracao <= 1961.36:
            taxa = 0.350
            parcela_abater = 295.25
            parcela_dependente = 21.43
        elif renumeracao > 1961.36 and renumeracao <= 2529.05:
            taxa = 0.370
            parcela_abater = 334.48
            parcela_dependente = 21.43
        elif renumeracao > 2529.05 and renumeracao <= 3694.46:
            taxa = 0.3872
            parcela_abater = 377.85
            parcela_dependente = 21.43
        elif renumeracao > 3694.46 and renumeracao <= 5469.90:
            taxa = 0.4005
            parcela_abater = 427.18
            parcela_dependente = 21.43
        elif renumeracao > 5469.90 and renumeracao <= 6420.55:
            taxa = 0.4272
            parcela_abater = 5573.22
            parcela_dependente = 21.43
        elif renumeracao > 6420.55 and renumeracao <= 20064.21:
            taxa = 0.4495
            parcela_abater = 716.08
            parcela_dependente = 21.43
        else:
            taxa = 0.4717
            parcela_abater = 1162.51
            parcela_dependente = 21.43
    valor_dependente = dependentes * parcela_dependente
    valor_irs = (renumeracao * taxa) - parcela_abater - valor_dependente
    renumeracao_liquida = renumeracao - valor_irs
    return valor_irs, parcela_abater, taxa, renumeracao_liquida, parcela_dependente


def ordenado_dependente_solteiro_invalidez(dependentes, renumeracao):
    if dependentes == 0:
        if renumeracao <= 1519.41:
            renumeracao_liquida = renumeracao
            taxa = 0
            parcela_abater = 0
            parcela_dependente = 0
        elif renumeracao > 1519.41 and renumeracao <= 1971.21:
            taxa = 0.2650
            parcela_abater = 402.64
            parcela_dependente = 0

        elif renumeracao > 1971.21 and renumeracao <= 2093.21:
            taxa = 0.2850
            parcela_abater = 442.07
            parcela_dependente = 0

        elif renumeracao > 2093.21 and renumeracao <= 2354.21:
            taxa = 0.35
            parcela_abater = 578.13
            parcela_dependente = 0

        elif renumeracao > 4015.41 and renumeracao <= 4252.25:
            taxa = 0.3872
            parcela_abater = 694.08
            parcela_dependente = 0

        elif renumeracao > 4252.25 and renumeracao <= 6527.69:
            taxa = 0.4005
            parcela_abater = 750.84
            parcela_dependente = 0

        elif renumeracao > 6527.69 and renumeracao <= 6621.19:
            taxa = 0.4272
            parcela_abater = 925.13
            parcela_dependente = 0

        elif renumeracao > 6621.19 and renumeracao <= 20264.85:
            taxa = 0.4495
            parcela_abater = 1072.45
            parcela_dependente = 0

        else:
            taxa = 0.4717
            parcela_abater = 1523.35
            parcela_dependente = 0


    else:
        if renumeracao <= 1677.09:
            taxa = 0
            parcela_abater = 0
            parcela_dependente = 0
        elif renumeracao > 1677.09 and renumeracao <= 2042.64:
            taxa = 0.265
            parcela_abater = 401.57
            parcela_dependente = 42.86 ###

        elif renumeracao > 2042.64 and renumeracao <= 2307.50:
            taxa = 0.2850
            parcela_abater = 442.07
            parcela_dependente = 42.86

        elif renumeracao > 2307.50 and renumeracao <= 2425.64 :
            taxa = 0.35
            parcela_abater = 592.41
            parcela_dependente = 42.86

        elif renumeracao > 2425.64 and renumeracao <= 3743.98 :
            taxa = 0.37
            parcela_abater = 640.92
            parcela_dependente = 42.86

        elif renumeracao > 3743.98 and renumeracao <= 4252.25:
            taxa = 0.3872
            parcela_abater = 705.13
            parcela_dependente = 42.86

        elif renumeracao > 4252.25 and renumeracao <= 6527.69:
            taxa = 0.4005
            parcela_abater = 761.90
            parcela_dependente = 42.86

        elif renumeracao > 6527.69 and renumeracao <= 6621.19:
            taxa = 0.4272
            parcela_abater = 936.19
            parcela_dependente = 42.86
        elif renumeracao > 6621.19 and renumeracao <= 20264.85:
            taxa = 0.4495
            parcela_abater = 1083.51
            parcela_dependente = 42.86
        else:
            taxa = 0.4717
            parcela_abater = 1534.40
            parcela_dependente = 42.86

    valor_dependente = dependentes * parcela_dependente
    valor_irs = (renumeracao * taxa) - parcela_abater - valor_dependente
    renumeracao_liquida = renumeracao - valor_irs
    return valor_irs, parcela_abater, taxa, renumeracao_liquida, parcela_dependente

def ordenado_casado_1t_invalidez (dependentes, renumeracao):
    if dependentes == 0:
        if renumeracao <= 1779.19:
            taxa = 0
            parcela_abater = 0
            parcela_dependente = 0
        elif renumeracao > 1779.19 and renumeracao <= 2664.64:
            taxa = 0.21
            parcela_abater = 373.63
            parcela_dependente = 0
        elif renumeracao > 2664.64 and renumeracao <= 2818.50:
            taxa = 0.2468
            parcela_abater = 471.79
            parcela_dependente = 0
        if renumeracao > 2818.50 and renumeracao <= 3051.12:
            taxa = 0.2758
            parcela_abater = 553.49
            parcela_dependente = 0
        elif renumeracao > 3051.12 and renumeracao <= 3395.10:
            taxa = 0.2980
            parcela_abater = 621.08
            parcela_dependente = 0
        elif renumeracao > 3395.10 and renumeracao <= 6527.69:
            taxa = 0.3311
            parcela_abater = 733.56
            parcela_dependente = 0

        elif renumeracao > 6527.69 and renumeracao <= 6621.19:
            taxa = 0.3872
            parcela_abater = 1099.39
            parcela_dependente = 0

        elif renumeracao > 6621.19 and renumeracao <= 20264.85:
            taxa = 0.4251
            parcela_abater = 1350.89
            parcela_dependente = 0

        else:
            taxa = 0.4717
            parcela_abater = 2294.54
            parcela_dependente = 0
    else:
        if renumeracao <= 1881.23:
            taxa = 0
            parcela_abater = 0
            parcela_dependente = 0
        elif renumeracao > 1881.23 and renumeracao <= 2664.64:
            taxa = 0.21
            parcela_abater = 352.20
            parcela_dependente = 42.86
        elif renumeracao >2664.64  and renumeracao <= 2818.50:
            taxa = 0.2468
            parcela_abater = 450.36
            parcela_dependente = 42.86
        if renumeracao > 2818.50 and renumeracao <= 3051.12:
            taxa = 0.2758
            parcela_abater = 532.06
            parcela_dependente = 42.86
        elif renumeracao > 3051.12 and renumeracao <= 3395.10:
            taxa = 0.2980
            parcela_abater = 599.65
            parcela_dependente = 42.86
        elif renumeracao > 3395.10 and renumeracao <= 6527.69:
            taxa = 0.3311
            parcela_abater = 712.13
            parcela_dependente = 42.86
        elif renumeracao > 6527.69 and renumeracao <= 6621.19:
            taxa = 0.3872
            parcela_abater = 1077.96
            parcela_dependente = 42.86

        elif renumeracao > 6621.19 and renumeracao <= 20264.85:
            taxa = 0.4251
            parcela_abater = 1329.46
            parcela_dependente = 42.86

        else:
            taxa = 0.4717
            parcela_abater = 2273.11
            parcela_dependente = 42.86

    valor_dependente = dependentes * parcela_dependente
    valor_irs = (renumeracao * taxa) - parcela_abater - valor_dependente
    renumeracao_liquida = renumeracao - valor_irs
    return valor_irs, parcela_abater, taxa, renumeracao_liquida, parcela_dependente

def casados_2t_invalidez(dependentes, renumeracao):
    if dependentes == 0:
        if renumeracao <= 1519.41:
            taxa = 0
            parcela_abater = 0
            parcela_dependente = 0
        elif renumeracao > 1519.41 and renumeracao <= 1971.21:
            taxa = 0.2650
            parcela_abater = 402.64
            parcela_dependente = 0

        elif renumeracao > 1971.21 and renumeracao <= 2093.21:
            taxa = 0.2850
            parcela_abater = 442.07
            parcela_dependente = 0

        elif renumeracao > 2093.21 and renumeracao <= 2354.21:
            taxa = 0.35
            parcela_abater = 578.13
            parcela_dependente = 0

        elif renumeracao > 4015.41 and renumeracao <= 4252.25:
            taxa = 0.3872
            parcela_abater = 694.08
            parcela_dependente = 0

        elif renumeracao > 4252.25 and renumeracao <= 6527.69:
            taxa = 0.4005
            parcela_abater = 750.84
            parcela_dependente = 0

        elif renumeracao > 6527.69 and renumeracao <= 6621.19:
            taxa = 0.4272
            parcela_abater = 925.13
            parcela_dependente = 0

        elif renumeracao > 6621.19 and renumeracao <= 20264.85:
            taxa = 0.4495
            parcela_abater = 1072.45
            parcela_dependente = 0

        else:
            taxa = 0.4717
            parcela_abater = 1523.35
            parcela_dependente = 0

    else:
        if renumeracao <= 1574.66:
            taxa = 0
            parcela_abater = 0
            parcela_dependente = 0
        elif renumeracao > 1574.66 and renumeracao <= 2185.50:
            taxa = 0.2650
            parcela_abater = 395.86
            parcela_dependente = 21.43
        elif renumeracao > 2185.50 and renumeracao <= 2307.50:
            taxa = 0.285
            parcela_abater = 439.57
            parcela_dependente = 21.43
        elif renumeracao > 2307.50 and renumeracao <= 2354.21:
            taxa = 0.35
            parcela_abater = 589.55
            parcela_dependente = 21.43
        elif renumeracao > 2354.21 and renumeracao <= 3301.12:
            taxa = 0.37
            parcela_abater = 636.64
            parcela_dependente = 21.43
        elif renumeracao > 3301.12 and renumeracao <= 4252.25:
            taxa = 0.3872
            parcela_abater = 693.25
            parcela_dependente = 21.43
        elif renumeracao > 4252.25 and renumeracao <= 6527.69:
            taxa = 0.4005
            parcela_abater = 750.02
            parcela_dependente = 21.43
        elif renumeracao > 6527.69 and renumeracao <= 6621.19:
            taxa = 0.4272
            parcela_abater = 924.31
            parcela_dependente = 21.43
        elif renumeracao > 6621.19 and renumeracao <= 20264.85:
            taxa = 0.4495
            parcela_abater = 1071.63
            parcela_dependente = 21.43
        else:
            taxa = 0.4717
            parcela_abater = 1522.52
            parcela_dependente = 21.43

    valor_dependente = dependentes * parcela_dependente
    valor_irs = (renumeracao * taxa) - parcela_abater - valor_dependente
    renumeracao_liquida = renumeracao - valor_irs
    return valor_irs, parcela_abater, taxa, renumeracao_liquida, parcela_dependente




def pensao_solteiro_casado_2t(renumeracao):

    if renumeracao <= 762:
        taxa = 0
        parcela_abater = 0
    elif renumeracao > 762 and renumeracao <= 886.57:
        taxa = 0.145
        parcela_abater = taxa * 2.3 * (1136.14 - renumeracao)

    elif renumeracao > 886.57 and renumeracao <= 932.14:
        taxa = 0.210
        parcela_abater = taxa * 1.3 * (1402.55 - renumeracao)

    elif renumeracao > 932.14 and renumeracao <= 1067.00:
        taxa = 0.21
        parcela_abater = 128.43
    elif renumeracao > 1067.00 and renumeracao <= 1349.79:
        taxa = 0.2650
        parcela_abater = 214.11

    elif renumeracao > 1349.79 and renumeracao <= 1871.79:
        taxa = 0.2850
        parcela_abater = 214.11

    elif renumeracao > 1871.79 and renumeracao <= 1932.79:
        taxa = 0.350
        parcela_abater = 335.77

    elif renumeracao > 1932.79 and renumeracao <= 2131.14:
        taxa = 0.37
        parcela_abater = 374.43

    elif renumeracao > 2131.14 and renumeracao <= 3184.79:
        taxa = 0.4350
        parcela_abater = 512.95

    elif renumeracao > 3184.79 and renumeracao <= 5924.21:
        taxa = 0.45
        parcela_abater = 560.73

    elif renumeracao > 5924.21 and renumeracao <= 6007.43:
        taxa = 0.4800
        parcela_abater = 738.45


    elif renumeracao > 6007.43 and renumeracao <= 18150.29:
        taxa = 0.5050
        parcela_abater = 888.64

    else:
        taxa = 0.53
        parcela_abater = 1342.39

    valor_irs = (renumeracao * taxa) - parcela_abater
    renumeracao_liquida = renumeracao - valor_irs
    return valor_irs, parcela_abater, taxa, renumeracao_liquida

def pensao_casado_1t(renumeracao):
    if renumeracao <= 762:
        taxa = 0
        parcela_abater = 0

    elif renumeracao > 762 and renumeracao <= 886.57:
        taxa = 0.145
        parcela_abater = taxa * 2.3 * (1222.89 - renumeracao)

    elif renumeracao > 886.57 and renumeracao <= 932.14:
        taxa = 0.145
        parcela_abater = taxa * 1.883 * (1297.43 - renumeracao)

    elif renumeracao > 932.14 and renumeracao <= 1120.57:
        taxa = 0.145
        parcela_abater = 99.73
    elif renumeracao > 1120.57 and renumeracao <= 1151.21:
        taxa = 0.1593
        parcela_abater = 115.74

    elif renumeracao > 1151.21 and renumeracao <= 1771.79:
        taxa = 0.2480
        parcela_abater = 217.81

    elif (renumeracao > 1771.79 and renumeracao <= 1932.79):
        taxa = 0.2625
        parcela_abater = 243.59

    elif renumeracao > 1932.79 and renumeracao <= 2284.71:
        taxa = 0.2758
        parcela_abater = 269.35

    elif renumeracao > 2284.71 and renumeracao <= 3184.79:
        taxa = 0.3348
        parcela_abater = 404.10

    elif renumeracao > 3184.79 and renumeracao <= 5924.21:
        taxa = 0.3720
        parcela_abater = 522.65

    elif renumeracao > 5924.21 and renumeracao <= 6007.43:
        taxa = 0.4350
        parcela_abater = 895.69


    elif renumeracao > 6007.43 and renumeracao <= 18150.29:
        taxa = 0.4777
        parcela_abater = 1152.08

    else:
        taxa = 0.53
        parcela_abater = 2101.72

    valor_irs = (renumeracao * taxa) - parcela_abater
    renumeracao_liquida = renumeracao - valor_irs
    return valor_irs, parcela_abater, taxa, renumeracao_liquida

def pensao_solteiro_casado_2t_deficiente(renumeracao):

    if renumeracao <= 1573.29:
        taxa = 0
        parcela_abater = 0
    elif renumeracao > 1573.29 and renumeracao <= 1595.00:
        taxa = 0.2385
        parcela_abater = 375.23

    elif renumeracao > 1595.0 and renumeracao <= 1692.86:
        taxa = 0.2565
        parcela_abater = 403.94

    elif renumeracao > 1692.86 and renumeracao <= 1811.79:
        taxa = 0.2850
        parcela_abater = 452.19
    elif renumeracao > 1811.79 and renumeracao <= 2354.21:
        taxa = 0.35
        parcela_abater = 569.95

    elif renumeracao > 2354.21 and renumeracao <= 3174.00:
        taxa = 0.37
        parcela_abater = 617.04

    elif renumeracao > 3174 and renumeracao <= 4077.64:
        taxa = 0.4350
        parcela_abater = 823.35

    elif renumeracao > 4077.64 and renumeracao <= 6102.79:
        taxa = 0.45
        parcela_abater = 884.51

    elif renumeracao > 6102.79 and renumeracao <= 6186.00:
        taxa = 0.48
        parcela_abater = 1067.59

    elif renumeracao > 6186.00 and renumeracao <= 18328.86:
        taxa = 0.5050
        parcela_abater = 1222.24

    else:
        taxa = 0.53
        parcela_abater = 1680.47

    valor_irs = (renumeracao * taxa) - parcela_abater
    renumeracao_liquida = renumeracao - valor_irs
    return valor_irs, parcela_abater, taxa, renumeracao_liquida

def pensao_casado_1t_deficiente(renumeracao):
    if renumeracao <= 1744.18:
        taxa = 0
        parcela_abater = 0

    elif renumeracao > 1744.18 and renumeracao <= 2144.29:
        taxa = 0.1890
        parcela_abater = 329.65

    elif renumeracao > 2144.29 and renumeracao <= 2664.64:
        taxa = 0.21
        parcela_abater = 374.68

    elif renumeracao > 2664.64 and renumeracao <= 2711.36 :
        taxa = 0.2468
        parcela_abater = 472.84
    elif renumeracao > 2711.36 and renumeracao <= 2731.14:
        taxa = 0.2758
        parcela_abater = 551.44

    elif renumeracao > 2731.14 and renumeracao <= 2934.79:
        taxa = 0.3348
        parcela_abater = 715.52

    elif (renumeracao > 2934.79 and renumeracao <= 6102.79):
        taxa = 0.3720
        parcela_abater = 821.77

    elif renumeracao > 6102.79 and renumeracao <= 18328.66:
        taxa = 0.4777
        parcela_abater = 1206.05

    else:
        taxa = 0.53
        parcela_abater = 2429.05

    valor_irs = (renumeracao * taxa) - parcela_abater
    renumeracao_liquida = renumeracao - valor_irs
    return valor_irs, parcela_abater, taxa, renumeracao_liquida

def pensao_solteiro_casado_2t_deficiente_fa(renumeracao):

    if renumeracao <= 1608.54:
        taxa = 0
        parcela_abater = 0
    elif renumeracao > 1608.54 and renumeracao <= 1700.0:
        taxa = 0.2565
        parcela_abater = 412.59

    elif renumeracao > 1700 and renumeracao <= 1866.07:
        taxa = 0.2850
        parcela_abater = 461.04

    elif renumeracao > 1866.07 and renumeracao <= 2354.21:
        taxa = 0.35
        parcela_abater = 582.33
    elif renumeracao > 2354.21 and renumeracao <= 3302.57:
        taxa = 0.37
        parcela_abater = 629.42

    elif renumeracao > 3302.57 and renumeracao <= 4077.64:
        taxa = 0.4350
        parcela_abater = 844.09

    elif renumeracao > 4077.64 and renumeracao <= 6102.79:
        taxa = 0.45
        parcela_abater = 905.25

    elif renumeracao > 6102.79 and renumeracao <= 6186:
        taxa = 0.48
        parcela_abater = 1088.33

    elif renumeracao > 6186 and renumeracao <= 18328.86:
        taxa = 0.5050
        parcela_abater = 1242.98

    else:
        taxa = 0.53
        parcela_abater = 1701.21

    valor_irs = (renumeracao * taxa) - parcela_abater
    renumeracao_liquida = renumeracao - valor_irs
    return valor_irs, parcela_abater, taxa, renumeracao_liquida

def pensao_casado_1t_deficiente_fa(renumeracao):
    if renumeracao <= 1779.71:
        taxa = 0
        parcela_abater = 0
        parcela_dependente = 0
    elif renumeracao > 1779.71 and renumeracao <= 2144.29:
        taxa = 0.1890
        parcela_abater = 336.37

    elif renumeracao > 2144.29 and renumeracao <= 2454.64:
        taxa = 0.21
        parcela_abater = 380.77

    elif renumeracao > 2454.64 and renumeracao <= 2639.93:
        taxa = 0.2468
        parcela_abater = 471.19
    elif renumeracao > 2639.93 and renumeracao <= 2816.86:
        taxa = 0.2758
        parcela_abater = 547.72

    elif renumeracao > 2816.86 and renumeracao <= 4077.64:
        taxa = 0.3348
        parcela_abater = 713.86

    elif (renumeracao > 4077.64 and renumeracao <= 6102.79):
        taxa = 0.3720
        parcela_abater = 865.64

    elif renumeracao > 6102.79 and renumeracao <= 18328.66:
        taxa = 0.4777
        parcela_abater = 1513.94

    else:
        taxa = 0.53
        parcela_abater = 24272.93

    valor_irs = (renumeracao * taxa) - parcela_abater
    renumeracao_liquida = renumeracao - valor_irs
    return valor_irs, parcela_abater, taxa, renumeracao_liquida

