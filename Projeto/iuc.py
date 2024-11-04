def iuc(categoria, tabela, combustivel, cilindrada, ano, ciclo, co2, eixos, peso, suspensao):
    valor = 0
    imposto_diesel = 0
    valor_total = 0
    taxa_co2 = 0
    taxa_adicional = 0
    coeficiente = 1

    if categoria == "a" or categoria == "A":
        if tabela == "A" or tabela == "a":
            if cilindrada < 1000:
                if ano > 1995:
                    valor = 19.34
                elif ano >= 1990 and ano <= 1995:
                    valor = 12.20
                elif ano >= 1981 and ano <= 1989:
                    valor = 8.55
            elif cilindrada >= 1000 and cilindrada <= 1300:
                if ano > 1995:
                    valor = 38.82
                elif ano >= 1990 and ano <= 1995:
                    valor = 21.82
                elif ano >= 1981 and ano <= 1989:
                    valor = 12.20
            elif cilindrada > 1300 and cilindrada <= 1750:
                if ano > 1995:
                    valor = 60.64
                elif ano >= 1990 and ano <= 1995:
                    valor = 33.89
                elif ano >= 1981 and ano <= 1989:
                    valor = 17.00
            elif cilindrada > 1750 and cilindrada <= 2600:
                if ano > 1995:
                    valor = 153.85
                elif ano >= 1990 and ano <= 1995:
                    valor = 81.14
                elif ano >= 1981 and ano <= 1989:
                    valor = 35.07
            elif cilindrada > 2600 and cilindrada <= 3500:
                if ano > 1995:
                    valor = 279.39
                elif ano >= 1990 and ano <= 1995:
                    valor = 152.13
                elif ano >= 1981 and ano <= 1989:
                    valor = 77.47
            else:
                if ano > 1995:
                    valor = 497.79
                elif ano >= 1990 and ano <= 1995:
                    valor = 255.69
                elif ano >= 1981 and ano <= 1989:
                    valor = 177.49

            if combustivel == 1:
                imposto_diesel = 0

            elif combustivel == 2:
                if cilindrada < 1500:
                    if ano > 1995:
                        imposto_diesel = 3.14
                    elif ano >= 1990 and ano <= 1995:
                        imposto_diesel = 1.98
                    elif ano >= 1981 and ano <= 1989:
                        imposto_diesel = 1.39
                elif cilindrada >= 1500 and cilindrada < 2000:
                    if ano > 1995:
                        imposto_diesel = 6.31
                    elif ano >= 1990 and ano <= 1995:
                        imposto_diesel = 3.55
                    elif ano >= 1981 and ano <= 1989:
                        imposto_diesel = 1.98
                elif cilindrada >= 2000 and cilindrada < 3000:
                    if ano > 1995:
                        imposto_diesel = 9.86
                    elif ano >= 1990 and ano <= 1995:
                        imposto_diesel = 5.51
                    elif ano >= 1981 and ano <= 1989:
                        imposto_diesel = 2.76
                else:
                    if ano > 1995:
                        imposto_diesel = 25.01
                    elif ano >= 1990 and ano <= 1995:
                        imposto_diesel = 13.19
                    elif ano >= 1981 and ano <= 1989:
                        imposto_diesel = 5.70
            valor_total = valor + imposto_diesel




        elif tabela == "B" or tabela == "b":
            if cilindrada < 1250:
                valor = 30.87
            elif cilindrada >= 1250 and cilindrada < 1750:
                valor = 61.94
            elif cilindrada >= 1750 and cilindrada < 2500:
                valor = 123.76
            else:
                valor = 423.55



            if ano == 2007:
                coeficiente = 1
            elif ano == 2008:
                coeficiente = 1.05
            elif ano == 2009:
                coeficiente = 1.10
            else:
                coeficiente = 1.15




            if combustivel == 1:
                imposto_diesel = 0
            elif combustivel == 2:
                if cilindrada <= 1250:
                    imposto_diesel = 5.02
                elif cilindrada >= 1251 and cilindrada <= 1750:
                    imposto_diesel = 10.07
                elif cilindrada >= 1751 and cilindrada <= 2500:
                    imposto_diesel = 20.12
                else:
                    imposto_diesel = 68.85


            if ciclo == 1:
                if co2 <= 120:
                    taxa_co2 = 63.22
                elif co2 >= 121 and co2 <= 180:
                    taxa_co2 = 94.88
                elif co2 >= 181 and co2 <= 250:
                    taxa_co2 = 206.07
                    taxa_adicional = 30.87
                else:
                    taxa_co2 = 353.01
                    taxa_adicional = 61.94
            elif ciclo == 2:
                if co2 <= 140:
                    taxa_co2 = 63.22
                elif co2 >= 141 and co2 <= 205:
                    taxa_co2 = 94.88
                elif co2 >= 206 and co2 <= 260:
                    taxa_co2 = 206.07
                    taxa_adicional = 30.87
                else:
                    taxa_co2 = 353.01
                    taxa_adicional = 61.94
            valor_total = ((valor + taxa_co2 + taxa_adicional) * coeficiente) + imposto_diesel




### MOTAS ###
    elif  categoria == "E" or categoria == "e":
        if cilindrada <= 119:
            valor = 0
        elif cilindrada >= 120 and cilindrada <= 250:
            if ano >= 1992 and ano <= 1996:
                valor = 0
            elif ano >= 1997 and ano <=2023:
                valor= 6.02
        elif cilindrada >= 251 and cilindrada <= 350:
            if ano >= 1992 and ano <= 1996:
                valor = 6.02
            elif ano >= 1997 and ano <=2023:
                valor = 8.51
        elif cilindrada >= 351 and cilindrada <= 500:
            if ano >= 1992 and ano <= 1996:
                valor = 12.18
            elif ano >= 1997 and ano <= 2023:
                valor = 20.58
        elif cilindrada >= 501 and cilindrada <= 750:
            if ano >= 1992 and ano <= 1996:
                valor = 36.41
            elif ano >= 1997 and ano <= 2023:
                valor = 61.83
        elif cilindrada >= 750:
            if ano >= 1992 and ano <= 1996:
                valor = 65.85
            elif ano >= 1997  and ano <= 2023:
                valor = 134.26
        valor_total = valor

 ###VEICULOS CATEGORTIA C###
    elif categoria == "C1" or categoria == "c1": #peso inferior a 12t
        if peso <= 2500:
            valor = 32.42
        elif peso >= 2501 and peso <= 3500:
            valor = 53.69
        elif peso >= 3501 and peso <= 7500:
            valor= 128.65
        elif peso >= 7501 and peso <= 11999:
            valor = 208.68
        valor_total = valor
    elif categoria == "C2" or categoria == "c2": #peso maior que 12t
        if eixos == 2:
            if ano <= 1990:
                if suspensao == 1: ## suspensão pneumatica ou equivalente ##
                    if peso == 12000:
                        valor = 226
                    elif peso >= 12001 and peso <= 12999:
                        valor= 321
                    elif peso >= 13000 and peso <= 14999:
                        valor = 324
                    elif peso >= 15000 and peso <= 17999:
                         valor= 361
                    else:
                        valor = 458
                elif suspensao == 2: ## outro suspensão  ##
                    if peso == 12000:
                        valor = 234
                    elif peso >= 12001 and peso <= 12999:
                        valor= 378
                    elif peso >= 13000 and peso <= 14999:
                        valor = 383
                    elif peso >= 15000 and peso <= 17999:
                         valor= 402
                    else:
                        valor = 510

            if ano >= 1991  and ano <= 1993:
                if suspensao == 1: ## suspensão pneumatica ou equivalente ##
                    if peso == 12000:
                        valor = 209
                    elif peso >= 12001 and peso <= 12999:
                        valor= 298
                    elif peso >= 13000 and peso <= 14999:
                        valor = 300
                    elif peso >= 15000 and peso <= 17999:
                         valor= 335
                    else:
                        valor = 425
                elif suspensao == 2: ## outro suspensão  ##
                    if peso == 12000:
                        valor = 219
                    elif peso >= 12001 and peso <= 12999:
                        valor= 349
                    elif peso >= 13000 and peso <= 14999:
                        valor = 355
                    elif peso >= 15000 and peso <= 17999:
                         valor= 376
                    else:
                        valor = 473
            if ano >= 1994 and ano <= 1996:
                if suspensao == 1: ## suspensão pneumatica ou equivalente ##
                    if peso == 12000:
                        valor = 198
                    elif peso >= 12001 and peso <= 12999:
                        valor= 285
                    elif peso >= 13000 and peso <= 14999:
                        valor = 288
                    elif peso >= 15000 and peso <= 17999:
                         valor= 321
                    else:
                        valor = 407
                elif suspensao == 2: ## outro suspensão  ##
                    if peso == 12000:
                        valor = 208
                    elif peso >= 12001 and peso <= 12999:
                        valor= 334
                    elif peso >= 13000 and peso <= 14999:
                        valor = 338
                    elif peso >= 15000 and peso <= 17999:
                         valor= 358
                    else:
                        valor = 452
            if ano >= 1997 and ano <= 1999:
                if suspensao == 1: ## suspensão pneumatica ou equivalente ##
                    if peso == 12000:
                        valor = 191
                    elif peso >= 12001 and peso <= 12999:
                        valor= 274
                    elif peso >= 13000 and peso <= 14999:
                        valor = 277
                    elif peso >= 15000 and peso <= 17999:
                         valor= 307
                    else:
                        valor = 392
                elif suspensao == 2: ## outro suspensão  ##
                    if peso == 12000:
                        valor = 198
                    elif peso >= 12001 and peso <= 12999:
                        valor= 322
                    elif peso >= 13000 and peso <= 14999:
                        valor = 326
                    elif peso >= 15000 and peso <= 17999:
                         valor= 343
                    else:
                        valor = 433
            if ano >= 2000:
                if suspensao == 1: ## suspensão pneumatica ou equivalente ##
                    if peso == 12000:
                        valor = 189
                    elif peso >= 12001 and peso <= 12999:
                        valor= 271
                    elif peso >= 13000 and peso <= 14999:
                        valor = 275
                    elif peso >= 15000 and peso <= 17999:
                         valor= 305
                    else:
                        valor = 389
                elif suspensao == 2: ## outro suspensão  ##
                    if peso == 12000:
                        valor = 196
                    elif peso >= 12001 and peso <= 12999:
                        valor= 320
                    elif peso >= 13000 and peso <= 14999:
                        valor = 324
                    elif peso >= 15000 and peso <= 17999:
                         valor= 340
                    else:
                        valor = 428
        elif eixos == 3:
            if ano<= 1990:
                if suspensao == 1:
                    if peso < 15000:
                        valor = 226
                    elif peso >= 15000 and peso <=16999:
                        valor = 318
                    elif peso >= 17000 and peso <= 17999:
                        valor = 318
                    elif peso >= 18000 and peso <= 18999:
                        valor = 413
                    elif peso >= 19000 and peso <= 20999:
                        valor = 414
                    elif peso >= 21000 and peso <= 22999:
                        valor = 416
                    else:
                        valor = 465
                elif suspensao == 2:
                    if peso < 15000:
                        valor = 321
                    elif peso >= 15000 and peso <=16999:
                        valor = 359
                    elif peso >= 17000 and peso <= 17999:
                        valor = 367
                    elif peso >= 18000 and peso <= 18999:
                        valor = 456
                    elif peso >= 19000 and peso <= 20999:
                        valor = 456
                    elif peso >= 21000 and peso <= 22999:
                        valor = 462
                    else:
                        valor = 517
            elif ano >= 1991 and ano <= 1993:
                if suspensao == 1:
                    if peso < 15000:
                        valor = 209
                    elif peso >= 15000 and peso <=16999:
                        valor = 295
                    elif peso >= 17000 and peso <= 17999:
                        valor = 295
                    elif peso >= 18000 and peso <= 18999:
                        valor = 384
                    elif peso >= 19000 and peso <= 20999:
                        valor = 386
                    elif peso >= 21000 and peso <= 22999:
                        valor = 387
                    else:
                        valor = 432
                elif suspensao == 2:
                    if peso < 15000:
                        valor = 297
                    elif peso >= 15000 and peso <=16999:
                        valor = 333
                    elif peso >= 17000 and peso <= 17999:
                        valor = 340
                    elif peso >= 18000 and peso <= 18999:
                        valor = 423
                    elif peso >= 19000 and peso <= 20999:
                        valor = 423
                    elif peso >= 21000 and peso <= 22999:
                        valor = 427
                    else:
                        valor = 482
            elif ano >= 1994 and ano <= 1996:
                if suspensao == 1:
                    if peso < 15000:
                        valor = 198
                    elif peso >= 15000 and peso <=16999:
                        valor = 282
                    elif peso >= 17000 and peso <= 17999:
                        valor = 282
                    elif peso >= 18000 and peso <= 18999:
                        valor = 367
                    elif peso >= 19000 and peso <= 20999:
                        valor = 369
                    elif peso >= 21000 and peso <= 22999:
                        valor = 372
                    else:
                        valor = 414
                if suspensao == 2:
                    if peso < 15000:
                        valor = 284
                    elif peso >= 15000 and peso <=16999:
                        valor = 320
                    elif peso >= 17000 and peso <= 17999:
                        valor = 325
                    elif peso >= 18000 and peso <= 18999:
                        valor = 405
                    elif peso >= 19000 and peso <= 20999:
                        valor = 409
                    elif peso >= 21000 and peso <= 22999:
                        valor = 460
                    else:
                        valor = 460
            elif ano >= 1997 and ano <= 1999:
                if suspensao == 1:
                    if peso < 15000:
                        valor = 190
                    elif peso >= 15000 and peso <=16999:
                        valor = 270
                    elif peso >= 17000 and peso <= 17999:
                        valor = 270
                    elif peso >= 18000 and peso <= 18999:
                        valor = 350
                    elif peso >= 19000 and peso <= 20999:
                        valor = 353
                    elif peso >= 21000 and peso <= 22999:
                        valor = 355
                    else:
                        valor = 396
                elif suspensao == 2:
                    if peso < 15000:
                        valor = 274
                    elif peso >= 15000 and peso <=16999:
                        valor = 305
                    elif peso >= 17000 and peso <= 17999:
                        valor = 312
                    elif peso >= 18000 and peso <= 18999:
                        valor = 390
                    elif peso >= 19000 and peso <= 20999:
                        valor = 390
                    elif peso >= 21000 and peso <= 22999:
                        valor = 393
                    else:
                        valor = 440
            elif ano >= 2000:
                if suspensao == 1:
                    if peso < 15000:
                        valor = 189
                    elif peso >= 15000 and peso <=16999:
                        valor = 268
                    elif peso >= 17000 and peso <= 17999:
                        valor = 268
                    elif peso >= 18000 and peso <= 18999:
                        valor = 347
                    elif peso >= 19000 and peso <= 20999:
                        valor = 349
                    elif peso >= 21000 and peso <= 22999:
                        valor = 350
                    else:
                        valor = 394
                elif suspensao == 2:
                    if peso < 15000:
                        valor = 271
                    elif peso >= 15000 and peso <=16999:
                        valor = 302
                    elif peso >= 17000 and peso <= 17999:
                        valor = 309
                    elif peso >= 18000 and peso <= 18999:
                        valor = 386
                    elif peso >= 19000 and peso <= 20999:
                        valor = 391
                    elif peso >= 21000 and peso <= 22999:
                        valor = 437
                    else:
                        valor = 437
        else :
            if ano <= 1990:
                if suspensao == 1:
                    if peso < 23000:
                        valor = 319
                    elif peso >= 23000 and peso <= 24999:
                        valor = 402
                    elif peso >= 25000 and peso <= 25999:
                        valor = 413
                    elif peso >= 26000 and peso <= 26999:
                         valor = 757
                    elif peso >= 27000 and peso <= 28999:
                        valor = 767
                    else:
                        valor = 790

                elif suspensao == 2:
                    if peso < 23000:
                        valor = 357
                    elif peso >= 23000 and peso <= 24999:
                        valor = 453
                    elif peso >= 25000 and peso <= 25999:
                        valor = 456
                    elif peso >= 26000 and peso <= 26999:
                        valor = 857
                    elif peso >= 27000 and peso <= 28999:
                        valor = 877
                    else:
                        valor = 890
            elif ano >= 1991 and ano <= 1993:
                if suspensao == 1:
                    if peso < 23000:
                        valor = 296
                    elif peso >= 23000 and peso <= 24999:
                        valor = 376
                    elif peso >= 25000 and peso <= 25999:
                        valor = 384
                    elif peso >= 26000 and peso <= 26999:
                         valor = 704
                    elif peso >= 27000 and peso <= 28999:
                        valor = 713
                    else:
                        valor = 732

                elif suspensao == 2:
                    if peso < 23000:
                        valor = 331
                    elif peso >= 23000 and peso <= 24999:
                        valor = 421
                    elif peso >= 25000 and peso <= 25999:
                        valor = 423
                    elif peso >= 26000 and peso <= 26999:
                        valor = 799
                    elif peso >= 27000 and peso <= 28999:
                        valor = 817
                    else:
                        valor = 828
            elif ano >= 1994 and ano <= 1996:
                if suspensao == 1:
                    if peso < 23000:
                        valor = 282
                    elif peso >= 23000 and peso <= 24999:
                        valor = 358
                    elif peso >= 25000 and peso <= 25999:
                        valor = 367
                    elif peso >= 26000 and peso <= 26999:
                         valor = 671
                    elif peso >= 27000 and peso <= 28999:
                        valor = 680
                    else:
                        valor = 700

                elif suspensao == 2:
                    if peso < 23000:
                        valor = 318
                    elif peso >= 23000 and peso <= 24999:
                        valor = 402
                    elif peso >= 25000 and peso <= 25999:
                        valor = 405
                    elif peso >= 26000 and peso <= 26999:
                        valor = 761
                    elif peso >= 27000 and peso <= 28999:
                        valor = 780
                    else:
                        valor = 793
            elif ano >= 1997 and ano <= 1999:
                if suspensao == 1:
                    if peso < 23000:
                        valor = 271
                    elif peso >= 23000 and peso <= 24999:
                        valor = 343
                    elif peso >= 25000 and peso <= 25999:
                        valor = 350
                    elif peso >= 26000 and peso <= 26999:
                         valor = 645
                    elif peso >= 27000 and peso <= 28999:
                        valor = 655
                    else:
                        valor = 671

                elif suspensao == 2:
                    if peso < 23000:
                        valor = 302
                    elif peso >= 23000 and peso <= 24999:
                        valor = 387
                    elif peso >= 25000 and peso <= 25999:
                        valor = 390
                    elif peso >= 26000 and peso <= 26999:
                        valor = 730
                    elif peso >= 27000 and peso <= 28999:
                        valor = 751
                    else:
                        valor = 760

            else:
                if suspensao == 1:
                    if peso < 23000:
                        valor = 268
                    elif peso >= 23000 and peso <= 24999:
                        valor = 340
                    elif peso >= 25000 and peso <= 25999:
                        valor = 347
                    elif peso >= 26000 and peso <= 26999:
                         valor = 640
                    elif peso >= 27000 and peso <= 28999:
                        valor = 649
                    else:
                        valor = 666

                elif suspensao == 2:
                    if peso < 23000:
                        valor = 300
                    elif peso >= 23000 and peso <= 24999:
                        valor = 384
                    elif peso >= 25000 and peso <= 25999:
                        valor = 386
                    elif peso >= 26000 and peso <= 26999:
                        valor = 723
                    elif peso >= 27000 and peso <= 28999:
                        valor = 744
                    else:
                        valor = 755
        valor_total = valor
    elif categoria == "C3" or categoria == "c3": #articulados
        if eixos == "2+1":
            if ano <= 1990:
                if suspensao == 1: ## suspensão pneumatica ou equivalente ##
                    if peso == 12000:
                        valor = 225
                    elif peso >= 12001 and peso <= 17999:
                        valor= 311
                    elif peso >= 18000 and peso <= 24999:
                        valor = 413
                    elif peso >= 25000 and peso <= 25999:
                         valor= 446
                    else:
                        valor = 831
                elif suspensao == 2: ## outro suspensão  ##
                    if peso == 12000:
                        valor = 227
                    elif peso >= 12001 and peso <= 17999:
                        valor= 383
                    elif peso >= 18000 and peso <= 24999:
                        valor = 486
                    elif peso >= 25000 and peso <= 25999:
                         valor= 498
                    else:
                        valor = 915

            elif ano >= 1991  and ano <= 1993:
                if suspensao == 1: ## suspensão pneumatica ou equivalente ##
                    if peso == 12000:
                        valor = 208
                    elif peso >= 12001 and peso <= 17999:
                        valor= 292
                    elif peso >= 18000 and peso <= 24999:
                        valor = 387
                    elif peso >= 25000 and peso <= 25999:
                         valor= 419
                    else:
                        valor = 780
                elif suspensao == 2: ## outro suspensão  ##
                    if peso == 12000:
                        valor = 210
                    elif peso >= 12001 and peso <= 17999:
                        valor = 355
                    elif peso >= 18000 and peso <= 24999:
                        valor = 452
                    elif peso >= 25000 and peso <= 25999:
                        valor = 464
                    else:
                        valor = 850
            elif ano >= 1994 and ano <= 1996:
                if suspensao == 1: ## suspensão pneumatica ou equivalente ##
                    if peso == 12000:
                        valor = 197
                    elif peso >= 12001 and peso <= 17999:
                        valor= 280
                    elif peso >= 18000 and peso <= 24999:
                        valor = 372
                    elif peso >= 25000 and peso <= 25999:
                         valor= 400
                    else:
                        valor = 745

                elif suspensao == 2: ## outro suspensão  ##
                    if peso == 12000:
                        valor = 200
                    elif peso >= 12001 and peso <= 17999:
                        valor = 337
                    elif peso >= 18000 and peso <= 24999:
                        valor = 431
                    elif peso >= 25000 and peso <= 25999:
                        valor = 441
                    else:
                        valor = 812
            elif ano >= 1997 and ano <= 1999:
                if suspensao == 1: ## suspensão pneumatica ou equivalente ##
                    if peso == 12000:
                        valor = 190
                    elif peso >= 12001 and peso <= 17999:
                        valor= 270
                    elif peso >= 18000 and peso <= 24999:
                        valor = 358
                    elif peso >= 25000 and peso <= 25999:
                         valor= 387
                    else:
                        valor = 717
                elif suspensao == 2: ## outro suspensão  ##
                    if peso == 12000:
                        valor = 192
                    elif peso >= 12001 and peso <= 12999:
                        valor= 325
                    elif peso >= 13000 and peso <= 14999:
                        valor = 415
                    elif peso >= 15000 and peso <= 17999:
                         valor= 424
                    else:
                        valor = 779
            else:
                if suspensao == 1: ## suspensão pneumatica ou equivalente ##
                    if peso == 12000:
                        valor = 188
                    elif peso >= 12001 and peso <= 17999:
                        valor = 268
                    elif peso >= 18000 and peso <= 24999:
                        valor = 354
                    elif peso >= 25000 and peso <= 25999:
                        valor = 385
                    else:
                        valor = 713
                elif suspensao == 2: ## outro suspensão  ##
                    if peso == 12000:
                        valor = 191
                    elif peso >= 12001 and peso <= 12999:
                        valor= 323
                    elif peso >= 13000 and peso <= 14999:
                        valor = 412
                    elif peso >= 15000 and peso <= 17999:
                         valor= 421
                    else:
                        valor = 772
        elif eixos == "2+2":
            if ano<= 1990:
                if suspensao == 1:
                    if peso < 23000:
                        valor = 307
                    elif peso >= 23000 and peso <=25999:
                        valor = 397
                    elif peso >= 26000 and peso <= 30999:
                        valor = 758
                    elif peso >= 31000 and peso <= 32999:
                        valor = 819
                    else:
                        valor = 871
                elif suspensao == 2:
                    if peso < 23000:
                        valor = 353
                    elif peso >= 23000 and peso <=25999:
                        valor = 449
                    elif peso >= 26000 and peso <= 30999:
                        valor = 863
                    elif peso >= 31000 and peso <= 32999:
                        valor = 886
                    else:
                        valor = 1051
            elif ano >= 1991 and ano <= 1993:
                if suspensao == 1:
                    if peso < 23000:
                        valor = 290
                    elif peso >= 23000 and peso <= 25999:
                        valor = 375
                    elif peso >= 26000 and peso <= 30999:
                        valor = 710
                    elif peso >= 31000 and peso <= 32999:
                        valor = 768
                    else:
                        valor = 819
                elif suspensao == 2:
                    if peso < 23000:
                        valor = 328
                    elif peso >= 23000 and peso <= 25999:
                        valor = 419
                    elif peso >= 26000 and peso <= 30999:
                        valor = 804
                    elif peso >= 31000 and peso <= 32999:
                        valor = 825
                    else:
                        valor = 976
            elif ano >= 1994 and ano <= 1996:
                if suspensao == 1:
                    if peso < 23000:
                        valor = 277
                    elif peso >= 23000 and peso <= 25999:
                        valor = 355
                    elif peso >= 26000 and peso <= 30999:
                        valor = 676
                    elif peso >= 31000 and peso <= 32999:
                        valor = 732
                    else:
                        valor = 781
                elif suspensao == 2:
                    if peso < 23000:
                        valor = 312
                    elif peso >= 23000 and peso <= 25999:
                        valor = 400
                    elif peso >= 26000 and peso <= 30999:
                        valor = 767
                    elif peso >= 31000 and peso <= 32999:
                        valor = 790
                    else:
                        valor = 933
            elif ano >= 1997 and ano <= 1999:
                if suspensao == 1:
                    if peso < 23000:
                        valor = 267
                    elif peso >= 23000 and peso <= 25999:
                        valor = 344
                    elif peso >= 26000 and peso <= 30999:
                        valor = 656
                    elif peso >= 31000 and peso <= 32999:
                        valor = 709
                    else:
                        valor = 757
                elif suspensao == 2:
                    if peso < 23000:
                        valor = 300
                    elif peso >= 23000 and peso <= 25999:
                        valor = 385
                    elif peso >= 26000 and peso <= 30999:
                        valor = 737
                    elif peso >= 31000 and peso <= 32999:
                        valor = 757
                    else:
                        valor = 898
            elif ano >= 2000:
                if suspensao == 1:
                    if peso < 23000:
                        valor = 266
                    elif peso >= 23000 and peso <= 25999:
                        valor = 342
                    elif peso >= 26000 and peso <= 30999:
                        valor = 650
                    elif peso >= 31000 and peso <= 32999:
                        valor = 704
                    else:
                        valor = 751
                elif suspensao == 2:
                    if peso < 23000:
                        valor = 298
                    elif peso >= 23000 and peso <= 25999:
                        valor = 382
                    elif peso >= 26000 and peso <= 30999:
                        valor = 730
                    elif peso >= 31000 and peso <= 32999:
                        valor = 751
                    else:
                        valor = 888
        elif eixos == "2+3":
            if ano<= 1990:
                if suspensao == 1:
                    if peso < 36000:
                        valor = 771
                    elif peso >= 36000 and peso <=37999:
                        valor = 851
                    else:
                        valor = 882
                elif suspensao == 2:
                    if peso < 36000:
                        valor = 868
                    elif peso >= 36000 and peso <=37999:
                        valor = 824
                    else:
                        valor = 1040
            elif ano >= 1991 and ano <= 1993:
                if suspensao == 1:
                    if peso < 36000:
                        valor = 722
                    elif peso >= 36000 and peso <=37999:
                        valor = 801
                    else:
                        valor = 827
                elif suspensao == 2:
                    if peso < 36000:
                        valor = 808
                    elif peso >= 36000 and peso <=37999:
                        valor = 865
                    else:
                        valor = 976
            elif ano >= 1994 and ano <= 1996:
                if suspensao == 1:
                    if peso < 36000:
                        valor = 691
                    elif peso >= 36000 and peso <=37999:
                        valor = 764
                    else:
                        valor = 792
                elif suspensao == 2:
                    if peso < 36000:
                        valor = 771
                    elif peso >= 36000 and peso <=37999:
                        valor = 827
                    else:
                        valor = 930
            elif ano >= 1997 and ano <= 1999:
                if suspensao == 1:
                    if peso < 36000:
                        valor = 669
                    elif peso >= 36000 and peso <=37999:
                        valor = 738
                    else:
                        valor = 765
                elif suspensao == 2:
                    if peso < 36000:
                        valor = 742
                    elif peso >= 36000 and peso <=37999:
                        valor = 801
                    else:
                        valor = 901
            elif ano >= 2000:

                if suspensao == 1:
                    if peso < 36000:
                        valor = 663
                    elif peso >= 36000 and peso <=37999:
                        valor = 731
                    else:
                        valor = 759
                elif suspensao == 2:
                    if peso < 36000:
                        valor = 733
                    elif peso >= 36000 and peso <=37999:
                        valor = 795
                    else:
                        valor = 893
        elif eixos == "3+2":
            if ano<= 1990:
                if suspensao == 1:
                    if peso < 36000:
                        valor = 765
                    elif peso >= 36000 and peso <= 37999:
                        valor = 784
                    elif peso >= 38000 and peso <= 39999:
                        valor = 786
                    else:
                        valor = 915
                elif suspensao == 2:
                    if peso < 36000:
                        valor = 844
                    elif peso >= 36000 and peso <=37999:
                        valor = 893
                    elif peso >= 38000 and peso <= 39999:
                        valor = 950
                    else:
                        valor = 1175
            elif ano >= 1991 and ano <= 1993:
                if suspensao == 1:
                    if peso < 36000:
                        valor = 717
                    elif peso >= 36000 and peso <= 37999:
                        valor = 737
                    elif peso >= 38000 and peso <= 39999:
                        valor = 738
                    else:
                        valor = 858
                elif suspensao == 2:
                    if peso < 36000:
                        valor = 784
                    elif peso >= 36000 and peso <= 37999:
                        valor = 831
                    elif peso >= 38000 and peso <= 39999:
                        valor = 882
                    else:
                        valor = 1094
            elif ano >= 1994 and ano <= 1996:
                if suspensao == 1:
                    if peso < 36000:
                        valor = 686
                    elif peso >= 36000 and peso <= 37999:
                        valor = 704
                    elif peso >= 38000 and peso <= 39999:
                        valor = 705
                    else:
                        valor = 819
                elif suspensao == 2:
                    if peso < 36000:
                        valor = 751
                    elif peso >= 36000 and peso <= 37999:
                        valor = 795
                    elif peso >= 38000 and peso <= 39999:
                        valor = 843
                    else:
                        valor = 1045
            elif ano >= 1997 and ano <= 1999:
                if suspensao == 1:
                    if peso < 36000:
                        valor = 663
                    elif peso >= 36000 and peso <= 37999:
                        valor = 667
                    elif peso >= 38000 and peso <= 39999:
                        valor = 680
                    else:
                        valor = 795

                elif suspensao == 2:
                    if peso < 36000:
                        valor = 718
                    elif peso >= 36000 and peso <= 37999:
                        valor = 761
                    elif peso >= 38000 and peso <= 39999:
                        valor = 809
                    else:
                        valor = 1003
            elif ano >= 2000:
                if suspensao == 1:
                    if peso < 36000:
                        valor = 658
                    elif peso >= 36000 and peso <= 37999:
                        valor = 672
                    elif peso >= 38000 and peso <= 39999:
                        valor = 673
                    else:
                        valor = 787

                elif suspensao == 2:
                    if peso < 36000:
                        valor = 717
                    elif peso >= 36000 and peso <= 37999:
                        valor = 760
                    elif peso >= 38000 and peso <= 39999:
                        valor = 807
                    else:
                        valor = 1002
        else:
            if ano<= 1990:
                if suspensao == 1:
                    if peso < 36000:
                        valor = 715
                    elif peso >= 36000 and peso <= 37999:
                        valor = 843
                    elif peso >= 38000 and peso <= 39999:
                        valor = 851
                    else:
                        valor = 870
                elif suspensao == 2:
                    if peso < 36000:
                        valor = 847
                    elif peso >= 36000 and peso <=37999:
                        valor = 936
                    elif peso >= 38000 and peso <= 39999:
                        valor = 953
                    else:
                        valor = 967
            elif ano >= 1991 and ano <= 1993:
                if suspensao == 1:
                    if peso < 36000:
                        valor = 670
                    elif peso >= 36000 and peso <= 37999:
                        valor = 793
                    elif peso >= 38000 and peso <= 39999:
                        valor = 800
                    else:
                        valor = 816
                elif suspensao == 2:
                    if peso < 36000:
                        valor = 790
                    elif peso >= 36000 and peso <= 37999:
                        valor = 870
                    elif peso >= 38000 and peso <= 39999:
                        valor = 884
                    else:
                        valor = 901
            elif ano >= 1994 and ano <= 1996:
                if suspensao == 1:
                    if peso < 36000:
                        valor = 641
                    elif peso >= 36000 and peso <= 37999:
                        valor = 756
                    elif peso >= 38000 and peso <= 39999:
                        valor = 763
                    else:
                        valor = 780
                elif suspensao == 2:
                    if peso < 36000:
                        valor = 752
                    elif peso >= 36000 and peso <= 37999:
                        valor = 842
                    elif peso >= 38000 and peso <= 39999:
                        valor = 846
                    else:
                        valor = 858
            elif ano >= 1997 and ano <= 1999:
                if suspensao == 1:
                    if peso < 36000:
                        valor = 620
                    elif peso >= 36000 and peso <= 37999:
                        valor = 730
                    elif peso >= 38000 and peso <= 39999:
                        valor = 737
                    else:
                        valor = 756

                elif suspensao == 2:
                    if peso < 36000:
                        valor = 721
                    elif peso >= 36000 and peso <= 37999:
                        valor = 800
                    elif peso >= 38000 and peso <= 39999:
                        valor = 812
                    else:
                        valor = 825
            elif ano >= 2000:
                if suspensao == 1:
                    if peso < 36000:
                        valor = 613
                    elif peso >= 36000 and peso <= 37999:
                        valor = 723
                    elif peso >= 38000 and peso <= 39999:
                        valor = 730
                    else:
                        valor = 748

                elif suspensao == 2:
                    if peso < 36000:
                        valor = 716
                    elif peso >= 36000 and peso <= 37999:
                        valor = 793
                    elif peso >= 38000 and peso <= 39999:
                        valor = 806
                    else:
                        valor = 819
        valor_total = valor
###veiculos publicos###

    elif categoria == "D1" or categoria == "d1":  # peso inferior a 12t
        if peso <= 2500:
            valor = 17.22
        elif peso >= 2501 and peso <= 3500:
            valor = 29.38
        elif peso >= 3501 and peso <= 7500:
            valor = 66.86
        elif peso >= 7501 and peso <= 11999:
            valor = 111.43
        valor_total = valor

    elif categoria == "D2" or categoria == "d2":  # peso maior que 12t
        if eixos == 2:
            if ano <= 1990:
                if suspensao == 1:  ## suspensão pneumatica ou equivalente ##
                    if peso == 12000:
                        valor = 131
                    elif peso >= 12001 and peso <= 12999:
                        valor = 152
                    elif peso >= 13000 and peso <= 14999:
                        valor = 154
                    elif peso >= 15000 and peso <= 17999:
                        valor = 188
                    else:
                        valor = 222
                elif suspensao == 2:  ## outro suspensão  ##
                    if peso == 12000:
                        valor = 135
                    elif peso >= 12001 and peso <= 12999:
                        valor = 197
                    elif peso >= 13000 and peso <= 14999:
                        valor = 198
                    elif peso >= 15000 and peso <= 17999:
                        valor = 274
                    else:
                        valor = 344

            if ano >= 1991 and ano <= 1993:
                if suspensao == 1:  ## suspensão pneumatica ou equivalente ##
                    if peso == 12000:
                        valor = 123
                    elif peso >= 12001 and peso <= 12999:
                        valor = 143
                    elif peso >= 13000 and peso <= 14999:
                        valor = 145
                    elif peso >= 15000 and peso <= 17999:
                        valor = 177
                    else:
                        valor = 207
                elif suspensao == 2:  ## outro suspensão  ##
                    if peso == 12000:
                        valor = 127
                    elif peso >= 12001 and peso <= 12999:
                        valor = 185
                    elif peso >= 13000 and peso <= 14999:
                        valor = 186
                    elif peso >= 15000 and peso <= 17999:
                        valor = 254
                    else:
                        valor = 325
            if ano >= 1994 and ano <= 1996:
                if suspensao == 1:  ## suspensão pneumatica ou equivalente ##
                    if peso == 12000:
                        valor = 115
                    elif peso >= 12001 and peso <= 12999:
                        valor = 137
                    elif peso >= 13000 and peso <= 14999:
                        valor = 139
                    elif peso >= 15000 and peso <= 17999:
                        valor = 170
                    else:
                        valor = 198
                elif suspensao == 2:  ## outro suspensão  ##
                    if peso == 12000:
                        valor = 121
                    elif peso >= 12001 and peso <= 12999:
                        valor = 177
                    elif peso >= 13000 and peso <= 14999:
                        valor = 178
                    elif peso >= 15000 and peso <= 17999:
                        valor = 244
                    else:
                        valor = 310
            if ano >= 1997 and ano <= 1999:
                if suspensao == 1:  ## suspensão pneumatica ou equivalente ##
                    if peso == 12000:
                        valor = 111
                    elif peso >= 12001 and peso <= 12999:
                        valor = 133
                    elif peso >= 13000 and peso <= 14999:
                        valor = 135
                    elif peso >= 15000 and peso <= 17999:
                        valor = 163
                    else:
                        valor = 191
                elif suspensao == 2:  ## outro suspensão  ##
                    if peso == 12000:
                        valor = 114
                    elif peso >= 12001 and peso <= 12999:
                        valor = 172
                    elif peso >= 13000 and peso <= 14999:
                        valor = 173
                    elif peso >= 15000 and peso <= 17999:
                        valor = 236
                    else:
                        valor = 299
            else:
                if suspensao == 1:  ## suspensão pneumatica ou equivalente ##
                    if peso == 12000:
                        valor = 110
                    elif peso >= 12001 and peso <= 12999:
                        valor = 132
                    elif peso >= 13000 and peso <= 14999:
                        valor = 134
                    elif peso >= 15000 and peso <= 17999:
                        valor = 161
                    else:
                        valor = 189
                elif suspensao == 2:  ## outro suspensão  ##
                    if peso == 12000:
                        valor = 113
                    elif peso >= 12001 and peso <= 12999:
                        valor = 171
                    elif peso >= 13000 and peso <= 14999:
                        valor = 171
                    elif peso >= 15000 and peso <= 17999:
                        valor = 235
                    else:
                        valor = 297
        elif eixos == 3:
            if ano <= 1990:
                if suspensao == 1:
                    if peso < 15000:
                        valor = 130
                    elif peso >= 15000 and peso <= 16999:
                        valor = 154
                    elif peso >= 17000 and peso <= 17999:
                        valor = 154
                    elif peso >= 18000 and peso <= 18999:
                        valor = 185
                    elif peso >= 19000 and peso <= 20999:
                        valor = 185
                    elif peso >= 21000 and peso <= 22999:
                        valor = 187
                    else:
                        valor = 281
                elif suspensao == 2:
                    if peso < 15000:
                        valor = 155
                    elif peso >= 15000 and peso <= 16999:
                        valor = 200
                    elif peso >= 17000 and peso <= 17999:
                        valor = 200
                    elif peso >= 18000 and peso <= 18999:
                        valor = 264
                    elif peso >= 19000 and peso <= 20999:
                        valor = 264
                    elif peso >= 21000 and peso <= 22999:
                        valor = 282
                    else:
                        valor = 350
            elif ano >= 1991 and ano <= 1993:
                if suspensao == 1:
                    if peso < 15000:
                        valor = 122
                    elif peso >= 15000 and peso <= 16999:
                        valor = 145
                    elif peso >= 17000 and peso <= 17999:
                        valor = 145
                    elif peso >= 18000 and peso <= 18999:
                        valor = 175
                    elif peso >= 19000 and peso <= 20999:
                        valor = 175
                    elif peso >= 21000 and peso <= 22999:
                        valor = 176
                    else:
                        valor = 264
                elif suspensao == 2:
                    if peso < 15000:
                        valor = 146
                    elif peso >= 15000 and peso <= 16999:
                        valor = 187
                    elif peso >= 17000 and peso <= 17999:
                        valor = 187
                    elif peso >= 18000 and peso <= 18999:
                        valor = 246
                    elif peso >= 19000 and peso <= 20999:
                        valor = 246
                    elif peso >= 21000 and peso <= 22999:
                        valor = 265
                    else:
                        valor = 330
            elif ano >= 1994 and ano <= 1996:
                if suspensao == 1:
                    if peso < 15000:
                        valor = 114
                    elif peso >= 15000 and peso <= 16999:
                        valor = 139
                    elif peso >= 17000 and peso <= 17999:
                        valor = 139
                    elif peso >= 18000 and peso <= 18999:
                        valor = 166
                    elif peso >= 19000 and peso <= 20999:
                        valor = 166
                    elif peso >= 21000 and peso <= 22999:
                        valor = 169
                    else:
                        valor = 250
                if suspensao == 2:
                    if peso < 15000:
                        valor = 140
                    elif peso >= 15000 and peso <= 16999:
                        valor = 179
                    elif peso >= 17000 and peso <= 17999:
                        valor = 179
                    elif peso >= 18000 and peso <= 18999:
                        valor = 236
                    elif peso >= 19000 and peso <= 20999:
                        valor = 236
                    elif peso >= 21000 and peso <= 22999:
                        valor = 251
                    else:
                        valor = 316
            elif ano >= 1997 and ano <= 1999:
                if suspensao == 1:
                    if peso < 15000:
                        valor = 110
                    elif peso >= 15000 and peso <= 16999:
                        valor = 135
                    elif peso >= 17000 and peso <= 17999:
                        valor = 135
                    elif peso >= 18000 and peso <= 18999:
                        valor = 161
                    elif peso >= 19000 and peso <= 20999:
                        valor = 161
                    elif peso >= 21000 and peso <= 22999:
                        valor = 162
                    else:
                        valor = 243
                elif suspensao == 2:
                    if peso < 15000:
                        valor = 136
                    elif peso >= 15000 and peso <= 16999:
                        valor = 174
                    elif peso >= 17000 and peso <= 17999:
                        valor = 174
                    elif peso >= 18000 and peso <= 18999:
                        valor = 229
                    elif peso >= 19000 and peso <= 20999:
                        valor = 229
                    elif peso >= 21000 and peso <= 22999:
                        valor = 243
                    else:
                        valor = 303
            elif ano >= 2000:
                if suspensao == 1:
                    if peso < 15000:
                        valor = 109
                    elif peso >= 15000 and peso <= 16999:
                        valor = 134
                    elif peso >= 17000 and peso <= 17999:
                        valor = 134
                    elif peso >= 18000 and peso <= 18999:
                        valor = 159
                    elif peso >= 19000 and peso <= 20999:
                        valor = 159
                    elif peso >= 21000 and peso <= 22999:
                        valor = 161
                    else:
                        valor = 241
                elif suspensao == 2:
                    if peso < 15000:
                        valor = 135
                    elif peso >= 15000 and peso <= 16999:
                        valor = 173
                    elif peso >= 17000 and peso <= 17999:
                        valor = 173
                    elif peso >= 18000 and peso <= 18999:
                        valor = 227
                    elif peso >= 19000 and peso <= 20999:
                        valor = 227
                    elif peso >= 21000 and peso <= 22999:
                        valor = 241
                    else:
                        valor = 301
        else:
            if ano <= 1990:
                if suspensao == 1:
                    if peso < 23000:
                        valor = 154
                    elif peso >= 23000 and peso <= 24999:
                        valor = 218
                    elif peso >= 25000 and peso <= 25999:
                        valor = 247
                    elif peso >= 26000 and peso <= 26999:
                        valor = 402
                    elif peso >= 27000 and peso <= 28999:
                        valor = 405
                    else:
                        valor = 456

                elif suspensao == 2:
                    if peso < 23000:
                        valor = 196
                    elif peso >= 23000 and peso <= 24999:
                        valor = 261
                    elif peso >= 25000 and peso <= 25999:
                        valor = 288
                    elif peso >= 26000 and peso <= 26999:
                        valor = 503
                    elif peso >= 27000 and peso <= 28999:
                        valor = 504
                    else:
                        valor = 678

            elif ano >= 1991 and ano <= 1993:
                if suspensao == 1:
                    if peso < 23000:
                        valor = 145
                    elif peso >= 23000 and peso <= 24999:
                        valor = 203
                    elif peso >= 25000 and peso <= 25999:
                        valor = 233
                    elif peso >= 26000 and peso <= 26999:
                        valor = 378
                    elif peso >= 27000 and peso <= 28999:
                        valor = 380
                    else:
                        valor = 426

                elif suspensao == 2:
                    if peso < 23000:
                        valor = 184
                    elif peso >= 23000 and peso <= 24999:
                        valor = 245
                    elif peso >= 25000 and peso <= 25999:
                        valor = 270
                    elif peso >= 26000 and peso <= 26999:
                        valor = 471
                    elif peso >= 27000 and peso <= 28999:
                        valor = 474
                    else:
                        valor = 638
            elif ano >= 1994 and ano <= 1996:
                if suspensao == 1:
                    if peso < 23000:
                        valor = 139
                    elif peso >= 23000 and peso <= 24999:
                        valor = 193
                    elif peso >= 25000 and peso <= 25999:
                        valor = 223
                    elif peso >= 26000 and peso <= 26999:
                        valor = 361
                    elif peso >= 27000 and peso <= 28999:
                        valor =362
                    else:
                        valor = 409

                elif suspensao == 2:
                    if peso < 23000:
                        valor = 135
                    elif peso >= 23000 and peso <= 24999:
                        valor = 234
                    elif peso >= 25000 and peso <= 25999:
                        valor = 255
                    elif peso >= 26000 and peso <= 26999:
                        valor = 452
                    elif peso >= 27000 and peso <= 28999:
                        valor = 453
                    else:
                        valor = 609
            elif ano >= 1997 and ano <= 1999:
                if suspensao == 1:
                    if peso < 23000:
                        valor = 135
                    elif peso >= 23000 and peso <= 24999:
                        valor = 188
                    elif peso >= 25000 and peso <= 25999:
                        valor = 216
                    elif peso >= 26000 and peso <= 26999:
                        valor = 347
                    elif peso >= 27000 and peso <= 28999:
                        valor = 348
                    else:
                        valor = 394

                elif suspensao == 2:
                    if peso < 23000:
                        valor = 171
                    elif peso >= 23000 and peso <= 24999:
                        valor = 227
                    elif peso >= 25000 and peso <= 25999:
                        valor = 248
                    elif peso >= 26000 and peso <= 26999:
                        valor = 435
                    elif peso >= 27000 and peso <= 28999:
                        valor = 436
                    else:
                        valor = 590

            else:
                if suspensao == 1:
                    if peso < 23000:
                        valor = 134
                    elif peso >= 23000 and peso <= 24999:
                        valor = 186
                    elif peso >= 25000 and peso <= 25999:
                        valor = 215
                    elif peso >= 26000 and peso <= 26999:
                        valor = 344
                    elif peso >= 27000 and peso <= 28999:
                        valor = 346
                    else:
                        valor = 391

                elif suspensao == 2:
                    if peso < 23000:
                        valor = 170
                    elif peso >= 23000 and peso <= 24999:
                        valor = 226
                    elif peso >= 25000 and peso <= 25999:
                        valor = 246
                    elif peso >= 26000 and peso <= 26999:
                        valor = 432
                    elif peso >= 27000 and peso <= 28999:
                        valor = 433
                    else:
                        valor = 583
        valor_total = valor


    elif categoria == "D3" or categoria == "d3":  # articulados
        if eixos == "2+1":
            if ano <= 1990:
                if suspensao == 1:  ## suspensão pneumatica ou equivalente ##
                    if peso == 12000:
                        valor = 129
                    elif peso >= 12001 and peso <= 17999:
                        valor = 152
                    elif peso >= 18000 and peso <= 24999:
                        valor = 196
                    elif peso >= 25000 and peso <= 25999:
                        valor = 247
                    else:
                        valor = 376
                elif suspensao == 2:  ## outro suspensão  ##
                    if peso == 12000:
                        valor = 130
                    elif peso >= 12001 and peso <= 17999:
                        valor = 194
                    elif peso >= 18000 and peso <= 24999:
                        valor = 256
                    elif peso >= 25000 and peso <= 25999:
                        valor = 366
                    else:
                        valor = 502

            elif ano >= 1991 and ano <= 1993:
                if suspensao == 1:  ## suspensão pneumatica ou equivalente ##
                    if peso == 12000:
                        valor = 121
                    elif peso >= 12001 and peso <= 17999:
                        valor = 143
                    elif peso >= 18000 and peso <= 24999:
                        valor = 184
                    elif peso >= 25000 and peso <= 25999:
                        valor = 233
                    else:
                        valor = 350
                elif suspensao == 2:  ## outro suspensão  ##
                    if peso == 12000:
                        valor = 121
                    elif peso >= 12001 and peso <= 17999:
                        valor = 183
                    elif peso >= 18000 and peso <= 24999:
                        valor = 241
                    elif peso >= 25000 and peso <= 25999:
                        valor = 342
                    else:
                        valor = 471
            elif ano >= 1994 and ano <= 1996:
                if suspensao == 1:  ## suspensão pneumatica ou equivalente ##
                    if peso == 12000:
                        valor = 113
                    elif peso >= 12001 and peso <= 17999:
                        valor = 137
                    elif peso >= 18000 and peso <= 24999:
                        valor = 171
                    elif peso >= 25000 and peso <= 25999:
                        valor = 217
                    else:
                        valor = 325

                elif suspensao == 2:  ## outro suspensão  ##
                    if peso == 12000:
                        valor = 113
                    elif peso >= 12001 and peso <= 17999:
                        valor = 175
                    elif peso >= 18000 and peso <= 24999:
                        valor = 231
                    elif peso >= 25000 and peso <= 25999:
                        valor = 327
                    else:
                        valor = 449
            elif ano >= 1997 and ano <= 1999:
                if suspensao == 1:  ## suspensão pneumatica ou equivalente ##
                    if peso == 12000:
                        valor = 110
                    elif peso >= 12001 and peso <= 17999:
                        valor = 133
                    elif peso >= 18000 and peso <= 24999:
                        valor = 171
                    elif peso >= 25000 and peso <= 25999:
                        valor = 217
                    else:
                        valor = 325
                elif suspensao == 2:  ## outro suspensão  ##
                    if peso == 12000:
                        valor = 110
                    elif peso >= 12001 and peso <= 12999:
                        valor = 170
                    elif peso >= 13000 and peso <= 14999:
                        valor = 224
                    elif peso >= 15000 and peso <= 17999:
                        valor = 318
                    else:
                        valor = 434
            else:
                if suspensao == 1:  ## suspensão pneumatica ou equivalente ##
                    if peso == 12000:
                        valor = 109
                    elif peso >= 12001 and peso <= 17999:
                        valor = 132
                    elif peso >= 18000 and peso <= 24999:
                        valor = 170
                    elif peso >= 25000 and peso <= 25999:
                        valor = 215
                    else:
                        valor = 323
                elif suspensao == 2:  ## outro suspensão  ##
                    if peso == 12000:
                        valor = 109
                    elif peso >= 12001 and peso <= 12999:
                        valor = 169
                    elif peso >= 13000 and peso <= 14999:
                        valor = 222
                    elif peso >= 15000 and peso <= 17999:
                        valor = 315
                    else:
                        valor = 431
        elif eixos == "2+2":
            if ano <= 1990:
                if suspensao == 1:
                    if peso < 23000:
                        valor = 152
                    elif peso >= 23000 and peso <= 24999:
                        valor = 184
                    elif peso >= 25000 and peso <= 25999:
                        valor = 216
                    elif peso >= 26000 and peso <= 28999:
                        valor = 310
                    elif peso >= 29000 and peso <= 30999:
                        valor = 373
                    elif peso >= 31000 and peso <= 32999:
                        valor = 439
                    else:
                        valor = 585
                elif suspensao == 2:
                    if peso < 23000:
                        valor = 194
                    elif peso >= 23000 and peso <= 24999:
                        valor = 245
                    elif peso >= 25000 and peso <= 25999:
                        valor = 259
                    elif peso >= 26000 and peso <= 28999:
                        valor = 433
                    elif peso >= 29000 and peso <= 30999:
                        valor = 495
                    elif peso >= 31000 and peso <= 32999:
                        valor = 581
                    else:
                        valor = 682
            elif ano >= 1991 and ano <= 1993:
                if suspensao == 1:
                    if peso < 23000:
                        valor = 143
                    elif peso >= 23000 and peso <= 24999:
                        valor = 174
                    elif peso >= 25000 and peso <= 25999:
                        valor = 201
                    elif peso >= 26000 and peso <= 28999:
                        valor = 290
                    elif peso >= 29000 and peso <= 30999:
                        valor = 347
                    elif peso >= 31000 and peso <= 32999:
                        valor = 413
                    else:
                        valor = 549

                elif suspensao == 2:
                    if peso < 23000:
                        valor = 183
                    elif peso >= 23000 and peso <= 24999:
                        valor = 231
                    elif peso >= 25000 and peso <= 25999:
                        valor = 243
                    elif peso >= 26000 and peso <= 28999:
                        valor = 407
                    elif peso >= 29000 and peso <= 30999:
                        valor = 465
                    elif peso >= 31000 and peso <= 32999:
                        valor = 547
                    else:
                        valor = 641
            elif ano >= 1994 and ano <= 1996:
                if suspensao == 1:
                    if peso < 23000:
                        valor = 137
                    elif peso >= 23000 and peso <= 24999:
                        valor = 165
                    elif peso >= 25000 and peso <= 25999:
                        valor = 192
                    elif peso >= 26000 and peso <= 28999:
                        valor = 277
                    elif peso >= 29000 and peso <= 30999:
                        valor = 332
                    elif peso >= 31000 and peso <= 32999:
                        valor = 394
                    else:
                        valor = 523
                elif suspensao == 2:
                    if peso < 23000:
                        valor = 176
                    elif peso >= 23000 and peso <= 24999:
                        valor = 221
                    elif peso >= 25000 and peso <= 25999:
                        valor = 233
                    elif peso >= 26000 and peso <= 28999:
                        valor = 389
                    elif peso >= 29000 and peso <= 30999:
                        valor = 443
                    elif peso >= 31000 and peso <= 32999:
                        valor = 520
                    else:
                        valor = 612
            elif ano >= 1997 and ano <= 1999:
                if suspensao == 1:
                    if peso < 23000:
                        valor = 133
                    elif peso >= 23000 and peso <= 24999:
                        valor = 159
                    elif peso >= 25000 and peso <= 25999:
                        valor = 186
                    elif peso >= 26000 and peso <= 28999:
                        valor = 268
                    elif peso >= 29000 and peso <= 30999:
                        valor = 322
                    elif peso >= 31000 and peso <= 32999:
                        valor = 382
                    else:
                        valor = 506
                elif suspensao == 2:
                    if peso < 23000:
                        valor = 170
                    elif peso >= 23000 and peso <= 24999:
                        valor = 215
                    elif peso >= 25000 and peso <= 25999:
                        valor = 226
                    elif peso >= 26000 and peso <= 28999:
                        valor = 376
                    elif peso >= 29000 and peso <= 30999:
                        valor = 428
                    elif peso >= 31000 and peso <= 32999:
                        valor = 503
                    else:
                        valor = 592
            elif ano >= 2000:
                if suspensao == 1:
                    if peso < 23000:
                        valor = 132
                    elif peso >= 23000 and peso <= 24999:
                        valor = 158
                    elif peso >= 25000 and peso <= 25999:
                        valor = 184
                    elif peso >= 26000 and peso <= 28999:
                        valor = 266
                    elif peso >= 29000 and peso <= 30999:
                        valor = 320
                    elif peso >= 31000 and peso <= 32999:
                        valor = 379
                    else:
                        valor = 502

                elif suspensao == 2:
                    if peso < 23000:
                        valor = 169
                    elif peso >= 23000 and peso <= 24999:
                        valor = 213
                    elif peso >= 25000 and peso <= 25999:
                        valor = 224
                    elif peso >= 26000 and peso <= 28999:
                        valor = 374
                    elif peso >= 29000 and peso <= 30999:
                        valor = 425
                    elif peso >= 31000 and peso <= 32999:
                        valor = 500
                    else:
                        valor = 588
        elif eixos == "2+3":
            if ano <= 1990:
                if suspensao == 1:
                    if peso < 36000:
                        valor = 430
                    elif peso >= 36000 and peso <= 37999:
                        valor = 461
                    else:
                        valor = 634
                elif suspensao == 2:
                    if peso < 36000:
                        valor = 494
                    elif peso >= 36000 and peso <= 37999:
                        valor = 648
                    else:
                        valor = 702
            elif ano >= 1991 and ano <= 1993:
                if suspensao == 1:
                    if peso < 36000:
                        valor = 404
                    elif peso >= 36000 and peso <= 37999:
                        valor = 432
                    else:
                        valor = 596
                elif suspensao == 2:
                    if peso < 36000:
                        valor = 464
                    elif peso >= 36000 and peso <= 37999:
                        valor = 608
                    else:
                        valor = 658
            elif ano >= 1994 and ano <= 1996:
                if suspensao == 1:
                    if peso < 36000:
                        valor = 385
                    elif peso >= 36000 and peso <= 37999:
                        valor = 412
                    else:
                        valor = 567
                elif suspensao == 2:
                    if peso < 36000:
                        valor = 441
                    elif peso >= 36000 and peso <= 37999:
                        valor = 580
                    else:
                        valor = 628
            elif ano >= 1997 and ano <= 1999:
                if suspensao == 1:
                    if peso < 36000:
                        valor = 374
                    elif peso >= 36000 and peso <= 37999:
                        valor = 399
                    else:
                        valor = 550
                elif suspensao == 2:
                    if peso < 36000:
                        valor = 427
                    elif peso >= 36000 and peso <= 37999:
                        valor = 562
                    else:
                        valor = 608
            elif ano >= 2000:

                if suspensao == 1:
                    if peso < 36000:
                        valor = 371
                    elif peso >= 36000 and peso <= 37999:
                        valor = 395
                    else:
                        valor = 546
                elif suspensao == 2:
                    if peso < 36000:
                        valor = 424
                    elif peso >= 36000 and peso <= 37999:
                        valor = 557
                    else:
                        valor = 604
        elif eixos == "3+2":
            if ano <= 1990:
                if suspensao == 1:
                    if peso < 36000:
                        valor = 365
                    elif peso >= 36000 and peso <= 37999:
                        valor = 437
                    elif peso >= 38000 and peso <= 39999:
                        valor = 573
                    else:
                        valor = 795
                elif suspensao == 2:
                    if peso < 36000:
                        valor = 425
                    elif peso >= 36000 and peso <= 37999:
                        valor = 571
                    elif peso >= 38000 and peso <= 39999:
                        valor =  672
                    else:
                        valor = 926
            elif ano >= 1991 and ano <= 1993:
                if suspensao == 1:
                    if peso < 36000:
                        valor = 341
                    elif peso >= 36000 and peso <= 37999:
                        valor = 411
                    elif peso >= 38000 and peso <= 39999:
                        valor = 540
                    else:
                        valor = 746
                elif suspensao == 2:
                    if peso < 36000:
                        valor = 400
                    elif peso >= 36000 and peso <= 37999:
                        valor = 536
                    elif peso >= 38000 and peso <= 39999:
                        valor = 631
                    else:
                        valor = 868
            elif ano >= 1994 and ano <= 1996:
                if suspensao == 1:
                    if peso < 36000:
                        valor = 327
                    elif peso >= 36000 and peso <= 37999:
                        valor = 392
                    elif peso >= 38000 and peso <= 39999:
                        valor = 514
                    else:
                        valor = 711
                elif suspensao == 2:
                    if peso < 36000:
                        valor = 382
                    elif peso >= 36000 and peso <= 37999:
                        valor = 512
                    elif peso >= 38000 and peso <= 39999:
                        valor = 604
                    else:
                        valor = 830
            elif ano >= 1997 and ano <= 1999:
                if suspensao == 1:
                    if peso < 36000:
                        valor = 317
                    elif peso >= 36000 and peso <= 37999:
                        valor = 381
                    elif peso >= 38000 and peso <= 39999:
                        valor = 498
                    else:
                        valor = 689

                elif suspensao == 2:
                    if peso < 36000:
                        valor = 369
                    elif peso >= 36000 and peso <= 37999:
                        valor = 495
                    elif peso >= 38000 and peso <= 39999:
                        valor = 583
                    else:
                        valor = 802
            elif ano >= 2000:
                if suspensao == 1:
                    if peso < 36000:
                        valor = 315
                    elif peso >= 36000 and peso <= 37999:
                        valor = 378
                    elif peso >= 38000 and peso <= 39999:
                        valor = 493
                    else:
                        valor = 682

                elif suspensao == 2:
                    if peso < 36000:
                        valor = 366
                    elif peso >= 36000 and peso <= 37999:
                        valor = 490
                    elif peso >= 38000 and peso <= 39999:
                        valor = 578
                    else:
                        valor = 796
        else:
            if ano <= 1990:
                if suspensao == 1:
                    if peso < 36000:
                        valor = 303
                    elif peso >= 36000 and peso <= 37999:
                        valor = 399
                    elif peso >= 38000 and peso <= 39999:
                        valor = 465
                    else:
                        valor = 478
                elif suspensao == 2:
                    if peso < 36000:
                        valor = 395
                    elif peso >= 36000 and peso <= 37999:
                        valor = 495
                    elif peso >= 38000 and peso <= 39999:
                        valor = 501
                    else:
                        valor = 676
            elif ano >= 1991 and ano <= 1993:
                if suspensao == 1:
                    if peso < 36000:
                        valor = 285
                    elif peso >= 36000 and peso <= 37999:
                        valor = 376
                    elif peso >= 38000 and peso <= 39999:
                        valor = 436
                    else:
                        valor = 448
                elif suspensao == 2:
                    if peso < 36000:
                        valor = 372
                    elif peso >= 36000 and peso <= 37999:
                        valor = 465
                    elif peso >= 38000 and peso <= 39999:
                        valor = 469
                    else:
                        valor = 636
            elif ano >= 1994 and ano <= 1996:
                if suspensao == 1:
                    if peso < 36000:
                        valor = 272
                    elif peso >= 36000 and peso <= 37999:
                        valor = 358
                    elif peso >= 38000 and peso <= 39999:
                        valor = 416
                    else:
                        valor = 427
                elif suspensao == 2:
                    if peso < 36000:
                        valor = 354
                    elif peso >= 36000 and peso <= 37999:
                        valor = 443
                    elif peso >= 38000 and peso <= 39999:
                        valor = 448
                    else:
                        valor = 607
            elif ano >= 1997 and ano <= 1999:
                if suspensao == 1:
                    if peso < 36000:
                        valor = 264
                    elif peso >= 36000 and peso <= 37999:
                        valor = 344
                    elif peso >= 38000 and peso <= 39999:
                        valor = 404
                    else:
                        valor = 414

                elif suspensao == 2:
                    if peso < 36000:
                        valor = 341
                    elif peso >= 36000 and peso <= 37999:
                        valor = 428
                    elif peso >= 38000 and peso <= 39999:
                        valor = 433
                    else:
                        valor = 588
            elif ano >= 2000:
                if suspensao == 1:
                    if peso < 36000:
                        valor = 261
                    elif peso >= 36000 and peso <= 37999:
                        valor = 342
                    elif peso >= 38000 and peso <= 39999:
                        valor = 400
                    else:
                        valor = 411

                elif suspensao == 2:
                    if peso < 36000:
                        valor = 339
                    elif peso >= 36000 and peso <= 37999:
                        valor = 425
                    elif peso >= 38000 and peso <= 39999:
                        valor = 430
                    else:
                        valor = 582



        valor_total = valor
       
       

        valor_total = valor


    return valor_total, valor, taxa_co2, taxa_adicional, coeficiente, imposto_diesel


