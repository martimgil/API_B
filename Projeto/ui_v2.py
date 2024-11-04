import customtkinter
import iuc
import customtkinter as tk
from PIL import Image
import os
import sys
from datetime import datetime
import irs
from ordenado import ordenado_dependente_solteiro, pensao_solteiro_casado_2t_deficiente, pensao_casado_1t,pensao_casado_1t_deficiente, pensao_casado_1t_deficiente_fa, pensao_solteiro_casado_2t_deficiente_fa, ordenado_dependente_solteiro_invalidez, ordenado_casado_1t, ordenado_casado_1t_invalidez, casados_2t, casados_2t_invalidez,  pensao_solteiro_casado_2t
import subprocess

historico = 'historico.txt'
modelo_log = []
peso_log = []
dependentes_log = []
renumera_log = []
dias_log = []
alimentacao_log = []
outros_log = []
renumeracao_log = []
retencao_log = []
ss_log = []




def abrir_historico():

    os.system(f'start notepad {historico}')
    reiniciar_programa()
def reiniciar_programa():
    subprocess.Popen([sys.executable] + sys.argv)
    sys.exit(0)

############################ IUC CAMIÕES ##############################

def historico_iuc_cat_c(categoria, valor_total, eixos, suspensao, ano, resultado_eixos, eixos_articulado):
    data_atual = datetime.today().date()
    data_atual_formatada = "{}/{}/{}" .format(data_atual.day, data_atual.month, data_atual.year)
    hora_atual = datetime.now().time()
    f = open("historico.txt", "a+")
    f.write("--- SIMULAÇÃO DO IMPOSTO ÚNICO DE CIRCULAÇÃO 2023 ---\n")
    modelo_escrever_historico = modelo_log[0]
    peso_escrever_historico = peso_log[0]
    f.write("Simulação realizada no dia {} ás {}\n".format(data_atual_formatada, hora_atual))
    f.write(" --- Caracterização do pesado ---\n")
    f.write("Modelo: {} \n".format( modelo_escrever_historico))
    f.write("Categoria: {} \n" .format(categoria))
    if categoria == "C1":
        f.write("Tabela: Veículos comerciais de transporte particular com peso bruto inferior a 12t \n")
        f.write("Eixos: N/A\n")
        f.write("Suspensão: N/A \n")
        f.write("Ano: N/A \n")
    elif categoria == "C2":
        f.write("Tabela: Veículos comerciais de transporte particular com peso bruto superior a 12t sem articulado\n")
        f.write("Eixos: {}\n".format(eixos))
        if suspensao == 1:
            f.write("Suspensão: Com suspensão pneumática ou equivalente\n")
            f.write("Ano: {} \n".format(ano))
        elif suspensao == 2:
            f.write("Suspensão: Outra suspensão\n")
            f.write("Ano: {} \n".format(ano))
    elif categoria == "C3":
        f.write("Tabela: Veículos comerciais de transporte particular com peso bruto superior a 12t com articulado\n")
        f.write("Eixos: {}\n".format(resultado_eixos))
        f.write("Eixos do Articulado: {}\n".format(eixos_articulado))

        if suspensao == 1:
            f.write("Suspensão: Com suspensão pneumática ou equivalente\n")
            f.write("Ano: {} \n".format(ano))
        elif suspensao == 2:
            f.write("Suspensão: Outra suspensão\n")
            f.write("Ano: {} \n".format(ano))
    if categoria == "D1":
        f.write("Tabela: Veículos comerciais de transporte público com peso bruto inferior a 12t \n")
        f.write("Eixos: N/A\n")
        f.write("Suspensão: N/A \n")
        f.write("Ano: N/A \n")
    elif categoria == "D2":
        f.write("Tabela: Veículos comerciais de transporte público com peso bruto superior a 12t sem articulado\n")
        f.write("Eixos: {}\n".format(eixos))
        if suspensao == 1:
            f.write("Suspensão: Com suspensão pneumática ou equivalente\n")
            f.write("Ano: {} \n".format(ano))
        elif suspensao == 2:
            f.write("Suspensão: Outra suspensão\n")
            f.write("Ano: {} \n".format(ano))
    elif categoria == "D3":
        f.write("Tabela: Veículos comerciais de transporte público com peso bruto superior a 12t com articulado\n")
        f.write("Eixos: {}\n".format(resultado_eixos))
        f.write("Eixos do Articulado: {}\n".format(eixos_articulado))

        if suspensao == 1:
            f.write("Suspensão: Com suspensão pneumática ou equivalente\n")
            f.write("Ano: {} \n".format(ano))
        elif suspensao == 2:
            f.write("Suspensão: Outra suspensão\n")
            f.write("Ano: {} \n".format(ano))


    f.write("Peso Bruto: {} Kg\n".format(peso_escrever_historico))
    f.write("--- Resumo dos valores a pagar ---\n")
    f.write("Valor final a pagar: {}€\n".format(valor_total))
    f.write("----------------------------------------------------------------\n")
    f.close()
    os.system(f'start notepad {historico}')
    reiniciar_programa()


######################### CATEGORIA D #########################################################################


def peso_superior_publico_s_articulado_2(janela_peso_superiror_s_articulado, pedir_ano, pedir_eixos, pedir_eixos_articulado):
    janela_peso_superiror_s_articulado.withdraw()
    janela_peso_superiror_s_articulado_resultado = tk.CTkToplevel()
    janela_peso_superiror_s_articulado_resultado.geometry("1400x700")
    janela_peso_superiror_s_articulado_resultado.title("Imposto Único de Circulação - Categoria D - Peso Bruto superior a 12t")
    texto_peso_superior_n_articulado_resultado = tk.CTkLabel(janela_peso_superiror_s_articulado_resultado, text="Simulação do Imposto Único de Circulação\nCategoria D - Não articulado\nResultado Final", font=("Segoe UI", 20)).place(x=508, y=0)

    cilindrada = 0
    ano = int(pedir_ano.get())
    categoria = "D3"
    tabela = 0
    ciclo = 0
    co2 = 0
    eixos = int(pedir_eixos.get())
    eixos_articulado = int(pedir_eixos_articulado.get())
    peso  = peso_log[0]
    resultado_eixos = eixos

    suspensao = 2
    modelo_escrever = modelo_log[0]
    combustivel = 0

    if eixos == 2 and eixos_articulado == 1:
        eixos = "2+1"
    elif eixos == 2 and eixos_articulado == 2:
        eixos = "2+2"
    elif eixos == 2 and eixos_articulado == 3:
        eixos = "2+3"
    elif eixos == 3 and eixos_articulado == 2:
        eixos = "3+2"
    else:
        eixos = "3+3"

    valor_total, valor, taxa_co2, taxa_adicional, coeficiente, imposto_diesel = iuc.iuc(categoria, tabela, combustivel, cilindrada, ano, ciclo, co2, eixos, peso, suspensao)


    ### SINTESE DE CARACTERISTICAS ###
    titulo_caracteristicas_final = tk.CTkLabel(janela_peso_superiror_s_articulado_resultado,text="Caracteristicas do pesado", font=("Segoe UI", 20)).place(x=293, y=150)
    modelo_resultado_final = tk.CTkLabel(janela_peso_superiror_s_articulado_resultado, text=modelo_escrever, font=("Segoe UI", 20)).place(x=293, y=200)
    cilindrada_resultado_final = tk.CTkLabel(janela_peso_superiror_s_articulado_resultado, text=("Peso Bruto: {} kg".format(peso)), font=("Segoe UI", 20)).place(x=293, y=250)
    eixos_resultado_final = tk.CTkLabel(janela_peso_superiror_s_articulado_resultado, text=("Eixos: {}".format(resultado_eixos)), font=("Segoe UI", 20)).place(x=293, y=300)
    eixos_articulado_final = tk.CTkLabel(janela_peso_superiror_s_articulado_resultado, text=("Eixos do articulado: {}". format(eixos_articulado)), font=("Segoe UI", 20)) .place(x=293, y=350)
    combustivel_resultado_final = tk.CTkLabel(janela_peso_superiror_s_articulado_resultado,text=("Suspensão: Outro tipo de suspensão"), font=("Segoe UI", 20)).place(x=293, y=400)
    ano_resultado_final = tk.CTkLabel(janela_peso_superiror_s_articulado_resultado, text=("Ano: {}".format(ano)), font=("Segoe UI", 20)).place(x=293, y=450)

    ### APRESENTAÇÃO DOS VALORES ###
    titulo_resumo__valor_resultado_final = tk.CTkLabel(janela_peso_superiror_s_articulado_resultado, text=("Resumo dos valores a pagar:".format(valor)), font=("Segoe UI", 20)).place(x=879, y=150)
    cilindrada_valor_resultado_final = tk.CTkLabel(janela_peso_superiror_s_articulado_resultado, text=("Preço da Cilindrada: {:.2f}€".format(valor)),  font=("Segoe UI", 20)).place(x=879, y=200)
    valor_total_resultado_final = tk.CTkLabel(janela_peso_superiror_s_articulado_resultado, text=("Valor a pagar: {:.2f}€".format(valor_total)), font=("Segoe UI", 20), bg_color="red").place(x=879, y=250)

    ### FINAL - SAIR OU HISTORICO ###
    decidir_historico = tk.CTkLabel(janela_peso_superiror_s_articulado_resultado, text=("Deseja adicionar está simulação ao histórico?"), font=("Segoe UI", 20)).place(x=505, y=500)
    select_tabela_a = tk.CTkButton(janela_peso_superiror_s_articulado_resultado, text="Sim",command=lambda: historico_iuc_cat_c(categoria, valor_total, eixos, suspensao, ano, resultado_eixos, eixos_articulado), font=("Segoe UI", 20)).place(x=550, y=550)
    select_tabela_b = tk.CTkButton(janela_peso_superiror_s_articulado_resultado, text="Não", command=lambda: reiniciar_programa(), font=("Segoe UI", 20)).place(x=750, y=550)




def peso_superior_publico_s_articulado_1(janela_peso_superiror_s_articulado, pedir_ano, pedir_eixos, pedir_eixos_articulado):
    janela_peso_superiror_s_articulado.withdraw()
    janela_peso_superiror_s_articulado_resultado = tk.CTkToplevel()
    janela_peso_superiror_s_articulado_resultado.geometry("1400x700")
    janela_peso_superiror_s_articulado_resultado.title("Imposto Único de Circulação - Categoria D - Peso Bruto superior a 12t")
    texto_peso_superior_n_articulado_resultado = tk.CTkLabel(janela_peso_superiror_s_articulado_resultado, text="Simulação do Imposto Único de Circulação\nCategoria D - Não articulado\nResultado Final", font=("Segoe UI", 20)).place(x=508, y=0)

    cilindrada = 0
    ano = int(pedir_ano.get())
    categoria = "C3"
    tabela = 0
    ciclo = 0
    co2 = 0
    eixos = int(pedir_eixos.get())
    eixos_articulado = int(pedir_eixos_articulado.get())
    peso  = peso_log[0]
    resultado_eixos = eixos

    suspensao = 1
    modelo_escrever = modelo_log[0]
    combustivel = 0

    if eixos == 2 and eixos_articulado == 1:
        eixos = "2+1"
    elif eixos == 2 and eixos_articulado == 2:
        eixos = "2+2"
    elif eixos == 2 and eixos_articulado == 3:
        eixos = "2+3"
    elif eixos == 3 and eixos_articulado == 2:
        eixos = "3+2"
    else:
        eixos = "3+3"

    valor_total, valor, taxa_co2, taxa_adicional, coeficiente, imposto_diesel = iuc.iuc(categoria, tabela, combustivel, cilindrada, ano, ciclo, co2, eixos, peso, suspensao)


    ### SINTESE DE CARACTERISTICAS ###
    titulo_caracteristicas_final = tk.CTkLabel(janela_peso_superiror_s_articulado_resultado,text="Caracteristicas do pesado", font=("Segoe UI", 20)).place(x=293, y=150)
    modelo_resultado_final = tk.CTkLabel(janela_peso_superiror_s_articulado_resultado, text=modelo_escrever, font=("Segoe UI", 20)).place(x=293, y=200)
    cilindrada_resultado_final = tk.CTkLabel(janela_peso_superiror_s_articulado_resultado, text=("Peso Bruto: {} kg".format(peso)), font=("Segoe UI", 20)).place(x=293, y=250)
    eixos_resultado_final = tk.CTkLabel(janela_peso_superiror_s_articulado_resultado, text=("Eixos: {}".format(resultado_eixos)), font=("Segoe UI", 20)).place(x=293, y=300)
    eixos_articulado_final = tk.CTkLabel(janela_peso_superiror_s_articulado_resultado, text=("Eixos do articulado: {}". format(eixos_articulado)), font=("Segoe UI", 20)) .place(x=293, y=350)
    combustivel_resultado_final = tk.CTkLabel(janela_peso_superiror_s_articulado_resultado,text=("Suspensão: Com suspensão pneumática ou equivalente"), font=("Segoe UI", 20)).place(x=293, y=400)
    ano_resultado_final = tk.CTkLabel(janela_peso_superiror_s_articulado_resultado, text=("Ano: {}".format(ano)), font=("Segoe UI", 20)).place(x=293, y=450)

    ### APRESENTAÇÃO DOS VALORES ###
    titulo_resumo__valor_resultado_final = tk.CTkLabel(janela_peso_superiror_s_articulado_resultado, text=("Resumo dos valores a pagar:".format(valor)), font=("Segoe UI", 20)).place(x=879, y=150)
    cilindrada_valor_resultado_final = tk.CTkLabel(janela_peso_superiror_s_articulado_resultado, text=("Preço da Cilindrada: {:.2f}€".format(valor)),  font=("Segoe UI", 20)).place(x=879, y=200)
    valor_total_resultado_final = tk.CTkLabel(janela_peso_superiror_s_articulado_resultado, text=("Valor a pagar: {:.2f}€".format(valor_total)), font=("Segoe UI", 20), bg_color="red").place(x=879, y=250)

    ### FINAL - SAIR OU HISTORICO ###
    decidir_historico = tk.CTkLabel(janela_peso_superiror_s_articulado_resultado, text=("Deseja adicionar está simulação ao histórico?"), font=("Segoe UI", 20)).place(x=505, y=500)
    select_tabela_a = tk.CTkButton(janela_peso_superiror_s_articulado_resultado, text="Sim",command=lambda: historico_iuc_cat_c(categoria, valor_total, eixos, suspensao, ano, resultado_eixos, eixos_articulado), font=("Segoe UI", 20)).place(x=550, y=550)
    select_tabela_b = tk.CTkButton(janela_peso_superiror_s_articulado_resultado, text="Não", command=lambda: inicio1(), font=("Segoe UI", 20)).place(x=750, y=550)


def peso_superior_publico_s_articulado(janela_peso_superior):
    peso = peso_log[0]
    janela_peso_superior.withdraw()
    janela_peso_superiror_s_articulado = tk.CTkToplevel()
    janela_peso_superiror_s_articulado.geometry("1400x700")
    janela_peso_superiror_s_articulado.title("Imposto Único de Circulação - Categoria D - Peso Bruto superior a 12t")
    texto_cat_c_superior = tk.CTkLabel(janela_peso_superiror_s_articulado, text="Simulação do Imposto Único de Circulação\nCategoria D - Peso superior a 12t\nNão articulado ou não é um conjunto de veiculos", font=("Segoe UI", 20)) .place(x=508, y=0)

    texto_ano = tk.CTkLabel(janela_peso_superiror_s_articulado, text="Insira o ano da primeira matrícula", font = ("Segoe UI", 20)) .place(x=566,y=150)
    pedir_ano = tk.CTkEntry(janela_peso_superiror_s_articulado, placeholder_text = "Ano", font = ("Segoe UI", 20), width=150)
    pedir_ano.place(x=650,y=200)
    texto__eixos = tk.CTkLabel(janela_peso_superiror_s_articulado, text = "Insira o número de eixos", font = ("Segoe UI", 20)) .place(x=606,y=250)
    pedir_eixos = tk.CTkEntry(janela_peso_superiror_s_articulado, placeholder_text= "Eixos", font = ("Segoe UI", 20), width=150)
    pedir_eixos.place(x=650, y=300)
    texto__eixos_articulado = tk.CTkLabel(janela_peso_superiror_s_articulado, text = "Insira o número de eixos do articulado", font = ("Segoe UI", 20)) .place(x=540,y=350)
    pedir_eixos_articulado = tk.CTkEntry(janela_peso_superiror_s_articulado, placeholder_text= "Eixos", font = ("Segoe UI", 20), width=150)
    pedir_eixos_articulado.place(x=650, y=400)

    texto_suspensao = tk.CTkLabel(janela_peso_superiror_s_articulado, text = "Escolha o tipo de suspensão: ", font = ("Segoe UI",20)) . place(x= 577, y=450)
    escolher_suspensao_pneumatica = tk.CTkButton(janela_peso_superiror_s_articulado, command=lambda: peso_superior_publico_s_articulado_1(janela_peso_superiror_s_articulado, pedir_ano, pedir_eixos, pedir_eixos_articulado), text = "Com Suspensão pneumática ou equivalente", font=("Segoe UI",20)) .place(x=502, y=500)
    escolher_suspensao_outra = tk.CTkButton(janela_peso_superiror_s_articulado, command=lambda: peso_superior_publico_s_articulado_2(janela_peso_superiror_s_articulado, pedir_ano, pedir_eixos, pedir_eixos_articulado), text = "Com outro tipo de suspensão" , font=("Segoe UI",20)) .place(x = 567,y=560)


############################### NÃO ARTICULADO #############################

def peso_superior_publico_n_articulado_resultado_2(janela_peso_superiror_n_articulado, pedir_ano, pedir_eixos, peso):
    janela_peso_superiror_n_articulado.withdraw()
    janela_peso_superiror_n_articulado_resultado = tk.CTkToplevel()
    janela_peso_superiror_n_articulado_resultado.geometry("1400x700")
    janela_peso_superiror_n_articulado_resultado.title("Imposto Único de Circulação - Categoria D - Peso Bruto superior a 12t")
    texto_peso_superior_n_articulado_resultado = tk.CTkLabel(janela_peso_superiror_n_articulado_resultado,text = "Simulação do Imposto Único de Circulação\nCategoria D - Não articulado\nResultado Final", font = ("Segoe UI", 20)) .place(x =508, y=0)

    cilindrada = 0
    ano = int(pedir_ano.get())
    categoria = "D2"
    tabela = 0
    ciclo = 0
    co2 = 0
    eixos = int(pedir_eixos.get())
    suspensao = 2
    modelo_escrever = modelo_log[0]
    combustivel = 0
    resultado_eixos= 0
    eixos_articulado = 0


    valor_total, valor, taxa_co2, taxa_adicional, coeficiente, imposto_diesel = iuc.iuc(categoria,tabela,combustivel, cilindrada, ano, ciclo, co2, eixos, peso,suspensao)

    ### SINTESE DE CARACTERISTICAS ###
    titulo_caracteristicas_final = tk.CTkLabel(janela_peso_superiror_n_articulado_resultado, text = "Caracteristicas do pesado", font = ("Segoe UI",20)) .place(x = 293, y=150)
    modelo_resultado_final = tk.CTkLabel(janela_peso_superiror_n_articulado_resultado, text = modelo_escrever, font = ("Segoe UI",20)) .place(x = 293, y=200)
    cilindrada_resultado_final = tk.CTkLabel(janela_peso_superiror_n_articulado_resultado, text=("Peso Bruto: {} kg" .format(peso)), font=("Segoe UI", 20)).place(x=293, y=250)
    ano_resultado_final = tk.CTkLabel(janela_peso_superiror_n_articulado_resultado, text=("Eixos: {}" .format(eixos)), font=("Segoe UI", 20)).place(x=293, y=300)
    combustivel_resultado_final = tk.CTkLabel(janela_peso_superiror_n_articulado_resultado, text = ("Suspensão: Outro tipo de suspensão"), font=("Segoe UI", 20)).place(x=293, y=350)
    ano_resultado_final = tk.CTkLabel(janela_peso_superiror_n_articulado_resultado, text=("Ano: {}" .format(ano)), font =("Segoe UI", 20)).place(x=293, y=400)



    ### APRESENTAÇÃO DOS VALORES ###
    titulo_resumo__valor_resultado_final = tk.CTkLabel(janela_peso_superiror_n_articulado_resultado, text=("Resumo dos valores a pagar:".format(valor)), font=("Segoe UI", 20)).place(x=879, y=150)
    cilindrada_valor_resultado_final = tk.CTkLabel(janela_peso_superiror_n_articulado_resultado, text=("Preço da Cilindrada: {:.2f}€" .format(valor)), font=("Segoe UI", 20)).place(x=879 , y=200)
    valor_total_resultado_final = tk.CTkLabel(janela_peso_superiror_n_articulado_resultado, text=("Valor a pagar: {:.2f}€".format(valor_total)), font=("Segoe UI", 20), bg_color="red").place(x=879, y=250)

    ### FINAL - SAIR OU HISTORICO ###
    decidir_historico = tk.CTkLabel(janela_peso_superiror_n_articulado_resultado, text=("Deseja adicionar está simulação ao histórico?" ), font=("Segoe UI", 20)).place(x=505, y=500)
    select_tabela_a = tk.CTkButton(janela_peso_superiror_n_articulado_resultado, text="Sim",command=lambda: historico_iuc_cat_c(categoria, valor_total, eixos, suspensao, ano, resultado_eixos, eixos_articulado),font=("Segoe UI", 20)).place(x=550, y=550)
    select_tabela_b = tk.CTkButton(janela_peso_superiror_n_articulado_resultado, text="Não",command=lambda: reiniciar_programa(),font=("Segoe UI", 20)).place(x=750, y=550)



def peso_superior_publico_n_articulado_resultado_1(janela_peso_superiror_n_articulado, pedir_ano, pedir_eixos, peso):
    janela_peso_superiror_n_articulado.withdraw()
    janela_peso_superiror_n_articulado_resultado = tk.CTkToplevel()
    janela_peso_superiror_n_articulado_resultado.geometry("1400x700")
    janela_peso_superiror_n_articulado_resultado.title("Imposto Único de Circulação - Categoria D - Peso Bruto superior a 12t")
    texto_peso_superior_n_articulado_resultado = tk.CTkLabel(janela_peso_superiror_n_articulado_resultado,text = "Simulação do Imposto Único de Circulação\nCategoria D - Não articulado\nResultado Final", font = ("Segoe UI", 20)) .place(x =508, y=0)

    cilindrada = 0
    ano = int(pedir_ano.get())
    categoria = "D2"
    tabela = 0
    ciclo = 0
    co2 = 0
    eixos = int(pedir_eixos.get())
    suspensao = 1
    modelo_escrever = modelo_log[0]
    combustivel = 0
    resultado_eixos = 0
    eixos_articulado = 0

    valor_total, valor, taxa_co2, taxa_adicional, coeficiente, imposto_diesel = iuc.iuc(categoria,tabela,combustivel, cilindrada, ano, ciclo, co2, eixos, peso,suspensao)

    ### SINTESE DE CARACTERISTICAS ###
    titulo_caracteristicas_final = tk.CTkLabel(janela_peso_superiror_n_articulado_resultado, text = "Caracteristicas do pesado", font = ("Segoe UI",20)) .place(x = 293, y=150)
    modelo_resultado_final = tk.CTkLabel(janela_peso_superiror_n_articulado_resultado, text = modelo_escrever, font = ("Segoe UI",20)) .place(x = 293, y=200)
    cilindrada_resultado_final = tk.CTkLabel(janela_peso_superiror_n_articulado_resultado, text=("Peso Bruto: {} kg" .format(peso)), font=("Segoe UI", 20)).place(x=293, y=250)
    ano_resultado_final = tk.CTkLabel(janela_peso_superiror_n_articulado_resultado, text=("Eixos: {}" .format(eixos)), font=("Segoe UI", 20)).place(x=293, y=300)
    combustivel_resultado_final = tk.CTkLabel(janela_peso_superiror_n_articulado_resultado, text = ("Suspensão: Com suspensão pneumática ou equivalente"), font=("Segoe UI", 20)).place(x=293, y=350)
    ano_resultado_final = tk.CTkLabel(janela_peso_superiror_n_articulado_resultado, text=("Ano: {}" .format(ano)), font =("Segoe UI", 20)).place(x=293, y=400)



    ### APRESENTAÇÃO DOS VALORES ###
    titulo_resumo__valor_resultado_final = tk.CTkLabel(janela_peso_superiror_n_articulado_resultado, text=("Resumo dos valores a pagar:".format(valor)), font=("Segoe UI", 20)).place(x=879, y=150)
    cilindrada_valor_resultado_final = tk.CTkLabel(janela_peso_superiror_n_articulado_resultado, text=("Preço da Cilindrada: {:.2f}€" .format(valor)), font=("Segoe UI", 20)).place(x=879 , y=200)
    valor_total_resultado_final = tk.CTkLabel(janela_peso_superiror_n_articulado_resultado, text=("Valor a pagar: {:.2f}€".format(valor_total)), font=("Segoe UI", 20), bg_color="red").place(x=879, y=250)

    ### FINAL - SAIR OU HISTORICO ###
    decidir_historico = tk.CTkLabel(janela_peso_superiror_n_articulado_resultado, text=("Deseja adicionar está simulação ao histórico?" ), font=("Segoe UI", 20)).place(x=505, y=500)
    select_tabela_a = tk.CTkButton(janela_peso_superiror_n_articulado_resultado, text="Sim",command=lambda: historico_iuc_cat_c(categoria, valor_total, eixos, suspensao, ano, resultado_eixos, eixos_articulado),font=("Segoe UI", 20)).place(x=550, y=550)
    select_tabela_b = tk.CTkButton(janela_peso_superiror_n_articulado_resultado, text="Não",command=lambda: reiniciar_programa(),font=("Segoe UI", 20)).place(x=750, y=550)



def peso_superior_publico_n_articulado(janela_peso_superior):
    peso = peso_log[0]
    janela_peso_superior.withdraw()
    janela_peso_superiror_n_articulado = tk.CTkToplevel()
    janela_peso_superiror_n_articulado.geometry("1400x700")
    janela_peso_superiror_n_articulado.title("Imposto Único de Circulação - Categoria D - Peso Bruto superior a 12t")
    texto_cat_c_superior = tk.CTkLabel(janela_peso_superiror_n_articulado, text="Simulação do Imposto Único de Circulação\nCategoria D - Peso superior a 12t\nNão articulado ou não é um conjunto de veiculos", font=("Segoe UI", 20)) .place(x=508, y=0)

    texto_ano = tk.CTkLabel(janela_peso_superiror_n_articulado, text="Insira o ano da primeira matrícula", font = ("Segoe UI", 20)) .place(x=566,y=150)
    pedir_ano = tk.CTkEntry(janela_peso_superiror_n_articulado, placeholder_text = "Ano", font = ("Segoe UI", 20), width=150)
    pedir_ano.place(x=650,y=200)
    texto__eixos = tk.CTkLabel(janela_peso_superiror_n_articulado, text = "Insira o número de eixos", font = ("Segoe UI", 20)) .place(x=606,y=250)
    pedir_eixos = tk.CTkEntry(janela_peso_superiror_n_articulado, placeholder_text= "Eixos", font = ("Segoe UI", 20), width=150)
    pedir_eixos.place(x=650, y=300)
    texto_suspensao = tk.CTkLabel(janela_peso_superiror_n_articulado, text = "Escolha o tipo de suspensão: ", font = ("Segoe UI",20)) . place(x= 577, y=350)
    escolher_suspensao_pneumatica = tk.CTkButton(janela_peso_superiror_n_articulado, command=lambda: peso_superior_publico_n_articulado_resultado_1(janela_peso_superiror_n_articulado, pedir_ano, pedir_eixos, peso), text = "Com Suspensão pneumática ou equivalente", font=("Segoe UI",20)) .place(x=502, y=400)
    escolher_suspensao_outra = tk.CTkButton(janela_peso_superiror_n_articulado,command=lambda: peso_superior_publico_n_articulado_resultado_2(janela_peso_superiror_n_articulado, pedir_ano, pedir_eixos, peso), text = "Com outro tipo de suspensão" , font=("Segoe UI",20))  .place(x = 567,y=460)


def peso_superior_publico(pedir_peso_c):
    pedir_peso_c.withdraw()
    janela_peso_superior = tk.CTkToplevel()
    janela_peso_superior.title("Imposto Único de Circulação - Categoria D - Peso Bruto superior a 12t")
    janela_peso_superior.geometry("1400x700")
    texto_cat_c_superior = tk.CTkLabel(janela_peso_superior, text="Simulação do Imposto Único de Circulação\nCategoria D - Peso superior a 12t", font=("Segoe Ui", 20 )) .place(x=508, y=0)

    texto_questao_articulado = tk.CTkLabel(janela_peso_superior, text="O veículo é articulado ou é um conjunto de veículos?", font = ("Segoe UI", 20)) .place(x=470, y=100)
    botao_s_articulado = tk.CTkButton(janela_peso_superior, text="Sim", command=lambda: peso_superior_publico_s_articulado(janela_peso_superior), font = ("Segoe UI",20)).place(x=550, y = 200)
    botao_n_articulado = tk.CTkButton(janela_peso_superior, text="Não", command=lambda: peso_superior_publico_n_articulado(janela_peso_superior),font = ("Segoe UI", 20)) .place(x=720, y=200)




def peso_inferior_publico(pedir_peso_c, pedir_modelo, peso):
    pedir_peso_c.withdraw()
    janela_peso_inferior = tk.CTkToplevel()
    janela_peso_inferior.title("Imposto Único de Circulação - Categoria D - Peso Bruto inferior a 12 t")
    janela_peso_inferior.geometry("1400x700")
    texto_cat_c_inferior_resultado = tk.CTkLabel(janela_peso_inferior, text="Simulação do Imposto Único de Circulação\nCategoria D - Peso inferior a 12 t\nResultado Final", font=("Segoe UI", 20)).place(x=508, y=0)

    cilindrada = 0
    ano = 0
    categoria = "D1"
    tabela = 0
    ciclo = 0
    co2 = 0
    eixos = 0
    suspensao = 0
    modelo_escrever = modelo_log[0]
    combustivel = 0
    resultado_eixos = 0
    eixos_articulado = 0

    valor_total, valor, taxa_co2, taxa_adicional, coeficiente, imposto_diesel = iuc.iuc(categoria,tabela,combustivel, cilindrada, ano, ciclo, co2, eixos, peso,suspensao)

    ### SINTESE DE CARACTERISTICAS ###
    titulo_caracteristicas_final = tk.CTkLabel(janela_peso_inferior, text = "Caracteristicas do pesado", font = ("Segoe UI",20)) .place(x = 293, y=150)
    modelo_resultado_final = tk.CTkLabel(janela_peso_inferior, text = modelo_escrever, font = ("Segoe UI",20)) .place(x = 293, y=200)
    cilindrada_resultado_final = tk.CTkLabel(janela_peso_inferior, text=("Peso Bruto: {}" .format(peso)), font=("Segoe UI", 20)).place(x=293, y=250)
    ano_resultado_final = tk.CTkLabel(janela_peso_inferior, text=("Eixos: N/A"), font=("Segoe UI", 20)).place(x=293, y=300)
    combustivel_resultado_final = tk.CTkLabel(janela_peso_inferior, text=("Suspensão: N/A"), font=("Segoe UI", 20)).place(x=293, y=350)
    ano_resultado_final = tk.CTkLabel(janela_peso_inferior, text=("Ano: N/A"), font =("Segoe UI", 20)).place(x=293, y=400)



    ### APRESENTAÇÃO DOS VALORES ###
    titulo_resumo__valor_resultado_final = tk.CTkLabel(janela_peso_inferior, text=("Resumo dos valores a pagar:".format(valor)), font=("Segoe UI", 20)).place(x=879, y=150)
    cilindrada_valor_resultado_final = tk.CTkLabel(janela_peso_inferior, text=("Preço da Cilindrada: {:.2f}€" .format(valor)), font=("Segoe UI", 20)).place(x=879 , y=200)
    valor_total_resultado_final = tk.CTkLabel(janela_peso_inferior, text=("Valor a pagar: {:.2f}€".format(valor_total)), font=("Segoe UI", 20), bg_color="red").place(x=879, y=250)

    ### FINAL - SAIR OU HISTORICO ###
    decidir_historico = tk.CTkLabel(janela_peso_inferior, text=("Deseja adicionar está simulação ao histórico?" ), font=("Segoe UI", 20)).place(x=505, y=500)
    select_tabela_a = tk.CTkButton(janela_peso_inferior, text="Sim",command=lambda: historico_iuc_cat_c(categoria, valor_total, eixos, suspensao, ano, resultado_eixos, eixos_articulado),font=("Segoe UI", 20)).place(x=550, y=550)
    select_tabela_b = tk.CTkButton(janela_peso_inferior, text="Não",command=lambda: reiniciar_programa(),font=("Segoe UI", 20)).place(x=750, y=550)


def decisao_peso_publico(pedir_peso_bruto, pedir_modelo, pedir_peso_c):
    peso = float(pedir_peso_bruto.get())
    peso_log.append(peso)
    modelo = str(pedir_modelo.get())
    modelo_log.append(modelo)
    if peso <= 11999:
        peso_inferior_publico(pedir_peso_c, pedir_modelo, peso)
    else:
        peso_superior_publico(pedir_peso_c)


###### ARTICULADOS PARTICULARES ##################################################################################

def peso_superior_particular_s_articulado_2(janela_peso_superiror_s_articulado, pedir_ano, pedir_eixos, pedir_eixos_articulado):
    janela_peso_superiror_s_articulado.withdraw()
    janela_peso_superiror_s_articulado_resultado = tk.CTkToplevel()
    janela_peso_superiror_s_articulado_resultado.geometry("1400x700")
    janela_peso_superiror_s_articulado_resultado.title("Imposto Único de Circulação - Categoria C - Peso Bruto superior a 12t")
    texto_peso_superior_n_articulado_resultado = tk.CTkLabel(janela_peso_superiror_s_articulado_resultado, text="Simulação do Imposto Único de Circulação\nCategoria C - Não articulado\nResultado Final", font=("Segoe UI", 20)).place(x=508, y=0)

    cilindrada = 0
    ano = int(pedir_ano.get())
    categoria = "C3"
    tabela = 0
    ciclo = 0
    co2 = 0
    eixos = int(pedir_eixos.get())
    eixos_articulado = int(pedir_eixos_articulado.get())
    peso  = peso_log[0]
    resultado_eixos = eixos

    suspensao = 2
    modelo_escrever = modelo_log[0]
    combustivel = 0

    if eixos == 2 and eixos_articulado == 1:
        eixos = "2+1"
    elif eixos == 2 and eixos_articulado == 2:
        eixos = "2+2"
    elif eixos == 2 and eixos_articulado == 3:
        eixos = "2+3"
    elif eixos == 3 and eixos_articulado == 2:
        eixos = "3+2"
    else:
        eixos = "3+3"

    valor_total, valor, taxa_co2, taxa_adicional, coeficiente, imposto_diesel = iuc.iuc(categoria, tabela, combustivel, cilindrada, ano, ciclo, co2, eixos, peso, suspensao)


    ### SINTESE DE CARACTERISTICAS ###
    titulo_caracteristicas_final = tk.CTkLabel(janela_peso_superiror_s_articulado_resultado,text="Caracteristicas do pesado", font=("Segoe UI", 20)).place(x=293, y=150)
    modelo_resultado_final = tk.CTkLabel(janela_peso_superiror_s_articulado_resultado, text=modelo_escrever, font=("Segoe UI", 20)).place(x=293, y=200)
    cilindrada_resultado_final = tk.CTkLabel(janela_peso_superiror_s_articulado_resultado, text=("Peso Bruto: {} kg".format(peso)), font=("Segoe UI", 20)).place(x=293, y=250)
    eixos_resultado_final = tk.CTkLabel(janela_peso_superiror_s_articulado_resultado, text=("Eixos: {}".format(resultado_eixos)), font=("Segoe UI", 20)).place(x=293, y=300)
    eixos_articulado_final = tk.CTkLabel(janela_peso_superiror_s_articulado_resultado, text=("Eixos do articulado: {}". format(eixos_articulado)), font=("Segoe UI", 20)) .place(x=293, y=350)
    combustivel_resultado_final = tk.CTkLabel(janela_peso_superiror_s_articulado_resultado,text=("Suspensão: Outro tipo de suspensão"), font=("Segoe UI", 20)).place(x=293, y=400)
    ano_resultado_final = tk.CTkLabel(janela_peso_superiror_s_articulado_resultado, text=("Ano: {}".format(ano)), font=("Segoe UI", 20)).place(x=293, y=450)

    ### APRESENTAÇÃO DOS VALORES ###
    titulo_resumo__valor_resultado_final = tk.CTkLabel(janela_peso_superiror_s_articulado_resultado, text=("Resumo dos valores a pagar:".format(valor)), font=("Segoe UI", 20)).place(x=879, y=150)
    cilindrada_valor_resultado_final = tk.CTkLabel(janela_peso_superiror_s_articulado_resultado, text=("Preço da Cilindrada: {:.2f}€".format(valor)),  font=("Segoe UI", 20)).place(x=879, y=200)
    valor_total_resultado_final = tk.CTkLabel(janela_peso_superiror_s_articulado_resultado, text=("Valor a pagar: {:.2f}€".format(valor_total)), font=("Segoe UI", 20), bg_color="red").place(x=879, y=250)

    ### FINAL - SAIR OU HISTORICO ###
    decidir_historico = tk.CTkLabel(janela_peso_superiror_s_articulado_resultado, text=("Deseja adicionar está simulação ao histórico?"), font=("Segoe UI", 20)).place(x=505, y=500)
    select_tabela_a = tk.CTkButton(janela_peso_superiror_s_articulado_resultado, text="Sim",command=lambda: historico_iuc_cat_c(categoria, valor_total, eixos, suspensao, ano, resultado_eixos, eixos_articulado), font=("Segoe UI", 20)).place(x=550, y=550)
    select_tabela_b = tk.CTkButton(janela_peso_superiror_s_articulado_resultado, text="Não", command=lambda: reiniciar_programa(), font=("Segoe UI", 20)).place(x=750, y=550)




def peso_superior_particular_s_articulado_1(janela_peso_superiror_s_articulado, pedir_ano, pedir_eixos, pedir_eixos_articulado):
    janela_peso_superiror_s_articulado.withdraw()
    janela_peso_superiror_s_articulado_resultado = tk.CTkToplevel()
    janela_peso_superiror_s_articulado_resultado.geometry("1400x700")
    janela_peso_superiror_s_articulado_resultado.title("Imposto Único de Circulação - Categoria C - Peso Bruto superior a 12t")
    texto_peso_superior_n_articulado_resultado = tk.CTkLabel(janela_peso_superiror_s_articulado_resultado, text="Simulação do Imposto Único de Circulação\nCategoria C - Não articulado\nResultado Final", font=("Segoe UI", 20)).place(x=508, y=0)

    cilindrada = 0
    ano = int(pedir_ano.get())
    categoria = "C3"
    tabela = 0
    ciclo = 0
    co2 = 0
    eixos = int(pedir_eixos.get())
    eixos_articulado = int(pedir_eixos_articulado.get())
    peso  = peso_log[0]
    resultado_eixos = eixos

    suspensao = 1
    modelo_escrever = modelo_log[0]
    combustivel = 0

    if eixos == 2 and eixos_articulado == 1:
        eixos = "2+1"
    elif eixos == 2 and eixos_articulado == 2:
        eixos = "2+2"
    elif eixos == 2 and eixos_articulado == 3:
        eixos = "2+3"
    elif eixos == 3 and eixos_articulado == 2:
        eixos = "3+2"
    else:
        eixos = "3+3"

    valor_total, valor, taxa_co2, taxa_adicional, coeficiente, imposto_diesel = iuc.iuc(categoria, tabela, combustivel, cilindrada, ano, ciclo, co2, eixos, peso, suspensao)


    ### SINTESE DE CARACTERISTICAS ###
    titulo_caracteristicas_final = tk.CTkLabel(janela_peso_superiror_s_articulado_resultado,text="Caracteristicas do pesado", font=("Segoe UI", 20)).place(x=293, y=150)
    modelo_resultado_final = tk.CTkLabel(janela_peso_superiror_s_articulado_resultado, text=modelo_escrever, font=("Segoe UI", 20)).place(x=293, y=200)
    cilindrada_resultado_final = tk.CTkLabel(janela_peso_superiror_s_articulado_resultado, text=("Peso Bruto: {} kg".format(peso)), font=("Segoe UI", 20)).place(x=293, y=250)
    eixos_resultado_final = tk.CTkLabel(janela_peso_superiror_s_articulado_resultado, text=("Eixos: {}".format(resultado_eixos)), font=("Segoe UI", 20)).place(x=293, y=300)
    eixos_articulado_final = tk.CTkLabel(janela_peso_superiror_s_articulado_resultado, text=("Eixos do articulado: {}". format(eixos_articulado)), font=("Segoe UI", 20)) .place(x=293, y=350)
    combustivel_resultado_final = tk.CTkLabel(janela_peso_superiror_s_articulado_resultado,text=("Suspensão: Com suspensão pneumática ou equivalente"), font=("Segoe UI", 20)).place(x=293, y=400)
    ano_resultado_final = tk.CTkLabel(janela_peso_superiror_s_articulado_resultado, text=("Ano: {}".format(ano)), font=("Segoe UI", 20)).place(x=293, y=450)

    ### APRESENTAÇÃO DOS VALORES ###
    titulo_resumo__valor_resultado_final = tk.CTkLabel(janela_peso_superiror_s_articulado_resultado, text=("Resumo dos valores a pagar:".format(valor)), font=("Segoe UI", 20)).place(x=879, y=150)
    cilindrada_valor_resultado_final = tk.CTkLabel(janela_peso_superiror_s_articulado_resultado, text=("Preço da Cilindrada: {:.2f}€".format(valor)),  font=("Segoe UI", 20)).place(x=879, y=200)
    valor_total_resultado_final = tk.CTkLabel(janela_peso_superiror_s_articulado_resultado, text=("Valor a pagar: {:.2f}€".format(valor_total)), font=("Segoe UI", 20), bg_color="red").place(x=879, y=250)

    ### FINAL - SAIR OU HISTORICO ###
    decidir_historico = tk.CTkLabel(janela_peso_superiror_s_articulado_resultado, text=("Deseja adicionar está simulação ao histórico?"), font=("Segoe UI", 20)).place(x=505, y=500)
    select_tabela_a = tk.CTkButton(janela_peso_superiror_s_articulado_resultado, text="Sim",command=lambda: historico_iuc_cat_c(categoria, valor_total, eixos, suspensao, ano, resultado_eixos, eixos_articulado), font=("Segoe UI", 20)).place(x=550, y=550)
    select_tabela_b = tk.CTkButton(janela_peso_superiror_s_articulado_resultado, text="Não", command=lambda: reiniciar_programa(), font=("Segoe UI", 20)).place(x=750, y=550)


def peso_superior_particular_s_articulado(janela_peso_superior):
    peso = peso_log[0]
    janela_peso_superior.withdraw()
    janela_peso_superiror_s_articulado = tk.CTkToplevel()
    janela_peso_superiror_s_articulado.geometry("1400x700")
    janela_peso_superiror_s_articulado.title("Imposto Único de Circulação - Categoria C - Peso Bruto superior a 12t")
    texto_cat_c_superior = tk.CTkLabel(janela_peso_superiror_s_articulado, text="Simulação do Imposto Único de Circulação\nCategoria C - Peso superior a 12t\nNão articulado ou não é um conjunto de veiculos", font=("Segoe UI", 20)) .place(x=508, y=0)

    texto_ano = tk.CTkLabel(janela_peso_superiror_s_articulado, text="Insira o ano da primeira matrícula", font = ("Segoe UI", 20)) .place(x=566,y=150)
    pedir_ano = tk.CTkEntry(janela_peso_superiror_s_articulado, placeholder_text = "Ano", font = ("Segoe UI", 20), width=150)
    pedir_ano.place(x=650,y=200)
    texto__eixos = tk.CTkLabel(janela_peso_superiror_s_articulado, text = "Insira o número de eixos", font = ("Segoe UI", 20)) .place(x=606,y=250)
    pedir_eixos = tk.CTkEntry(janela_peso_superiror_s_articulado, placeholder_text= "Eixos", font = ("Segoe UI", 20), width=150)
    pedir_eixos.place(x=650, y=300)
    texto__eixos_articulado = tk.CTkLabel(janela_peso_superiror_s_articulado, text = "Insira o número de eixos do articulado", font = ("Segoe UI", 20)) .place(x=540,y=350)
    pedir_eixos_articulado = tk.CTkEntry(janela_peso_superiror_s_articulado, placeholder_text= "Eixos", font = ("Segoe UI", 20), width=150)
    pedir_eixos_articulado.place(x=650, y=400)

    texto_suspensao = tk.CTkLabel(janela_peso_superiror_s_articulado, text = "Escolha o tipo de suspensão: ", font = ("Segoe UI",20)) . place(x= 577, y=450)
    escolher_suspensao_pneumatica = tk.CTkButton(janela_peso_superiror_s_articulado, command=lambda: peso_superior_particular_s_articulado_1(janela_peso_superiror_s_articulado, pedir_ano, pedir_eixos, pedir_eixos_articulado), text = "Com Suspensão pneumática ou equivalente", font=("Segoe UI",20)) .place(x=502, y=500)
    escolher_suspensao_outra = tk.CTkButton(janela_peso_superiror_s_articulado, command=lambda: peso_superior_particular_s_articulado_2(janela_peso_superiror_s_articulado, pedir_ano, pedir_eixos, pedir_eixos_articulado), text = "Com outro tipo de suspensão" , font=("Segoe UI",20)) .place(x = 567,y=560)


############################### NÃO ARTICULADO #############################




def peso_superior_particular_n_articulado_resultado_2(janela_peso_superiror_n_articulado, pedir_ano, pedir_eixos, peso):
    janela_peso_superiror_n_articulado.withdraw()
    janela_peso_superiror_n_articulado_resultado = tk.CTkToplevel()
    janela_peso_superiror_n_articulado_resultado.geometry("1400x700")
    janela_peso_superiror_n_articulado_resultado.title("Imposto Único de Circulação - Categoria C - Peso Bruto superior a 12t")
    texto_peso_superior_n_articulado_resultado = tk.CTkLabel(janela_peso_superiror_n_articulado_resultado,text = "Simulação do Imposto Único de Circulação\nCategoria C - Não articulado\nResultado Final", font = ("Segoe UI", 20)) .place(x =508, y=0)

    cilindrada = 0
    ano = int(pedir_ano.get())
    categoria = "C2"
    tabela = 0
    ciclo = 0
    co2 = 0
    eixos = int(pedir_eixos.get())
    suspensao = 2
    modelo_escrever = modelo_log[0]
    combustivel = 0
    resultado_eixos= 0
    eixos_articulado = 0


    valor_total, valor, taxa_co2, taxa_adicional, coeficiente, imposto_diesel = iuc.iuc(categoria,tabela,combustivel, cilindrada, ano, ciclo, co2, eixos, peso,suspensao)

    ### SINTESE DE CARACTERISTICAS ###
    titulo_caracteristicas_final = tk.CTkLabel(janela_peso_superiror_n_articulado_resultado, text = "Caracteristicas do pesado", font = ("Segoe UI",20)) .place(x = 293, y=150)
    modelo_resultado_final = tk.CTkLabel(janela_peso_superiror_n_articulado_resultado, text = modelo_escrever, font = ("Segoe UI",20)) .place(x = 293, y=200)
    cilindrada_resultado_final = tk.CTkLabel(janela_peso_superiror_n_articulado_resultado, text=("Peso Bruto: {} kg" .format(peso)), font=("Segoe UI", 20)).place(x=293, y=250)
    ano_resultado_final = tk.CTkLabel(janela_peso_superiror_n_articulado_resultado, text=("Eixos: {}" .format(eixos)), font=("Segoe UI", 20)).place(x=293, y=300)
    combustivel_resultado_final = tk.CTkLabel(janela_peso_superiror_n_articulado_resultado, text = ("Suspensão: Outro tipo de suspensão"), font=("Segoe UI", 20)).place(x=293, y=350)
    ano_resultado_final = tk.CTkLabel(janela_peso_superiror_n_articulado_resultado, text=("Ano: {}" .format(ano)), font =("Segoe UI", 20)).place(x=293, y=400)



    ### APRESENTAÇÃO DOS VALORES ###
    titulo_resumo__valor_resultado_final = tk.CTkLabel(janela_peso_superiror_n_articulado_resultado, text=("Resumo dos valores a pagar:".format(valor)), font=("Segoe UI", 20)).place(x=879, y=150)
    cilindrada_valor_resultado_final = tk.CTkLabel(janela_peso_superiror_n_articulado_resultado, text=("Preço da Cilindrada: {:.2f}€" .format(valor)), font=("Segoe UI", 20)).place(x=879 , y=200)
    valor_total_resultado_final = tk.CTkLabel(janela_peso_superiror_n_articulado_resultado, text=("Valor a pagar: {:.2f}€".format(valor_total)), font=("Segoe UI", 20), bg_color="red").place(x=879, y=250)

    ### FINAL - SAIR OU HISTORICO ###
    decidir_historico = tk.CTkLabel(janela_peso_superiror_n_articulado_resultado, text=("Deseja adicionar está simulação ao histórico?" ), font=("Segoe UI", 20)).place(x=505, y=500)
    select_tabela_a = tk.CTkButton(janela_peso_superiror_n_articulado_resultado, text="Sim",command=lambda: historico_iuc_cat_c(categoria, valor_total, eixos, suspensao, ano, resultado_eixos, eixos_articulado),font=("Segoe UI", 20)).place(x=550, y=550)
    select_tabela_b = tk.CTkButton(janela_peso_superiror_n_articulado_resultado, text="Não",command=lambda: reiniciar_programa(),font=("Segoe UI", 20)).place(x=750, y=550)



def peso_superior_particular_n_articulado_resultado_1(janela_peso_superiror_n_articulado, pedir_ano, pedir_eixos, peso):
    janela_peso_superiror_n_articulado.withdraw()
    janela_peso_superiror_n_articulado_resultado = tk.CTkToplevel()
    janela_peso_superiror_n_articulado_resultado.geometry("1400x700")
    janela_peso_superiror_n_articulado_resultado.title("Imposto Único de Circulação - Categoria C - Peso Bruto superior a 12t")
    texto_peso_superior_n_articulado_resultado = tk.CTkLabel(janela_peso_superiror_n_articulado_resultado,text = "Simulação do Imposto Único de Circulação\nCategoria C - Não articulado\nResultado Final", font = ("Segoe UI", 20)) .place(x =508, y=0)

    cilindrada = 0
    ano = int(pedir_ano.get())
    categoria = "C2"
    tabela = 0
    ciclo = 0
    co2 = 0
    eixos = int(pedir_eixos.get())
    suspensao = 1
    modelo_escrever = modelo_log[0]
    combustivel = 0
    resultado_eixos = 0
    eixos_articulado = 0

    valor_total, valor, taxa_co2, taxa_adicional, coeficiente, imposto_diesel = iuc.iuc(categoria,tabela,combustivel, cilindrada, ano, ciclo, co2, eixos, peso,suspensao)

    ### SINTESE DE CARACTERISTICAS ###
    titulo_caracteristicas_final = tk.CTkLabel(janela_peso_superiror_n_articulado_resultado, text = "Caracteristicas do pesado", font = ("Segoe UI",20)) .place(x = 293, y=150)
    modelo_resultado_final = tk.CTkLabel(janela_peso_superiror_n_articulado_resultado, text = modelo_escrever, font = ("Segoe UI",20)) .place(x = 293, y=200)
    cilindrada_resultado_final = tk.CTkLabel(janela_peso_superiror_n_articulado_resultado, text=("Peso Bruto: {} kg" .format(peso)), font=("Segoe UI", 20)).place(x=293, y=250)
    ano_resultado_final = tk.CTkLabel(janela_peso_superiror_n_articulado_resultado, text=("Eixos: {}" .format(eixos)), font=("Segoe UI", 20)).place(x=293, y=300)
    combustivel_resultado_final = tk.CTkLabel(janela_peso_superiror_n_articulado_resultado, text = ("Suspensão: Com suspensão pneumática ou equivalente"), font=("Segoe UI", 20)).place(x=293, y=350)
    ano_resultado_final = tk.CTkLabel(janela_peso_superiror_n_articulado_resultado, text=("Ano: {}" .format(ano)), font =("Segoe UI", 20)).place(x=293, y=400)



    ### APRESENTAÇÃO DOS VALORES ###
    titulo_resumo__valor_resultado_final = tk.CTkLabel(janela_peso_superiror_n_articulado_resultado, text=("Resumo dos valores a pagar:".format(valor)), font=("Segoe UI", 20)).place(x=879, y=150)
    cilindrada_valor_resultado_final = tk.CTkLabel(janela_peso_superiror_n_articulado_resultado, text=("Preço da Cilindrada: {:.2f}€" .format(valor)), font=("Segoe UI", 20)).place(x=879 , y=200)
    valor_total_resultado_final = tk.CTkLabel(janela_peso_superiror_n_articulado_resultado, text=("Valor a pagar: {:.2f}€".format(valor_total)), font=("Segoe UI", 20), bg_color="red").place(x=879, y=250)

    ### FINAL - SAIR OU HISTORICO ###
    decidir_historico = tk.CTkLabel(janela_peso_superiror_n_articulado_resultado, text=("Deseja adicionar está simulação ao histórico?" ), font=("Segoe UI", 20)).place(x=505, y=500)
    select_tabela_a = tk.CTkButton(janela_peso_superiror_n_articulado_resultado, text="Sim",command=lambda: historico_iuc_cat_c(categoria, valor_total, eixos, suspensao, ano, resultado_eixos, eixos_articulado),font=("Segoe UI", 20)).place(x=550, y=550)
    select_tabela_b = tk.CTkButton(janela_peso_superiror_n_articulado_resultado, text="Não",command=lambda: reiniciar_programa(),font=("Segoe UI", 20)).place(x=750, y=550)



def peso_superior_particular_n_articulado(janela_peso_superior):
    peso = peso_log[0]
    janela_peso_superior.withdraw()
    janela_peso_superiror_n_articulado = tk.CTkToplevel()
    janela_peso_superiror_n_articulado.geometry("1400x700")
    janela_peso_superiror_n_articulado.title("Imposto Único de Circulação - Categoria C - Peso Bruto superior a 12t")
    texto_cat_c_superior = tk.CTkLabel(janela_peso_superiror_n_articulado, text="Simulação do Imposto Único de Circulação\nCategoria C - Peso superior a 12t\nNão articulado ou não é um conjunto de veiculos", font=("Segoe UI", 20)) .place(x=508, y=0)

    texto_ano = tk.CTkLabel(janela_peso_superiror_n_articulado, text="Insira o ano da primeira matrícula", font = ("Segoe UI", 20)) .place(x=566,y=150)
    pedir_ano = tk.CTkEntry(janela_peso_superiror_n_articulado, placeholder_text = "Ano", font = ("Segoe UI", 20), width=150)
    pedir_ano.place(x=650,y=200)
    texto__eixos = tk.CTkLabel(janela_peso_superiror_n_articulado, text = "Insira o número de eixos", font = ("Segoe UI", 20)) .place(x=606,y=250)
    pedir_eixos = tk.CTkEntry(janela_peso_superiror_n_articulado, placeholder_text= "Eixos", font = ("Segoe UI", 20), width=150)
    pedir_eixos.place(x=650, y=300)
    texto_suspensao = tk.CTkLabel(janela_peso_superiror_n_articulado, text = "Escolha o tipo de suspensão: ", font = ("Segoe UI",20)) . place(x= 577, y=350)
    escolher_suspensao_pneumatica = tk.CTkButton(janela_peso_superiror_n_articulado, command=lambda: peso_superior_particular_n_articulado_resultado_1(janela_peso_superiror_n_articulado, pedir_ano, pedir_eixos, peso), text = "Com Suspensão pneumática ou equivalente", font=("Segoe UI",20)) .place(x=502, y=400)
    escolher_suspensao_outra = tk.CTkButton(janela_peso_superiror_n_articulado,command=lambda: peso_superior_particular_n_articulado_resultado_2(janela_peso_superiror_n_articulado, pedir_ano, pedir_eixos, peso), text = "Com outro tipo de suspensão" , font=("Segoe UI",20))  .place(x = 567,y=460)


def peso_superior_particular(pedir_peso_c):
    pedir_peso_c.withdraw()
    janela_peso_superior = tk.CTkToplevel()
    janela_peso_superior.title("Imposto Único de Circulação - Categoria C - Peso Bruto superior a 12t")
    janela_peso_superior.geometry("1400x700")
    texto_cat_c_superior = tk.CTkLabel(janela_peso_superior, text="Simulação do Imposto Único de Circulação\nCategoria C - Peso superior a 12t", font=("Segoe Ui", 20 )) .place(x=508, y=0)

    texto_questao_articulado = tk.CTkLabel(janela_peso_superior, text="O veículo é articulado ou é um conjunto de veículos?", font = ("Segoe UI", 20)) .place(x=470, y=100)
    botao_s_articulado = tk.CTkButton(janela_peso_superior, text="Sim", command=lambda: peso_superior_particular_s_articulado(janela_peso_superior), font = ("Segoe UI",20)).place(x=550, y = 200)
    botao_n_articulado = tk.CTkButton(janela_peso_superior, text="Não", command=lambda: peso_superior_particular_n_articulado(janela_peso_superior),font = ("Segoe UI", 20)) .place(x=720, y=200)




def peso_inferior_particular(pedir_peso_c, pedir_modelo, peso):
    pedir_peso_c.withdraw()
    janela_peso_inferior = tk.CTkToplevel()
    janela_peso_inferior.title("Imposto Único de Circulação - Categoria C - Peso Bruto inferior a 12 t")
    janela_peso_inferior.geometry("1400x700")
    texto_cat_c_inferior_resultado = tk.CTkLabel(janela_peso_inferior, text="Simulação do Imposto Único de Circulação\nCategoria C - Peso inferior a 12 t\nResultado Final", font=("Segoe UI", 20)).place(x=508, y=0)

    cilindrada = 0
    ano = 0
    categoria = "C1"
    tabela = 0
    ciclo = 0
    co2 = 0
    eixos = 0
    suspensao = 0
    modelo_escrever = modelo_log[0]
    combustivel = 0
    resultado_eixos = 0
    eixos_articulado = 0

    valor_total, valor, taxa_co2, taxa_adicional, coeficiente, imposto_diesel = iuc.iuc(categoria,tabela,combustivel, cilindrada, ano, ciclo, co2, eixos, peso,suspensao)

    ### SINTESE DE CARACTERISTICAS ###
    titulo_caracteristicas_final = tk.CTkLabel(janela_peso_inferior, text = "Caracteristicas do pesado", font = ("Segoe UI",20)) .place(x = 293, y=150)
    modelo_resultado_final = tk.CTkLabel(janela_peso_inferior, text = modelo_escrever, font = ("Segoe UI",20)) .place(x = 293, y=200)
    cilindrada_resultado_final = tk.CTkLabel(janela_peso_inferior, text=("Peso Bruto: {}" .format(peso)), font=("Segoe UI", 20)).place(x=293, y=250)
    ano_resultado_final = tk.CTkLabel(janela_peso_inferior, text=("Eixos: N/A"), font=("Segoe UI", 20)).place(x=293, y=300)
    combustivel_resultado_final = tk.CTkLabel(janela_peso_inferior, text=("Suspensão: Com suspensão pneumática ou equivalente"), font=("Segoe UI", 20)).place(x=293, y=350)
    ano_resultado_final = tk.CTkLabel(janela_peso_inferior, text=("Ano: N/A"), font =("Segoe UI", 20)).place(x=293, y=400)



    ### APRESENTAÇÃO DOS VALORES ###
    titulo_resumo__valor_resultado_final = tk.CTkLabel(janela_peso_inferior, text=("Resumo dos valores a pagar:".format(valor)), font=("Segoe UI", 20)).place(x=879, y=150)
    cilindrada_valor_resultado_final = tk.CTkLabel(janela_peso_inferior, text=("Preço da Cilindrada: {:.2f}€" .format(valor)), font=("Segoe UI", 20)).place(x=879 , y=200)
    valor_total_resultado_final = tk.CTkLabel(janela_peso_inferior, text=("Valor a pagar: {:.2f}€".format(valor_total)), font=("Segoe UI", 20), bg_color="red").place(x=879, y=250)

    ### FINAL - SAIR OU HISTORICO ###
    decidir_historico = tk.CTkLabel(janela_peso_inferior, text=("Deseja adicionar está simulação ao histórico?" ), font=("Segoe UI", 20)).place(x=505, y=500)
    select_tabela_a = tk.CTkButton(janela_peso_inferior, text="Sim",command=lambda: historico_iuc_cat_c(categoria, valor_total, eixos, suspensao, ano, resultado_eixos, eixos_articulado),font=("Segoe UI", 20)).place(x=550, y=550)
    select_tabela_b = tk.CTkButton(janela_peso_inferior, text="Não",command=lambda: reiniciar_programa(),font=("Segoe UI", 20)).place(x=750, y=550)


def decisao_peso_particular(pedir_peso_bruto, pedir_modelo, pedir_peso_c):
    peso = float(pedir_peso_bruto.get())
    peso_log.append(peso)
    modelo = str(pedir_modelo.get())
    modelo_log.append(modelo)
    if peso <= 11999:
        peso_inferior_particular(pedir_peso_c, pedir_modelo, peso)
    else:
        peso_superior_particular(pedir_peso_c)

def pedir_peso(janela_iuc):
    janela_iuc.withdraw()
    pedir_peso_c = tk.CTkToplevel()
    pedir_peso_c.title("Imposto Único de Circulação - Categoria C e D")
    pedir_peso_c.geometry("1400x700")
    texto_cat_c_peso = tk.CTkLabel(pedir_peso_c, text="Simulação do Imposto Único de Circulação\nCategoria C e D",  font=("Segoe UI", 20)).place(x=508, y=0)
    texto_modelo = tk.CTkLabel(pedir_peso_c, text="Insira marca e modelo da viatura ", font = ("Segoe UI", 20)) .place(x=549,y=200)
    pedir_modelo = (tk.CTkEntry(pedir_peso_c, placeholder_text = "Insira modelo", font = ("Segoe UI", 20), width=500))
    pedir_modelo.place(x=493,y=250)
    texto_peso = tk.CTkLabel(pedir_peso_c, text="Insira o peso bruto da viatura (kg)", font = ("Segoe UI", 20)) .place(x=539,y=300)
    pedir_peso_bruto = (tk.CTkEntry(pedir_peso_c, placeholder_text = "Peso Bruto", font = ("Segoe UI", 20), width=500))
    pedir_peso_bruto.place(x=493,y=350)

    texto_finalidade=tk.CTkLabel(pedir_peso_c, text = "Indique a finalidade do pesado", font = ("Segoe UI",20)) .place(x=562, y=400)
    particular_simulacao_cat_E = tk.CTkButton(pedir_peso_c, text="Particular", command=lambda: decisao_peso_particular(pedir_peso_bruto, pedir_modelo, pedir_peso_c),font=("Segoe UI", 20)).place(x=550, y=450)
    particular_simulacao_cat_E = tk.CTkButton(pedir_peso_c, text="Público", command=lambda: decisao_peso_publico(pedir_peso_bruto, pedir_modelo, pedir_peso_c),font=("Segoe UI", 20)).place(x=720, y=450)



########################################## IUC MOTAS ################################################

def historico_cat_e(cilindrada, ano, valor, valor_total):
    data_atual = datetime.today().date()
    data_atual_formatada = "{}/{}/{}" .format(data_atual.day, data_atual.month, data_atual.year)
    hora_atual = datetime.now().time()

    f = open("historico.txt", "a+")
    f.write("--- SIMULAÇÃO DO IMPOSTO ÚNICO DE CIRCULAÇÃO 2023 ---\n")
    modelo_escrever_historico = modelo_log[0]
    f.write("Simulação realizada no dia {} ás {}\n".format(data_atual_formatada, hora_atual))
    f.write(" --- Caracterização do motociclo ---\n")
    f.write("Modelo: {} \n".format( modelo_escrever_historico))
    f.write("Categoria: E \n" )
    f.write("Cilindrada: {} cm3\n".format(cilindrada))
    f.write("Ano: {}\n".format(ano))
    f.write("--- Resumo dos valores a pagar ---\n")
    f.write("Preço da Cilindrada: {}€\n".format(valor))

    if valor < 10:
        f.write("Valor final a pagar: ISENTO\n")
    else:
        f.write("Valor final a pagar: {}€\n".format(valor_total))
    f.write("----------------------------------------------------------------\n")
    f.close()
    os.system(f'start notepad {historico}')
    reiniciar_programa()

def confirmar_simulacao_categoria_e(pedir_modelo, pedir_cilindrada_e, pedir_ano_e, janela_cat_e):
    modelo = str(pedir_modelo.get())
    modelo_log.append(modelo)
    cilindrada = int(pedir_cilindrada_e.get())
    ano = int(pedir_ano_e.get())
    categoria = "E"
    tabela = 0
    ciclo = 0
    co2 = 0
    eixos = 0
    peso = 0
    suspensao = 0
    modelo_escrever = modelo_log[0]
    combustivel = 1 #1 é o codigo da gasolina na função

    valor_total, valor, taxa_co2, taxa_adicional, coeficiente, imposto_diesel = iuc.iuc(categoria,tabela,combustivel, cilindrada, ano, ciclo, co2, eixos, peso,suspensao)

    janela_cat_e.withdraw()
    janela_cat_e_resultado = tk.CTkToplevel()
    janela_cat_e_resultado.geometry("1400x700")
    janela_cat_e_resultado.title("Imposto Único de Circulação - Categoria A - Tabela A - Resultado")
    texto_cat_b_tabela_a_gasolina_resultado = tk.CTkLabel(janela_cat_e_resultado,text = "Simulação do Imposto Único de Circulação\nCategoria E\nResultado Final", font = ("Segoe UI", 20)) .place(x =508, y=0)

    ### SINTESE DE CARACTERISTICAS ###
    titulo_caracteristicas_final = tk.CTkLabel(janela_cat_e_resultado, text = "Caracteristicas do motociclo", font = ("Segoe UI",20)) .place(x = 293, y=150)
    modelo_resultado_final = tk.CTkLabel(janela_cat_e_resultado, text = modelo_escrever, font = ("Segoe UI",20)) .place(x = 293, y=200)
    cilindrada_resultado_final = tk.CTkLabel(janela_cat_e_resultado, text=("Cilindrada:{} cm3" .format(cilindrada)), font=("Segoe UI", 20)).place(x=293, y=250)
    ano_resultado_final = tk.CTkLabel(janela_cat_e_resultado, text=("Ano:", ano), font=("Segoe UI", 20)).place(x=293, y=300)



    ### APRESENTAÇÃO DOS VALORES ###
    titulo_resumo__valor_resultado_final = tk.CTkLabel(janela_cat_e_resultado, text=("Resumo dos valores a pagar:".format(valor)), font=("Segoe UI", 20)).place(x=879, y=150)
    cilindrada_valor_resultado_final = tk.CTkLabel(janela_cat_e_resultado, text=("Preço da Cilindrada: {:.2f}€" .format(valor)), font=("Segoe UI", 20)).place(x=879 , y=200)

    if valor < 10:
        valor_total_resultado_final = tk.CTkLabel(janela_cat_e_resultado, text=("Valor a pagar: ISENTO"), font=("Segoe UI", 20), bg_color="red").place(x=879, y=250)
    else:
        valor_total_resultado_final = tk.CTkLabel(janela_cat_e_resultado, text=( "Valor a pagar: {:.2f}€" .format(valor_total)), font=("Segoe UI", 20), bg_color = "red").place(x=879 , y=250)


    ### FINAL - SAIR OU HISTORICO ###
    decidir_historico = tk.CTkLabel(janela_cat_e_resultado, text=("Deseja adicionar está simulação ao histórico?" ), font=("Segoe UI", 20)).place(x=505, y=400)
    select_tabela_a = tk.CTkButton(janela_cat_e_resultado, text="Sim",command=lambda: historico_cat_e(cilindrada, ano, valor, valor_total),font=("Segoe UI", 20)).place(x=550, y=500)
    select_tabela_b = tk.CTkButton(janela_cat_e_resultado, text="Não",command=lambda:reiniciar_programa(),font=("Segoe UI", 20)).place(x=750, y=500)



def iuc_motas(janela_iuc):
    janela_iuc.withdraw() #Fechar pagina inicial
    janela_cat_e = tk.CTkToplevel() #Abrir nova janela
    janela_cat_e.title("Imposto Único de Circulação - Categoria E")
    customtkinter.set_default_color_theme("dark-blue")
    janela_cat_e.geometry("1400x700")


    texto_cat_e = tk.CTkLabel(janela_cat_e, text="Simulação do Imposto Único de Circulação\nCategoria E ", font = ("Segoe UI", 20)) .place(x=550,y=0)
    texto_modelo = tk.CTkLabel(janela_cat_e, text="Insira marca e modelo da viatura (opcional)", font = ("Segoe UI", 20)) .place(x=550,y=150)
    pedir_modelo = (tk.CTkEntry(janela_cat_e, placeholder_text = "Insira modelo", font = ("Segoe UI", 20), width=500))
    pedir_modelo.place(x=500,y=200)
    texto_cilindrada_e = tk.CTkLabel(janela_cat_e, text="Insira a cilindrada (cm3)", font = ("Segoe UI", 20)) .place(x=599,y=250)
    pedir_cilindrada_e = (tk.CTkEntry(janela_cat_e, placeholder_text = "Cilindrada", font = ("Segoe UI", 20), width=300))
    pedir_cilindrada_e.place(x=550,y=300)
    texto_ano_e = tk.CTkLabel(janela_cat_e, text="Insira o ano da primeira matrícula", font = ("Segoe UI", 20)) .place(x=556,y=350)
    pedir_ano_e = (tk.CTkEntry(janela_cat_e, placeholder_text = "Ano", font = ("Segoe UI", 20), width=100))
    pedir_ano_e.place(x=650,y=400)
    avancar_simulacao_cat_E = tk.CTkButton(janela_cat_e, text="Confirmar", command=lambda: confirmar_simulacao_categoria_e(pedir_modelo, pedir_cilindrada_e, pedir_ano_e, janela_cat_e), font=("Segoe UI", 20)).place(x=626, y=550)

########################################## IUC CARROS ####################################


def historico_iuc_cat_a(categoria, ciclo, tabela, co2, ano, combustivel, cilindrada, valor, taxa_adicional, coeficiente, taxa_co2,imposto_diesel, valor_total):
    data_atual = datetime.today().date()
    data_atual_formatada = "{}/{}/{}" .format(data_atual.day, data_atual.month, data_atual.year)
    hora_atual = datetime.now().time()

    f = open("historico.txt", "a+")
    f.write("--- SIMULAÇÃO DO IMPOSTO ÚNICO DE CIRCULAÇÃO 2023 ---\n")
    modelo_escrever_historico = modelo_log[0]
    f.write("Simulação realizada no dia {} ás {}\n".format(data_atual_formatada, hora_atual))
    f.write(" --- Caracterização da viatura ---\n")
    f.write("Modelo: {} \n".format( modelo_escrever_historico))
    f.write("Categoria: {} \n" .format(categoria))
    f.write("Tabela: {}\n" .format(tabela))
    if co2 == 0:
        f.write("Consumo de CO2: N/A\n")
    else:
        f.write("Consumo de CO2: {} g/km\n".format(co2))

    if ciclo == 0:
        f.write("Ciclo de CO2: N/A \n")
    elif ciclo ==  1:
        f.write("Ciclo de CO2: NEDC\n")
    elif ciclo == 2:
        f.write("Ciclo de CO2: WLTP\n")

    if combustivel == 1:
        f.write("Combustível: Gasolina\n")
    elif combustivel == 2:
        f.write("Combustível: Gasóleo\n")
    f.write("Cilindrada: {} cm3\n".format(cilindrada))
    f.write("Ano: {}\n".format(ano))
    f.write("--- Resumo dos valores a pagar ---\n")
    f.write("Preço da Cilindrada: {}€\n".format(valor))
    f.write("Taxa adicional para altas cilindradas: {}€\n" .format(taxa_adicional))
    f.write("Coeficiente adicional: {}\n".format(coeficiente))
    f.write("Taxa de CO2: {}€\n".format(taxa_co2))
    f.write("Taxa de combustivel: {}€\n".format(imposto_diesel))
    f.write("Valor final a pagar: {}€\n".format(valor_total))
    f.write("----------------------------------------------------------------\n")
    f.close()
    os.system(f'start notepad {historico}')
    reiniciar_programa()





### SIMULAR CATEGORIA A TABELA A GASOLINA ###
def confirmar_simulacao_categoria_b_tab_a_gasolina(pedir_cilindrada_a, pedir_ano_a, janela_cat_b_tabela_a, modelo):
    cilindrada = int(pedir_cilindrada_a.get())
    ano = int(pedir_ano_a.get())
    categoria = "A"
    tabela = "A"
    ciclo = 0
    co2 = 0
    eixos = 0
    peso = 0
    suspensao = 0
    modelo_escrever = modelo_log[0]
    combustivel = 1 #1 é o codigo da gasolina na função

    valor_total, valor, taxa_co2, taxa_adicional, coeficiente, imposto_diesel = iuc.iuc(categoria,tabela,combustivel, cilindrada, ano, ciclo, co2, eixos, peso,suspensao)

    janela_cat_b_tabela_a.withdraw()
    janela_cat_b_tabela_a_gasolina_resultado = tk.CTkToplevel()
    janela_cat_b_tabela_a_gasolina_resultado.geometry("1400x700")
    janela_cat_b_tabela_a_gasolina_resultado.title("Imposto Único de Circulação - Categoria A - Tabela A - Resultado")
    texto_cat_b_tabela_a_gasolina_resultado = tk.CTkLabel(janela_cat_b_tabela_a_gasolina_resultado,text = "Simulação do Imposto Único de Circulação\nCategoria A - Tabela A\nResultado Final", font = ("Segoe UI", 20)) .place(x =508, y=0)

    ### SINTESE DE CARACTERISTICAS ###
    titulo_caracteristicas_final = tk.CTkLabel(janela_cat_b_tabela_a_gasolina_resultado, text = "Caracteristicas da viatura", font = ("Segoe UI",20)) .place(x = 293, y=150)
    modelo_resultado_final = tk.CTkLabel(janela_cat_b_tabela_a_gasolina_resultado, text = modelo_escrever, font = ("Segoe UI",20)) .place(x = 293, y=200)
    cilindrada_resultado_final = tk.CTkLabel(janela_cat_b_tabela_a_gasolina_resultado, text=("Cilindrada:{} cm3" .format(cilindrada)), font=("Segoe UI", 20)).place(x=293, y=250)
    combustivel_resultado_final = tk.CTkLabel(janela_cat_b_tabela_a_gasolina_resultado, text=("Combustivel: Gasolina"), font=("Segoe UI", 20)).place(x=293, y=300)
    ano_resultado_final = tk.CTkLabel(janela_cat_b_tabela_a_gasolina_resultado, text=("Ano:", ano), font=("Segoe UI", 20)).place(x=293, y=350)
    ciclo_resultado_final = tk.CTkLabel(janela_cat_b_tabela_a_gasolina_resultado, text=("Ciclo de CO2: N/A"), font=("Segoe UI", 20)).place(x=293, y=400)
    consumo_co2_resultado_final =  tk.CTkLabel(janela_cat_b_tabela_a_gasolina_resultado, text=("Consumo de CO2: N/A "), font=("Segoe UI", 20)).place(x=293, y=450)


    ### APRESENTAÇÃO DOS VALORES ###
    titulo_resumo__valor_resultado_final = tk.CTkLabel(janela_cat_b_tabela_a_gasolina_resultado, text=("Resumo dos valores a pagar:".format(valor)), font=("Segoe UI", 20)).place(x=879, y=150)
    cilindrada_valor_resultado_final = tk.CTkLabel(janela_cat_b_tabela_a_gasolina_resultado, text=("Preço da Cilindrada: {:.2f}€" .format(valor)), font=("Segoe UI", 20)).place(x=879 , y=200)
    taxa_adicional_cilindrada = tk.CTkLabel(janela_cat_b_tabela_a_gasolina_resultado, text=("Preço da Taxa adicional da cilindrada: {:.2f}€" .format(taxa_adicional)), font=("Segoe UI", 20)).place(x=879 , y=250)
    coeficiente_resultado_final = tk.CTkLabel(janela_cat_b_tabela_a_gasolina_resultado, text=("Coeficiente adicional:{:.2f}€ " .format(coeficiente)), font=("Segoe UI", 20)).place(x=879 , y=300)
    taxa_co2_resultado_final = tk.CTkLabel(janela_cat_b_tabela_a_gasolina_resultado, text=( "Preço da taxa de co2: {:.2f}€" .format(taxa_co2)), font=("Segoe UI", 20)).place(x=879 , y=350)
    taxa_diesel_resultado_final = tk.CTkLabel(janela_cat_b_tabela_a_gasolina_resultado, text=("Preço da taxa de combustível: {:.2f}€" .format(imposto_diesel)), font=("Segoe UI", 20)).place(x=879 , y=400)
    valor_total_resultado_final = tk.CTkLabel(janela_cat_b_tabela_a_gasolina_resultado, text=( "Valor a pagar: {:.2f}€" .format(valor_total)), font=("Segoe UI", 20), bg_color = "red").place(x=879 , y=450)


    ### FINAL - SAIR OU HISTORICO ###
    decidir_historico = tk.CTkLabel(janela_cat_b_tabela_a_gasolina_resultado, text=("Deseja adicionar está simulação ao histórico?" ), font=("Segoe UI", 20)).place(x=505, y=500)
    select_tabela_a = tk.CTkButton(janela_cat_b_tabela_a_gasolina_resultado, text="Sim",command=lambda: historico_iuc_cat_a(categoria, ciclo, tabela, co2, ano, combustivel, cilindrada, valor, taxa_adicional, coeficiente, taxa_co2,imposto_diesel, valor_total),font=("Segoe UI", 20)).place(x=550, y=550)
    select_tabela_b = tk.CTkButton(janela_cat_b_tabela_a_gasolina_resultado, text="Não",command=lambda: reiniciar_programa(),font=("Segoe UI", 20)).place(x=750, y=550)



def confirmar_simulacao_categoria_b_tab_a_gasoleo(pedir_cilindrada_a, pedir_ano_a, janela_cat_b_tabela_a, modelo):
    cilindrada = int(pedir_cilindrada_a.get())
    ano = int(pedir_ano_a.get())
    categoria = "A"
    tabela = "A"
    ciclo = 0
    co2 = 0
    eixos = 0
    peso = 0
    suspensao = 0
    modelo_escrever = modelo_log[0]
    combustivel = 2 #1 é o codigo da gasoleo na função

    valor_total, valor, taxa_co2, taxa_adicional, coeficiente, imposto_diesel = iuc.iuc(categoria,tabela,combustivel, cilindrada, ano, ciclo, co2, eixos, peso,suspensao)

    janela_cat_b_tabela_a.withdraw()
    janela_cat_b_tabela_a_gasolina_resultado = tk.CTkToplevel()
    janela_cat_b_tabela_a_gasolina_resultado.geometry("1400x700")
    janela_cat_b_tabela_a_gasolina_resultado.title("Imposto Único de Circulação - Categoria A - Tabela A - Resultado")
    texto_cat_b_tabela_a_gasolina_resultado = tk.CTkLabel(janela_cat_b_tabela_a_gasolina_resultado,text = "Simulação do Imposto Único de Circulação\nCategoria A - Tabela A\nResultado Final", font = ("Segoe UI", 20)) .place(x =508, y=0)

    ### SINTESE DE CARACTERISTICAS ###
    titulo_caracteristicas_final = tk.CTkLabel(janela_cat_b_tabela_a_gasolina_resultado, text = "Caracteristicas da viatura", font = ("Segoe UI",20)) .place(x = 293, y=150)
    modelo_resultado_final = tk.CTkLabel(janela_cat_b_tabela_a_gasolina_resultado, text = modelo_escrever, font = ("Segoe UI",20)) .place(x = 293, y=200)
    cilindrada_resultado_final = tk.CTkLabel(janela_cat_b_tabela_a_gasolina_resultado, text=("Cilindrada:{} cm3" .format(cilindrada)), font=("Segoe UI", 20)).place(x=293, y=250)
    combustivel_resultado_final = tk.CTkLabel(janela_cat_b_tabela_a_gasolina_resultado, text=("Combustível: Gasóleo"), font=("Segoe UI", 20)).place(x=293, y=300)
    ano_resultado_final = tk.CTkLabel(janela_cat_b_tabela_a_gasolina_resultado, text=("Ano:", ano), font=("Segoe UI", 20)).place(x=293, y=350)
    ciclo_resultado_final = tk.CTkLabel(janela_cat_b_tabela_a_gasolina_resultado, text=("Ciclo de CO2: N/A"), font=("Segoe UI", 20)).place(x=293, y=400)
    consumo_co2_resultado_final =  tk.CTkLabel(janela_cat_b_tabela_a_gasolina_resultado, text=("Consumo de CO2: N/A "), font=("Segoe UI", 20)).place(x=293, y=450)


    ### APRESENTAÇÃO DOS VALORES ###
    titulo_resumo__valor_resultado_final = tk.CTkLabel(janela_cat_b_tabela_a_gasolina_resultado, text=("Resumo dos valores a pagar:".format(valor)), font=("Segoe UI", 20)).place(x=879, y=150)
    cilindrada_valor_resultado_final = tk.CTkLabel(janela_cat_b_tabela_a_gasolina_resultado, text=("Preço da Cilindrada: {:.2f}€" .format(valor)), font=("Segoe UI", 20)).place(x=879 , y=200)
    taxa_adicional_cilindrada = tk.CTkLabel(janela_cat_b_tabela_a_gasolina_resultado, text=("Preço da Taxa adicional da cilindrada: {:.2f}€" .format(taxa_adicional)), font=("Segoe UI", 20)).place(x=879 , y=250)
    coeficiente_resultado_final = tk.CTkLabel(janela_cat_b_tabela_a_gasolina_resultado, text=("Coeficiente adicional:{:.2f}€ " .format(coeficiente)), font=("Segoe UI", 20)).place(x=879 , y=300)
    taxa_co2_resultado_final = tk.CTkLabel(janela_cat_b_tabela_a_gasolina_resultado, text=( "Preço da taxa de co2: {:.2f}€" .format(taxa_co2)), font=("Segoe UI", 20)).place(x=879 , y=350)
    taxa_diesel_resultado_final = tk.CTkLabel(janela_cat_b_tabela_a_gasolina_resultado, text=("Preço da taxa de combustível: {:.2f}€" .format(imposto_diesel)), font=("Segoe UI", 20)).place(x=879 , y=400)
    valor_total_resultado_final = tk.CTkLabel(janela_cat_b_tabela_a_gasolina_resultado, text=( "Valor a pagar: {:.2f}€" .format(valor_total)), font=("Segoe UI", 20), bg_color = "red").place(x=879 , y=450)


    ### FINAL - SAIR OU HISTORICO ###
    decidir_historico = tk.CTkLabel(janela_cat_b_tabela_a_gasolina_resultado, text=("Deseja adicionar está simulação ao histórico?" ), font=("Segoe UI", 20)).place(x=505, y=500)
    select_tabela_a = tk.CTkButton(janela_cat_b_tabela_a_gasolina_resultado, text="Sim",command=lambda: historico_iuc_cat_a(categoria, ciclo, tabela, co2, ano, combustivel, cilindrada, valor, taxa_adicional, coeficiente, taxa_co2,imposto_diesel, valor_total),font=("Segoe UI", 20)).place(x=550, y=550)
    select_tabela_b = tk.CTkButton(janela_cat_b_tabela_a_gasolina_resultado, text="Não",command=lambda: reiniciar_programa(),font=("Segoe UI", 20)).place(x=750, y=550)

#### BOTÃO TABELA A ###
def botao_iuc_cat_b_tabela_a(pedir_modelo, janela_cat_b):
    modelo = str(pedir_modelo.get())
    modelo_log.append(modelo)
    janela_cat_b.withdraw() #Fechar pagina inicial
    janela_cat_b_tabela_a = tk.CTkToplevel() #Abrir nova janela
    customtkinter.set_default_color_theme("dark-blue")
    janela_cat_b_tabela_a.geometry("1400x700")
    janela_cat_b_tabela_a.title("Imposto Único de Circulação - Categoria A - Tabela A")
    texto_cat_b_tabela_a = tk.CTkLabel(janela_cat_b_tabela_a, text="Simulação do Imposto Único de Circulação\nCategoria B - Tabela A ", font = ("Segoe UI", 20)) .place(x=508,y=0)
    texto_cilindrada_a = tk.CTkLabel(janela_cat_b_tabela_a, text="Insira a cilindrada (cm3)", font = ("Segoe UI", 20)) .place(x=599,y=100)
    pedir_cilindrada_a = (tk.CTkEntry(janela_cat_b_tabela_a, placeholder_text = "Cilindrada", font = ("Segoe UI", 20), width=300))
    pedir_cilindrada_a.place(x=550,y=150)
    texto_ano_a = tk.CTkLabel(janela_cat_b_tabela_a, text="Insira o ano da primeira matrícula", font = ("Segoe UI", 20)) .place(x=556,y=300)
    pedir_ano_a = (tk.CTkEntry(janela_cat_b_tabela_a, placeholder_text = "Ano", font = ("Segoe UI", 20), width=100))
    pedir_ano_a.place(x=650,y=350)
    gasolina_cat_b_tab_a = tk.CTkButton(janela_cat_b_tabela_a, text="Gasolina", command=lambda: confirmar_simulacao_categoria_b_tab_a_gasolina(pedir_cilindrada_a, pedir_ano_a,janela_cat_b_tabela_a, modelo), font=("Segoe UI", 20)).place(x=550, y=550)
    gasoleo_cat_b_tab_a = tk.CTkButton(janela_cat_b_tabela_a, text="Gasóleo", command=lambda: confirmar_simulacao_categoria_b_tab_a_gasoleo(pedir_cilindrada_a, pedir_ano_a, janela_cat_b_tabela_a, modelo), font=("Segoe UI", 20)).place(x=750, y=550)


def resultado_final_iuc_cat_b_tabela_b_co2_gasolina_nedc(cilindrada, ano, pedir_quantidade_co2, janela_cat_b_tabela_b_gasolina_co2):
    co2 = float(pedir_quantidade_co2.get())
    print(co2)

    categoria = "A"
    tabela = "B"
    ciclo = 1
    eixos = 0
    peso = 0
    suspensao = 0
    modelo_escrever = modelo_log[0]
    combustivel = 1 #1 é o codigo da gasolina na função

    valor_total, valor, taxa_co2, taxa_adicional, coeficiente, imposto_diesel = iuc.iuc(categoria,tabela,combustivel, cilindrada, ano, ciclo, co2, eixos, peso,suspensao)

    janela_cat_b_tabela_b_gasolina_co2.withdraw()
    janela_cat_b_tabela_b_nedc_gasolina_resultado = tk.CTkToplevel()
    janela_cat_b_tabela_b_nedc_gasolina_resultado.geometry("1400x700")
    janela_cat_b_tabela_b_nedc_gasolina_resultado.title("Imposto Único de Circulação - Categoria A - Tabela B - Resultado")
    texto_cat_b_tabela_a_gasolina_resultado = tk.CTkLabel(janela_cat_b_tabela_b_nedc_gasolina_resultado,text = "Simulação do Imposto Único de Circulação\nCategoria A - Tabela B\nResultado Final", font = ("Segoe UI", 20)) .place(x =508, y=0)

    ### SINTESE DE CARACTERISTICAS ###
    titulo_caracteristicas_final = tk.CTkLabel(janela_cat_b_tabela_b_nedc_gasolina_resultado, text = "Caracteristicas da viatura", font = ("Segoe UI",20)) .place(x = 293, y=150)
    modelo_resultado_final = tk.CTkLabel(janela_cat_b_tabela_b_nedc_gasolina_resultado, text = modelo_escrever, font = ("Segoe UI",20)) .place(x = 293, y=200)
    cilindrada_resultado_final = tk.CTkLabel(janela_cat_b_tabela_b_nedc_gasolina_resultado, text=("Cilindrada:{} cm3" .format(cilindrada)), font=("Segoe UI", 20)).place(x=293, y=250)
    combustivel_resultado_final = tk.CTkLabel(janela_cat_b_tabela_b_nedc_gasolina_resultado, text=("Combustível: Gasolina"), font=("Segoe UI", 20)).place(x=293, y=300)
    ano_resultado_final = tk.CTkLabel(janela_cat_b_tabela_b_nedc_gasolina_resultado, text=("Ano:", ano), font=("Segoe UI", 20)).place(x=293, y=350)
    ciclo_resultado_final = tk.CTkLabel(janela_cat_b_tabela_b_nedc_gasolina_resultado, text=("Ciclo de CO2: NEDC"), font=("Segoe UI", 20)).place(x=293, y=400)
    consumo_co2_resultado_final =  tk.CTkLabel(janela_cat_b_tabela_b_nedc_gasolina_resultado, text=("Consumo de CO2: {} ".format(co2)), font=("Segoe UI", 20)).place(x=293, y=450)


    ### APRESENTAÇÃO DOS VALORES ###
    titulo_resumo__valor_resultado_final = tk.CTkLabel(janela_cat_b_tabela_b_nedc_gasolina_resultado, text=("Resumo dos valores a pagar:".format(valor)), font=("Segoe UI", 20)).place(x=879, y=150)
    cilindrada_valor_resultado_final = tk.CTkLabel(janela_cat_b_tabela_b_nedc_gasolina_resultado, text=("Preço da Cilindrada: {:.2f}€" .format(valor)), font=("Segoe UI", 20)).place(x=879 , y=200)
    taxa_adicional_cilindrada = tk.CTkLabel(janela_cat_b_tabela_b_nedc_gasolina_resultado, text=("Preço da Taxa adicional da cilindrada: {:.2f}€" .format(taxa_adicional)), font=("Segoe UI", 20)).place(x=879 , y=250)
    coeficiente_resultado_final = tk.CTkLabel(janela_cat_b_tabela_b_nedc_gasolina_resultado, text=("Coeficiente adicional:{:.2f} " .format(coeficiente)), font=("Segoe UI", 20)).place(x=879 , y=300)
    taxa_co2_resultado_final = tk.CTkLabel(janela_cat_b_tabela_b_nedc_gasolina_resultado, text=( "Preço da taxa de co2: {:.2f}€" .format(taxa_co2)), font=("Segoe UI", 20)).place(x=879 , y=350)
    taxa_diesel_resultado_final = tk.CTkLabel(janela_cat_b_tabela_b_nedc_gasolina_resultado, text=("Preço da taxa de combustível: {:.2f}€" .format(imposto_diesel)), font=("Segoe UI", 20)).place(x=879 , y=400)
    valor_total_resultado_final = tk.CTkLabel(janela_cat_b_tabela_b_nedc_gasolina_resultado, text=( "Valor a pagar: {:.2f}€" .format(valor_total)), font=("Segoe UI", 20), bg_color = "red").place(x=879 , y=450)


    ### FINAL - SAIR OU HISTORICO ###
    decidir_historico = tk.CTkLabel(janela_cat_b_tabela_b_nedc_gasolina_resultado, text=("Deseja adicionar está simulação ao histórico?" ), font=("Segoe UI", 20)).place(x=505, y=500)
    select_tabela_a = tk.CTkButton(janela_cat_b_tabela_b_nedc_gasolina_resultado, text="Sim",command=lambda: historico_iuc_cat_a(categoria, ciclo, tabela, co2, ano, combustivel, cilindrada, valor, taxa_adicional, coeficiente, taxa_co2,imposto_diesel, valor_total),font=("Segoe UI", 20)).place(x=550, y=550)
    select_tabela_b = tk.CTkButton(janela_cat_b_tabela_b_nedc_gasolina_resultado, text="Não",command=lambda: reiniciar_programa(),font=("Segoe UI", 20)).place(x=750, y=550)


def resultado_final_iuc_cat_b_tabela_b_co2_gasolina_wltp(cilindrada, ano, pedir_quantidade_co2, janela_cat_b_tabela_b_gasolina_co2):
    co2 = float(pedir_quantidade_co2.get())
    print(co2)

    categoria = "A"
    tabela = "B"
    ciclo = 2 #2 corresponde a wltp
    eixos = 0
    peso = 0
    suspensao = 0
    modelo_escrever = modelo_log[0]
    combustivel = 1 #1 é o codigo da gasolina na função

    valor_total, valor, taxa_co2, taxa_adicional, coeficiente, imposto_diesel = iuc.iuc(categoria,tabela,combustivel, cilindrada, ano, ciclo, co2, eixos, peso,suspensao)

    janela_cat_b_tabela_b_gasolina_co2.withdraw()
    janela_cat_b_tabela_b_wltp_gasolina_resultado = tk.CTkToplevel()
    janela_cat_b_tabela_b_wltp_gasolina_resultado.geometry("1400x700")
    janela_cat_b_tabela_b_wltp_gasolina_resultado.title("Imposto Único de Circulação - Categoria A - Tabela B - Resultado")
    texto_cat_b_tabela_a_gasolina_resultado = tk.CTkLabel(janela_cat_b_tabela_b_wltp_gasolina_resultado,text = "Simulação do Imposto Único de Circulação\nCategoria A - Tabela B\nResultado Final", font = ("Segoe UI", 20)) .place(x =508, y=0)

    ### SINTESE DE CARACTERISTICAS ###
    titulo_caracteristicas_final = tk.CTkLabel(janela_cat_b_tabela_b_wltp_gasolina_resultado, text = "Caracteristicas da viatura", font = ("Segoe UI",20)) .place(x = 293, y=150)
    modelo_resultado_final = tk.CTkLabel(janela_cat_b_tabela_b_wltp_gasolina_resultado, text = modelo_escrever, font = ("Segoe UI",20)) .place(x = 293, y=200)
    cilindrada_resultado_final = tk.CTkLabel(janela_cat_b_tabela_b_wltp_gasolina_resultado, text=("Cilindrada:{} cm3" .format(cilindrada)), font=("Segoe UI", 20)).place(x=293, y=250)
    combustivel_resultado_final = tk.CTkLabel(janela_cat_b_tabela_b_wltp_gasolina_resultado, text=("Combustível: Gasolina"), font=("Segoe UI", 20)).place(x=293, y=300)
    ano_resultado_final = tk.CTkLabel(janela_cat_b_tabela_b_wltp_gasolina_resultado, text=("Ano:", ano), font=("Segoe UI", 20)).place(x=293, y=350)
    ciclo_resultado_final = tk.CTkLabel(janela_cat_b_tabela_b_wltp_gasolina_resultado, text=("Ciclo de CO2: WLTP"), font=("Segoe UI", 20)).place(x=293, y=400)
    consumo_co2_resultado_final =  tk.CTkLabel(janela_cat_b_tabela_b_wltp_gasolina_resultado, text=("Consumo de CO2: {} ".format(co2)), font=("Segoe UI", 20)).place(x=293, y=450)


    ### APRESENTAÇÃO DOS VALORES ###
    titulo_resumo__valor_resultado_final = tk.CTkLabel(janela_cat_b_tabela_b_wltp_gasolina_resultado, text=("Resumo dos valores a pagar:".format(valor)), font=("Segoe UI", 20)).place(x=879, y=150)
    cilindrada_valor_resultado_final = tk.CTkLabel(janela_cat_b_tabela_b_wltp_gasolina_resultado, text=("Preço da Cilindrada: {:.2f}€" .format(valor)), font=("Segoe UI", 20)).place(x=879 , y=200)
    taxa_adicional_cilindrada = tk.CTkLabel(janela_cat_b_tabela_b_wltp_gasolina_resultado, text=("Preço da Taxa adicional da cilindrada: {:.2f}€" .format(taxa_adicional)), font=("Segoe UI", 20)).place(x=879 , y=250)
    coeficiente_resultado_final = tk.CTkLabel(janela_cat_b_tabela_b_wltp_gasolina_resultado, text=("Coeficiente adicional:{:.2f} " .format(coeficiente)), font=("Segoe UI", 20)).place(x=879 , y=300)
    taxa_co2_resultado_final = tk.CTkLabel(janela_cat_b_tabela_b_wltp_gasolina_resultado, text=( "Preço da taxa de co2: {:.2f}€" .format(taxa_co2)), font=("Segoe UI", 20)).place(x=879 , y=350)
    taxa_diesel_resultado_final = tk.CTkLabel(janela_cat_b_tabela_b_wltp_gasolina_resultado, text=("Preço da taxa de combustível: {:.2f}€" .format(imposto_diesel)), font=("Segoe UI", 20)).place(x=879 , y=400)
    valor_total_resultado_final = tk.CTkLabel(janela_cat_b_tabela_b_wltp_gasolina_resultado, text=( "Valor a pagar: {:.2f}€" .format(valor_total)), font=("Segoe UI", 20), bg_color = "red").place(x=879 , y=450)


    ### FINAL - SAIR OU HISTORICO ###
    decidir_historico = tk.CTkLabel(janela_cat_b_tabela_b_wltp_gasolina_resultado, text=("Deseja adicionar está simulação ao histórico?" ), font=("Segoe UI", 20)).place(x=505, y=500)
    select_tabela_a = tk.CTkButton(janela_cat_b_tabela_b_wltp_gasolina_resultado, text="Sim",command=lambda: historico_iuc_cat_a(categoria, ciclo, tabela, co2, ano, combustivel, cilindrada, valor, taxa_adicional, coeficiente, taxa_co2,imposto_diesel, valor_total),font=("Segoe UI", 20)).place(x=550, y=550)
    select_tabela_b = tk.CTkButton(janela_cat_b_tabela_b_wltp_gasolina_resultado, text="Não",command=lambda: reiniciar_programa(),font=("Segoe UI", 20)).place(x=750, y=550)

def resultado_final_iuc_cat_b_tabela_b_co2_gasoleo_wltp(cilindrada, ano, pedir_quantidade_co2, janela_cat_b_tabela_b_gasoleo_co2):
    co2 = float(pedir_quantidade_co2.get())
    print(co2)

    categoria = "A"
    tabela = "B"
    ciclo = 2 #2 corresponde a wltp
    eixos = 0
    peso = 0
    suspensao = 0
    modelo_escrever = modelo_log[0]
    combustivel = 2 #1 é o codigo da gasoleo na função

    valor_total, valor, taxa_co2, taxa_adicional, coeficiente, imposto_diesel = iuc.iuc(categoria,tabela,combustivel, cilindrada, ano, ciclo, co2, eixos, peso,suspensao)

    janela_cat_b_tabela_b_gasoleo_co2.withdraw()
    janela_cat_b_tabela_b_wltp_gasoleo_resultado = tk.CTkToplevel()
    janela_cat_b_tabela_b_wltp_gasoleo_resultado.geometry("1400x700")
    janela_cat_b_tabela_b_wltp_gasoleo_resultado.title("Imposto Único de Circulação - Categoria A - Tabela B - Resultado")
    texto_cat_b_tabela_a_gasoleo_resultado = tk.CTkLabel(janela_cat_b_tabela_b_wltp_gasoleo_resultado,text = "Simulação do Imposto Único de Circulação\nCategoria A - Tabela B\nResultado Final", font = ("Segoe UI", 20)) .place(x =508, y=0)

    ### SINTESE DE CARACTERISTICAS ###
    titulo_caracteristicas_final = tk.CTkLabel(janela_cat_b_tabela_b_wltp_gasoleo_resultado, text = "Caracteristicas da viatura", font = ("Segoe UI",20)) .place(x = 293, y=150)
    modelo_resultado_final = tk.CTkLabel(janela_cat_b_tabela_b_wltp_gasoleo_resultado, text = modelo_escrever, font = ("Segoe UI",20)) .place(x = 293, y=200)
    cilindrada_resultado_final = tk.CTkLabel(janela_cat_b_tabela_b_wltp_gasoleo_resultado, text=("Cilindrada:{} cm3" .format(cilindrada)), font=("Segoe UI", 20)).place(x=293, y=250)
    combustivel_resultado_final = tk.CTkLabel(janela_cat_b_tabela_b_wltp_gasoleo_resultado, text=("Combustível: Gasolina"), font=("Segoe UI", 20)).place(x=293, y=300)
    ano_resultado_final = tk.CTkLabel(janela_cat_b_tabela_b_wltp_gasoleo_resultado, text=("Ano:", ano), font=("Segoe UI", 20)).place(x=293, y=350)
    ciclo_resultado_final = tk.CTkLabel(janela_cat_b_tabela_b_wltp_gasoleo_resultado, text=("Ciclo de CO2: WLTP"), font=("Segoe UI", 20)).place(x=293, y=400)
    consumo_co2_resultado_final =  tk.CTkLabel(janela_cat_b_tabela_b_wltp_gasoleo_resultado, text=("Consumo de CO2: {} ".format(co2)), font=("Segoe UI", 20)).place(x=293, y=450)


    ### APRESENTAÇÃO DOS VALORES ###
    titulo_resumo__valor_resultado_final = tk.CTkLabel(janela_cat_b_tabela_b_wltp_gasoleo_resultado, text=("Resumo dos valores a pagar:".format(valor)), font=("Segoe UI", 20)).place(x=879, y=150)
    cilindrada_valor_resultado_final = tk.CTkLabel(janela_cat_b_tabela_b_wltp_gasoleo_resultado, text=("Preço da Cilindrada: {:.2f}€" .format(valor)), font=("Segoe UI", 20)).place(x=879 , y=200)
    taxa_adicional_cilindrada = tk.CTkLabel(janela_cat_b_tabela_b_wltp_gasoleo_resultado, text=("Preço da Taxa adicional da cilindrada: {:.2f}€" .format(taxa_adicional)), font=("Segoe UI", 20)).place(x=879 , y=250)
    coeficiente_resultado_final = tk.CTkLabel(janela_cat_b_tabela_b_wltp_gasoleo_resultado, text=("Coeficiente adicional:{:.2f} " .format(coeficiente)), font=("Segoe UI", 20)).place(x=879 , y=300)
    taxa_co2_resultado_final = tk.CTkLabel(janela_cat_b_tabela_b_wltp_gasoleo_resultado, text=( "Preço da taxa de co2: {:.2f}€" .format(taxa_co2)), font=("Segoe UI", 20)).place(x=879 , y=350)
    taxa_diesel_resultado_final = tk.CTkLabel(janela_cat_b_tabela_b_wltp_gasoleo_resultado, text=("Preço da taxa de combustível: {:.2f}€" .format(imposto_diesel)), font=("Segoe UI", 20)).place(x=879 , y=400)
    valor_total_resultado_final = tk.CTkLabel(janela_cat_b_tabela_b_wltp_gasoleo_resultado, text=( "Valor a pagar: {:.2f}€" .format(valor_total)), font=("Segoe UI", 20), bg_color = "red").place(x=879 , y=450)


    ### FINAL - SAIR OU HISTORICO ###
    decidir_historico = tk.CTkLabel(janela_cat_b_tabela_b_wltp_gasoleo_resultado, text=("Deseja adicionar está simulação ao histórico?" ), font=("Segoe UI", 20)).place(x=505, y=500)
    select_tabela_a = tk.CTkButton(janela_cat_b_tabela_b_wltp_gasoleo_resultado, text="Sim",command=lambda: historico_iuc_cat_a(categoria, ciclo, tabela, co2, ano, combustivel, cilindrada, valor, taxa_adicional, coeficiente, taxa_co2,imposto_diesel, valor_total),font=("Segoe UI", 20)).place(x=550, y=550)
    select_tabela_b = tk.CTkButton(janela_cat_b_tabela_b_wltp_gasoleo_resultado, text="Não",command=lambda: reiniciar_programa(),font=("Segoe UI", 20)).place(x=750, y=550)

def resultado_final_iuc_cat_b_tabela_b_co2_gasoleo_nedc(cilindrada, ano, pedir_quantidade_co2, janela_cat_b_tabela_b_gasolina_co2):
    co2 = float(pedir_quantidade_co2.get())
    print(co2)

    categoria = "A"
    tabela = "B"
    ciclo = 1
    eixos = 0
    peso = 0
    suspensao = 0
    modelo_escrever = modelo_log[0]
    combustivel = 1 #1 é o codigo da gasolina na função

    valor_total, valor, taxa_co2, taxa_adicional, coeficiente, imposto_diesel = iuc.iuc(categoria,tabela,combustivel, cilindrada, ano, ciclo, co2, eixos, peso,suspensao)

    janela_cat_b_tabela_b_gasolina_co2.withdraw()
    janela_cat_b_tabela_b_nedc_gasolina_resultado = tk.CTkToplevel()
    janela_cat_b_tabela_b_nedc_gasolina_resultado.geometry("1400x700")
    janela_cat_b_tabela_b_nedc_gasolina_resultado.title("Imposto Único de Circulação - Categoria A - Tabela B - Resultado")
    texto_cat_b_tabela_a_gasolina_resultado = tk.CTkLabel(janela_cat_b_tabela_b_nedc_gasolina_resultado,text = "Simulação do Imposto Único de Circulação\nCategoria A - Tabela B\nResultado Final", font = ("Segoe UI", 20)) .place(x =508, y=0)

    ### SINTESE DE CARACTERISTICAS ###
    titulo_caracteristicas_final = tk.CTkLabel(janela_cat_b_tabela_b_nedc_gasolina_resultado, text = "Caracteristicas da viatura", font = ("Segoe UI",20)) .place(x = 293, y=150)
    modelo_resultado_final = tk.CTkLabel(janela_cat_b_tabela_b_nedc_gasolina_resultado, text = modelo_escrever, font = ("Segoe UI",20)) .place(x = 293, y=200)
    cilindrada_resultado_final = tk.CTkLabel(janela_cat_b_tabela_b_nedc_gasolina_resultado, text=("Cilindrada:{} cm3" .format(cilindrada)), font=("Segoe UI", 20)).place(x=293, y=250)
    combustivel_resultado_final = tk.CTkLabel(janela_cat_b_tabela_b_nedc_gasolina_resultado, text=("Combustível: Gasolina"), font=("Segoe UI", 20)).place(x=293, y=300)
    ano_resultado_final = tk.CTkLabel(janela_cat_b_tabela_b_nedc_gasolina_resultado, text=("Ano:", ano), font=("Segoe UI", 20)).place(x=293, y=350)
    ciclo_resultado_final = tk.CTkLabel(janela_cat_b_tabela_b_nedc_gasolina_resultado, text=("Ciclo de CO2: NEDC"), font=("Segoe UI", 20)).place(x=293, y=400)
    consumo_co2_resultado_final =  tk.CTkLabel(janela_cat_b_tabela_b_nedc_gasolina_resultado, text=("Consumo de CO2: {} ".format(co2)), font=("Segoe UI", 20)).place(x=293, y=450)


    ### APRESENTAÇÃO DOS VALORES ###
    titulo_resumo__valor_resultado_final = tk.CTkLabel(janela_cat_b_tabela_b_nedc_gasolina_resultado, text=("Resumo dos valores a pagar:".format(valor)), font=("Segoe UI", 20)).place(x=879, y=150)
    cilindrada_valor_resultado_final = tk.CTkLabel(janela_cat_b_tabela_b_nedc_gasolina_resultado, text=("Preço da Cilindrada: {:.2f}€" .format(valor)), font=("Segoe UI", 20)).place(x=879 , y=200)
    taxa_adicional_cilindrada = tk.CTkLabel(janela_cat_b_tabela_b_nedc_gasolina_resultado, text=("Preço da Taxa adicional da cilindrada: {:.2f}€" .format(taxa_adicional)), font=("Segoe UI", 20)).place(x=879 , y=250)
    coeficiente_resultado_final = tk.CTkLabel(janela_cat_b_tabela_b_nedc_gasolina_resultado, text=("Coeficiente adicional:{:.2f} " .format(coeficiente)), font=("Segoe UI", 20)).place(x=879 , y=300)
    taxa_co2_resultado_final = tk.CTkLabel(janela_cat_b_tabela_b_nedc_gasolina_resultado, text=( "Preço da taxa de co2: {:.2f}€" .format(taxa_co2)), font=("Segoe UI", 20)).place(x=879 , y=350)
    taxa_diesel_resultado_final = tk.CTkLabel(janela_cat_b_tabela_b_nedc_gasolina_resultado, text=("Preço da taxa de combustível: {:.2f}€" .format(imposto_diesel)), font=("Segoe UI", 20)).place(x=879 , y=400)
    valor_total_resultado_final = tk.CTkLabel(janela_cat_b_tabela_b_nedc_gasolina_resultado, text=( "Valor a pagar: {:.2f}€" .format(valor_total)), font=("Segoe UI", 20), bg_color = "red").place(x=879 , y=450)


    ### FINAL - SAIR OU HISTORICO ###
    decidir_historico = tk.CTkLabel(janela_cat_b_tabela_b_nedc_gasolina_resultado, text=("Deseja adicionar está simulação ao histórico?" ), font=("Segoe UI", 20)).place(x=505, y=500)
    select_tabela_a = tk.CTkButton(janela_cat_b_tabela_b_nedc_gasolina_resultado, text="Sim",command=lambda: historico_iuc_cat_a(categoria, ciclo, tabela, co2, ano, combustivel, cilindrada, valor, taxa_adicional, coeficiente, taxa_co2,imposto_diesel, valor_total),font=("Segoe UI", 20)).place(x=550, y=550)
    select_tabela_b = tk.CTkButton(janela_cat_b_tabela_b_nedc_gasolina_resultado, text="Não",command=lambda: reiniciar_programa(),font=("Segoe UI", 20)).place(x=750, y=550)




### PEDIR CONSUMO GAS CO2 TABELA B CARROS ###

def botao_iuc_cat_b_tabela_b_co2_gasolina(modelo,pedir_cilindrada_b, pedir_ano_b,janela_cat_b_tabela_b):
    cilindrada = int(pedir_cilindrada_b.get())
    ano = int(pedir_ano_b.get())

    janela_cat_b_tabela_b.withdraw()  # Fechar pagina inicial
    janela_cat_b_tabela_b_gasolina_co2 = tk.CTkToplevel() #Abrir nova janela
    customtkinter.set_default_color_theme("dark-blue")
    janela_cat_b_tabela_b_gasolina_co2.geometry("1400x700")
    janela_cat_b_tabela_b_gasolina_co2.title("Imposto Único de Circulação - Categoria A - Tabela B")
    texto_cat_b_tabela_b = tk.CTkLabel(janela_cat_b_tabela_b_gasolina_co2, text="Simulação do Imposto Único de Circulação\nCategoria B - Tabela B ", font=("Segoe UI", 20)).place(x=508, y=0)


    texto_quantidade_co2 = tk.CTkLabel(janela_cat_b_tabela_b_gasolina_co2, text="Insira as emissões de CO2 (g/km)", font=("Segoe UI", 20)).place(x=561, y=100)
    pedir_quantidade_co2 = (tk.CTkEntry(janela_cat_b_tabela_b_gasolina_co2, placeholder_text = "CO2", font = ("Segoe UI", 20), width=300))
    pedir_quantidade_co2.place(x=550,y=150)
    texto_ciclo = tk.CTkLabel(janela_cat_b_tabela_b_gasolina_co2, text="Escolha o ciclo de consumo da sua viatura: ", font=("Segoe UI", 20)).place(x=505, y=450)
    nedc_cat_b_tab_b = tk.CTkButton(janela_cat_b_tabela_b_gasolina_co2, text="NEDC", command=lambda: resultado_final_iuc_cat_b_tabela_b_co2_gasolina_nedc(cilindrada, ano, pedir_quantidade_co2, janela_cat_b_tabela_b_gasolina_co2), font=("Segoe UI", 20)).place(x=525, y=550)
    wltp_cat_b_tab_b = tk.CTkButton(janela_cat_b_tabela_b_gasolina_co2, text="WLTP", command=lambda:  resultado_final_iuc_cat_b_tabela_b_co2_gasolina_wltp(cilindrada, ano, pedir_quantidade_co2, janela_cat_b_tabela_b_gasolina_co2), font=("Segoe UI", 20)).place(x=725, y=550)


def botao_iuc_cat_b_tabela_b_co2_gasoleo(modelo,pedir_cilindrada_b, pedir_ano_b, janela_cat_b_tabela_b):
    cilindrada = int(pedir_cilindrada_b.get())
    ano = int(pedir_ano_b.get())

    janela_cat_b_tabela_b.withdraw()  # Fechar pagina inicial
    janela_cat_b_tabela_b_gasoleo_co2 = tk.CTkToplevel()  # Abrir nova janela
    customtkinter.set_default_color_theme("dark-blue")
    janela_cat_b_tabela_b_gasoleo_co2.geometry("1400x700")
    janela_cat_b_tabela_b_gasoleo_co2.title("Imposto Único de Circulação - Categoria A - Tabela B")
    texto_cat_b_tabela_b = tk.CTkLabel(janela_cat_b_tabela_b_gasoleo_co2, text="Simulação do Imposto Único de Circulação\nCategoria B - Tabela B ", font=("Segoe UI", 20)).place(x=508, y=0)

    texto_quantidade_co2 = tk.CTkLabel(janela_cat_b_tabela_b_gasoleo_co2, text="Insira as emissões de CO2 (g/km)", font=("Segoe UI", 20)).place(x=561, y=100)
    pedir_quantidade_co2 = (tk.CTkEntry(janela_cat_b_tabela_b_gasoleo_co2, placeholder_text="CO2", font=("Segoe UI", 20), width=300))
    pedir_quantidade_co2.place(x=550, y=150)
    texto_ciclo = tk.CTkLabel(janela_cat_b_tabela_b_gasoleo_co2, text="Escolha o ciclo de consumo da sua viatura: ", font=("Segoe UI", 20)).place(x=505, y=450)
    nedc_cat_b_tab_b = tk.CTkButton(janela_cat_b_tabela_b_gasoleo_co2, text="NEDC", command=lambda:resultado_final_iuc_cat_b_tabela_b_co2_gasoleo_nedc(cilindrada, ano, pedir_quantidade_co2, janela_cat_b_tabela_b_gasoleo_co2), font=("Segoe UI", 20)).place(x=525, y=550)
    wltp_cat_b_tab_b = tk.CTkButton(janela_cat_b_tabela_b_gasoleo_co2, text="WLTP", command=lambda: resultado_final_iuc_cat_b_tabela_b_co2_gasoleo_wltp(cilindrada, ano, pedir_quantidade_co2, janela_cat_b_tabela_b_gasoleo_co2), font=("Segoe UI", 20)).place(x=725, y=550)


### BOTÃO DA TABELA B ###
def botao_iuc_cat_b_tabela_b(pedir_modelo, janela_cat_b):
    modelo = str(pedir_modelo.get())
    modelo_log.append(modelo)
    janela_cat_b.withdraw() #Fechar pagina inicial
    janela_cat_b_tabela_b = tk.CTkToplevel() #Abrir nova janela
    customtkinter.set_default_color_theme("dark-blue")
    janela_cat_b_tabela_b.geometry("1400x700")
    janela_cat_b_tabela_b.title("Imposto Único de Circulação - Categoria A - Tabela B")
    texto_cat_b_tabela_b = tk.CTkLabel(janela_cat_b_tabela_b, text="Simulação do Imposto Único de Circulação\nCategoria B - Tabela B ", font = ("Segoe UI", 20)) .place(x=508,y=0)
    texto_cilindrada_b = tk.CTkLabel(janela_cat_b_tabela_b, text="Insira a cilindrada (cm3)", font = ("Segoe UI", 20)) .place(x=599,y=100)
    pedir_cilindrada_b = (tk.CTkEntry(janela_cat_b_tabela_b, placeholder_text = "Cilindrada", font = ("Segoe UI", 20), width=300))
    pedir_cilindrada_b.place(x=550,y=150)
    texto_ano_b = tk.CTkLabel(janela_cat_b_tabela_b, text="Insira o ano da primeira matrícula", font = ("Segoe UI", 20)) .place(x=556,y=300)
    pedir_ano_b = (tk.CTkEntry(janela_cat_b_tabela_b, placeholder_text = "Ano", font = ("Segoe UI", 20), width=100))
    pedir_ano_b.place(x=650,y=350)
    gasolina_cat_b_tab_b = tk.CTkButton(janela_cat_b_tabela_b, text="Gasolina", command=lambda: botao_iuc_cat_b_tabela_b_co2_gasolina(modelo,pedir_cilindrada_b, pedir_ano_b,janela_cat_b_tabela_b), font=("Segoe UI", 20)).place(x=550, y=550)
    gasoleo_cat_b_tab_b = tk.CTkButton(janela_cat_b_tabela_b, text="Gasóleo", command=lambda: botao_iuc_cat_b_tabela_b_co2_gasoleo(modelo,pedir_cilindrada_b, pedir_ano_b, janela_cat_b_tabela_b) , font=("Segoe UI", 20)).place(x=750, y=550)

### AÇÃO DO BOTÃO CATEGORIA B DA PAGINA PRINCIPAL. METER MODELO E ESCOLHER TABELA ###
def botao3_iuc_cat_b(janela_iuc):
    janela_iuc.withdraw() #Fechar pagina inicial
    janela_cat_b = tk.CTkToplevel() #Abrir nova janela
    janela_cat_b.title("Imposto Único de Circulação - Categoria A/B")
    customtkinter.set_default_color_theme("dark-blue")
    janela_cat_b.geometry("1400x700")
    texto_cat_b = tk.CTkLabel(janela_cat_b, text="Simulação do Imposto Único de Circulação\nCategoria A ", font = ("Segoe UI", 20)) .place(x=550,y=0)
    texto_modelo = tk.CTkLabel(janela_cat_b, text="Insira marca e modelo da viatura (opcional)", font = ("Segoe UI", 20)) .place(x=550,y=200)
    pedir_modelo = (tk.CTkEntry(janela_cat_b, placeholder_text = "Insira modelo", font = ("Segoe UI", 20), width=500))
    pedir_modelo.place(x=500,y=250)

    select_tabela_a = tk.CTkButton(janela_cat_b, text="Tabela A", command=lambda: (botao_iuc_cat_b_tabela_a(pedir_modelo, janela_cat_b)), font=("Segoe UI", 20)).place(x=567, y=350)
    select_tabela_b = tk.CTkButton(janela_cat_b, text="Tabela B", command=lambda: (botao_iuc_cat_b_tabela_b(pedir_modelo, janela_cat_b)), font=("Segoe UI", 20)).place(x=720, y=350)

### PAGINA PRINCIPAL IUC ###
def botao_menu1(inicio):
    inicio.withdraw() #Fechar pagina inicial

    janela_iuc = tk.CTkToplevel() #Abrir nova janela
    janela_iuc.title("Imposto Único de Circulação")
    customtkinter.set_default_color_theme("dark-blue")
    janela_iuc.geometry("1400x700")

    #### ESCOLHER MOTA ###

    texto_iuc = tk.CTkLabel(janela_iuc, text="Selecione a categoria da viatura. ", font = ("Segoe UI", 20)) .place(x=550,y=0)
    botao2 = tk.CTkButton(janela_iuc, text="Categoria E", command=lambda: iuc_motas(janela_iuc), font=("Segoe UI", 20)).place(x=974, y=350)

    moto = tk.CTkImage(dark_image=Image.open("moto.png"), size=(150, 150))
    imagem_moto = tk.CTkLabel(janela_iuc, image=moto, text="").place(x=974, y=150)

    ### ESCOLHER CARRO ###

    botao3 = tk.CTkButton(janela_iuc, text="Categoria A e B", command= lambda: botao3_iuc_cat_b(janela_iuc), font=("Segoe UI", 20)).place(x=274, y=350)

    carro = tk.CTkImage(dark_image=Image.open("carro2.png"), size=(150, 150))
    imagem_carro = tk.CTkLabel(janela_iuc, image=carro, text="").place(x=274, y=150)

    ### ESCOLHER CAMIÃO ###
    camiao1 = tk.CTkImage(dark_image=Image.open("camiao1.png"), size = (150,150))
    imagem_camiao = tk.CTkLabel(janela_iuc, image = camiao1, text = "") .place(x=624, y=150)
    botao4 = tk.CTkButton(janela_iuc, text="Categoria C e D", command=lambda: pedir_peso(janela_iuc), font=("Segoe UI", 20)).place(x=624, y=350)



####################### ORDENADO ########################


### DEPENDENTE ###

def historico_ordenado(regime, situacao_fiscal, dependentes, contribuicao_social, adse, valor_alimentacao, dias_alimentacao, forma_pagamento, outros, renumeracao, valor_irs, valor_adse, valor_ss, renumeracao_final, invalidez):
    data_atual = datetime.today().date()
    data_atual_formatada = "{}/{}/{}" .format(data_atual.day, data_atual.month, data_atual.year)
    hora_atual = datetime.now().time()
    f = open("historico.txt", "a+")
    f.write("--- SIMULAÇÃO DOS IMPOSTOS SOBRE OS RENDIMENTOS 2023 2ºSEMESTRE ---\n")

    f.write("Simulação realizada no dia {} ás {}\n".format(data_atual_formatada, hora_atual))
    f.write(" --- Caracterização ---\n")
    f.write("Trabalhador Dependente\n")

    if situacao_fiscal == 1:
        f.write("Situação Fiscal: Solteiro\n")
    elif situacao_fiscal == 2:
        f.write("Situação Fiscal: Casado: 1 titular\n")
    else:
        f.write("Situação Fiscal: Casado: 2 titular\n")
    f.write("Dependentes: {}\n" .format(dependentes))
    if contribuicao_social == 1:
        f.write("Contribuição Social: Segurança Social\n")
    else:
        f.write("Contribuição Social: Caixa Geral de Aposentações\n")
    if adse==1:
        f.write("ADSE: Sim\n")
    else:
        f.write("ADSE: Não \n")
    f.write("Valor do subsidio de alimentação {:.2f}€\n" .format(valor_alimentacao))
    f.write("Dias com subsidio de alimentação: {:.2f}\n" .format(dias_alimentacao))
    if forma_pagamento == 1:
        f.write("Forma de pagamento do subsidio de alimentação: Dinheiro\n")
    else:
        f.write("Forma de pagamento do subsidio de alimentação: Cartão/Vale de refeição\n")
    f.write("Outros subsidios tributaveis: {:.2f} €\n".format(outros))
    if invalidez == 1:
        f.write("Invalidez, defeciencia ou incapacidade: Não\n")
    else:
        f.write("Invalidez, deficiencia ou incapacidade: Sim\n")
    f.write("--- Resumo dos descontos ---\n")
    f.write("Valor tributável: {:.2f}€\n".format(renumeracao))
    f.write("Retenção na fonte: {:.2f}€\n".format(valor_irs))
    f.write("Taxa Social Única: {:.2f}€\n".format(valor_ss))
    f.write("Desconto ADSE: {:.2f}€\n".format(valor_adse))
    f.write("Valor após descontos: {:.2f}€\n".format(renumeracao_final))
    f.write("----------------------------------------------------------------\n")
    f.close()
    os.system(f'start notepad {historico}')
    reiniciar_programa()

### 2 TITULARES ###

def dependente_2t_n_vale_cga_resultado(janela_solteiro_n_vale_cga):
    regime = 1
    situacao_fiscal = 3
    contribuicao_social = 2
    adse = 2
    forma_pagamento = 2
    valor_irs=0
    invalidez = 1
    valor_adse=0
    janela_solteiro_n_vale_cga.withdraw()
    janela_solteiro_n_vale_cga_resultado = tk.CTkToplevel()
    janela_solteiro_n_vale_cga_resultado.geometry("1400x700")
    janela_solteiro_n_vale_cga_resultado.title( "Simulação do ordenado liquido - Trabalhador Dependente - Casado - 2 Titular  - Resultado Final")
    texto_topo = tk.CTkLabel(janela_solteiro_n_vale_cga_resultado, text="Simulação do ordenado liquido\nTrabalhador Dependente\nCasado - 1 Titular \nResultado Final", font=("Segoe UI", 20)).place(x=550, y=0)
    ordenado1 = float(renumera_log[0])
    dependentes = int(dependentes_log[0])
    alimentacao = float(alimentacao_log[0])
    dias_alimentacao = int(dias_log[0])
    outros = float(outros_log[0])
    if alimentacao < 9.6:
        excedente_alimentacao = 0
    else:
        excedente_alimentacao = alimentacao-9.6
    valor_alimentacao = alimentacao*dias_alimentacao
    excedente_alimentacao_dias = excedente_alimentacao*dias_alimentacao
    renumeracao = ordenado1+excedente_alimentacao_dias+outros

    if renumeracao<=762:
        renumeracao_liquida = 762
        taxa = 0
        parcela_dependente = 0
        parcela_abater = 0

    else:
        valor_irs, parcela_abater, taxa, renumeracao_liquida, parcela_dependente = casados_2t(dependentes, renumeracao)
    if valor_irs<0:
        valor_irs = 0
    else:
        valor_irs = valor_irs
    valor_ss = renumeracao*0.11
    renumeracao_final = renumeracao - valor_ss - valor_irs + valor_alimentacao


    ### SINTESE DE CARACTERISTICAS ###

    escrever_renumeracao = tk.CTkLabel(janela_solteiro_n_vale_cga_resultado, text=("Ordenado Base: {} €" .format(ordenado1)), font=("Segoe UI", 20)).place(x=150, y=100)
    escrever_regime = tk.CTkLabel(janela_solteiro_n_vale_cga_resultado, text=("Regime: Trabalhador Dependente"), font=("Segoe UI", 20)).place(x=150, y=150)
    escrever_fiscal = tk.CTkLabel(janela_solteiro_n_vale_cga_resultado, text = ("Situação Fiscal: Casado - 2 Titular "), font=("Segoe UI", 20)).place(x=150,y=200)
    escrever_dependentes = tk.CTkLabel(janela_solteiro_n_vale_cga_resultado, text=("Dependentes: {}".format(dependentes)), font=("Segoe UI", 20)).place(x=150, y=250)
    escrever_social = tk.CTkLabel(janela_solteiro_n_vale_cga_resultado, text=("Contribuição Social: Caixa Geral de Aposentações"), font=("Segoe UI", 20)).place(x=150, y=300)
    escrever_adse = tk.CTkLabel(janela_solteiro_n_vale_cga_resultado, text=("ADSE: Não"), font=("Segoe UI", 20)).place(x=150, y=350)
    escrever_alimentacao = tk.CTkLabel(janela_solteiro_n_vale_cga_resultado, text=("Subsidio de Alimentação: {} €".format(valor_alimentacao)), font=("Segoe UI", 20)).place(x=150, y=400)
    escrever_dias = tk.CTkLabel(janela_solteiro_n_vale_cga_resultado, text=("Dias com susbsidio de alimentação: {}".format(dias_alimentacao)), font=("Segoe UI", 20)).place(x=150, y=450)
    escrever_pagamento = tk.CTkLabel(janela_solteiro_n_vale_cga_resultado, text=("Forma de pagamento do subsidio de alimentação: Vale/Cartão de refeição"), font=("Segoe UI", 20)).place(x=150, y=500)
    escrever_outros = tk.CTkLabel(janela_solteiro_n_vale_cga_resultado, text=("Outros subsidios tributaveis: {} €".format(outros)), font=("Segoe UI", 20)).place(x=150, y=550)
    escrever_invalidez = tk.CTkLabel(janela_solteiro_n_vale_cga_resultado, text=("Invalidez ou incapacidade: Não"), font=("Segoe UI", 20)).place(x=150, y=600)

### APRESENTAÇÃO DOS VALORES ###
    texto_descontos = tk.CTkLabel(janela_solteiro_n_vale_cga_resultado, text=("Resumo dos descontos"), font=("Segoe UI", 20)) .place(x=879, y=150)
    texto_valor = tk.CTkLabel(janela_solteiro_n_vale_cga_resultado, text=("Valor tributável:{:.2f}€ " .format(renumeracao)), font=("Segoe UI", 20)).place(x=879 , y=300)
    texto_irs = tk.CTkLabel(janela_solteiro_n_vale_cga_resultado, text=("Retenção na fonte: {:.2f}€" .format(valor_irs)), font=("Segoe UI", 20)).place(x=879 , y=200)
    texto_ss = tk.CTkLabel(janela_solteiro_n_vale_cga_resultado, text=("Taxa Social Única: {:.2f}€" .format(valor_ss)), font=("Segoe UI", 20)).place(x=879 , y=250)
    valor_final = tk.CTkLabel(janela_solteiro_n_vale_cga_resultado, text=( "Valor após descontos: {:.2f}€" .format(renumeracao_final)), font=("Segoe UI", 20), bg_color = "red").place(x=879 , y=300)

### FINAL - SAIR OU HISTORICO ###
    decidir_historico = tk.CTkLabel(janela_solteiro_n_vale_cga_resultado, text=("Deseja adicionar está simulação ao histórico?" ), font=("Segoe UI", 20)).place(x=879, y=500)
    select_tabela_a = tk.CTkButton(janela_solteiro_n_vale_cga_resultado, text="Sim",command=lambda: historico_ordenado(regime, situacao_fiscal, dependentes, contribuicao_social, adse, valor_alimentacao, dias_alimentacao, forma_pagamento, outros, renumeracao, valor_irs, valor_adse, valor_ss, renumeracao_final, invalidez),font=("Segoe UI", 20)).place(x=879, y=550)
    select_tabela_b = tk.CTkButton(janela_solteiro_n_vale_cga_resultado, text="Não",command=lambda: reiniciar_programa(),font=("Segoe UI", 20)).place(x=1079, y=550)



def dependente_2t_n_vale_cga_adse(janela_solteiro_n_vale_cga):
    regime = 1
    situacao_fiscal = 3
    contribuicao_social = 2
    adse = 1
    forma_pagamento = 2
    valor_irs=0
    invalidez = 1
    janela_solteiro_n_vale_cga.withdraw()
    janela_solteiro_n_vale_cga_adse = tk.CTkToplevel()
    janela_solteiro_n_vale_cga_adse.geometry("1400x700")
    janela_solteiro_n_vale_cga_adse.title( "Simulação do ordenado liquido - Trabalhador Dependente - Casado - 2 Titular  - Resultado Final")
    texto_topo = tk.CTkLabel(janela_solteiro_n_vale_cga_adse, text="Simulação do ordenado liquido\nTrabalhador Dependente\nCasado - 2 Titular \nResultado Final", font=("Segoe UI", 20)).place(x=550, y=0)
    ordenado1 = float(renumera_log[0])
    dependentes = int(dependentes_log[0])
    alimentacao = float(alimentacao_log[0])
    dias_alimentacao = int(dias_log[0])
    outros = float(outros_log[0])
    if alimentacao < 9.6:
        excedente_alimentacao = 0
    else:
        excedente_alimentacao = alimentacao-9.6
    valor_alimentacao = alimentacao*dias_alimentacao
    excedente_alimentacao_dias = excedente_alimentacao*dias_alimentacao
    renumeracao = ordenado1+excedente_alimentacao_dias+outros

    if renumeracao<=762:
        renumeracao_liquida = 762
        taxa = 0
        parcela_dependente = 0
        parcela_abater = 0

    else:
        valor_irs, parcela_abater, taxa, renumeracao_liquida, parcela_dependente = casados_2t(dependentes, renumeracao)

    valor_ss = renumeracao*0.11
    valor_adse = renumeracao*0.035
    if valor_irs<0:
        valor_irs = 0
    else:
        valor_irs = valor_irs
    renumeracao_final = renumeracao - valor_adse - valor_ss - valor_irs+valor_alimentacao

    ### SINTESE DE CARACTERISTICAS ###

    escrever_renumeracao = tk.CTkLabel(janela_solteiro_n_vale_cga_adse, text=("Ordenado Base: {} €" .format(ordenado1)), font=("Segoe UI", 20)).place(x=150, y=100)
    escrever_regime = tk.CTkLabel(janela_solteiro_n_vale_cga_adse, text=("Regime: Trabalhador Dependente"), font=("Segoe UI", 20)).place(x=150, y=150)
    escrever_fiscal = tk.CTkLabel(janela_solteiro_n_vale_cga_adse, text = ("Situação Fiscal: Casado - 2 Titular"), font=("Segoe UI", 20)).place(x=150,y=200)
    escrever_dependentes = tk.CTkLabel(janela_solteiro_n_vale_cga_adse, text=("Dependentes: {}".format(dependentes)), font=("Segoe UI", 20)).place(x=150, y=250)
    escrever_social = tk.CTkLabel(janela_solteiro_n_vale_cga_adse, text=("Contribuição Social: Caixa Geral de Aposentações"), font=("Segoe UI", 20)).place(x=150, y=300)
    escrever_adse = tk.CTkLabel(janela_solteiro_n_vale_cga_adse, text=("ADSE: Sim"), font=("Segoe UI", 20)).place(x=150, y=350)
    escrever_alimentacao = tk.CTkLabel(janela_solteiro_n_vale_cga_adse, text=("Subsidio de Alimentação: {} €".format(valor_alimentacao)), font=("Segoe UI", 20)).place(x=150, y=400)
    escrever_dias = tk.CTkLabel(janela_solteiro_n_vale_cga_adse, text=("Dias com susbsidio de alimentação: {}".format(dias_alimentacao)), font=("Segoe UI", 20)).place(x=150, y=450)
    escrever_pagamento = tk.CTkLabel(janela_solteiro_n_vale_cga_adse, text=("Forma de pagamento do subsidio de alimentação: Vale/Cartão de alimentação"), font=("Segoe UI", 20)).place(x=150, y=500)
    escrever_outros = tk.CTkLabel(janela_solteiro_n_vale_cga_adse, text=("Outros subsidios tributaveis: {} €".format(outros)), font=("Segoe UI", 20)).place(x=150, y=550)
    escrever_invalidez = tk.CTkLabel(janela_solteiro_n_vale_cga_adse, text=("Invalidez ou incapacidade: Não"), font=("Segoe UI", 20)).place(x=150, y=600)

### APRESENTAÇÃO DOS VALORES ###
    texto_descontos = tk.CTkLabel(janela_solteiro_n_vale_cga_adse, text=("Resumo dos descontos"), font=("Segoe UI", 20)) .place(x=879, y=150)
    texto_valor = tk.CTkLabel(janela_solteiro_n_vale_cga_adse, text=("Valor tributável:{:.2f}€ " .format(renumeracao)), font=("Segoe UI", 20)).place(x=879 , y=300)
    texto_irs = tk.CTkLabel(janela_solteiro_n_vale_cga_adse, text=("Retenção na fonte: {:.2f}€" .format(valor_irs)), font=("Segoe UI", 20)).place(x=879 , y=200)
    texto_ss = tk.CTkLabel(janela_solteiro_n_vale_cga_adse, text=("Taxa Social Única: {:.2f}€" .format(valor_ss)), font=("Segoe UI", 20)).place(x=879 , y=250)
    taxa_adse = tk.CTkLabel(janela_solteiro_n_vale_cga_adse, text=("Desconto ADSE: {:.2f}€" .format(valor_adse)), font=("Segoe UI", 20)).place(x=879 , y=350)
    valor_final = tk.CTkLabel(janela_solteiro_n_vale_cga_adse, text=( "Valor após descontos: {:.2f}€" .format(renumeracao_final)), font=("Segoe UI", 20), bg_color = "red").place(x=879 , y=450)

### FINAL - SAIR OU HISTORICO ###
    decidir_historico = tk.CTkLabel(janela_solteiro_n_vale_cga_adse, text=("Deseja adicionar está simulação ao histórico?" ), font=("Segoe UI", 20)).place(x=879, y=500)
    select_tabela_a = tk.CTkButton(janela_solteiro_n_vale_cga_adse, text="Sim",command=lambda: historico_ordenado(regime, situacao_fiscal, dependentes, contribuicao_social, adse, valor_alimentacao, dias_alimentacao, forma_pagamento, outros, renumeracao, valor_irs, valor_adse, valor_ss, renumeracao_final, invalidez),font=("Segoe UI", 20)).place(x=879, y=550)
    select_tabela_b = tk.CTkButton(janela_solteiro_n_vale_cga_adse, text="Não",command=lambda: reiniciar_programa(),font=("Segoe UI", 20)).place(x=1079, y=550)



def dependente_2t_n_vale_cga(janela_solteiro_n_vale):
    janela_solteiro_n_vale.withdraw()
    janela_solteiro_n_vale_cga = tk.CTkToplevel()
    janela_solteiro_n_vale_cga.geometry("1400x700")
    janela_solteiro_n_vale_cga.title("Simulação do ordenado liquido - Trabalhador Dependente - Casado - 2 Titular - Outras contribuições")
    texto_topo = tk.CTkLabel(janela_solteiro_n_vale_cga, text="Simulação do ordenado liquido\nTrabalhador Dependente\nCasado - 2 Titular\nOutras contribuições", font=("Segoe UI", 20)).place(x=550, y=0)
    texto_adse = tk.CTkLabel(janela_solteiro_n_vale_cga, text="É beneficiário da ADSE?", font=("Segoe UI", 20)).place(x=590, y=150)
    botao_sim = tk.CTkButton(janela_solteiro_n_vale_cga, text= "Sim", command=lambda: dependente_2t_n_vale_cga_adse(janela_solteiro_n_vale_cga), font=("Segoe UI", 20)).place(x=530, y=200)
    botao_nao = tk.CTkButton(janela_solteiro_n_vale_cga, text="Não", command=lambda: dependente_2t_n_vale_cga_resultado(janela_solteiro_n_vale_cga), font=("Segoe UI", 20)).place(x=730, y=200)

def dependente_2t_n_vale_ss_resultado(janela_solteiro_n_vale_ss):
    regime = 1
    situacao_fiscal = 3
    contribuicao_social = 1
    adse = 2
    forma_pagamento = 2
    valor_irs=0
    invalidez = 1
    valor_adse=0
    janela_solteiro_n_vale_ss.withdraw()
    janela_solteiro_n_vale_ss_resultado = tk.CTkToplevel()
    janela_solteiro_n_vale_ss_resultado.geometry("1400x700")
    janela_solteiro_n_vale_ss_resultado.title( "Simulação do ordenado liquido - Trabalhador Dependente - Casado - 2 Titular - Resultado Final")
    texto_topo = tk.CTkLabel(janela_solteiro_n_vale_ss_resultado, text="Simulação do ordenado liquido\nTrabalhador Dependente\nCasado - 2 Titular\nResultado Final", font=("Segoe UI", 20)).place(x=550, y=0)
    ordenado1 = float(renumera_log[0])
    dependentes = int(dependentes_log[0])
    alimentacao = float(alimentacao_log[0])
    dias_alimentacao = int(dias_log[0])
    outros = float(outros_log[0])
    if alimentacao <9.6:
        excedente_alimentacao = 0
    else:
        excedente_alimentacao = alimentacao-9.6
    valor_alimentacao = alimentacao*dias_alimentacao
    excedente_alimentacao_dias = excedente_alimentacao*dias_alimentacao
    renumeracao = ordenado1+excedente_alimentacao_dias+outros

    if renumeracao<=762:
        renumeracao_liquida = 762
        taxa = 0
        parcela_dependente = 0
        parcela_abater = 0

    else:
        valor_irs, parcela_abater, taxa, renumeracao_liquida, parcela_dependente = casados_2t(dependentes, renumeracao)
    if valor_irs<0:
        valor_irs = 0
    else:
        valor_irs = valor_irs
    valor_ss = renumeracao*0.11
    renumeracao_final = renumeracao - valor_ss - valor_irs + valor_alimentacao


    ### SINTESE DE CARACTERISTICAS ###

    escrever_renumeracao = tk.CTkLabel(janela_solteiro_n_vale_ss_resultado, text=("Ordenado Base: {} €" .format(ordenado1)), font=("Segoe UI", 20)).place(x=150, y=100)
    escrever_regime = tk.CTkLabel(janela_solteiro_n_vale_ss_resultado, text=("Regime: Trabalhador Dependente"), font=("Segoe UI", 20)).place(x=150, y=150)
    escrever_fiscal = tk.CTkLabel(janela_solteiro_n_vale_ss_resultado, text = ("Situação Fiscal: Casado - 2 Titular"), font=("Segoe UI", 20)).place(x=150,y=200)
    escrever_dependentes = tk.CTkLabel(janela_solteiro_n_vale_ss_resultado, text=("Dependentes: {}".format(dependentes)), font=("Segoe UI", 20)).place(x=150, y=250)
    escrever_social = tk.CTkLabel(janela_solteiro_n_vale_ss_resultado, text=("Contribuição Social: Segurança Social"), font=("Segoe UI", 20)).place(x=150, y=300)
    escrever_adse = tk.CTkLabel(janela_solteiro_n_vale_ss_resultado, text=("ADSE: Não"), font=("Segoe UI", 20)).place(x=150, y=350)
    escrever_alimentacao = tk.CTkLabel(janela_solteiro_n_vale_ss_resultado, text=("Subsidio de Alimentação: {} €".format(valor_alimentacao)), font=("Segoe UI", 20)).place(x=150, y=400)
    escrever_dias = tk.CTkLabel(janela_solteiro_n_vale_ss_resultado, text=("Dias com susbsidio de alimentação: {}".format(dias_alimentacao)), font=("Segoe UI", 20)).place(x=150, y=450)
    escrever_pagamento = tk.CTkLabel(janela_solteiro_n_vale_ss_resultado, text=("Forma de pagamento do subsidio de alimentação: Vale/Cartão de Refeição"), font=("Segoe UI", 20)).place(x=150, y=500)
    escrever_outros = tk.CTkLabel(janela_solteiro_n_vale_ss_resultado, text=("Outros subsidios tributaveis: {} €".format(outros)), font=("Segoe UI", 20)).place(x=150, y=550)
    escrever_invalidez = tk.CTkLabel(janela_solteiro_n_vale_ss_resultado, text=("Invalidez ou incapacidade: Não"), font=("Segoe UI", 20)).place(x=150, y=600)

### APRESENTAÇÃO DOS VALORES ###
    texto_descontos = tk.CTkLabel(janela_solteiro_n_vale_ss_resultado, text=("Resumo dos descontos"), font=("Segoe UI", 20)) .place(x=879, y=150)
    texto_valor = tk.CTkLabel(janela_solteiro_n_vale_ss_resultado, text=("Valor tributável:{:.2f}€ " .format(renumeracao)), font=("Segoe UI", 20)).place(x=879 , y=300)
    texto_irs = tk.CTkLabel(janela_solteiro_n_vale_ss_resultado, text=("Retenção na fonte: {:.2f}€" .format(valor_irs)), font=("Segoe UI", 20)).place(x=879 , y=200)
    texto_ss = tk.CTkLabel(janela_solteiro_n_vale_ss_resultado, text=("Taxa Social Única: {:.2f}€" .format(valor_ss)), font=("Segoe UI", 20)).place(x=879 , y=250)
    valor_final = tk.CTkLabel(janela_solteiro_n_vale_ss_resultado, text=( "Valor após descontos: {:.2f}€" .format(renumeracao_final)), font=("Segoe UI", 20), bg_color = "red").place(x=879 , y=300)

### FINAL - SAIR OU HISTORICO ###
    decidir_historico = tk.CTkLabel(janela_solteiro_n_vale_ss_resultado, text=("Deseja adicionar está simulação ao histórico?" ), font=("Segoe UI", 20)).place(x=879, y=500)
    select_tabela_a = tk.CTkButton(janela_solteiro_n_vale_ss_resultado, text="Sim",command=lambda: historico_ordenado(regime, situacao_fiscal, dependentes, contribuicao_social, adse, valor_alimentacao, dias_alimentacao, forma_pagamento, outros, renumeracao, valor_irs, valor_adse, valor_ss, renumeracao_final, invalidez),font=("Segoe UI", 20)).place(x=879, y=550)
    select_tabela_b = tk.CTkButton(janela_solteiro_n_vale_ss_resultado, text="Não",command=lambda: reiniciar_programa(),font=("Segoe UI", 20)).place(x=1079, y=550)



def dependente_2t_n_vale_ss_adse(janela_solteiro_n_vale_ss):
    regime = 1
    situacao_fiscal = 3
    contribuicao_social = 1
    adse = 1
    forma_pagamento = 2
    valor_irs=0
    invalidez = 1
    janela_solteiro_n_vale_ss.withdraw()
    janela_solteiro_n_vale_ss_adse = tk.CTkToplevel()
    janela_solteiro_n_vale_ss_adse.geometry("1400x700")
    janela_solteiro_n_vale_ss_adse.title( "Simulação do ordenado liquido - Trabalhador Dependente - Casado - 2 Titular - Resultado Final")
    texto_topo = tk.CTkLabel(janela_solteiro_n_vale_ss_adse, text="Simulação do ordenado liquido\nTrabalhador Dependente\nCasado - 2 Titular\nResultado Final", font=("Segoe UI", 20)).place(x=550, y=0)
    ordenado1 = float(renumera_log[0])
    dependentes = int(dependentes_log[0])
    alimentacao = float(alimentacao_log[0])
    dias_alimentacao = int(dias_log[0])
    outros = float(outros_log[0])
    if alimentacao < 9.6:
        excedente_alimentacao = 0
    else:
        excedente_alimentacao = alimentacao-9.6
    valor_alimentacao = alimentacao*dias_alimentacao
    excedente_alimentacao_dias = excedente_alimentacao*dias_alimentacao
    renumeracao = ordenado1+excedente_alimentacao_dias+outros

    if renumeracao<=762:
        renumeracao_liquida = 762
        taxa = 0
        parcela_dependente = 0
        parcela_abater = 0

    else:
        valor_irs, parcela_abater, taxa, renumeracao_liquida, parcela_dependente = casados_2t(dependentes, renumeracao)

    valor_ss = renumeracao*0.11
    valor_adse = renumeracao*0.035

    if valor_irs<0:
        valor_irs = 0
    else:
        valor_irs = valor_irs

    renumeracao_final = renumeracao - valor_adse - valor_ss - valor_irs+valor_alimentacao

    ### SINTESE DE CARACTERISTICAS ###

    escrever_renumeracao = tk.CTkLabel(janela_solteiro_n_vale_ss_adse, text=("Ordenado Base: {} €" .format(ordenado1)), font=("Segoe UI", 20)).place(x=150, y=100)
    escrever_regime = tk.CTkLabel(janela_solteiro_n_vale_ss_adse, text=("Regime: Trabalhador Dependente"), font=("Segoe UI", 20)).place(x=150, y=150)
    escrever_fiscal = tk.CTkLabel(janela_solteiro_n_vale_ss_adse, text = ("Situação Fiscal: Casado - 2 Titular"), font=("Segoe UI", 20)).place(x=150,y=200)
    escrever_dependentes = tk.CTkLabel(janela_solteiro_n_vale_ss_adse, text=("Dependentes: {}".format(dependentes)), font=("Segoe UI", 20)).place(x=150, y=250)
    escrever_social = tk.CTkLabel(janela_solteiro_n_vale_ss_adse, text=("Contribuição Social: Segurança Social"), font=("Segoe UI", 20)).place(x=150, y=300)
    escrever_adse = tk.CTkLabel(janela_solteiro_n_vale_ss_adse, text=("ADSE: Sim"), font=("Segoe UI", 20)).place(x=150, y=350)
    escrever_alimentacao = tk.CTkLabel(janela_solteiro_n_vale_ss_adse, text=("Subsidio de Alimentação: {} €".format(valor_alimentacao)), font=("Segoe UI", 20)).place(x=150, y=400)
    escrever_dias = tk.CTkLabel(janela_solteiro_n_vale_ss_adse, text=("Dias com susbsidio de alimentação: {}".format(dias_alimentacao)), font=("Segoe UI", 20)).place(x=150, y=450)
    escrever_pagamento = tk.CTkLabel(janela_solteiro_n_vale_ss_adse, text=("Forma de pagamento do subsidio de alimentação: Cartão/Vale de alimentação"), font=("Segoe UI", 20)).place(x=150, y=500)
    escrever_outros = tk.CTkLabel(janela_solteiro_n_vale_ss_adse, text=("Outros subsidios tributaveis: {} €".format(outros)), font=("Segoe UI", 20)).place(x=150, y=550)
    escrever_invalidez = tk.CTkLabel(janela_solteiro_n_vale_ss_adse, text=("Invalidez ou incapacidade: Não"), font=("Segoe UI", 20)).place(x=150, y=600)

### APRESENTAÇÃO DOS VALORES ###
    texto_descontos = tk.CTkLabel(janela_solteiro_n_vale_ss_adse, text=("Resumo dos descontos"), font=("Segoe UI", 20)) .place(x=879, y=150)
    texto_valor = tk.CTkLabel(janela_solteiro_n_vale_ss_adse, text=("Valor tributável:{:.2f}€ " .format(renumeracao)), font=("Segoe UI", 20)).place(x=879 , y=300)
    texto_irs = tk.CTkLabel(janela_solteiro_n_vale_ss_adse, text=("Retenção na fonte: {:.2f}€" .format(valor_irs)), font=("Segoe UI", 20)).place(x=879 , y=200)
    texto_ss = tk.CTkLabel(janela_solteiro_n_vale_ss_adse, text=("Taxa Social Única: {:.2f}€" .format(valor_ss)), font=("Segoe UI", 20)).place(x=879 , y=250)
    taxa_adse = tk.CTkLabel(janela_solteiro_n_vale_ss_adse, text=("Desconto ADSE: {:.2f}€" .format(valor_adse)), font=("Segoe UI", 20)).place(x=879 , y=350)
    valor_final = tk.CTkLabel(janela_solteiro_n_vale_ss_adse, text=( "Valor após descontos: {:.2f}€" .format(renumeracao_final)), font=("Segoe UI", 20), bg_color = "red").place(x=879 , y=450)

### FINAL - SAIR OU HISTORICO ###
    decidir_historico = tk.CTkLabel(janela_solteiro_n_vale_ss_adse, text=("Deseja adicionar está simulação ao histórico?" ), font=("Segoe UI", 20)).place(x=879, y=500)
    select_tabela_a = tk.CTkButton(janela_solteiro_n_vale_ss_adse, text="Sim",command=lambda: historico_ordenado(regime, situacao_fiscal, dependentes, contribuicao_social, adse, valor_alimentacao, dias_alimentacao, forma_pagamento, outros, renumeracao, valor_irs, valor_adse, valor_ss, renumeracao_final, invalidez),font=("Segoe UI", 20)).place(x=879, y=550)
    select_tabela_b = tk.CTkButton(janela_solteiro_n_vale_ss_adse, text="Não",command=lambda: reiniciar_programa(),font=("Segoe UI", 20)).place(x=1079, y=550)



def dependente_2t_n_vale_ss(janela_solteiro_n_vale):
    janela_solteiro_n_vale.withdraw()
    janela_solteiro_n_vale_ss = tk.CTkToplevel()
    janela_solteiro_n_vale_ss.geometry("1400x700")
    janela_solteiro_n_vale_ss.title("Simulação do ordenado liquido - Trabalhador Dependente - Casado - 2 Titular - Outras contribuições")
    texto_topo = tk.CTkLabel(janela_solteiro_n_vale_ss, text="Simulação do ordenado liquido\nTrabalhador Dependente\nCasado - 2 Titular\nOutras contribuições", font=("Segoe UI", 20)).place(x=550, y=0)
    texto_adse = tk.CTkLabel(janela_solteiro_n_vale_ss, text="É beneficiário da ADSE?", font=("Segoe UI", 20)).place(x=590, y=150)
    botao_sim = tk.CTkButton(janela_solteiro_n_vale_ss, text= "Sim", command=lambda: dependente_2t_n_vale_ss_adse(janela_solteiro_n_vale_ss), font=("Segoe UI", 20)).place(x=530, y=200)
    botao_nao = tk.CTkButton(janela_solteiro_n_vale_ss, text="Não", command=lambda: dependente_2t_n_vale_ss_resultado(janela_solteiro_n_vale_ss), font=("Segoe UI", 20)).place(x=730, y=200)




def dependente_2t_n_vale(janela_solteiro_n, pedir_outros, pedir_alimentacao, pedir_dias):
    alimentacao = float(pedir_alimentacao.get())
    alimentacao_log.append(alimentacao)
    dias = float(pedir_dias.get())
    dias_log.append(dias)
    outros = float(pedir_outros.get())
    outros_log.append(outros)
    janela_solteiro_n.withdraw()
    janela_solteiro_n_vale = tk.CTkToplevel()
    janela_solteiro_n_vale.geometry("1400x700")
    janela_solteiro_n_vale.title("Simulação do ordenado liquido - Trabalhador Dependente - Casado - 2 Titular - Outras contribuições")
    texto_topo = tk.CTkLabel(janela_solteiro_n_vale, text="Simulação do ordenado liquido\nTrabalhador Dependente\nCasado - 2 Titular\nOutras contribuições", font=("Segoe UI", 20)).place(x=550, y=0)
    texto_forma = tk.CTkLabel(janela_solteiro_n_vale, text = "Selecione a sua forma de contribuição social", font=("Segoe UI", 20)).place(x=510, y=150)
    botao_ss = tk.CTkButton(janela_solteiro_n_vale, text="Segurança Social", command=lambda:dependente_2t_n_vale_ss(janela_solteiro_n_vale), font=("Segoe UI", 20)) .place(x=606, y=200)
    botao_cga = tk.CTkButton(janela_solteiro_n_vale, text="Caixa Geral de Aposentações", command=lambda: dependente_2t_n_vale_cga(janela_solteiro_n_vale),  font=("Segoe UI",20)) .place(x=560, y=250)

def dependente_2t_n_dinheiro_ss_resultado(janela_solteiro_n_dinheiro_ss):
    regime = 1
    situacao_fiscal = 3
    contribuicao_social = 1
    adse = 2
    forma_pagamento = 1
    valor_irs=0
    invalidez = 1
    valor_adse=0
    janela_solteiro_n_dinheiro_ss.withdraw()
    janela_solteiro_n_dinheiro_ss_resultado = tk.CTkToplevel()
    janela_solteiro_n_dinheiro_ss_resultado.geometry("1400x700")
    janela_solteiro_n_dinheiro_ss_resultado.title( "Simulação do ordenado liquido - Trabalhador Dependente - Casado - 2 Titular - Resultado Final")
    texto_topo = tk.CTkLabel(janela_solteiro_n_dinheiro_ss_resultado, text="Simulação do ordenado liquido\nTrabalhador Dependente\nCasado - 2 Titular\nResultado Final", font=("Segoe UI", 20)).place(x=550, y=0)
    ordenado1 = float(renumera_log[0])
    dependentes = int(dependentes_log[0])
    alimentacao = float(alimentacao_log[0])
    dias_alimentacao = int(dias_log[0])
    outros = float(outros_log[0])
    if alimentacao < 6:
        excedente_alimentacao = 0
    else:
        excedente_alimentacao = alimentacao-6
    valor_alimentacao = alimentacao*dias_alimentacao
    excedente_alimentacao_dias = excedente_alimentacao*dias_alimentacao
    renumeracao = ordenado1+excedente_alimentacao_dias+outros

    if renumeracao<=762:
        renumeracao_liquida = 762
        taxa = 0
        parcela_dependente = 0
        parcela_abater = 0

    else:
        valor_irs, parcela_abater, taxa, renumeracao_liquida, parcela_dependente = casados_2t(dependentes, renumeracao)
    if valor_irs<0:
        valor_irs = 0
    else:
        valor_irs = valor_irs
    valor_ss = renumeracao*0.11
    renumeracao_final = renumeracao - valor_ss - valor_irs + valor_alimentacao


    ### SINTESE DE CARACTERISTICAS ###

    escrever_renumeracao = tk.CTkLabel(janela_solteiro_n_dinheiro_ss_resultado, text=("Ordenado Base: {} €" .format(ordenado1)), font=("Segoe UI", 20)).place(x=150, y=100)
    escrever_regime = tk.CTkLabel(janela_solteiro_n_dinheiro_ss_resultado, text=("Regime: Trabalhador Dependente"), font=("Segoe UI", 20)).place(x=150, y=150)
    escrever_fiscal = tk.CTkLabel(janela_solteiro_n_dinheiro_ss_resultado, text = ("Situação Fiscal: Casado - 2 Titular"), font=("Segoe UI", 20)).place(x=150,y=200)
    escrever_dependentes = tk.CTkLabel(janela_solteiro_n_dinheiro_ss_resultado, text=("Dependentes: {}".format(dependentes)), font=("Segoe UI", 20)).place(x=150, y=250)
    escrever_social = tk.CTkLabel(janela_solteiro_n_dinheiro_ss_resultado, text=("Contribuição Social: Segurança Social"), font=("Segoe UI", 20)).place(x=150, y=300)
    escrever_adse = tk.CTkLabel(janela_solteiro_n_dinheiro_ss_resultado, text=("ADSE: Não"), font=("Segoe UI", 20)).place(x=150, y=350)
    escrever_alimentacao = tk.CTkLabel(janela_solteiro_n_dinheiro_ss_resultado, text=("Subsidio de Alimentação: {} €".format(valor_alimentacao)), font=("Segoe UI", 20)).place(x=150, y=400)
    escrever_dias = tk.CTkLabel(janela_solteiro_n_dinheiro_ss_resultado, text=("Dias com susbsidio de alimentação: {}".format(dias_alimentacao)), font=("Segoe UI", 20)).place(x=150, y=450)
    escrever_pagamento = tk.CTkLabel(janela_solteiro_n_dinheiro_ss_resultado, text=("Forma de pagamento do subsidio de alimentação: Dinheiro"), font=("Segoe UI", 20)).place(x=150, y=500)
    escrever_outros = tk.CTkLabel(janela_solteiro_n_dinheiro_ss_resultado, text=("Outros subsidios tributaveis: {} €".format(outros)), font=("Segoe UI", 20)).place(x=150, y=550)
    escrever_invalidez = tk.CTkLabel(janela_solteiro_n_dinheiro_ss_resultado, text=("Invalidez ou incapacidade: Não"), font=("Segoe UI", 20)).place(x=150, y=600)

### APRESENTAÇÃO DOS VALORES ###
    texto_descontos = tk.CTkLabel(janela_solteiro_n_dinheiro_ss_resultado, text=("Resumo dos descontos"), font=("Segoe UI", 20)) .place(x=879, y=150)
    texto_valor = tk.CTkLabel(janela_solteiro_n_dinheiro_ss_resultado, text=("Valor tributável:{:.2f}€ " .format(renumeracao)), font=("Segoe UI", 20)).place(x=879 , y=300)
    texto_irs = tk.CTkLabel(janela_solteiro_n_dinheiro_ss_resultado, text=("Retenção na fonte: {:.2f}€" .format(valor_irs)), font=("Segoe UI", 20)).place(x=879 , y=200)
    texto_ss = tk.CTkLabel(janela_solteiro_n_dinheiro_ss_resultado, text=("Taxa Social Única: {:.2f}€" .format(valor_ss)), font=("Segoe UI", 20)).place(x=879 , y=250)
    valor_final = tk.CTkLabel(janela_solteiro_n_dinheiro_ss_resultado, text=( "Valor após descontos: {:.2f}€" .format(renumeracao_final)), font=("Segoe UI", 20), bg_color = "red").place(x=879 , y=300)

### FINAL - SAIR OU HISTORICO ###
    decidir_historico = tk.CTkLabel(janela_solteiro_n_dinheiro_ss_resultado, text=("Deseja adicionar está simulação ao histórico?" ), font=("Segoe UI", 20)).place(x=879, y=500)
    select_tabela_a = tk.CTkButton(janela_solteiro_n_dinheiro_ss_resultado, text="Sim",command=lambda: historico_ordenado(regime, situacao_fiscal, dependentes, contribuicao_social, adse, valor_alimentacao, dias_alimentacao, forma_pagamento, outros, renumeracao, valor_irs, valor_adse, valor_ss, renumeracao_final, invalidez),font=("Segoe UI", 20)).place(x=879, y=550)
    select_tabela_b = tk.CTkButton(janela_solteiro_n_dinheiro_ss_resultado, text="Não",command=lambda: reiniciar_programa(),font=("Segoe UI", 20)).place(x=1079, y=550)



def dependente_2t_n_dinheiro_ss_adse(janela_solteiro_n_dinheiro_ss):
    regime = 1
    situacao_fiscal = 3
    contribuicao_social = 1
    adse = 1
    forma_pagamento = 1
    valor_irs=0
    invalidez = 1
    janela_solteiro_n_dinheiro_ss.withdraw()
    janela_solteiro_n_dinheiro_ss_adse = tk.CTkToplevel()
    janela_solteiro_n_dinheiro_ss_adse.geometry("1400x700")
    janela_solteiro_n_dinheiro_ss_adse.title( "Simulação do ordenado liquido - Trabalhador Dependente - Casado - 2 Titular - Resultado Final")
    texto_topo = tk.CTkLabel(janela_solteiro_n_dinheiro_ss_adse, text="Simulação do ordenado liquido\nTrabalhador Dependente\nCasado - 2 Titular\nResultado Final", font=("Segoe UI", 20)).place(x=550, y=0)
    ordenado1 = float(renumera_log[0])
    dependentes = int(dependentes_log[0])
    alimentacao = float(alimentacao_log[0])
    dias_alimentacao = int(dias_log[0])
    outros = float(outros_log[0])
    if alimentacao < 6:
        excedente_alimentacao = 0
    else:
        excedente_alimentacao = alimentacao-6
    valor_alimentacao = alimentacao*dias_alimentacao
    excedente_alimentacao_dias = excedente_alimentacao*dias_alimentacao
    renumeracao = ordenado1+excedente_alimentacao_dias+outros

    if renumeracao<=762:
        renumeracao_liquida = 762
        taxa = 0
        parcela_dependente = 0
        parcela_abater = 0

    else:
        valor_irs, parcela_abater, taxa, renumeracao_liquida, parcela_dependente = casados_2t(dependentes, renumeracao)

    valor_ss = renumeracao*0.11
    valor_adse = renumeracao*0.035

    if valor_irs<0:
        valor_irs = 0
    else:
        valor_irs = valor_irs

    renumeracao_final = renumeracao - valor_adse - valor_ss - valor_irs+valor_alimentacao

    ### SINTESE DE CARACTERISTICAS ###

    escrever_renumeracao = tk.CTkLabel(janela_solteiro_n_dinheiro_ss_adse, text=("Ordenado Base: {} €" .format(ordenado1)), font=("Segoe UI", 20)).place(x=150, y=100)
    escrever_regime = tk.CTkLabel(janela_solteiro_n_dinheiro_ss_adse, text=("Regime: Trabalhador Dependente"), font=("Segoe UI", 20)).place(x=150, y=150)
    escrever_fiscal = tk.CTkLabel(janela_solteiro_n_dinheiro_ss_adse, text = ("Situação Fiscal: Casado - 2 Titular"), font=("Segoe UI", 20)).place(x=150,y=200)
    escrever_dependentes = tk.CTkLabel(janela_solteiro_n_dinheiro_ss_adse, text=("Dependentes: {}".format(dependentes)), font=("Segoe UI", 20)).place(x=150, y=250)
    escrever_social = tk.CTkLabel(janela_solteiro_n_dinheiro_ss_adse, text=("Contribuição Social: Segurança Social"), font=("Segoe UI", 20)).place(x=150, y=300)
    escrever_adse = tk.CTkLabel(janela_solteiro_n_dinheiro_ss_adse, text=("ADSE: Sim"), font=("Segoe UI", 20)).place(x=150, y=350)
    escrever_alimentacao = tk.CTkLabel(janela_solteiro_n_dinheiro_ss_adse, text=("Subsidio de Alimentação: {} €".format(valor_alimentacao)), font=("Segoe UI", 20)).place(x=150, y=400)
    escrever_dias = tk.CTkLabel(janela_solteiro_n_dinheiro_ss_adse, text=("Dias com susbsidio de alimentação: {}".format(dias_alimentacao)), font=("Segoe UI", 20)).place(x=150, y=450)
    escrever_pagamento = tk.CTkLabel(janela_solteiro_n_dinheiro_ss_adse, text=("Forma de pagamento do subsidio de alimentação: Dinheiro"), font=("Segoe UI", 20)).place(x=150, y=500)
    escrever_outros = tk.CTkLabel(janela_solteiro_n_dinheiro_ss_adse, text=("Outros subsidios tributaveis: {} €".format(outros)), font=("Segoe UI", 20)).place(x=150, y=550)
    escrever_invalidez = tk.CTkLabel(janela_solteiro_n_dinheiro_ss_adse, text=("Invalidez ou incapacidade: Não"), font=("Segoe UI", 20)).place(x=150, y=600)

### APRESENTAÇÃO DOS VALORES ###
    texto_descontos = tk.CTkLabel(janela_solteiro_n_dinheiro_ss_adse, text=("Resumo dos descontos"), font=("Segoe UI", 20)) .place(x=879, y=150)
    texto_valor = tk.CTkLabel(janela_solteiro_n_dinheiro_ss_adse, text=("Valor tributável:{:.2f}€ " .format(renumeracao)), font=("Segoe UI", 20)).place(x=879 , y=300)
    texto_irs = tk.CTkLabel(janela_solteiro_n_dinheiro_ss_adse, text=("Retenção na fonte: {:.2f}€" .format(valor_irs)), font=("Segoe UI", 20)).place(x=879 , y=200)
    texto_ss = tk.CTkLabel(janela_solteiro_n_dinheiro_ss_adse, text=("Taxa Social Única: {:.2f}€" .format(valor_ss)), font=("Segoe UI", 20)).place(x=879 , y=250)
    taxa_adse = tk.CTkLabel(janela_solteiro_n_dinheiro_ss_adse, text=("Desconto ADSE: {:.2f}€" .format(valor_adse)), font=("Segoe UI", 20)).place(x=879 , y=350)
    valor_final = tk.CTkLabel(janela_solteiro_n_dinheiro_ss_adse, text=( "Valor após descontos: {:.2f}€" .format(renumeracao_final)), font=("Segoe UI", 20), bg_color = "red").place(x=879 , y=450)

### FINAL - SAIR OU HISTORICO ###
    decidir_historico = tk.CTkLabel(janela_solteiro_n_dinheiro_ss_adse, text=("Deseja adicionar está simulação ao histórico?" ), font=("Segoe UI", 20)).place(x=879, y=500)
    select_tabela_a = tk.CTkButton(janela_solteiro_n_dinheiro_ss_adse, text="Sim",command=lambda: historico_ordenado(regime, situacao_fiscal, dependentes, contribuicao_social, adse, valor_alimentacao, dias_alimentacao, forma_pagamento, outros, renumeracao, valor_irs, valor_adse, valor_ss, renumeracao_final, invalidez),font=("Segoe UI", 20)).place(x=879, y=550)
    select_tabela_b = tk.CTkButton(janela_solteiro_n_dinheiro_ss_adse, text="Não",command=lambda: reiniciar_programa(),font=("Segoe UI", 20)).place(x=1079, y=550)



def dependente_2t_n_dinheiro_ss(janela_solteiro_n_dinheiro):
    janela_solteiro_n_dinheiro.withdraw()
    janela_solteiro_n_dinheiro_ss = tk.CTkToplevel()
    janela_solteiro_n_dinheiro_ss.geometry("1400x700")
    janela_solteiro_n_dinheiro_ss.title("Simulação do ordenado liquido - Trabalhador Dependente - Casado - 2 Titular - Outras contribuições")
    texto_topo = tk.CTkLabel(janela_solteiro_n_dinheiro_ss, text="Simulação do ordenado liquido\nTrabalhador Dependente\nCasado - 2 Titular\nOutras contribuições", font=("Segoe UI", 20)).place(x=550, y=0)
    texto_adse = tk.CTkLabel(janela_solteiro_n_dinheiro_ss, text="É beneficiário da ADSE?", font=("Segoe UI", 20)).place(x=590, y=150)
    botao_sim = tk.CTkButton(janela_solteiro_n_dinheiro_ss, text= "Sim", command=lambda: dependente_2t_n_dinheiro_ss_adse(janela_solteiro_n_dinheiro_ss), font=("Segoe UI", 20)).place(x=530, y=200)
    botao_nao = tk.CTkButton(janela_solteiro_n_dinheiro_ss, text="Não", command=lambda: dependente_2t_n_dinheiro_ss_resultado(janela_solteiro_n_dinheiro_ss), font=("Segoe UI", 20)).place(x=730, y=200)

#
def dependente_2t_n_dinheiro(janela_solteiro_n, pedir_outros, pedir_alimentacao, pedir_dias):
    alimentacao = float(pedir_alimentacao.get())
    alimentacao_log.append(alimentacao)
    dias = float(pedir_dias.get())
    dias_log.append(dias)
    outros = float(pedir_outros.get())
    outros_log.append(outros)
    janela_solteiro_n.withdraw()
    janela_solteiro_n_dinheiro = tk.CTkToplevel()
    janela_solteiro_n_dinheiro.geometry("1400x700")
    janela_solteiro_n_dinheiro.title("Simulação do ordenado liquido - Trabalhador Dependente - Casado - 2 Titular - Outras contribuições")
    texto_topo = tk.CTkLabel(janela_solteiro_n_dinheiro, text="Simulação do ordenado liquido\nTrabalhador Dependente\nCasado - 2 Titular\nOutras contribuições", font=("Segoe UI", 20)).place(x=550, y=0)
    texto_forma = tk.CTkLabel(janela_solteiro_n_dinheiro, text = "Selecione a sua forma de contribuição social", font=("Segoe UI", 20)).place(x=510, y=150)
    botao_ss = tk.CTkButton(janela_solteiro_n_dinheiro, text="Segurança Social", command=lambda:dependente_2t_n_dinheiro_ss(janela_solteiro_n_dinheiro), font=("Segoe UI", 20)) .place(x=606, y=200)
    botao_cga = tk.CTkButton(janela_solteiro_n_dinheiro, text="Caixa Geral de Aposentações", command=lambda: dependente_2t_n_dinheiro_cga(janela_solteiro_n_dinheiro),  font=("Segoe UI",20)) .place(x=560, y=250)


def dependente_2t_n_dinheiro_cga_resultado(janela_solteiro_n_dinheiro_cga):
    regime = 1
    situacao_fiscal = 3
    contribuicao_social = 2
    adse = 2
    forma_pagamento = 1
    valor_irs=0
    invalidez = 1
    valor_adse=0
    janela_solteiro_n_dinheiro_cga.withdraw()
    janela_solteiro_n_dinheiro_cga_resultado = tk.CTkToplevel()
    janela_solteiro_n_dinheiro_cga_resultado.geometry("1400x700")
    janela_solteiro_n_dinheiro_cga_resultado.title( "Simulação do ordenado liquido - Trabalhador Dependente - Casado - 2 Titular - Resultado Final")
    texto_topo = tk.CTkLabel(janela_solteiro_n_dinheiro_cga_resultado, text="Simulação do ordenado liquido\nTrabalhador Dependente\nCasado - 2 Titular\nResultado Final", font=("Segoe UI", 20)).place(x=550, y=0)
    ordenado1 = float(renumera_log[0])
    dependentes = int(dependentes_log[0])
    alimentacao = float(alimentacao_log[0])
    dias_alimentacao = int(dias_log[0])
    outros = float(outros_log[0])
    if alimentacao <6:
        excedente_alimentacao = 0
    else:
        excedente_alimentacao = alimentacao-6
    valor_alimentacao = alimentacao*dias_alimentacao
    excedente_alimentacao_dias = excedente_alimentacao*dias_alimentacao
    renumeracao = ordenado1+excedente_alimentacao_dias+outros

    if renumeracao<=762:
        renumeracao_liquida = 762
        taxa = 0
        parcela_dependente = 0
        parcela_abater = 0

    else:
        valor_irs, parcela_abater, taxa, renumeracao_liquida, parcela_dependente = casados_2t(dependentes, renumeracao)
    if valor_irs<0:
        valor_irs = 0
    else:
        valor_irs = valor_irs
    valor_ss = renumeracao*0.11
    renumeracao_final = renumeracao - valor_ss - valor_irs + valor_alimentacao


    ### SINTESE DE CARACTERISTICAS ###

    escrever_renumeracao = tk.CTkLabel(janela_solteiro_n_dinheiro_cga_resultado, text=("Ordenado Base: {} €" .format(ordenado1)), font=("Segoe UI", 20)).place(x=150, y=100)
    escrever_regime = tk.CTkLabel(janela_solteiro_n_dinheiro_cga_resultado, text=("Regime: Trabalhador Dependente"), font=("Segoe UI", 20)).place(x=150, y=150)
    escrever_fiscal = tk.CTkLabel(janela_solteiro_n_dinheiro_cga_resultado, text = ("Situação Fiscal: Casado - 2 Titular"), font=("Segoe UI", 20)).place(x=150,y=200)
    escrever_dependentes = tk.CTkLabel(janela_solteiro_n_dinheiro_cga_resultado, text=("Dependentes: {}".format(dependentes)), font=("Segoe UI", 20)).place(x=150, y=250)
    escrever_social = tk.CTkLabel(janela_solteiro_n_dinheiro_cga_resultado, text=("Contribuição Social: Caixa Geral de Aposentações"), font=("Segoe UI", 20)).place(x=150, y=300)
    escrever_adse = tk.CTkLabel(janela_solteiro_n_dinheiro_cga_resultado, text=("ADSE: Não"), font=("Segoe UI", 20)).place(x=150, y=350)
    escrever_alimentacao = tk.CTkLabel(janela_solteiro_n_dinheiro_cga_resultado, text=("Subsidio de Alimentação: {} €".format(valor_alimentacao)), font=("Segoe UI", 20)).place(x=150, y=400)
    escrever_dias = tk.CTkLabel(janela_solteiro_n_dinheiro_cga_resultado, text=("Dias com susbsidio de alimentação: {}".format(dias_alimentacao)), font=("Segoe UI", 20)).place(x=150, y=450)
    escrever_pagamento = tk.CTkLabel(janela_solteiro_n_dinheiro_cga_resultado, text=("Forma de pagamento do subsidio de alimentação: Dinheiro"), font=("Segoe UI", 20)).place(x=150, y=500)
    escrever_outros = tk.CTkLabel(janela_solteiro_n_dinheiro_cga_resultado, text=("Outros subsidios tributaveis: {} €".format(outros)), font=("Segoe UI", 20)).place(x=150, y=550)
    escrever_invalidez = tk.CTkLabel(janela_solteiro_n_dinheiro_cga_resultado, text=("Invalidez ou incapacidade: Não"), font=("Segoe UI", 20)).place(x=150, y=600)

### APRESENTAÇÃO DOS VALORES ###
    texto_descontos = tk.CTkLabel(janela_solteiro_n_dinheiro_cga_resultado, text=("Resumo dos descontos"), font=("Segoe UI", 20)) .place(x=879, y=150)
    texto_valor = tk.CTkLabel(janela_solteiro_n_dinheiro_cga_resultado, text=("Valor tributável:{:.2f}€ " .format(renumeracao)), font=("Segoe UI", 20)).place(x=879 , y=300)
    texto_irs = tk.CTkLabel(janela_solteiro_n_dinheiro_cga_resultado, text=("Retenção na fonte: {:.2f}€" .format(valor_irs)), font=("Segoe UI", 20)).place(x=879 , y=200)
    texto_ss = tk.CTkLabel(janela_solteiro_n_dinheiro_cga_resultado, text=("Taxa Social Única: {:.2f}€" .format(valor_ss)), font=("Segoe UI", 20)).place(x=879 , y=250)
    valor_final = tk.CTkLabel(janela_solteiro_n_dinheiro_cga_resultado, text=( "Valor após descontos: {:.2f}€" .format(renumeracao_final)), font=("Segoe UI", 20), bg_color = "red").place(x=879 , y=300)

### FINAL - SAIR OU HISTORICO ###
    decidir_historico = tk.CTkLabel(janela_solteiro_n_dinheiro_cga_resultado, text=("Deseja adicionar está simulação ao histórico?" ), font=("Segoe UI", 20)).place(x=879, y=500)
    select_tabela_a = tk.CTkButton(janela_solteiro_n_dinheiro_cga_resultado, text="Sim",command=lambda: historico_ordenado(regime, situacao_fiscal, dependentes, contribuicao_social, adse, valor_alimentacao, dias_alimentacao, forma_pagamento, outros, renumeracao, valor_irs, valor_adse, valor_ss, renumeracao_final, invalidez),font=("Segoe UI", 20)).place(x=879, y=550)
    select_tabela_b = tk.CTkButton(janela_solteiro_n_dinheiro_cga_resultado, text="Não",command=lambda: reiniciar_programa(),font=("Segoe UI", 20)).place(x=1079, y=550)



def dependente_2t_n_dinheiro_cga_adse(janela_solteiro_n_dinheiro_cga):
    regime = 1
    situacao_fiscal = 3
    contribuicao_social = 2
    adse = 1
    forma_pagamento = 1
    valor_irs=0
    invalidez = 1
    janela_solteiro_n_dinheiro_cga.withdraw()
    janela_solteiro_n_dinheiro_cga_adse = tk.CTkToplevel()
    janela_solteiro_n_dinheiro_cga_adse.geometry("1400x700")
    janela_solteiro_n_dinheiro_cga_adse.title( "Simulação do ordenado liquido - Trabalhador Dependente - Casado - 2 Titular - Resultado Final")
    texto_topo = tk.CTkLabel(janela_solteiro_n_dinheiro_cga_adse, text="Simulação do ordenado liquido\nTrabalhador Dependente\nCasado - 2 Titular\nResultado Final", font=("Segoe UI", 20)).place(x=550, y=0)
    ordenado1 = float(renumera_log[0])
    dependentes = int(dependentes_log[0])
    alimentacao = float(alimentacao_log[0])
    dias_alimentacao = int(dias_log[0])
    outros = float(outros_log[0])
    if alimentacao < 6:
        excedente_alimentacao = 0
    else:
        excedente_alimentacao = alimentacao-6
    valor_alimentacao = alimentacao*dias_alimentacao
    excedente_alimentacao_dias = excedente_alimentacao*dias_alimentacao
    renumeracao = ordenado1+excedente_alimentacao_dias+outros

    if renumeracao<=762:
        renumeracao_liquida = 762
        taxa = 0
        parcela_dependente = 0
        parcela_abater = 0

    else:
        valor_irs, parcela_abater, taxa, renumeracao_liquida, parcela_dependente = casados_2t(dependentes, renumeracao)

    valor_ss = renumeracao*0.11
    valor_adse = renumeracao*0.035
    if valor_irs<0:
        valor_irs = 0
    else:
        valor_irs = valor_irs
    renumeracao_final = renumeracao - valor_adse - valor_ss - valor_irs+valor_alimentacao

    ### SINTESE DE CARACTERISTICAS ###

    escrever_renumeracao = tk.CTkLabel(janela_solteiro_n_dinheiro_cga_adse, text=("Ordenado Base: {} €" .format(ordenado1)), font=("Segoe UI", 20)).place(x=150, y=100)
    escrever_regime = tk.CTkLabel(janela_solteiro_n_dinheiro_cga_adse, text=("Regime: Trabalhador Dependente"), font=("Segoe UI", 20)).place(x=150, y=150)
    escrever_fiscal = tk.CTkLabel(janela_solteiro_n_dinheiro_cga_adse, text = ("Situação Fiscal: Casado - 2 Titular"), font=("Segoe UI", 20)).place(x=150,y=200)
    escrever_dependentes = tk.CTkLabel(janela_solteiro_n_dinheiro_cga_adse, text=("Dependentes: {}".format(dependentes)), font=("Segoe UI", 20)).place(x=150, y=250)
    escrever_social = tk.CTkLabel(janela_solteiro_n_dinheiro_cga_adse, text=("Contribuição Social: Caixa Geral de Aposentações"), font=("Segoe UI", 20)).place(x=150, y=300)
    escrever_adse = tk.CTkLabel(janela_solteiro_n_dinheiro_cga_adse, text=("ADSE: Sim"), font=("Segoe UI", 20)).place(x=150, y=350)
    escrever_alimentacao = tk.CTkLabel(janela_solteiro_n_dinheiro_cga_adse, text=("Subsidio de Alimentação: {} €".format(valor_alimentacao)), font=("Segoe UI", 20)).place(x=150, y=400)
    escrever_dias = tk.CTkLabel(janela_solteiro_n_dinheiro_cga_adse, text=("Dias com susbsidio de alimentação: {}".format(dias_alimentacao)), font=("Segoe UI", 20)).place(x=150, y=450)
    escrever_pagamento = tk.CTkLabel(janela_solteiro_n_dinheiro_cga_adse, text=("Forma de pagamento do subsidio de alimentação: Dinheiro"), font=("Segoe UI", 20)).place(x=150, y=500)
    escrever_outros = tk.CTkLabel(janela_solteiro_n_dinheiro_cga_adse, text=("Outros subsidios tributaveis: {} €".format(outros)), font=("Segoe UI", 20)).place(x=150, y=550)
    escrever_invalidez = tk.CTkLabel(janela_solteiro_n_dinheiro_cga_adse, text=("Invalidez ou incapacidade: Não"), font=("Segoe UI", 20)).place(x=150, y=600)

### APRESENTAÇÃO DOS VALORES ###
    texto_descontos = tk.CTkLabel(janela_solteiro_n_dinheiro_cga_adse, text=("Resumo dos descontos"), font=("Segoe UI", 20)) .place(x=879, y=150)
    texto_valor = tk.CTkLabel(janela_solteiro_n_dinheiro_cga_adse, text=("Valor tributável:{:.2f}€ " .format(renumeracao)), font=("Segoe UI", 20)).place(x=879 , y=300)
    texto_irs = tk.CTkLabel(janela_solteiro_n_dinheiro_cga_adse, text=("Retenção na fonte: {:.2f}€" .format(valor_irs)), font=("Segoe UI", 20)).place(x=879 , y=200)
    texto_ss = tk.CTkLabel(janela_solteiro_n_dinheiro_cga_adse, text=("Taxa Social Única: {:.2f}€" .format(valor_ss)), font=("Segoe UI", 20)).place(x=879 , y=250)
    taxa_adse = tk.CTkLabel(janela_solteiro_n_dinheiro_cga_adse, text=("Desconto ADSE: {:.2f}€" .format(valor_adse)), font=("Segoe UI", 20)).place(x=879 , y=350)
    valor_final = tk.CTkLabel(janela_solteiro_n_dinheiro_cga_adse, text=( "Valor após descontos: {:.2f}€" .format(renumeracao_final)), font=("Segoe UI", 20), bg_color = "red").place(x=879 , y=450)

### FINAL - SAIR OU HISTORICO ###
    decidir_historico = tk.CTkLabel(janela_solteiro_n_dinheiro_cga_adse, text=("Deseja adicionar está simulação ao histórico?" ), font=("Segoe UI", 20)).place(x=879, y=500)
    select_tabela_a = tk.CTkButton(janela_solteiro_n_dinheiro_cga_adse, text="Sim",command=lambda: historico_ordenado(regime, situacao_fiscal, dependentes, contribuicao_social, adse, valor_alimentacao, dias_alimentacao, forma_pagamento, outros, renumeracao, valor_irs, valor_adse, valor_ss, renumeracao_final, invalidez),font=("Segoe UI", 20)).place(x=879, y=550)
    select_tabela_b = tk.CTkButton(janela_solteiro_n_dinheiro_cga_adse, text="Não",command=lambda: reiniciar_programa(),font=("Segoe UI", 20)).place(x=1079, y=550)



def dependente_2t_n_dinheiro_cga(janela_solteiro_n_dinheiro):
    janela_solteiro_n_dinheiro.withdraw()
    janela_solteiro_n_dinheiro_cga = tk.CTkToplevel()
    janela_solteiro_n_dinheiro_cga.geometry("1400x700")
    janela_solteiro_n_dinheiro_cga.title("Simulação do ordenado liquido - Trabalhador Dependente - Casado - 2 Titular - Outras contribuições")
    texto_topo = tk.CTkLabel(janela_solteiro_n_dinheiro_cga, text="Simulação do ordenado liquido\nTrabalhador Dependente\nCasado - 2 Titular\nOutras contribuições", font=("Segoe UI", 20)).place(x=550, y=0)
    texto_adse = tk.CTkLabel(janela_solteiro_n_dinheiro_cga, text="É beneficiário da ADSE?", font=("Segoe UI", 20)).place(x=590, y=150)
    botao_sim = tk.CTkButton(janela_solteiro_n_dinheiro_cga, text= "Sim", command=lambda: dependente_2t_n_dinheiro_cga_adse(janela_solteiro_n_dinheiro_cga), font=("Segoe UI", 20)).place(x=530, y=200)
    botao_nao = tk.CTkButton(janela_solteiro_n_dinheiro_cga, text="Não", command=lambda: dependente_2t_n_dinheiro_cga_resultado(janela_solteiro_n_dinheiro_cga), font=("Segoe UI", 20)).place(x=730, y=200)


def dependente_2t_n_dinheiro_ss_resultado(janela_solteiro_n_dinheiro_ss):
    regime = 1
    situacao_fiscal = 3
    contribuicao_social = 1
    adse = 2
    forma_pagamento = 1
    valor_irs=0
    invalidez = 1
    valor_adse=0
    janela_solteiro_n_dinheiro_ss.withdraw()
    janela_solteiro_n_dinheiro_ss_resultado = tk.CTkToplevel()
    janela_solteiro_n_dinheiro_ss_resultado.geometry("1400x700")
    janela_solteiro_n_dinheiro_ss_resultado.title( "Simulação do ordenado liquido - Trabalhador Dependente - Casado - 2 Titular - Resultado Final")
    texto_topo = tk.CTkLabel(janela_solteiro_n_dinheiro_ss_resultado, text="Simulação do ordenado liquido\nTrabalhador Dependente\nCasado - 2 Titular\nResultado Final", font=("Segoe UI", 20)).place(x=550, y=0)
    ordenado1 = float(renumera_log[0])
    dependentes = int(dependentes_log[0])
    alimentacao = float(alimentacao_log[0])
    dias_alimentacao = int(dias_log[0])
    outros = float(outros_log[0])
    if alimentacao <6:
        excedente_alimentacao = 0
    else:
        excedente_alimentacao = alimentacao-6
    valor_alimentacao = alimentacao*dias_alimentacao
    excedente_alimentacao_dias = excedente_alimentacao*dias_alimentacao
    renumeracao = ordenado1+excedente_alimentacao_dias+outros

    if renumeracao<=762:
        renumeracao_liquida = 762
        taxa = 0
        parcela_dependente = 0
        parcela_abater = 0

    else:
        valor_irs, parcela_abater, taxa, renumeracao_liquida, parcela_dependente = casados_2t(dependentes, renumeracao)
    if valor_irs<0:
        valor_irs = 0
    else:
        valor_irs = valor_irs
    valor_ss = renumeracao*0.11
    renumeracao_final = renumeracao - valor_ss - valor_irs + valor_alimentacao


    ### SINTESE DE CARACTERISTICAS ###

    escrever_renumeracao = tk.CTkLabel(janela_solteiro_n_dinheiro_ss_resultado, text=("Ordenado Base: {} €" .format(ordenado1)), font=("Segoe UI", 20)).place(x=150, y=100)
    escrever_regime = tk.CTkLabel(janela_solteiro_n_dinheiro_ss_resultado, text=("Regime: Trabalhador Dependente"), font=("Segoe UI", 20)).place(x=150, y=150)
    escrever_fiscal = tk.CTkLabel(janela_solteiro_n_dinheiro_ss_resultado, text = ("Situação Fiscal: Casado - 2 Titular"), font=("Segoe UI", 20)).place(x=150,y=200)
    escrever_dependentes = tk.CTkLabel(janela_solteiro_n_dinheiro_ss_resultado, text=("Dependentes: {}".format(dependentes)), font=("Segoe UI", 20)).place(x=150, y=250)
    escrever_social = tk.CTkLabel(janela_solteiro_n_dinheiro_ss_resultado, text=("Contribuição Social: Segurança Social"), font=("Segoe UI", 20)).place(x=150, y=300)
    escrever_adse = tk.CTkLabel(janela_solteiro_n_dinheiro_ss_resultado, text=("ADSE: Não"), font=("Segoe UI", 20)).place(x=150, y=350)
    escrever_alimentacao = tk.CTkLabel(janela_solteiro_n_dinheiro_ss_resultado, text=("Subsidio de Alimentação: {} €".format(valor_alimentacao)), font=("Segoe UI", 20)).place(x=150, y=400)
    escrever_dias = tk.CTkLabel(janela_solteiro_n_dinheiro_ss_resultado, text=("Dias com susbsidio de alimentação: {}".format(dias_alimentacao)), font=("Segoe UI", 20)).place(x=150, y=450)
    escrever_pagamento = tk.CTkLabel(janela_solteiro_n_dinheiro_ss_resultado, text=("Forma de pagamento do subsidio de alimentação: Dinheiro"), font=("Segoe UI", 20)).place(x=150, y=500)
    escrever_outros = tk.CTkLabel(janela_solteiro_n_dinheiro_ss_resultado, text=("Outros subsidios tributaveis: {} €".format(outros)), font=("Segoe UI", 20)).place(x=150, y=550)
    escrever_invalidez = tk.CTkLabel(janela_solteiro_n_dinheiro_ss_resultado, text=("Invalidez ou incapacidade: Não"), font=("Segoe UI", 20)).place(x=150, y=600)

### APRESENTAÇÃO DOS VALORES ###
    texto_descontos = tk.CTkLabel(janela_solteiro_n_dinheiro_ss_resultado, text=("Resumo dos descontos"), font=("Segoe UI", 20)) .place(x=879, y=150)
    texto_valor = tk.CTkLabel(janela_solteiro_n_dinheiro_ss_resultado, text=("Valor tributável:{:.2f}€ " .format(renumeracao)), font=("Segoe UI", 20)).place(x=879 , y=300)
    texto_irs = tk.CTkLabel(janela_solteiro_n_dinheiro_ss_resultado, text=("Retenção na fonte: {:.2f}€" .format(valor_irs)), font=("Segoe UI", 20)).place(x=879 , y=200)
    texto_ss = tk.CTkLabel(janela_solteiro_n_dinheiro_ss_resultado, text=("Taxa Social Única: {:.2f}€" .format(valor_ss)), font=("Segoe UI", 20)).place(x=879 , y=250)
    valor_final = tk.CTkLabel(janela_solteiro_n_dinheiro_ss_resultado, text=( "Valor após descontos: {:.2f}€" .format(renumeracao_final)), font=("Segoe UI", 20), bg_color = "red").place(x=879 , y=300)

### FINAL - SAIR OU HISTORICO ###
    decidir_historico = tk.CTkLabel(janela_solteiro_n_dinheiro_ss_resultado, text=("Deseja adicionar está simulação ao histórico?" ), font=("Segoe UI", 20)).place(x=879, y=500)
    select_tabela_a = tk.CTkButton(janela_solteiro_n_dinheiro_ss_resultado, text="Sim",command=lambda: historico_ordenado(regime, situacao_fiscal, dependentes, contribuicao_social, adse, valor_alimentacao, dias_alimentacao, forma_pagamento, outros, renumeracao, valor_irs, valor_adse, valor_ss, renumeracao_final, invalidez),font=("Segoe UI", 20)).place(x=879, y=550)
    select_tabela_b = tk.CTkButton(janela_solteiro_n_dinheiro_ss_resultado, text="Não",command=lambda: reiniciar_programa(),font=("Segoe UI", 20)).place(x=1079, y=550)



def dependente_2t_n_dinheiro_ss_adse(janela_solteiro_n_dinheiro_ss):
    regime = 1
    situacao_fiscal = 3
    contribuicao_social = 1
    adse = 1
    forma_pagamento = 1
    valor_irs=0
    invalidez = 1
    janela_solteiro_n_dinheiro_ss.withdraw()
    janela_solteiro_n_dinheiro_ss_adse = tk.CTkToplevel()
    janela_solteiro_n_dinheiro_ss_adse.geometry("1400x700")
    janela_solteiro_n_dinheiro_ss_adse.title( "Simulação do ordenado liquido - Trabalhador Dependente - Casado - 2 Titular - Resultado Final")
    texto_topo = tk.CTkLabel(janela_solteiro_n_dinheiro_ss_adse, text="Simulação do ordenado liquido\nTrabalhador Dependente\nCasado - 2 Titular\nResultado Final", font=("Segoe UI", 20)).place(x=550, y=0)
    ordenado1 = float(renumera_log[0])
    dependentes = int(dependentes_log[0])
    alimentacao = float(alimentacao_log[0])
    dias_alimentacao = int(dias_log[0])
    outros = float(outros_log[0])
    if alimentacao < 6:
        excedente_alimentacao = 0
    else:
        excedente_alimentacao = alimentacao-6
    valor_alimentacao = alimentacao*dias_alimentacao
    excedente_alimentacao_dias = excedente_alimentacao*dias_alimentacao
    renumeracao = ordenado1+excedente_alimentacao_dias+outros

    if renumeracao<=762:
        renumeracao_liquida = 762
        taxa = 0
        parcela_dependente = 0
        parcela_abater = 0

    else:
        valor_irs, parcela_abater, taxa, renumeracao_liquida, parcela_dependente = casados_2t(dependentes, renumeracao)

    valor_ss = renumeracao*0.11
    valor_adse = renumeracao*0.035

    if valor_irs<0:
        valor_irs = 0
    else:
        valor_irs = valor_irs

    renumeracao_final = renumeracao - valor_adse - valor_ss - valor_irs+valor_alimentacao

    ### SINTESE DE CARACTERISTICAS ###

    escrever_renumeracao = tk.CTkLabel(janela_solteiro_n_dinheiro_ss_adse, text=("Ordenado Base: {} €" .format(ordenado1)), font=("Segoe UI", 20)).place(x=150, y=100)
    escrever_regime = tk.CTkLabel(janela_solteiro_n_dinheiro_ss_adse, text=("Regime: Trabalhador Dependente"), font=("Segoe UI", 20)).place(x=150, y=150)
    escrever_fiscal = tk.CTkLabel(janela_solteiro_n_dinheiro_ss_adse, text = ("Situação Fiscal: Casado - 2 Titular"), font=("Segoe UI", 20)).place(x=150,y=200)
    escrever_dependentes = tk.CTkLabel(janela_solteiro_n_dinheiro_ss_adse, text=("Dependentes: {}".format(dependentes)), font=("Segoe UI", 20)).place(x=150, y=250)
    escrever_social = tk.CTkLabel(janela_solteiro_n_dinheiro_ss_adse, text=("Contribuição Social: Segurança Social"), font=("Segoe UI", 20)).place(x=150, y=300)
    escrever_adse = tk.CTkLabel(janela_solteiro_n_dinheiro_ss_adse, text=("ADSE: Sim"), font=("Segoe UI", 20)).place(x=150, y=350)
    escrever_alimentacao = tk.CTkLabel(janela_solteiro_n_dinheiro_ss_adse, text=("Subsidio de Alimentação: {} €".format(valor_alimentacao)), font=("Segoe UI", 20)).place(x=150, y=400)
    escrever_dias = tk.CTkLabel(janela_solteiro_n_dinheiro_ss_adse, text=("Dias com susbsidio de alimentação: {}".format(dias_alimentacao)), font=("Segoe UI", 20)).place(x=150, y=450)
    escrever_pagamento = tk.CTkLabel(janela_solteiro_n_dinheiro_ss_adse, text=("Forma de pagamento do subsidio de alimentação: Dinheiro"), font=("Segoe UI", 20)).place(x=150, y=500)
    escrever_outros = tk.CTkLabel(janela_solteiro_n_dinheiro_ss_adse, text=("Outros subsidios tributaveis: {} €".format(outros)), font=("Segoe UI", 20)).place(x=150, y=550)
    escrever_invalidez = tk.CTkLabel(janela_solteiro_n_dinheiro_ss_adse, text=("Invalidez ou incapacidade: Não"), font=("Segoe UI", 20)).place(x=150, y=600)

### APRESENTAÇÃO DOS VALORES ###
    texto_descontos = tk.CTkLabel(janela_solteiro_n_dinheiro_ss_adse, text=("Resumo dos descontos"), font=("Segoe UI", 20)) .place(x=879, y=150)
    texto_valor = tk.CTkLabel(janela_solteiro_n_dinheiro_ss_adse, text=("Valor tributável:{:.2f}€ " .format(renumeracao)), font=("Segoe UI", 20)).place(x=879 , y=300)
    texto_irs = tk.CTkLabel(janela_solteiro_n_dinheiro_ss_adse, text=("Retenção na fonte: {:.2f}€" .format(valor_irs)), font=("Segoe UI", 20)).place(x=879 , y=200)
    texto_ss = tk.CTkLabel(janela_solteiro_n_dinheiro_ss_adse, text=("Taxa Social Única: {:.2f}€" .format(valor_ss)), font=("Segoe UI", 20)).place(x=879 , y=250)
    taxa_adse = tk.CTkLabel(janela_solteiro_n_dinheiro_ss_adse, text=("Desconto ADSE: {:.2f}€" .format(valor_adse)), font=("Segoe UI", 20)).place(x=879 , y=350)
    valor_final = tk.CTkLabel(janela_solteiro_n_dinheiro_ss_adse, text=( "Valor após descontos: {:.2f}€" .format(renumeracao_final)), font=("Segoe UI", 20), bg_color = "red").place(x=879 , y=450)

### FINAL - SAIR OU HISTORICO ###
    decidir_historico = tk.CTkLabel(janela_solteiro_n_dinheiro_ss_adse, text=("Deseja adicionar está simulação ao histórico?" ), font=("Segoe UI", 20)).place(x=879, y=500)
    select_tabela_a = tk.CTkButton(janela_solteiro_n_dinheiro_ss_adse, text="Sim",command=lambda: historico_ordenado(regime, situacao_fiscal, dependentes, contribuicao_social, adse, valor_alimentacao, dias_alimentacao, forma_pagamento, outros, renumeracao, valor_irs, valor_adse, valor_ss, renumeracao_final, invalidez),font=("Segoe UI", 20)).place(x=879, y=550)
    select_tabela_b = tk.CTkButton(janela_solteiro_n_dinheiro_ss_adse, text="Não",command=lambda: reiniciar_programa(),font=("Segoe UI", 20)).place(x=1079, y=550)



def dependente_2t_n_dinheiro_ss(janela_solteiro_n_dinheiro):
    janela_solteiro_n_dinheiro.withdraw()
    janela_solteiro_n_dinheiro_ss = tk.CTkToplevel()
    janela_solteiro_n_dinheiro_ss.geometry("1400x700")
    janela_solteiro_n_dinheiro_ss.title("Simulação do ordenado liquido - Trabalhador Dependente - Casado - 2 Titular - Outras contribuições")
    texto_topo = tk.CTkLabel(janela_solteiro_n_dinheiro_ss, text="Simulação do ordenado liquido\nTrabalhador Dependente\nCasado - 2 Titular\nOutras contribuições", font=("Segoe UI", 20)).place(x=550, y=0)
    texto_adse = tk.CTkLabel(janela_solteiro_n_dinheiro_ss, text="É beneficiário da ADSE?", font=("Segoe UI", 20)).place(x=590, y=150)
    botao_sim = tk.CTkButton(janela_solteiro_n_dinheiro_ss, text= "Sim", command=lambda: dependente_2t_n_dinheiro_ss_adse(janela_solteiro_n_dinheiro_ss), font=("Segoe UI", 20)).place(x=530, y=200)
    botao_nao = tk.CTkButton(janela_solteiro_n_dinheiro_ss, text="Não", command=lambda: dependente_2t_n_dinheiro_ss_resultado(janela_solteiro_n_dinheiro_ss), font=("Segoe UI", 20)).place(x=730, y=200)


def dependente_2t_n_dinheiro(janela_solteiro_n, pedir_outros, pedir_alimentacao, pedir_dias):
    alimentacao = float(pedir_alimentacao.get())
    alimentacao_log.append(alimentacao)
    dias = float(pedir_dias.get())
    dias_log.append(dias)
    outros = float(pedir_outros.get())
    outros_log.append(outros)
    janela_solteiro_n.withdraw()
    janela_solteiro_n_dinheiro = tk.CTkToplevel()
    janela_solteiro_n_dinheiro.geometry("1400x700")
    janela_solteiro_n_dinheiro.title("Simulação do ordenado liquido - Trabalhador Dependente - Casado - 2 Titular - Outras contribuições")
    texto_topo = tk.CTkLabel(janela_solteiro_n_dinheiro, text="Simulação do ordenado liquido\nTrabalhador Dependente\nCasado - 2 Titular\nOutras contribuições", font=("Segoe UI", 20)).place(x=550, y=0)
    texto_forma = tk.CTkLabel(janela_solteiro_n_dinheiro, text = "Selecione a sua forma de contribuição social", font=("Segoe UI", 20)).place(x=510, y=150)
    botao_ss = tk.CTkButton(janela_solteiro_n_dinheiro, text="Segurança Social", command=lambda:dependente_2t_n_dinheiro_ss(janela_solteiro_n_dinheiro), font=("Segoe UI", 20)) .place(x=606, y=200)
    botao_cga = tk.CTkButton(janela_solteiro_n_dinheiro, text="Caixa Geral de Aposentações", command=lambda: dependente_2t_n_dinheiro_cga(janela_solteiro_n_dinheiro),  font=("Segoe UI",20)) .place(x=560, y=250)

def dependente_2t_n(janela_dependente_solteiro, pedir_renumeracao_base):

    ordenado2 = float(pedir_renumeracao_base.get())
    renumera_log.append(ordenado2)
    janela_dependente_solteiro.withdraw()
    janela_solteiro_n = tk.CTkToplevel()
    janela_solteiro_n.geometry("1400x700")
    janela_solteiro_n.title("Simulação do ordenado liquido - Trabalhador Dependente - Casado - 2 Titular - Subsidios")
    texto_topo = tk.CTkLabel(janela_solteiro_n,text="Simulação do ordenado liquido\nTrabalhador Dependente\nCasado - 2 Titular", font=("Segoe UI", 20)).place(x=550, y=0)
    texto_alimentacao = tk.CTkLabel(janela_solteiro_n,text="Insira o valor diário do subsidio de alimentação", font=("Segoe UI", 20)).place(x=490, y=100)
    pedir_alimentacao = tk.CTkEntry(janela_solteiro_n, placeholder_text= "Valor", font=("Segoe UI",20))
    pedir_alimentacao.place(x=636, y=150)
    texto_dias = tk.CTkLabel(janela_solteiro_n,text="Insira o número de dias com subsidio de alimentação", font=("Segoe UI", 20)).place(x=475, y=200)
    pedir_dias = tk.CTkEntry(janela_solteiro_n, placeholder_text="Dias", font=("Segoe UI", 20))
    pedir_dias.place(x=636, y=250)
    texto_outros = tk.CTkLabel(janela_solteiro_n, text = "Insira o valor de outros subsidios", font=("Segoe UI",20)) .place(x=550,y=300)
    pedir_outros = tk.CTkEntry(janela_solteiro_n, placeholder_text= "Valor", font=("Segoe UI",20))
    pedir_outros.place(x=636,y=350)
    texto_pag_alimentacao = tk.CTkLabel(janela_solteiro_n, text = "Selecione a forma de pagamento do subsidio de alimentacão", font=("Segoe UI", 20)) .place(x=450, y=400)
    botao_dinheiro = tk.CTkButton(janela_solteiro_n, text = "Dinheiro", font=("Segoe UI", 20), command=lambda: dependente_2t_n_dinheiro(janela_solteiro_n, pedir_outros, pedir_alimentacao, pedir_dias)) .place(x=490, y=450)
    botao_cartao = tk.CTkButton(janela_solteiro_n, text="Cartão/Vale de refeição", command=lambda:dependente_2t_n_vale(janela_solteiro_n, pedir_outros, pedir_alimentacao, pedir_dias),font=("Segoe UI", 20)) .place(x=690, y=450)

############################################ INVALIDEZ ####################


def dependente_2t_s_vale_cga_resultado(janela_solteiro_n_vale_cga):
    regime = 1
    situacao_fiscal = 3
    contribuicao_social = 2
    adse = 2
    forma_pagamento = 2
    valor_irs=0
    invalidez = 2
    valor_adse=0
    janela_solteiro_n_vale_cga.withdraw()
    janela_solteiro_n_vale_cga_resultado = tk.CTkToplevel()
    janela_solteiro_n_vale_cga_resultado.geometry("1400x700")
    janela_solteiro_n_vale_cga_resultado.title( "Simulação do ordenado liquido - Trabalhador Dependente - Casado - 2 Titular  - Resultado Final")
    texto_topo = tk.CTkLabel(janela_solteiro_n_vale_cga_resultado, text="Simulação do ordenado liquido\nTrabalhador Dependente\nCasado - 1 Titular\nResultado Final", font=("Segoe UI", 20)).place(x=550, y=0)
    ordenado1 = float(renumera_log[0])
    dependentes = int(dependentes_log[0])
    alimentacao = float(alimentacao_log[0])
    dias_alimentacao = int(dias_log[0])
    outros = float(outros_log[0])
    if alimentacao < 9.6:
        excedente_alimentacao = 0
    else:
        excedente_alimentacao = alimentacao-9.6
    valor_alimentacao = alimentacao*dias_alimentacao
    excedente_alimentacao_dias = excedente_alimentacao*dias_alimentacao
    renumeracao = ordenado1+excedente_alimentacao_dias+outros


    valor_irs, parcela_abater, taxa, renumeracao_liquida, parcela_dependente = casados_2t_invalidez(dependentes, renumeracao)
    if valor_irs<0:
        valor_irs = 0
    else:
        valor_irs = valor_irs
    valor_ss = renumeracao*0.11
    renumeracao_final = renumeracao - valor_ss - valor_irs + valor_alimentacao


    ### SINTESE DE CARACTERISTICAS ###

    escrever_renumeracao = tk.CTkLabel(janela_solteiro_n_vale_cga_resultado, text=("Ordenado Base: {} €" .format(ordenado1)), font=("Segoe UI", 20)).place(x=150, y=100)
    escrever_regime = tk.CTkLabel(janela_solteiro_n_vale_cga_resultado, text=("Regime: Trabalhador Dependente"), font=("Segoe UI", 20)).place(x=150, y=150)
    escrever_fiscal = tk.CTkLabel(janela_solteiro_n_vale_cga_resultado, text = ("Situação Fiscal: Casado - 2 Titular"), font=("Segoe UI", 20)).place(x=150,y=200)
    escrever_dependentes = tk.CTkLabel(janela_solteiro_n_vale_cga_resultado, text=("Dependentes: {}".format(dependentes)), font=("Segoe UI", 20)).place(x=150, y=250)
    escrever_social = tk.CTkLabel(janela_solteiro_n_vale_cga_resultado, text=("Contribuição Social: Caixa Geral de Aposentações"), font=("Segoe UI", 20)).place(x=150, y=300)
    escrever_adse = tk.CTkLabel(janela_solteiro_n_vale_cga_resultado, text=("ADSE: Não"), font=("Segoe UI", 20)).place(x=150, y=350)
    escrever_alimentacao = tk.CTkLabel(janela_solteiro_n_vale_cga_resultado, text=("Subsidio de Alimentação: {} €".format(valor_alimentacao)), font=("Segoe UI", 20)).place(x=150, y=400)
    escrever_dias = tk.CTkLabel(janela_solteiro_n_vale_cga_resultado, text=("Dias com susbsidio de alimentação: {}".format(dias_alimentacao)), font=("Segoe UI", 20)).place(x=150, y=450)
    escrever_pagamento = tk.CTkLabel(janela_solteiro_n_vale_cga_resultado, text=("Forma de pagamento do subsidio de alimentação: Vale/Cartão de refeição"), font=("Segoe UI", 20)).place(x=150, y=500)
    escrever_outros = tk.CTkLabel(janela_solteiro_n_vale_cga_resultado, text=("Outros subsidios tributaveis: {} €".format(outros)), font=("Segoe UI", 20)).place(x=150, y=550)
    escrever_invalidez = tk.CTkLabel(janela_solteiro_n_vale_cga_resultado, text=("Invalidez ou incapacidade: Sim"), font=("Segoe UI", 20)).place(x=150, y=600)

### APRESENTAÇÃO DOS VALORES ###
    texto_descontos = tk.CTkLabel(janela_solteiro_n_vale_cga_resultado, text=("Resumo dos descontos"), font=("Segoe UI", 20)) .place(x=879, y=150)
    texto_valor = tk.CTkLabel(janela_solteiro_n_vale_cga_resultado, text=("Valor tributável:{:.2f}€ " .format(renumeracao)), font=("Segoe UI", 20)).place(x=879 , y=300)
    texto_irs = tk.CTkLabel(janela_solteiro_n_vale_cga_resultado, text=("Retenção na fonte: {:.2f}€" .format(valor_irs)), font=("Segoe UI", 20)).place(x=879 , y=200)
    texto_ss = tk.CTkLabel(janela_solteiro_n_vale_cga_resultado, text=("Taxa Social Única: {:.2f}€" .format(valor_ss)), font=("Segoe UI", 20)).place(x=879 , y=250)
    valor_final = tk.CTkLabel(janela_solteiro_n_vale_cga_resultado, text=( "Valor após descontos: {:.2f}€" .format(renumeracao_final)), font=("Segoe UI", 20), bg_color = "red").place(x=879 , y=300)

### FINAL - SAIR OU HISTORICO ###
    decidir_historico = tk.CTkLabel(janela_solteiro_n_vale_cga_resultado, text=("Deseja adicionar está simulação ao histórico?" ), font=("Segoe UI", 20)).place(x=879, y=500)
    select_tabela_a = tk.CTkButton(janela_solteiro_n_vale_cga_resultado, text="Sim",command=lambda: historico_ordenado(regime, situacao_fiscal, dependentes, contribuicao_social, adse, valor_alimentacao, dias_alimentacao, forma_pagamento, outros, renumeracao, valor_irs, valor_adse, valor_ss, renumeracao_final, invalidez),font=("Segoe UI", 20)).place(x=879, y=550)
    select_tabela_b = tk.CTkButton(janela_solteiro_n_vale_cga_resultado, text="Não",command=lambda: reiniciar_programa(),font=("Segoe UI", 20)).place(x=1079, y=550)

def dependente_2t_s_vale_cga_adse(janela_solteiro_n_vale_cga):
    regime = 1
    situacao_fiscal = 3
    contribuicao_social = 2
    adse = 1
    forma_pagamento = 2
    valor_irs=0
    invalidez = 2
    janela_solteiro_n_vale_cga.withdraw()
    janela_solteiro_n_vale_cga_adse = tk.CTkToplevel()
    janela_solteiro_n_vale_cga_adse.geometry("1400x700")
    janela_solteiro_n_vale_cga_adse.title( "Simulação do ordenado liquido - Trabalhador Dependente - Casado - 2 Titular  - Resultado Final")
    texto_topo = tk.CTkLabel(janela_solteiro_n_vale_cga_adse, text="Simulação do ordenado liquido\nTrabalhador Dependente\nCasado - 2 Titular\nResultado Final", font=("Segoe UI", 20)).place(x=550, y=0)
    ordenado1 = float(renumera_log[0])
    dependentes = int(dependentes_log[0])
    alimentacao = float(alimentacao_log[0])
    dias_alimentacao = int(dias_log[0])
    outros = float(outros_log[0])
    if alimentacao < 9.6:
        excedente_alimentacao = 0
    else:
        excedente_alimentacao = alimentacao-9.6
    valor_alimentacao = alimentacao*dias_alimentacao
    excedente_alimentacao_dias = excedente_alimentacao*dias_alimentacao
    renumeracao = ordenado1+excedente_alimentacao_dias+outros


    valor_irs, parcela_abater, taxa, renumeracao_liquida, parcela_dependente = casados_2t_invalidez(dependentes, renumeracao)

    valor_ss = renumeracao*0.11
    valor_adse = renumeracao*0.035
    if valor_irs<0:
        valor_irs = 0
    else:
        valor_irs = valor_irs
    renumeracao_final = renumeracao - valor_adse - valor_ss - valor_irs+valor_alimentacao

    ### SINTESE DE CARACTERISTICAS ###

    escrever_renumeracao = tk.CTkLabel(janela_solteiro_n_vale_cga_adse, text=("Ordenado Base: {} €" .format(ordenado1)), font=("Segoe UI", 20)).place(x=150, y=100)
    escrever_regime = tk.CTkLabel(janela_solteiro_n_vale_cga_adse, text=("Regime: Trabalhador Dependente"), font=("Segoe UI", 20)).place(x=150, y=150)
    escrever_fiscal = tk.CTkLabel(janela_solteiro_n_vale_cga_adse, text = ("Situação Fiscal:  Casado - 2 Titular"), font=("Segoe UI", 20)).place(x=150,y=200)
    escrever_dependentes = tk.CTkLabel(janela_solteiro_n_vale_cga_adse, text=("Dependentes: {}".format(dependentes)), font=("Segoe UI", 20)).place(x=150, y=250)
    escrever_social = tk.CTkLabel(janela_solteiro_n_vale_cga_adse, text=("Contribuição Social: Caixa Geral de Aposentações"), font=("Segoe UI", 20)).place(x=150, y=300)
    escrever_adse = tk.CTkLabel(janela_solteiro_n_vale_cga_adse, text=("ADSE: Sim"), font=("Segoe UI", 20)).place(x=150, y=350)
    escrever_alimentacao = tk.CTkLabel(janela_solteiro_n_vale_cga_adse, text=("Subsidio de Alimentação: {} €".format(valor_alimentacao)), font=("Segoe UI", 20)).place(x=150, y=400)
    escrever_dias = tk.CTkLabel(janela_solteiro_n_vale_cga_adse, text=("Dias com susbsidio de alimentação: {}".format(dias_alimentacao)), font=("Segoe UI", 20)).place(x=150, y=450)
    escrever_pagamento = tk.CTkLabel(janela_solteiro_n_vale_cga_adse, text=("Forma de pagamento do subsidio de alimentação: Vale/Cartão de alimentação"), font=("Segoe UI", 20)).place(x=150, y=500)
    escrever_outros = tk.CTkLabel(janela_solteiro_n_vale_cga_adse, text=("Outros subsidios tributaveis: {} €".format(outros)), font=("Segoe UI", 20)).place(x=150, y=550)
    escrever_invalidez = tk.CTkLabel(janela_solteiro_n_vale_cga_adse, text=("Invalidez ou incapacidade: Sim"), font=("Segoe UI", 20)).place(x=150, y=600)

### APRESENTAÇÃO DOS VALORES ###
    texto_descontos = tk.CTkLabel(janela_solteiro_n_vale_cga_adse, text=("Resumo dos descontos"), font=("Segoe UI", 20)) .place(x=879, y=150)
    texto_valor = tk.CTkLabel(janela_solteiro_n_vale_cga_adse, text=("Valor tributável:{:.2f}€ " .format(renumeracao)), font=("Segoe UI", 20)).place(x=879 , y=300)
    texto_irs = tk.CTkLabel(janela_solteiro_n_vale_cga_adse, text=("Retenção na fonte: {:.2f}€" .format(valor_irs)), font=("Segoe UI", 20)).place(x=879 , y=200)
    texto_ss = tk.CTkLabel(janela_solteiro_n_vale_cga_adse, text=("Taxa Social Única: {:.2f}€" .format(valor_ss)), font=("Segoe UI", 20)).place(x=879 , y=250)
    taxa_adse = tk.CTkLabel(janela_solteiro_n_vale_cga_adse, text=("Desconto ADSE: {:.2f}€" .format(valor_adse)), font=("Segoe UI", 20)).place(x=879 , y=350)
    valor_final = tk.CTkLabel(janela_solteiro_n_vale_cga_adse, text=( "Valor após descontos: {:.2f}€" .format(renumeracao_final)), font=("Segoe UI", 20), bg_color = "red").place(x=879 , y=450)

### FINAL - SAIR OU HISTORICO ###
    decidir_historico = tk.CTkLabel(janela_solteiro_n_vale_cga_adse, text=("Deseja adicionar está simulação ao histórico?" ), font=("Segoe UI", 20)).place(x=879, y=500)
    select_tabela_a = tk.CTkButton(janela_solteiro_n_vale_cga_adse, text="Sim",command=lambda: historico_ordenado(regime, situacao_fiscal, dependentes, contribuicao_social, adse, valor_alimentacao, dias_alimentacao, forma_pagamento, outros, renumeracao, valor_irs, valor_adse, valor_ss, renumeracao_final, invalidez),font=("Segoe UI", 20)).place(x=879, y=550)
    select_tabela_b = tk.CTkButton(janela_solteiro_n_vale_cga_adse, text="Não",command=lambda: reiniciar_programa(),font=("Segoe UI", 20)).place(x=1079, y=550)



def dependente_2t_s_vale_cga(janela_solteiro_n_vale):
    janela_solteiro_n_vale.withdraw()
    janela_solteiro_n_vale_cga = tk.CTkToplevel()
    janela_solteiro_n_vale_cga.geometry("1400x700")
    janela_solteiro_n_vale_cga.title("Simulação do ordenado liquido - Trabalhador Dependente - Casado - 1 Titular  - Outras contribuições")
    texto_topo = tk.CTkLabel(janela_solteiro_n_vale_cga, text="Simulação do ordenado liquido\nTrabalhador Dependente\nCasado - 1 Titular\nOutras contribuições", font=("Segoe UI", 20)).place(x=550, y=0)
    texto_adse = tk.CTkLabel(janela_solteiro_n_vale_cga, text="É beneficiário da ADSE?", font=("Segoe UI", 20)).place(x=590, y=150)
    botao_sim = tk.CTkButton(janela_solteiro_n_vale_cga, text= "Sim", command=lambda: dependente_2t_s_vale_cga_adse(janela_solteiro_n_vale_cga), font=("Segoe UI", 20)).place(x=530, y=200)
    botao_nao = tk.CTkButton(janela_solteiro_n_vale_cga, text="Não", command=lambda: dependente_2t_s_vale_cga_resultado(janela_solteiro_n_vale_cga), font=("Segoe UI", 20)).place(x=730, y=200)

def dependente_2t_s_vale_ss_resultado(janela_solteiro_n_vale_ss):
    regime = 1
    situacao_fiscal = 3
    contribuicao_social = 1
    adse = 2
    forma_pagamento = 2
    valor_irs=0
    invalidez = 2
    valor_adse=0
    janela_solteiro_n_vale_ss.withdraw()
    janela_solteiro_n_vale_ss_resultado = tk.CTkToplevel()
    janela_solteiro_n_vale_ss_resultado.geometry("1400x700")
    janela_solteiro_n_vale_ss_resultado.title( "Simulação do ordenado liquido - Trabalhador Dependente - Casado - 2 Titular  - Resultado Final")
    texto_topo = tk.CTkLabel(janela_solteiro_n_vale_ss_resultado, text="Simulação do ordenado liquido\nTrabalhador Dependente\nCasado - 2 Titular \nResultado Final", font=("Segoe UI", 20)).place(x=550, y=0)
    ordenado1 = float(renumera_log[0])
    dependentes = int(dependentes_log[0])
    alimentacao = float(alimentacao_log[0])
    dias_alimentacao = int(dias_log[0])
    outros = float(outros_log[0])
    if alimentacao <9.6:
        excedente_alimentacao = 0
    else:
        excedente_alimentacao = alimentacao-9.6
    valor_alimentacao = alimentacao*dias_alimentacao
    excedente_alimentacao_dias = excedente_alimentacao*dias_alimentacao
    renumeracao = ordenado1+excedente_alimentacao_dias+outros


    valor_irs, parcela_abater, taxa, renumeracao_liquida, parcela_dependente = casados_2t_invalidez(dependentes, renumeracao)
    if valor_irs<0:
        valor_irs = 0
    else:
        valor_irs = valor_irs
    valor_ss = renumeracao*0.11
    renumeracao_final = renumeracao - valor_ss - valor_irs + valor_alimentacao


    ### SINTESE DE CARACTERISTICAS ###

    escrever_renumeracao = tk.CTkLabel(janela_solteiro_n_vale_ss_resultado, text=("Ordenado Base: {} €" .format(ordenado1)), font=("Segoe UI", 20)).place(x=150, y=100)
    escrever_regime = tk.CTkLabel(janela_solteiro_n_vale_ss_resultado, text=("Regime: Trabalhador Dependente"), font=("Segoe UI", 20)).place(x=150, y=150)
    escrever_fiscal = tk.CTkLabel(janela_solteiro_n_vale_ss_resultado, text = ("Situação Fiscal:Casado - 2 Titular"), font=("Segoe UI", 20)).place(x=150,y=200)
    escrever_dependentes = tk.CTkLabel(janela_solteiro_n_vale_ss_resultado, text=("Dependentes: {}".format(dependentes)), font=("Segoe UI", 20)).place(x=150, y=250)
    escrever_social = tk.CTkLabel(janela_solteiro_n_vale_ss_resultado, text=("Contribuição Social: Segurança Social"), font=("Segoe UI", 20)).place(x=150, y=300)
    escrever_adse = tk.CTkLabel(janela_solteiro_n_vale_ss_resultado, text=("ADSE: Não"), font=("Segoe UI", 20)).place(x=150, y=350)
    escrever_alimentacao = tk.CTkLabel(janela_solteiro_n_vale_ss_resultado, text=("Subsidio de Alimentação: {} €".format(valor_alimentacao)), font=("Segoe UI", 20)).place(x=150, y=400)
    escrever_dias = tk.CTkLabel(janela_solteiro_n_vale_ss_resultado, text=("Dias com susbsidio de alimentação: {}".format(dias_alimentacao)), font=("Segoe UI", 20)).place(x=150, y=450)
    escrever_pagamento = tk.CTkLabel(janela_solteiro_n_vale_ss_resultado, text=("Forma de pagamento do subsidio de alimentação: Vale/Cartão de Refeição"), font=("Segoe UI", 20)).place(x=150, y=500)
    escrever_outros = tk.CTkLabel(janela_solteiro_n_vale_ss_resultado, text=("Outros subsidios tributaveis: {} €".format(outros)), font=("Segoe UI", 20)).place(x=150, y=550)
    escrever_invalidez = tk.CTkLabel(janela_solteiro_n_vale_ss_resultado, text=("Invalidez ou incapacidade: Sim"), font=("Segoe UI", 20)).place(x=150, y=600)

### APRESENTAÇÃO DOS VALORES ###
    texto_descontos = tk.CTkLabel(janela_solteiro_n_vale_ss_resultado, text=("Resumo dos descontos"), font=("Segoe UI", 20)) .place(x=879, y=150)
    texto_valor = tk.CTkLabel(janela_solteiro_n_vale_ss_resultado, text=("Valor tributável:{:.2f}€ " .format(renumeracao)), font=("Segoe UI", 20)).place(x=879 , y=300)
    texto_irs = tk.CTkLabel(janela_solteiro_n_vale_ss_resultado, text=("Retenção na fonte: {:.2f}€" .format(valor_irs)), font=("Segoe UI", 20)).place(x=879 , y=200)
    texto_ss = tk.CTkLabel(janela_solteiro_n_vale_ss_resultado, text=("Taxa Social Única: {:.2f}€" .format(valor_ss)), font=("Segoe UI", 20)).place(x=879 , y=250)
    valor_final = tk.CTkLabel(janela_solteiro_n_vale_ss_resultado, text=( "Valor após descontos: {:.2f}€" .format(renumeracao_final)), font=("Segoe UI", 20), bg_color = "red").place(x=879 , y=300)

### FINAL - SAIR OU HISTORICO ###
    decidir_historico = tk.CTkLabel(janela_solteiro_n_vale_ss_resultado, text=("Deseja adicionar está simulação ao histórico?" ), font=("Segoe UI", 20)).place(x=879, y=500)
    select_tabela_a = tk.CTkButton(janela_solteiro_n_vale_ss_resultado, text="Sim",command=lambda: historico_ordenado(regime, situacao_fiscal, dependentes, contribuicao_social, adse, valor_alimentacao, dias_alimentacao, forma_pagamento, outros, renumeracao, valor_irs, valor_adse, valor_ss, renumeracao_final, invalidez),font=("Segoe UI", 20)).place(x=879, y=550)
    select_tabela_b = tk.CTkButton(janela_solteiro_n_vale_ss_resultado, text="Não",command=lambda: reiniciar_programa(),font=("Segoe UI", 20)).place(x=1079, y=550)



def dependente_2t_s_vale_ss_adse(janela_solteiro_n_vale_ss):
    regime = 1
    situacao_fiscal = 3
    contribuicao_social = 1
    adse = 1
    forma_pagamento = 2
    valor_irs=0
    invalidez = 2
    janela_solteiro_n_vale_ss.withdraw()
    janela_solteiro_n_vale_ss_adse = tk.CTkToplevel()
    janela_solteiro_n_vale_ss_adse.geometry("1400x700")
    janela_solteiro_n_vale_ss_adse.title( "Simulação do ordenado liquido - Trabalhador Dependente - Casado - 2 Titular  - Resultado Final")
    texto_topo = tk.CTkLabel(janela_solteiro_n_vale_ss_adse, text="Simulação do ordenado liquido\nTrabalhador Dependente\nCasado - 2 Titular \nResultado Final", font=("Segoe UI", 20)).place(x=550, y=0)
    ordenado1 = float(renumera_log[0])
    dependentes = int(dependentes_log[0])
    alimentacao = float(alimentacao_log[0])
    dias_alimentacao = int(dias_log[0])
    outros = float(outros_log[0])
    if alimentacao < 9.6:
        excedente_alimentacao = 0
    else:
        excedente_alimentacao = alimentacao-9.6
    valor_alimentacao = alimentacao*dias_alimentacao
    excedente_alimentacao_dias = excedente_alimentacao*dias_alimentacao
    renumeracao = ordenado1+excedente_alimentacao_dias+outros


    valor_irs, parcela_abater, taxa, renumeracao_liquida, parcela_dependente = casados_2t_invalidez(dependentes, renumeracao)

    valor_ss = renumeracao*0.11
    valor_adse = renumeracao*0.035

    if valor_irs<0:
        valor_irs = 0
    else:
        valor_irs = valor_irs

    renumeracao_final = renumeracao - valor_adse - valor_ss - valor_irs+valor_alimentacao

    ### SINTESE DE CARACTERISTICAS ###

    escrever_renumeracao = tk.CTkLabel(janela_solteiro_n_vale_ss_adse, text=("Ordenado Base: {} €" .format(ordenado1)), font=("Segoe UI", 20)).place(x=150, y=100)
    escrever_regime = tk.CTkLabel(janela_solteiro_n_vale_ss_adse, text=("Regime: Trabalhador Dependente"), font=("Segoe UI", 20)).place(x=150, y=150)
    escrever_fiscal = tk.CTkLabel(janela_solteiro_n_vale_ss_adse, text = ("Situação Fiscal: Casado - 2 Titular"), font=("Segoe UI", 20)).place(x=150,y=200)
    escrever_dependentes = tk.CTkLabel(janela_solteiro_n_vale_ss_adse, text=("Dependentes: {}".format(dependentes)), font=("Segoe UI", 20)).place(x=150, y=250)
    escrever_social = tk.CTkLabel(janela_solteiro_n_vale_ss_adse, text=("Contribuição Social: Segurança Social"), font=("Segoe UI", 20)).place(x=150, y=300)
    escrever_adse = tk.CTkLabel(janela_solteiro_n_vale_ss_adse, text=("ADSE: Sim"), font=("Segoe UI", 20)).place(x=150, y=350)
    escrever_alimentacao = tk.CTkLabel(janela_solteiro_n_vale_ss_adse, text=("Subsidio de Alimentação: {} €".format(valor_alimentacao)), font=("Segoe UI", 20)).place(x=150, y=400)
    escrever_dias = tk.CTkLabel(janela_solteiro_n_vale_ss_adse, text=("Dias com susbsidio de alimentação: {}".format(dias_alimentacao)), font=("Segoe UI", 20)).place(x=150, y=450)
    escrever_pagamento = tk.CTkLabel(janela_solteiro_n_vale_ss_adse, text=("Forma de pagamento do subsidio de alimentação: Cartão/Vale de alimentação"), font=("Segoe UI", 20)).place(x=150, y=500)
    escrever_outros = tk.CTkLabel(janela_solteiro_n_vale_ss_adse, text=("Outros subsidios tributaveis: {} €".format(outros)), font=("Segoe UI", 20)).place(x=150, y=550)
    escrever_invalidez = tk.CTkLabel(janela_solteiro_n_vale_ss_adse, text=("Invalidez ou incapacidade: Sim"), font=("Segoe UI", 20)).place(x=150, y=600)

### APRESENTAÇÃO DOS VALORES ###
    texto_descontos = tk.CTkLabel(janela_solteiro_n_vale_ss_adse, text=("Resumo dos descontos"), font=("Segoe UI", 20)) .place(x=879, y=150)
    texto_valor = tk.CTkLabel(janela_solteiro_n_vale_ss_adse, text=("Valor tributável:{:.2f}€ " .format(renumeracao)), font=("Segoe UI", 20)).place(x=879 , y=300)
    texto_irs = tk.CTkLabel(janela_solteiro_n_vale_ss_adse, text=("Retenção na fonte: {:.2f}€" .format(valor_irs)), font=("Segoe UI", 20)).place(x=879 , y=200)
    texto_ss = tk.CTkLabel(janela_solteiro_n_vale_ss_adse, text=("Taxa Social Única: {:.2f}€" .format(valor_ss)), font=("Segoe UI", 20)).place(x=879 , y=250)
    taxa_adse = tk.CTkLabel(janela_solteiro_n_vale_ss_adse, text=("Desconto ADSE: {:.2f}€" .format(valor_adse)), font=("Segoe UI", 20)).place(x=879 , y=350)
    valor_final = tk.CTkLabel(janela_solteiro_n_vale_ss_adse, text=( "Valor após descontos: {:.2f}€" .format(renumeracao_final)), font=("Segoe UI", 20), bg_color = "red").place(x=879 , y=450)

### FINAL - SAIR OU HISTORICO ###
    decidir_historico = tk.CTkLabel(janela_solteiro_n_vale_ss_adse, text=("Deseja adicionar está simulação ao histórico?" ), font=("Segoe UI", 20)).place(x=879, y=500)
    select_tabela_a = tk.CTkButton(janela_solteiro_n_vale_ss_adse, text="Sim",command=lambda: historico_ordenado(regime, situacao_fiscal, dependentes, contribuicao_social, adse, valor_alimentacao, dias_alimentacao, forma_pagamento, outros, renumeracao, valor_irs, valor_adse, valor_ss, renumeracao_final, invalidez),font=("Segoe UI", 20)).place(x=879, y=550)
    select_tabela_b = tk.CTkButton(janela_solteiro_n_vale_ss_adse, text="Não",command=lambda: reiniciar_programa(),font=("Segoe UI", 20)).place(x=1079, y=550)



def dependente_2t_s_vale_ss(janela_solteiro_n_vale):
    janela_solteiro_n_vale.withdraw()
    janela_solteiro_n_vale_ss = tk.CTkToplevel()
    janela_solteiro_n_vale_ss.geometry("1400x700")
    janela_solteiro_n_vale_ss.title("Simulação do ordenado liquido - Trabalhador Dependente - Casado - 2 Titular  - Outras contribuições")
    texto_topo = tk.CTkLabel(janela_solteiro_n_vale_ss, text="Simulação do ordenado liquido\nTrabalhador Dependente\nCasado - 2 Titular\nOutras contribuições", font=("Segoe UI", 20)).place(x=550, y=0)
    texto_adse = tk.CTkLabel(janela_solteiro_n_vale_ss, text="É beneficiário da ADSE?", font=("Segoe UI", 20)).place(x=590, y=150)
    botao_sim = tk.CTkButton(janela_solteiro_n_vale_ss, text= "Sim", command=lambda: dependente_2t_s_vale_ss_adse(janela_solteiro_n_vale_ss), font=("Segoe UI", 20)).place(x=530, y=200)
    botao_nao = tk.CTkButton(janela_solteiro_n_vale_ss, text="Não", command=lambda: dependente_2t_s_vale_ss_resultado(janela_solteiro_n_vale_ss), font=("Segoe UI", 20)).place(x=730, y=200)




def dependente_2t_s_vale(janela_solteiro_n, pedir_outros, pedir_alimentacao, pedir_dias):
    alimentacao = float(pedir_alimentacao.get())
    alimentacao_log.append(alimentacao)
    dias = float(pedir_dias.get())
    dias_log.append(dias)
    outros = float(pedir_outros.get())
    outros_log.append(outros)
    janela_solteiro_n.withdraw()
    janela_solteiro_n_vale = tk.CTkToplevel()
    janela_solteiro_n_vale.geometry("1400x700")
    janela_solteiro_n_vale.title("Simulação do ordenado liquido - Trabalhador Dependente - Casado - 2 Titular  - Outras contribuições")
    texto_topo = tk.CTkLabel(janela_solteiro_n_vale, text="Simulação do ordenado liquido\nTrabalhador Dependente\nCasado - 2 Titular \nOutras contribuições", font=("Segoe UI", 20)).place(x=550, y=0)
    texto_forma = tk.CTkLabel(janela_solteiro_n_vale, text = "Selecione a sua forma de contribuição social", font=("Segoe UI", 20)).place(x=510, y=150)
    botao_ss = tk.CTkButton(janela_solteiro_n_vale, text="Segurança Social", command=lambda:dependente_2t_s_vale_ss(janela_solteiro_n_vale), font=("Segoe UI", 20)) .place(x=606, y=200)
    botao_cga = tk.CTkButton(janela_solteiro_n_vale, text="Caixa Geral de Aposentações", command=lambda: dependente_2t_s_vale_cga(janela_solteiro_n_vale),  font=("Segoe UI",20)) .place(x=560, y=250)



def dependente_2t_s_dinheiro_ss_resultado(janela_solteiro_n_dinheiro_ss):
    regime = 1
    situacao_fiscal = 3
    contribuicao_social = 1
    adse = 2
    forma_pagamento = 1
    valor_irs=0
    invalidez = 2
    valor_adse=0
    janela_solteiro_n_dinheiro_ss.withdraw()
    janela_solteiro_n_dinheiro_ss_resultado = tk.CTkToplevel()
    janela_solteiro_n_dinheiro_ss_resultado.geometry("1400x700")
    janela_solteiro_n_dinheiro_ss_resultado.title( "Simulação do ordenado liquido - Trabalhador Dependente - Casado - 2 Titular  - Resultado Final")
    texto_topo = tk.CTkLabel(janela_solteiro_n_dinheiro_ss_resultado, text="Simulação do ordenado liquido\nTrabalhador Dependente\nCasado - 2 Titular \nResultado Final", font=("Segoe UI", 20)).place(x=550, y=0)
    ordenado1 = float(renumera_log[0])
    dependentes = int(dependentes_log[0])
    alimentacao = float(alimentacao_log[0])
    dias_alimentacao = int(dias_log[0])
    outros = float(outros_log[0])
    if alimentacao < 6:
        excedente_alimentacao = 0
    else:
        excedente_alimentacao = alimentacao-6
    valor_alimentacao = alimentacao*dias_alimentacao
    excedente_alimentacao_dias = excedente_alimentacao*dias_alimentacao
    renumeracao = ordenado1+excedente_alimentacao_dias+outros

    valor_irs, parcela_abater, taxa, renumeracao_liquida, parcela_dependente = casados_2t_invalidez(dependentes, renumeracao)
    if valor_irs<0:
        valor_irs = 0
    else:
        valor_irs = valor_irs
    valor_ss = renumeracao*0.11
    renumeracao_final = renumeracao - valor_ss - valor_irs + valor_alimentacao


    ### SINTESE DE CARACTERISTICAS ###

    escrever_renumeracao = tk.CTkLabel(janela_solteiro_n_dinheiro_ss_resultado, text=("Ordenado Base: {} €" .format(ordenado1)), font=("Segoe UI", 20)).place(x=150, y=100)
    escrever_regime = tk.CTkLabel(janela_solteiro_n_dinheiro_ss_resultado, text=("Regime: Trabalhador Dependente"), font=("Segoe UI", 20)).place(x=150, y=150)
    escrever_fiscal = tk.CTkLabel(janela_solteiro_n_dinheiro_ss_resultado, text = ("Situação Fiscal: Casado - 2 Titular"), font=("Segoe UI", 20)).place(x=150,y=200)
    escrever_dependentes = tk.CTkLabel(janela_solteiro_n_dinheiro_ss_resultado, text=("Dependentes: {}".format(dependentes)), font=("Segoe UI", 20)).place(x=150, y=250)
    escrever_social = tk.CTkLabel(janela_solteiro_n_dinheiro_ss_resultado, text=("Contribuição Social: Segurança Social"), font=("Segoe UI", 20)).place(x=150, y=300)
    escrever_adse = tk.CTkLabel(janela_solteiro_n_dinheiro_ss_resultado, text=("ADSE: Não"), font=("Segoe UI", 20)).place(x=150, y=350)
    escrever_alimentacao = tk.CTkLabel(janela_solteiro_n_dinheiro_ss_resultado, text=("Subsidio de Alimentação: {} €".format(valor_alimentacao)), font=("Segoe UI", 20)).place(x=150, y=400)
    escrever_dias = tk.CTkLabel(janela_solteiro_n_dinheiro_ss_resultado, text=("Dias com susbsidio de alimentação: {}".format(dias_alimentacao)), font=("Segoe UI", 20)).place(x=150, y=450)
    escrever_pagamento = tk.CTkLabel(janela_solteiro_n_dinheiro_ss_resultado, text=("Forma de pagamento do subsidio de alimentação: Dinheiro"), font=("Segoe UI", 20)).place(x=150, y=500)
    escrever_outros = tk.CTkLabel(janela_solteiro_n_dinheiro_ss_resultado, text=("Outros subsidios tributaveis: {} €".format(outros)), font=("Segoe UI", 20)).place(x=150, y=550)
    escrever_invalidez = tk.CTkLabel(janela_solteiro_n_dinheiro_ss_resultado, text=("Invalidez ou incapacidade: Sim"), font=("Segoe UI", 20)).place(x=150, y=600)

### APRESENTAÇÃO DOS VALORES ###
    texto_descontos = tk.CTkLabel(janela_solteiro_n_dinheiro_ss_resultado, text=("Resumo dos descontos"), font=("Segoe UI", 20)) .place(x=879, y=150)
    texto_valor = tk.CTkLabel(janela_solteiro_n_dinheiro_ss_resultado, text=("Valor tributável:{:.2f}€ " .format(renumeracao)), font=("Segoe UI", 20)).place(x=879 , y=300)
    texto_irs = tk.CTkLabel(janela_solteiro_n_dinheiro_ss_resultado, text=("Retenção na fonte: {:.2f}€" .format(valor_irs)), font=("Segoe UI", 20)).place(x=879 , y=200)
    texto_ss = tk.CTkLabel(janela_solteiro_n_dinheiro_ss_resultado, text=("Taxa Social Única: {:.2f}€" .format(valor_ss)), font=("Segoe UI", 20)).place(x=879 , y=250)
    valor_final = tk.CTkLabel(janela_solteiro_n_dinheiro_ss_resultado, text=( "Valor após descontos: {:.2f}€" .format(renumeracao_final)), font=("Segoe UI", 20), bg_color = "red").place(x=879 , y=300)

### FINAL - SAIR OU HISTORICO ###
    decidir_historico = tk.CTkLabel(janela_solteiro_n_dinheiro_ss_resultado, text=("Deseja adicionar está simulação ao histórico?" ), font=("Segoe UI", 20)).place(x=879, y=500)
    select_tabela_a = tk.CTkButton(janela_solteiro_n_dinheiro_ss_resultado, text="Sim",command=lambda: historico_ordenado(regime, situacao_fiscal, dependentes, contribuicao_social, adse, valor_alimentacao, dias_alimentacao, forma_pagamento, outros, renumeracao, valor_irs, valor_adse, valor_ss, renumeracao_final, invalidez),font=("Segoe UI", 20)).place(x=879, y=550)
    select_tabela_b = tk.CTkButton(janela_solteiro_n_dinheiro_ss_resultado, text="Não",command=lambda: reiniciar_programa(),font=("Segoe UI", 20)).place(x=1079, y=550)



def dependente_2t_s_dinheiro_ss_adse(janela_solteiro_n_dinheiro_ss):
    regime = 1
    situacao_fiscal = 3
    contribuicao_social = 1
    adse = 1
    forma_pagamento = 1
    valor_irs=0
    invalidez = 2
    janela_solteiro_n_dinheiro_ss.withdraw()
    janela_solteiro_n_dinheiro_ss_adse = tk.CTkToplevel()
    janela_solteiro_n_dinheiro_ss_adse.geometry("1400x700")
    janela_solteiro_n_dinheiro_ss_adse.title( "Simulação do ordenado liquido - Trabalhador Dependente - Casado - 2 Titular  - Resultado Final")
    texto_topo = tk.CTkLabel(janela_solteiro_n_dinheiro_ss_adse, text="Simulação do ordenado liquido\nTrabalhador Dependente\nCasado - 2 Titular \nResultado Final", font=("Segoe UI", 20)).place(x=550, y=0)
    ordenado1 = float(renumera_log[0])
    dependentes = int(dependentes_log[0])
    alimentacao = float(alimentacao_log[0])
    dias_alimentacao = int(dias_log[0])
    outros = float(outros_log[0])
    if alimentacao < 6:
        excedente_alimentacao = 0
    else:
        excedente_alimentacao = alimentacao-6
    valor_alimentacao = alimentacao*dias_alimentacao
    excedente_alimentacao_dias = excedente_alimentacao*dias_alimentacao
    renumeracao = ordenado1+excedente_alimentacao_dias+outros


    valor_irs, parcela_abater, taxa, renumeracao_liquida, parcela_dependente = casados_2t_invalidez(dependentes, renumeracao)

    valor_ss = renumeracao*0.11
    valor_adse = renumeracao*0.035

    if valor_irs<0:
        valor_irs = 0
    else:
        valor_irs = valor_irs

    renumeracao_final = renumeracao - valor_adse - valor_ss - valor_irs+valor_alimentacao

    ### SINTESE DE CARACTERISTICAS ###

    escrever_renumeracao = tk.CTkLabel(janela_solteiro_n_dinheiro_ss_adse, text=("Ordenado Base: {} €" .format(ordenado1)), font=("Segoe UI", 20)).place(x=150, y=100)
    escrever_regime = tk.CTkLabel(janela_solteiro_n_dinheiro_ss_adse, text=("Regime: Trabalhador Dependente"), font=("Segoe UI", 20)).place(x=150, y=150)
    escrever_fiscal = tk.CTkLabel(janela_solteiro_n_dinheiro_ss_adse, text = ("Situação Fiscal: Casado - 2 Titular"), font=("Segoe UI", 20)).place(x=150,y=200)
    escrever_dependentes = tk.CTkLabel(janela_solteiro_n_dinheiro_ss_adse, text=("Dependentes: {}".format(dependentes)), font=("Segoe UI", 20)).place(x=150, y=250)
    escrever_social = tk.CTkLabel(janela_solteiro_n_dinheiro_ss_adse, text=("Contribuição Social: Segurança Social"), font=("Segoe UI", 20)).place(x=150, y=300)
    escrever_adse = tk.CTkLabel(janela_solteiro_n_dinheiro_ss_adse, text=("ADSE: Sim"), font=("Segoe UI", 20)).place(x=150, y=350)
    escrever_alimentacao = tk.CTkLabel(janela_solteiro_n_dinheiro_ss_adse, text=("Subsidio de Alimentação: {} €".format(valor_alimentacao)), font=("Segoe UI", 20)).place(x=150, y=400)
    escrever_dias = tk.CTkLabel(janela_solteiro_n_dinheiro_ss_adse, text=("Dias com susbsidio de alimentação: {}".format(dias_alimentacao)), font=("Segoe UI", 20)).place(x=150, y=450)
    escrever_pagamento = tk.CTkLabel(janela_solteiro_n_dinheiro_ss_adse, text=("Forma de pagamento do subsidio de alimentação: Dinheiro"), font=("Segoe UI", 20)).place(x=150, y=500)
    escrever_outros = tk.CTkLabel(janela_solteiro_n_dinheiro_ss_adse, text=("Outros subsidios tributaveis: {} €".format(outros)), font=("Segoe UI", 20)).place(x=150, y=550)
    escrever_invalidez = tk.CTkLabel(janela_solteiro_n_dinheiro_ss_adse, text=("Invalidez ou incapacidade: Sim"), font=("Segoe UI", 20)).place(x=150, y=600)

### APRESENTAÇÃO DOS VALORES ###
    texto_descontos = tk.CTkLabel(janela_solteiro_n_dinheiro_ss_adse, text=("Resumo dos descontos"), font=("Segoe UI", 20)) .place(x=879, y=150)
    texto_valor = tk.CTkLabel(janela_solteiro_n_dinheiro_ss_adse, text=("Valor tributável:{:.2f}€ " .format(renumeracao)), font=("Segoe UI", 20)).place(x=879 , y=300)
    texto_irs = tk.CTkLabel(janela_solteiro_n_dinheiro_ss_adse, text=("Retenção na fonte: {:.2f}€" .format(valor_irs)), font=("Segoe UI", 20)).place(x=879 , y=200)
    texto_ss = tk.CTkLabel(janela_solteiro_n_dinheiro_ss_adse, text=("Taxa Social Única: {:.2f}€" .format(valor_ss)), font=("Segoe UI", 20)).place(x=879 , y=250)
    taxa_adse = tk.CTkLabel(janela_solteiro_n_dinheiro_ss_adse, text=("Desconto ADSE: {:.2f}€" .format(valor_adse)), font=("Segoe UI", 20)).place(x=879 , y=350)
    valor_final = tk.CTkLabel(janela_solteiro_n_dinheiro_ss_adse, text=( "Valor após descontos: {:.2f}€" .format(renumeracao_final)), font=("Segoe UI", 20), bg_color = "red").place(x=879 , y=450)

### FINAL - SAIR OU HISTORICO ###
    decidir_historico = tk.CTkLabel(janela_solteiro_n_dinheiro_ss_adse, text=("Deseja adicionar está simulação ao histórico?" ), font=("Segoe UI", 20)).place(x=879, y=500)
    select_tabela_a = tk.CTkButton(janela_solteiro_n_dinheiro_ss_adse, text="Sim",command=lambda: historico_ordenado(regime, situacao_fiscal, dependentes, contribuicao_social, adse, valor_alimentacao, dias_alimentacao, forma_pagamento, outros, renumeracao, valor_irs, valor_adse, valor_ss, renumeracao_final, invalidez),font=("Segoe UI", 20)).place(x=879, y=550)
    select_tabela_b = tk.CTkButton(janela_solteiro_n_dinheiro_ss_adse, text="Não",command=lambda: reiniciar_programa(),font=("Segoe UI", 20)).place(x=1079, y=550)



def dependente_2t_s_dinheiro_ss(janela_solteiro_n_dinheiro):
    janela_solteiro_n_dinheiro.withdraw()
    janela_solteiro_n_dinheiro_ss = tk.CTkToplevel()
    janela_solteiro_n_dinheiro_ss.geometry("1400x700")
    janela_solteiro_n_dinheiro_ss.title("Simulação do ordenado liquido - Trabalhador Dependente - Casado - 2 Titular  - Outras contribuições")
    texto_topo = tk.CTkLabel(janela_solteiro_n_dinheiro_ss, text="Simulação do ordenado liquido\nTrabalhador Dependente\nCasado - 2 Titular \nOutras contribuições", font=("Segoe UI", 20)).place(x=550, y=0)
    texto_adse = tk.CTkLabel(janela_solteiro_n_dinheiro_ss, text="É beneficiário da ADSE?", font=("Segoe UI", 20)).place(x=590, y=150)
    botao_sim = tk.CTkButton(janela_solteiro_n_dinheiro_ss, text= "Sim", command=lambda: dependente_2t_s_dinheiro_ss_adse(janela_solteiro_n_dinheiro_ss), font=("Segoe UI", 20)).place(x=530, y=200)
    botao_nao = tk.CTkButton(janela_solteiro_n_dinheiro_ss, text="Não", command=lambda: dependente_2t_s_dinheiro_ss_resultado(janela_solteiro_n_dinheiro_ss), font=("Segoe UI", 20)).place(x=730, y=200)


def dependente_2t_s_dinheiro(janela_solteiro_n, pedir_outros, pedir_alimentacao, pedir_dias):
    alimentacao = float(pedir_alimentacao.get())
    alimentacao_log.append(alimentacao)
    dias = float(pedir_dias.get())
    dias_log.append(dias)
    outros = float(pedir_outros.get())
    outros_log.append(outros)
    janela_solteiro_n.withdraw()
    janela_solteiro_n_dinheiro = tk.CTkToplevel()
    janela_solteiro_n_dinheiro.geometry("1400x700")
    janela_solteiro_n_dinheiro.title("Simulação do ordenado liquido - Trabalhador Dependente - Casado - 1 Titular  - Outras contribuições")
    texto_topo = tk.CTkLabel(janela_solteiro_n_dinheiro, text="Simulação do ordenado liquido\nTrabalhador Dependente\nCasado - 1 Titular \nOutras contribuições", font=("Segoe UI", 20)).place(x=550, y=0)
    texto_forma = tk.CTkLabel(janela_solteiro_n_dinheiro, text = "Selecione a sua forma de contribuição social", font=("Segoe UI", 20)).place(x=510, y=150)
    botao_ss = tk.CTkButton(janela_solteiro_n_dinheiro, text="Segurança Social", command=lambda:dependente_2t_s_dinheiro_ss(janela_solteiro_n_dinheiro), font=("Segoe UI", 20)) .place(x=606, y=200)
    botao_cga = tk.CTkButton(janela_solteiro_n_dinheiro, text="Caixa Geral de Aposentações", command=lambda: dependente_2t_s_dinheiro_cga(janela_solteiro_n_dinheiro),  font=("Segoe UI",20)) .place(x=560, y=250)


def dependente_2t_s_dinheiro_cga_resultado(janela_solteiro_n_dinheiro_cga):
    regime = 1
    situacao_fiscal = 3
    contribuicao_social = 2
    adse = 2
    forma_pagamento = 1
    valor_irs=0
    invalidez = 2
    valor_adse=0
    janela_solteiro_n_dinheiro_cga.withdraw()
    janela_solteiro_n_dinheiro_cga_resultado = tk.CTkToplevel()
    janela_solteiro_n_dinheiro_cga_resultado.geometry("1400x700")
    janela_solteiro_n_dinheiro_cga_resultado.title( "Simulação do ordenado liquido - Trabalhador Dependente - Casado - 2 Titulares  - Resultado Final")
    texto_topo = tk.CTkLabel(janela_solteiro_n_dinheiro_cga_resultado, text="Simulação do ordenado liquido\nTrabalhador Dependente\nCasado - 2 Titulares \nResultado Final", font=("Segoe UI", 20)).place(x=550, y=0)
    ordenado1 = float(renumera_log[0])
    dependentes = int(dependentes_log[0])
    alimentacao = float(alimentacao_log[0])
    dias_alimentacao = int(dias_log[0])
    outros = float(outros_log[0])
    if alimentacao <6:
        excedente_alimentacao = 0
    else:
        excedente_alimentacao = alimentacao-6
    valor_alimentacao = alimentacao*dias_alimentacao
    excedente_alimentacao_dias = excedente_alimentacao*dias_alimentacao
    renumeracao = ordenado1+excedente_alimentacao_dias+outros


    valor_irs, parcela_abater, taxa, renumeracao_liquida, parcela_dependente = casados_2t_invalidez(dependentes, renumeracao)
    if valor_irs<0:
        valor_irs = 0
    else:
        valor_irs = valor_irs
    valor_ss = renumeracao*0.11
    renumeracao_final = renumeracao - valor_ss - valor_irs + valor_alimentacao


    ### SINTESE DE CARACTERISTICAS ###

    escrever_renumeracao = tk.CTkLabel(janela_solteiro_n_dinheiro_cga_resultado, text=("Ordenado Base: {} €" .format(ordenado1)), font=("Segoe UI", 20)).place(x=150, y=100)
    escrever_regime = tk.CTkLabel(janela_solteiro_n_dinheiro_cga_resultado, text=("Regime: Trabalhador Dependente"), font=("Segoe UI", 20)).place(x=150, y=150)
    escrever_fiscal = tk.CTkLabel(janela_solteiro_n_dinheiro_cga_resultado, text = ("Situação Fiscal: Casado - 2 Titular"), font=("Segoe UI", 20)).place(x=150,y=200)
    escrever_dependentes = tk.CTkLabel(janela_solteiro_n_dinheiro_cga_resultado, text=("Dependentes: {}".format(dependentes)), font=("Segoe UI", 20)).place(x=150, y=250)
    escrever_social = tk.CTkLabel(janela_solteiro_n_dinheiro_cga_resultado, text=("Contribuição Social: Caixa Geral de Aposentações"), font=("Segoe UI", 20)).place(x=150, y=300)
    escrever_adse = tk.CTkLabel(janela_solteiro_n_dinheiro_cga_resultado, text=("ADSE: Não"), font=("Segoe UI", 20)).place(x=150, y=350)
    escrever_alimentacao = tk.CTkLabel(janela_solteiro_n_dinheiro_cga_resultado, text=("Subsidio de Alimentação: {} €".format(valor_alimentacao)), font=("Segoe UI", 20)).place(x=150, y=400)
    escrever_dias = tk.CTkLabel(janela_solteiro_n_dinheiro_cga_resultado, text=("Dias com susbsidio de alimentação: {}".format(dias_alimentacao)), font=("Segoe UI", 20)).place(x=150, y=450)
    escrever_pagamento = tk.CTkLabel(janela_solteiro_n_dinheiro_cga_resultado, text=("Forma de pagamento do subsidio de alimentação: Dinheiro"), font=("Segoe UI", 20)).place(x=150, y=500)
    escrever_outros = tk.CTkLabel(janela_solteiro_n_dinheiro_cga_resultado, text=("Outros subsidios tributaveis: {} €".format(outros)), font=("Segoe UI", 20)).place(x=150, y=550)
    escrever_invalidez = tk.CTkLabel(janela_solteiro_n_dinheiro_cga_resultado, text=("Invalidez ou incapacidade: Sim"), font=("Segoe UI", 20)).place(x=150, y=600)

### APRESENTAÇÃO DOS VALORES ###
    texto_descontos = tk.CTkLabel(janela_solteiro_n_dinheiro_cga_resultado, text=("Resumo dos descontos"), font=("Segoe UI", 20)) .place(x=879, y=150)
    texto_valor = tk.CTkLabel(janela_solteiro_n_dinheiro_cga_resultado, text=("Valor tributável:{:.2f}€ " .format(renumeracao)), font=("Segoe UI", 20)).place(x=879 , y=300)
    texto_irs = tk.CTkLabel(janela_solteiro_n_dinheiro_cga_resultado, text=("Retenção na fonte: {:.2f}€" .format(valor_irs)), font=("Segoe UI", 20)).place(x=879 , y=200)
    texto_ss = tk.CTkLabel(janela_solteiro_n_dinheiro_cga_resultado, text=("Taxa Social Única: {:.2f}€" .format(valor_ss)), font=("Segoe UI", 20)).place(x=879 , y=250)
    valor_final = tk.CTkLabel(janela_solteiro_n_dinheiro_cga_resultado, text=( "Valor após descontos: {:.2f}€" .format(renumeracao_final)), font=("Segoe UI", 20), bg_color = "red").place(x=879 , y=300)

### FINAL - SAIR OU HISTORICO ###
    decidir_historico = tk.CTkLabel(janela_solteiro_n_dinheiro_cga_resultado, text=("Deseja adicionar está simulação ao histórico?" ), font=("Segoe UI", 20)).place(x=879, y=500)
    select_tabela_a = tk.CTkButton(janela_solteiro_n_dinheiro_cga_resultado, text="Sim",command=lambda: historico_ordenado(regime, situacao_fiscal, dependentes, contribuicao_social, adse, valor_alimentacao, dias_alimentacao, forma_pagamento, outros, renumeracao, valor_irs, valor_adse, valor_ss, renumeracao_final, invalidez),font=("Segoe UI", 20)).place(x=879, y=550)
    select_tabela_b = tk.CTkButton(janela_solteiro_n_dinheiro_cga_resultado, text="Não",command=lambda: reiniciar_programa(),font=("Segoe UI", 20)).place(x=1079, y=550)


def dependente_2t_s_dinheiro_cga_adse(janela_solteiro_n_dinheiro_cga):
    regime = 1
    situacao_fiscal =3
    contribuicao_social = 2
    adse = 1
    forma_pagamento = 1
    valor_irs=0
    invalidez = 2
    janela_solteiro_n_dinheiro_cga.withdraw()
    janela_solteiro_n_dinheiro_cga_adse = tk.CTkToplevel()
    janela_solteiro_n_dinheiro_cga_adse.geometry("1400x700")
    janela_solteiro_n_dinheiro_cga_adse.title( "Simulação do ordenado liquido - Trabalhador Dependente - Casado - 2 Titular - Resultado Final")
    texto_topo = tk.CTkLabel(janela_solteiro_n_dinheiro_cga_adse, text="Simulação do ordenado liquido\nTrabalhador Dependente\nCasado - 2 Titular \nResultado Final", font=("Segoe UI", 20)).place(x=550, y=0)
    ordenado1 = float(renumera_log[0])
    dependentes = int(dependentes_log[0])
    alimentacao = float(alimentacao_log[0])
    dias_alimentacao = int(dias_log[0])
    outros = float(outros_log[0])
    if alimentacao < 6:
        excedente_alimentacao = 0
    else:
        excedente_alimentacao = alimentacao-6
    valor_alimentacao = alimentacao*dias_alimentacao
    excedente_alimentacao_dias = excedente_alimentacao*dias_alimentacao
    renumeracao = ordenado1+excedente_alimentacao_dias+outros


    valor_irs, parcela_abater, taxa, renumeracao_liquida, parcela_dependente = casados_2t_invalidez (dependentes, renumeracao)

    valor_ss = renumeracao*0.11
    valor_adse = renumeracao*0.035
    if valor_irs<0:
        valor_irs = 0
    else:
        valor_irs = valor_irs
    renumeracao_final = renumeracao - valor_adse - valor_ss - valor_irs+valor_alimentacao

    ### SINTESE DE CARACTERISTICAS ###

    escrever_renumeracao = tk.CTkLabel(janela_solteiro_n_dinheiro_cga_adse, text=("Ordenado Base: {} €" .format(ordenado1)), font=("Segoe UI", 20)).place(x=150, y=100)
    escrever_regime = tk.CTkLabel(janela_solteiro_n_dinheiro_cga_adse, text=("Regime: Trabalhador Dependente"), font=("Segoe UI", 20)).place(x=150, y=150)
    escrever_fiscal = tk.CTkLabel(janela_solteiro_n_dinheiro_cga_adse, text = ("Situação Fiscal: Casado - 2 Titular"), font=("Segoe UI", 20)).place(x=150,y=200)
    escrever_dependentes = tk.CTkLabel(janela_solteiro_n_dinheiro_cga_adse, text=("Dependentes: {}".format(dependentes)), font=("Segoe UI", 20)).place(x=150, y=250)
    escrever_social = tk.CTkLabel(janela_solteiro_n_dinheiro_cga_adse, text=("Contribuição Social: Caixa Geral de Aposentações"), font=("Segoe UI", 20)).place(x=150, y=300)
    escrever_adse = tk.CTkLabel(janela_solteiro_n_dinheiro_cga_adse, text=("ADSE: Sim"), font=("Segoe UI", 20)).place(x=150, y=350)
    escrever_alimentacao = tk.CTkLabel(janela_solteiro_n_dinheiro_cga_adse, text=("Subsidio de Alimentação: {} €".format(valor_alimentacao)), font=("Segoe UI", 20)).place(x=150, y=400)
    escrever_dias = tk.CTkLabel(janela_solteiro_n_dinheiro_cga_adse, text=("Dias com susbsidio de alimentação: {}".format(dias_alimentacao)), font=("Segoe UI", 20)).place(x=150, y=450)
    escrever_pagamento = tk.CTkLabel(janela_solteiro_n_dinheiro_cga_adse, text=("Forma de pagamento do subsidio de alimentação: Dinheiro"), font=("Segoe UI", 20)).place(x=150, y=500)
    escrever_outros = tk.CTkLabel(janela_solteiro_n_dinheiro_cga_adse, text=("Outros subsidios tributaveis: {} €".format(outros)), font=("Segoe UI", 20)).place(x=150, y=550)
    escrever_invalidez = tk.CTkLabel(janela_solteiro_n_dinheiro_cga_adse, text=("Invalidez ou incapacidade: Sim"), font=("Segoe UI", 20)).place(x=150, y=600)

### APRESENTAÇÃO DOS VALORES ###
    texto_descontos = tk.CTkLabel(janela_solteiro_n_dinheiro_cga_adse, text=("Resumo dos descontos"), font=("Segoe UI", 20)) .place(x=879, y=150)
    texto_valor = tk.CTkLabel(janela_solteiro_n_dinheiro_cga_adse, text=("Valor tributável:{:.2f}€ " .format(renumeracao)), font=("Segoe UI", 20)).place(x=879 , y=300)
    texto_irs = tk.CTkLabel(janela_solteiro_n_dinheiro_cga_adse, text=("Retenção na fonte: {:.2f}€" .format(valor_irs)), font=("Segoe UI", 20)).place(x=879 , y=200)
    texto_ss = tk.CTkLabel(janela_solteiro_n_dinheiro_cga_adse, text=("Taxa Social Única: {:.2f}€" .format(valor_ss)), font=("Segoe UI", 20)).place(x=879 , y=250)
    taxa_adse = tk.CTkLabel(janela_solteiro_n_dinheiro_cga_adse, text=("Desconto ADSE: {:.2f}€" .format(valor_adse)), font=("Segoe UI", 20)).place(x=879 , y=350)
    valor_final = tk.CTkLabel(janela_solteiro_n_dinheiro_cga_adse, text=( "Valor após descontos: {:.2f}€" .format(renumeracao_final)), font=("Segoe UI", 20), bg_color = "red").place(x=879 , y=450)

### FINAL - SAIR OU HISTORICO ###
    decidir_historico = tk.CTkLabel(janela_solteiro_n_dinheiro_cga_adse, text=("Deseja adicionar está simulação ao histórico?" ), font=("Segoe UI", 20)).place(x=879, y=500)
    select_tabela_a = tk.CTkButton(janela_solteiro_n_dinheiro_cga_adse, text="Sim",command=lambda: historico_ordenado(regime, situacao_fiscal, dependentes, contribuicao_social, adse, valor_alimentacao, dias_alimentacao, forma_pagamento, outros, renumeracao, valor_irs, valor_adse, valor_ss, renumeracao_final, invalidez),font=("Segoe UI", 20)).place(x=879, y=550)
    select_tabela_b = tk.CTkButton(janela_solteiro_n_dinheiro_cga_adse, text="Não",command=lambda: reiniciar_programa(),font=("Segoe UI", 20)).place(x=1079, y=550)

def dependente_2t_s_dinheiro_cga(janela_solteiro_n_dinheiro):
    janela_solteiro_n_dinheiro.withdraw()
    janela_solteiro_n_dinheiro_cga = tk.CTkToplevel()
    janela_solteiro_n_dinheiro_cga.geometry("1400x700")
    janela_solteiro_n_dinheiro_cga.title("Simulação do ordenado liquido - Trabalhador Dependente - Casado - 2 Titular - Outras contribuições")
    texto_topo = tk.CTkLabel(janela_solteiro_n_dinheiro_cga, text="Simulação do ordenado liquido\nTrabalhador Dependente\nCasado - 2 Titular\nOutras contribuições", font=("Segoe UI", 20)).place(x=550, y=0)
    texto_adse = tk.CTkLabel(janela_solteiro_n_dinheiro_cga, text="É beneficiário da ADSE?", font=("Segoe UI", 20)).place(x=590, y=150)
    botao_sim = tk.CTkButton(janela_solteiro_n_dinheiro_cga, text= "Sim", command=lambda: dependente_1t_s_dinheiro_cga_adse(janela_solteiro_n_dinheiro_cga), font=("Segoe UI", 20)).place(x=530, y=200)
    botao_nao = tk.CTkButton(janela_solteiro_n_dinheiro_cga, text="Não", command=lambda: dependente_1t_s_dinheiro_cga_resultado(janela_solteiro_n_dinheiro_cga), font=("Segoe UI", 20)).place(x=730, y=200)


def dependente_2t_s_dinheiro_ss_resultado(janela_solteiro_n_dinheiro_ss):
    regime = 1
    situacao_fiscal = 3
    contribuicao_social = 1
    adse = 2
    forma_pagamento = 1
    valor_irs=0
    invalidez = 2
    valor_adse=0
    janela_solteiro_n_dinheiro_ss.withdraw()
    janela_solteiro_n_dinheiro_ss_resultado = tk.CTkToplevel()
    janela_solteiro_n_dinheiro_ss_resultado.geometry("1400x700")
    janela_solteiro_n_dinheiro_ss_resultado.title( "Simulação do ordenado liquido - Trabalhador Dependente - Casado - 2 Titular - Resultado Final")
    texto_topo = tk.CTkLabel(janela_solteiro_n_dinheiro_ss_resultado, text="Simulação do ordenado liquido\nTrabalhador Dependente\nCasado - 2 Titular\nResultado Final", font=("Segoe UI", 20)).place(x=550, y=0)
    ordenado1 = float(renumera_log[0])
    dependentes = int(dependentes_log[0])
    alimentacao = float(alimentacao_log[0])
    dias_alimentacao = int(dias_log[0])
    outros = float(outros_log[0])
    if alimentacao <6:
        excedente_alimentacao = 0
    else:
        excedente_alimentacao = alimentacao-6
    valor_alimentacao = alimentacao*dias_alimentacao
    excedente_alimentacao_dias = excedente_alimentacao*dias_alimentacao
    renumeracao = ordenado1+excedente_alimentacao_dias+outros


    valor_irs, parcela_abater, taxa, renumeracao_liquida, parcela_dependente = casados_2t_invalidez(dependentes, renumeracao)
    if valor_irs<0:
        valor_irs = 0
    else:
        valor_irs = valor_irs
    valor_ss = renumeracao*0.11
    renumeracao_final = renumeracao - valor_ss - valor_irs + valor_alimentacao


    ### SINTESE DE CARACTERISTICAS ###

    escrever_renumeracao = tk.CTkLabel(janela_solteiro_n_dinheiro_ss_resultado, text=("Ordenado Base: {} €" .format(ordenado1)), font=("Segoe UI", 20)).place(x=150, y=100)
    escrever_regime = tk.CTkLabel(janela_solteiro_n_dinheiro_ss_resultado, text=("Regime: Trabalhador Dependente"), font=("Segoe UI", 20)).place(x=150, y=150)
    escrever_fiscal = tk.CTkLabel(janela_solteiro_n_dinheiro_ss_resultado, text = ("Situação Fiscal:  Casado - 2 Titular"), font=("Segoe UI", 20)).place(x=150,y=200)
    escrever_dependentes = tk.CTkLabel(janela_solteiro_n_dinheiro_ss_resultado, text=("Dependentes: {}".format(dependentes)), font=("Segoe UI", 20)).place(x=150, y=250)
    escrever_social = tk.CTkLabel(janela_solteiro_n_dinheiro_ss_resultado, text=("Contribuição Social: Segurança Social"), font=("Segoe UI", 20)).place(x=150, y=300)
    escrever_adse = tk.CTkLabel(janela_solteiro_n_dinheiro_ss_resultado, text=("ADSE: Não"), font=("Segoe UI", 20)).place(x=150, y=350)
    escrever_alimentacao = tk.CTkLabel(janela_solteiro_n_dinheiro_ss_resultado, text=("Subsidio de Alimentação: {} €".format(valor_alimentacao)), font=("Segoe UI", 20)).place(x=150, y=400)
    escrever_dias = tk.CTkLabel(janela_solteiro_n_dinheiro_ss_resultado, text=("Dias com susbsidio de alimentação: {}".format(dias_alimentacao)), font=("Segoe UI", 20)).place(x=150, y=450)
    escrever_pagamento = tk.CTkLabel(janela_solteiro_n_dinheiro_ss_resultado, text=("Forma de pagamento do subsidio de alimentação: Dinheiro"), font=("Segoe UI", 20)).place(x=150, y=500)
    escrever_outros = tk.CTkLabel(janela_solteiro_n_dinheiro_ss_resultado, text=("Outros subsidios tributaveis: {} €".format(outros)), font=("Segoe UI", 20)).place(x=150, y=550)
    escrever_invalidez = tk.CTkLabel(janela_solteiro_n_dinheiro_ss_resultado, text=("Invalidez ou incapacidade: Sim"), font=("Segoe UI", 20)).place(x=150, y=600)

### APRESENTAÇÃO DOS VALORES ###
    texto_descontos = tk.CTkLabel(janela_solteiro_n_dinheiro_ss_resultado, text=("Resumo dos descontos"), font=("Segoe UI", 20)) .place(x=879, y=150)
    texto_valor = tk.CTkLabel(janela_solteiro_n_dinheiro_ss_resultado, text=("Valor tributável:{:.2f}€ " .format(renumeracao)), font=("Segoe UI", 20)).place(x=879 , y=300)
    texto_irs = tk.CTkLabel(janela_solteiro_n_dinheiro_ss_resultado, text=("Retenção na fonte: {:.2f}€" .format(valor_irs)), font=("Segoe UI", 20)).place(x=879 , y=200)
    texto_ss = tk.CTkLabel(janela_solteiro_n_dinheiro_ss_resultado, text=("Taxa Social Única: {:.2f}€" .format(valor_ss)), font=("Segoe UI", 20)).place(x=879 , y=250)
    valor_final = tk.CTkLabel(janela_solteiro_n_dinheiro_ss_resultado, text=( "Valor após descontos: {:.2f}€" .format(renumeracao_final)), font=("Segoe UI", 20), bg_color = "red").place(x=879 , y=300)

### FINAL - SAIR OU HISTORICO ###
    decidir_historico = tk.CTkLabel(janela_solteiro_n_dinheiro_ss_resultado, text=("Deseja adicionar está simulação ao histórico?" ), font=("Segoe UI", 20)).place(x=879, y=500)
    select_tabela_a = tk.CTkButton(janela_solteiro_n_dinheiro_ss_resultado, text="Sim",command=lambda: historico_ordenado(regime, situacao_fiscal, dependentes, contribuicao_social, adse, valor_alimentacao, dias_alimentacao, forma_pagamento, outros, renumeracao, valor_irs, valor_adse, valor_ss, renumeracao_final, invalidez),font=("Segoe UI", 20)).place(x=879, y=550)
    select_tabela_b = tk.CTkButton(janela_solteiro_n_dinheiro_ss_resultado, text="Não",command=lambda: reiniciar_programa(),font=("Segoe UI", 20)).place(x=1079, y=550)


def dependente_2t_dinheiro_ss_adse(janela_solteiro_n_dinheiro_ss):
    regime = 1
    situacao_fiscal = 3
    contribuicao_social = 1
    adse = 1
    forma_pagamento = 1
    valor_irs=0
    invalidez = 2
    janela_solteiro_n_dinheiro_ss.withdraw()
    janela_solteiro_n_dinheiro_ss_adse = tk.CTkToplevel()
    janela_solteiro_n_dinheiro_ss_adse.geometry("1400x700")
    janela_solteiro_n_dinheiro_ss_adse.title( "Simulação do ordenado liquido - Trabalhador Dependente - Casado - 2 Titular - Resultado Final")
    texto_topo = tk.CTkLabel(janela_solteiro_n_dinheiro_ss_adse, text="Simulação do ordenado liquido\nTrabalhador Dependente\nCasado - 2 Titular\nResultado Final", font=("Segoe UI", 20)).place(x=550, y=0)
    ordenado1 = float(renumera_log[0])
    dependentes = int(dependentes_log[0])
    alimentacao = float(alimentacao_log[0])
    dias_alimentacao = int(dias_log[0])
    outros = float(outros_log[0])
    if alimentacao < 6:
        excedente_alimentacao = 0
    else:
        excedente_alimentacao = alimentacao-6
    valor_alimentacao = alimentacao*dias_alimentacao
    excedente_alimentacao_dias = excedente_alimentacao*dias_alimentacao
    renumeracao = ordenado1+excedente_alimentacao_dias+outros

    valor_irs, parcela_abater, taxa, renumeracao_liquida, parcela_dependente = casados_2t_invalidez (dependentes, renumeracao)

    valor_ss = renumeracao*0.11
    valor_adse = renumeracao*0.035

    if valor_irs<0:
        valor_irs = 0
    else:
        valor_irs = valor_irs

    renumeracao_final = renumeracao - valor_adse - valor_ss - valor_irs+valor_alimentacao

    ### SINTESE DE CARACTERISTICAS ###

    escrever_renumeracao = tk.CTkLabel(janela_solteiro_n_dinheiro_ss_adse, text=("Ordenado Base: {} €" .format(ordenado1)), font=("Segoe UI", 20)).place(x=150, y=100)
    escrever_regime = tk.CTkLabel(janela_solteiro_n_dinheiro_ss_adse, text=("Regime: Trabalhador Dependente"), font=("Segoe UI", 20)).place(x=150, y=150)
    escrever_fiscal = tk.CTkLabel(janela_solteiro_n_dinheiro_ss_adse, text = ("Situação Fiscal: Casado - 2 Titular"), font=("Segoe UI", 20)).place(x=150,y=200)
    escrever_dependentes = tk.CTkLabel(janela_solteiro_n_dinheiro_ss_adse, text=("Dependentes: {}".format(dependentes)), font=("Segoe UI", 20)).place(x=150, y=250)
    escrever_social = tk.CTkLabel(janela_solteiro_n_dinheiro_ss_adse, text=("Contribuição Social: Segurança Social"), font=("Segoe UI", 20)).place(x=150, y=300)
    escrever_adse = tk.CTkLabel(janela_solteiro_n_dinheiro_ss_adse, text=("ADSE: Sim"), font=("Segoe UI", 20)).place(x=150, y=350)
    escrever_alimentacao = tk.CTkLabel(janela_solteiro_n_dinheiro_ss_adse, text=("Subsidio de Alimentação: {} €".format(valor_alimentacao)), font=("Segoe UI", 20)).place(x=150, y=400)
    escrever_dias = tk.CTkLabel(janela_solteiro_n_dinheiro_ss_adse, text=("Dias com susbsidio de alimentação: {}".format(dias_alimentacao)), font=("Segoe UI", 20)).place(x=150, y=450)
    escrever_pagamento = tk.CTkLabel(janela_solteiro_n_dinheiro_ss_adse, text=("Forma de pagamento do subsidio de alimentação: Dinheiro"), font=("Segoe UI", 20)).place(x=150, y=500)
    escrever_outros = tk.CTkLabel(janela_solteiro_n_dinheiro_ss_adse, text=("Outros subsidios tributaveis: {} €".format(outros)), font=("Segoe UI", 20)).place(x=150, y=550)
    escrever_invalidez = tk.CTkLabel(janela_solteiro_n_dinheiro_ss_adse, text=("Invalidez ou incapacidade: Sim"), font=("Segoe UI", 20)).place(x=150, y=600)

### APRESENTAÇÃO DOS VALORES ###
    texto_descontos = tk.CTkLabel(janela_solteiro_n_dinheiro_ss_adse, text=("Resumo dos descontos"), font=("Segoe UI", 20)) .place(x=879, y=150)
    texto_valor = tk.CTkLabel(janela_solteiro_n_dinheiro_ss_adse, text=("Valor tributável:{:.2f}€ " .format(renumeracao)), font=("Segoe UI", 20)).place(x=879 , y=300)
    texto_irs = tk.CTkLabel(janela_solteiro_n_dinheiro_ss_adse, text=("Retenção na fonte: {:.2f}€" .format(valor_irs)), font=("Segoe UI", 20)).place(x=879 , y=200)
    texto_ss = tk.CTkLabel(janela_solteiro_n_dinheiro_ss_adse, text=("Taxa Social Única: {:.2f}€" .format(valor_ss)), font=("Segoe UI", 20)).place(x=879 , y=250)
    taxa_adse = tk.CTkLabel(janela_solteiro_n_dinheiro_ss_adse, text=("Desconto ADSE: {:.2f}€" .format(valor_adse)), font=("Segoe UI", 20)).place(x=879 , y=350)
    valor_final = tk.CTkLabel(janela_solteiro_n_dinheiro_ss_adse, text=( "Valor após descontos: {:.2f}€" .format(renumeracao_final)), font=("Segoe UI", 20), bg_color = "red").place(x=879 , y=450)

### FINAL - SAIR OU HISTORICO ###
    decidir_historico = tk.CTkLabel(janela_solteiro_n_dinheiro_ss_adse, text=("Deseja adicionar está simulação ao histórico?" ), font=("Segoe UI", 20)).place(x=879, y=500)
    select_tabela_a = tk.CTkButton(janela_solteiro_n_dinheiro_ss_adse, text="Sim",command=lambda: historico_ordenado(regime, situacao_fiscal, dependentes, contribuicao_social, adse, valor_alimentacao, dias_alimentacao, forma_pagamento, outros, renumeracao, valor_irs, valor_adse, valor_ss, renumeracao_final, invalidez),font=("Segoe UI", 20)).place(x=879, y=550)
    select_tabela_b = tk.CTkButton(janela_solteiro_n_dinheiro_ss_adse, text="Não",command=lambda: reiniciar_programa(),font=("Segoe UI", 20)).place(x=1079, y=550)


def dependente_2t_dinheiro_ss(janela_solteiro_n_dinheiro):
    janela_solteiro_n_dinheiro.withdraw()
    janela_solteiro_n_dinheiro_ss = tk.CTkToplevel()
    janela_solteiro_n_dinheiro_ss.geometry("1400x700")
    janela_solteiro_n_dinheiro_ss.title("Simulação do ordenado liquido - Trabalhador Dependente - Casado - 2 Titular - Outras contribuições")
    texto_topo = tk.CTkLabel(janela_solteiro_n_dinheiro_ss, text="Simulação do ordenado liquido\nTrabalhador Dependente\nSolteiro\nOutras contribuições", font=("Segoe UI", 20)).place(x=550, y=0)
    texto_adse = tk.CTkLabel(janela_solteiro_n_dinheiro_ss, text="É beneficiário da ADSE?", font=("Segoe UI", 20)).place(x=590, y=150)
    botao_sim = tk.CTkButton(janela_solteiro_n_dinheiro_ss, text= "Sim", command=lambda: dependente_2t_s_dinheiro_ss_adse(janela_solteiro_n_dinheiro_ss), font=("Segoe UI", 20)).place(x=530, y=200)
    botao_nao = tk.CTkButton(janela_solteiro_n_dinheiro_ss, text="Não", command=lambda: dependente_2t_s_dinheiro_ss_resultado(janela_solteiro_n_dinheiro_ss), font=("Segoe UI", 20)).place(x=730, y=200)


def dependente_2t_s_dinheiro(janela_solteiro_n, pedir_outros, pedir_alimentacao, pedir_dias):
    alimentacao = float(pedir_alimentacao.get())
    alimentacao_log.append(alimentacao)
    dias = float(pedir_dias.get())
    dias_log.append(dias)
    outros = float(pedir_outros.get())
    outros_log.append(outros)
    janela_solteiro_n.withdraw()
    janela_solteiro_n_dinheiro = tk.CTkToplevel()
    janela_solteiro_n_dinheiro.geometry("1400x700")
    janela_solteiro_n_dinheiro.title("Simulação do ordenado liquido - Trabalhador Dependente - Casado - 2 Titular - Outras contribuições")
    texto_topo = tk.CTkLabel(janela_solteiro_n_dinheiro, text="Simulação do ordenado liquido\nTrabalhador Dependente\nCasado - 2 Titular\nOutras contribuições", font=("Segoe UI", 20)).place(x=550, y=0)
    texto_forma = tk.CTkLabel(janela_solteiro_n_dinheiro, text = "Selecione a sua forma de contribuição social", font=("Segoe UI", 20)).place(x=510, y=150)
    botao_ss = tk.CTkButton(janela_solteiro_n_dinheiro, text="Segurança Social", command=lambda:dependente_2t_s_dinheiro_ss(janela_solteiro_n_dinheiro), font=("Segoe UI", 20)) .place(x=606, y=200)
    botao_cga = tk.CTkButton(janela_solteiro_n_dinheiro, text="Caixa Geral de Aposentações", command=lambda: dependente_2t_s_dinheiro_cga(janela_solteiro_n_dinheiro),  font=("Segoe UI",20)) .place(x=560, y=250)

def dependente_2t_s(janela_dependente_solteiro, pedir_renumeracao_base):

    ordenado2 = float(pedir_renumeracao_base.get())
    renumera_log.append(ordenado2)
    janela_dependente_solteiro.withdraw()
    janela_solteiro_n = tk.CTkToplevel()
    janela_solteiro_n.geometry("1400x700")
    janela_solteiro_n.title("Simulação do ordenado liquido - Trabalhador Dependente - Casado - 2 Titular - Subsidios")
    texto_topo = tk.CTkLabel(janela_solteiro_n,text="Simulação do ordenado liquido\nTrabalhador Dependente\nCasado - 2 Titular", font=("Segoe UI", 20)).place(x=550, y=0)
    texto_alimentacao = tk.CTkLabel(janela_solteiro_n,text="Insira o valor diário do subsidio de alimentação", font=("Segoe UI", 20)).place(x=490, y=100)
    pedir_alimentacao = tk.CTkEntry(janela_solteiro_n, placeholder_text= "Valor", font=("Segoe UI",20))
    pedir_alimentacao.place(x=636, y=150)
    texto_dias = tk.CTkLabel(janela_solteiro_n,text="Insira o número de dias com subsidio de alimentação", font=("Segoe UI", 20)).place(x=475, y=200)
    pedir_dias = tk.CTkEntry(janela_solteiro_n, placeholder_text="Dias", font=("Segoe UI", 20))
    pedir_dias.place(x=636, y=250)
    texto_outros = tk.CTkLabel(janela_solteiro_n, text = "Insira o valor de outros subsidios", font=("Segoe UI",20)) .place(x=550,y=300)
    pedir_outros = tk.CTkEntry(janela_solteiro_n, placeholder_text= "Valor", font=("Segoe UI",20))
    pedir_outros.place(x=636,y=350)
    texto_pag_alimentacao = tk.CTkLabel(janela_solteiro_n, text = "Selecione a forma de pagamento do subsidio de alimentacão", font=("Segoe UI", 20)) .place(x=450, y=400)
    botao_dinheiro = tk.CTkButton(janela_solteiro_n, text = "Dinheiro", font=("Segoe UI", 20), command=lambda: dependente_2t_s_dinheiro(janela_solteiro_n, pedir_outros, pedir_alimentacao, pedir_dias)) .place(x=490, y=450)
    botao_cartao = tk.CTkButton(janela_solteiro_n, text="Cartão/Vale de refeição", command=lambda:dependente_2t_s_vale(janela_solteiro_n, pedir_outros, pedir_alimentacao, pedir_dias),font=("Segoe UI", 20)) .place(x=690, y=450)


def dependente_2t(janela_dependente, pedir_dependentes):
    janela_dependente.withdraw()
    dependentes_log.append(pedir_dependentes.get())
    janela_dependente_solteiro=tk.CTkToplevel()
    janela_dependente_solteiro.title("Simulação do ordenado liquido - Trabalhador Dependente - Casado - 2 Titular")
    janela_dependente_solteiro.geometry("1400x700")
    texto_topo = tk.CTkLabel(janela_dependente_solteiro, text = "Simulação do ordenado liquido\nTrabalhador Dependente\nCasado - 2 Titular", font = ("Segoe UI", 20)) .place(x=560, y=0)
    texto_renumeracao_base = tk.CTkLabel(janela_dependente_solteiro, text = "Insira a sua renumeração base", font = ("Segoe UI", 20)) .place(x=569, y=100)
    pedir_renumeracao_base = tk.CTkEntry(janela_dependente_solteiro, placeholder_text = "Renumeração base", font = ("Segoe UI",20))
    pedir_renumeracao_base.place(x=616, y=150)
    texto_invalidez= tk.CTkLabel(janela_dependente_solteiro, text = "Possui algum tipo de invalidez (deficiencia)?", font = ("Segoe UI",20)) .place(x=524, y=200)
    sim_invalidez = tk.CTkButton(janela_dependente_solteiro, text = "Sim", font=("Sego UI",20), command = lambda: dependente_2t_s(janela_dependente_solteiro, pedir_renumeracao_base)). place(x = 626, y=250)
    nao_invalidez = tk.CTkButton(janela_dependente_solteiro, text = "Não", font=("Sego UI",20), command=lambda:dependente_2t_n(janela_dependente_solteiro, pedir_renumeracao_base)). place(x=626, y=300)





#### 1 TITULAR ###



def dependente_1t_n_vale_cga_resultado(janela_solteiro_n_vale_cga):
    regime = 1
    situacao_fiscal = 2
    contribuicao_social = 2
    adse = 2
    forma_pagamento = 2
    valor_irs=0
    invalidez = 1
    valor_adse=0
    janela_solteiro_n_vale_cga.withdraw()
    janela_solteiro_n_vale_cga_resultado = tk.CTkToplevel()
    janela_solteiro_n_vale_cga_resultado.geometry("1400x700")
    janela_solteiro_n_vale_cga_resultado.title( "Simulação do ordenado liquido - Trabalhador Dependente - Casado - 1 Titular  - Resultado Final")
    texto_topo = tk.CTkLabel(janela_solteiro_n_vale_cga_resultado, text="Simulação do ordenado liquido\nTrabalhador Dependente\nCasado - 1 Titular \nResultado Final", font=("Segoe UI", 20)).place(x=550, y=0)
    ordenado1 = float(renumera_log[0])
    dependentes = int(dependentes_log[0])
    alimentacao = float(alimentacao_log[0])
    dias_alimentacao = int(dias_log[0])
    outros = float(outros_log[0])
    if alimentacao < 9.6:
        excedente_alimentacao = 0
    else:
        excedente_alimentacao = alimentacao-9.6
    valor_alimentacao = alimentacao*dias_alimentacao
    excedente_alimentacao_dias = excedente_alimentacao*dias_alimentacao
    renumeracao = ordenado1+excedente_alimentacao_dias+outros

    if renumeracao<=762:
        renumeracao_liquida = 762
        taxa = 0
        parcela_dependente = 0
        parcela_abater = 0

    else:
        valor_irs, parcela_abater, taxa, renumeracao_liquida, parcela_dependente = ordenado_casado_1t(dependentes, renumeracao)
    if valor_irs<0:
        valor_irs = 0
    else:
        valor_irs = valor_irs
    valor_ss = renumeracao*0.11
    renumeracao_final = renumeracao - valor_ss - valor_irs + valor_alimentacao


    ### SINTESE DE CARACTERISTICAS ###

    escrever_renumeracao = tk.CTkLabel(janela_solteiro_n_vale_cga_resultado, text=("Ordenado Base: {} €" .format(ordenado1)), font=("Segoe UI", 20)).place(x=150, y=100)
    escrever_regime = tk.CTkLabel(janela_solteiro_n_vale_cga_resultado, text=("Regime: Trabalhador Dependente"), font=("Segoe UI", 20)).place(x=150, y=150)
    escrever_fiscal = tk.CTkLabel(janela_solteiro_n_vale_cga_resultado, text = ("Situação Fiscal: Casado - 1 Titular "), font=("Segoe UI", 20)).place(x=150,y=200)
    escrever_dependentes = tk.CTkLabel(janela_solteiro_n_vale_cga_resultado, text=("Dependentes: {}".format(dependentes)), font=("Segoe UI", 20)).place(x=150, y=250)
    escrever_social = tk.CTkLabel(janela_solteiro_n_vale_cga_resultado, text=("Contribuição Social: Caixa Geral de Aposentações"), font=("Segoe UI", 20)).place(x=150, y=300)
    escrever_adse = tk.CTkLabel(janela_solteiro_n_vale_cga_resultado, text=("ADSE: Não"), font=("Segoe UI", 20)).place(x=150, y=350)
    escrever_alimentacao = tk.CTkLabel(janela_solteiro_n_vale_cga_resultado, text=("Subsidio de Alimentação: {} €".format(valor_alimentacao)), font=("Segoe UI", 20)).place(x=150, y=400)
    escrever_dias = tk.CTkLabel(janela_solteiro_n_vale_cga_resultado, text=("Dias com susbsidio de alimentação: {}".format(dias_alimentacao)), font=("Segoe UI", 20)).place(x=150, y=450)
    escrever_pagamento = tk.CTkLabel(janela_solteiro_n_vale_cga_resultado, text=("Forma de pagamento do subsidio de alimentação: Vale/Cartão de refeição"), font=("Segoe UI", 20)).place(x=150, y=500)
    escrever_outros = tk.CTkLabel(janela_solteiro_n_vale_cga_resultado, text=("Outros subsidios tributaveis: {} €".format(outros)), font=("Segoe UI", 20)).place(x=150, y=550)
    escrever_invalidez = tk.CTkLabel(janela_solteiro_n_vale_cga_resultado, text=("Invalidez ou incapacidade: Não"), font=("Segoe UI", 20)).place(x=150, y=600)

### APRESENTAÇÃO DOS VALORES ###
    texto_descontos = tk.CTkLabel(janela_solteiro_n_vale_cga_resultado, text=("Resumo dos descontos"), font=("Segoe UI", 20)) .place(x=879, y=150)
    texto_valor = tk.CTkLabel(janela_solteiro_n_vale_cga_resultado, text=("Valor tributável:{:.2f}€ " .format(renumeracao)), font=("Segoe UI", 20)).place(x=879 , y=300)
    texto_irs = tk.CTkLabel(janela_solteiro_n_vale_cga_resultado, text=("Retenção na fonte: {:.2f}€" .format(valor_irs)), font=("Segoe UI", 20)).place(x=879 , y=200)
    texto_ss = tk.CTkLabel(janela_solteiro_n_vale_cga_resultado, text=("Taxa Social Única: {:.2f}€" .format(valor_ss)), font=("Segoe UI", 20)).place(x=879 , y=250)
    valor_final = tk.CTkLabel(janela_solteiro_n_vale_cga_resultado, text=( "Valor após descontos: {:.2f}€" .format(renumeracao_final)), font=("Segoe UI", 20), bg_color = "red").place(x=879 , y=300)

### FINAL - SAIR OU HISTORICO ###
    decidir_historico = tk.CTkLabel(janela_solteiro_n_vale_cga_resultado, text=("Deseja adicionar está simulação ao histórico?" ), font=("Segoe UI", 20)).place(x=879, y=500)
    select_tabela_a = tk.CTkButton(janela_solteiro_n_vale_cga_resultado, text="Sim",command=lambda: historico_ordenado(regime, situacao_fiscal, dependentes, contribuicao_social, adse, valor_alimentacao, dias_alimentacao, forma_pagamento, outros, renumeracao, valor_irs, valor_adse, valor_ss, renumeracao_final, invalidez),font=("Segoe UI", 20)).place(x=879, y=550)
    select_tabela_b = tk.CTkButton(janela_solteiro_n_vale_cga_resultado, text="Não",command=lambda: reiniciar_programa(),font=("Segoe UI", 20)).place(x=1079, y=550)



def dependente_1t_n_vale_cga_adse(janela_solteiro_n_vale_cga):
    regime = 1
    situacao_fiscal = 2
    contribuicao_social = 2
    adse = 1
    forma_pagamento = 2
    valor_irs=0
    invalidez = 1
    janela_solteiro_n_vale_cga.withdraw()
    janela_solteiro_n_vale_cga_adse = tk.CTkToplevel()
    janela_solteiro_n_vale_cga_adse.geometry("1400x700")
    janela_solteiro_n_vale_cga_adse.title( "Simulação do ordenado liquido - Trabalhador Dependente - Casado - 1 Titular  - Resultado Final")
    texto_topo = tk.CTkLabel(janela_solteiro_n_vale_cga_adse, text="Simulação do ordenado liquido\nTrabalhador Dependente\nCasado - 1 Titular \nResultado Final", font=("Segoe UI", 20)).place(x=550, y=0)
    ordenado1 = float(renumera_log[0])
    dependentes = int(dependentes_log[0])
    alimentacao = float(alimentacao_log[0])
    dias_alimentacao = int(dias_log[0])
    outros = float(outros_log[0])
    if alimentacao < 9.6:
        excedente_alimentacao = 0
    else:
        excedente_alimentacao = alimentacao-9.6
    valor_alimentacao = alimentacao*dias_alimentacao
    excedente_alimentacao_dias = excedente_alimentacao*dias_alimentacao
    renumeracao = ordenado1+excedente_alimentacao_dias+outros

    if renumeracao<=762:
        renumeracao_liquida = 762
        taxa = 0
        parcela_dependente = 0
        parcela_abater = 0

    else:
        valor_irs, parcela_abater, taxa, renumeracao_liquida, parcela_dependente = ordenado_casado_1t(dependentes, renumeracao)

    valor_ss = renumeracao*0.11
    valor_adse = renumeracao*0.035
    if valor_irs<0:
        valor_irs = 0
    else:
        valor_irs = valor_irs
    renumeracao_final = renumeracao - valor_adse - valor_ss - valor_irs+valor_alimentacao

    ### SINTESE DE CARACTERISTICAS ###

    escrever_renumeracao = tk.CTkLabel(janela_solteiro_n_vale_cga_adse, text=("Ordenado Base: {} €" .format(ordenado1)), font=("Segoe UI", 20)).place(x=150, y=100)
    escrever_regime = tk.CTkLabel(janela_solteiro_n_vale_cga_adse, text=("Regime: Trabalhador Dependente"), font=("Segoe UI", 20)).place(x=150, y=150)
    escrever_fiscal = tk.CTkLabel(janela_solteiro_n_vale_cga_adse, text = ("Situação Fiscal: Casado - 1 Titular"), font=("Segoe UI", 20)).place(x=150,y=200)
    escrever_dependentes = tk.CTkLabel(janela_solteiro_n_vale_cga_adse, text=("Dependentes: {}".format(dependentes)), font=("Segoe UI", 20)).place(x=150, y=250)
    escrever_social = tk.CTkLabel(janela_solteiro_n_vale_cga_adse, text=("Contribuição Social: Caixa Geral de Aposentações"), font=("Segoe UI", 20)).place(x=150, y=300)
    escrever_adse = tk.CTkLabel(janela_solteiro_n_vale_cga_adse, text=("ADSE: Sim"), font=("Segoe UI", 20)).place(x=150, y=350)
    escrever_alimentacao = tk.CTkLabel(janela_solteiro_n_vale_cga_adse, text=("Subsidio de Alimentação: {} €".format(valor_alimentacao)), font=("Segoe UI", 20)).place(x=150, y=400)
    escrever_dias = tk.CTkLabel(janela_solteiro_n_vale_cga_adse, text=("Dias com susbsidio de alimentação: {}".format(dias_alimentacao)), font=("Segoe UI", 20)).place(x=150, y=450)
    escrever_pagamento = tk.CTkLabel(janela_solteiro_n_vale_cga_adse, text=("Forma de pagamento do subsidio de alimentação: Vale/Cartão de alimentação"), font=("Segoe UI", 20)).place(x=150, y=500)
    escrever_outros = tk.CTkLabel(janela_solteiro_n_vale_cga_adse, text=("Outros subsidios tributaveis: {} €".format(outros)), font=("Segoe UI", 20)).place(x=150, y=550)
    escrever_invalidez = tk.CTkLabel(janela_solteiro_n_vale_cga_adse, text=("Invalidez ou incapacidade: Não"), font=("Segoe UI", 20)).place(x=150, y=600)

### APRESENTAÇÃO DOS VALORES ###
    texto_descontos = tk.CTkLabel(janela_solteiro_n_vale_cga_adse, text=("Resumo dos descontos"), font=("Segoe UI", 20)) .place(x=879, y=150)
    texto_valor = tk.CTkLabel(janela_solteiro_n_vale_cga_adse, text=("Valor tributável:{:.2f}€ " .format(renumeracao)), font=("Segoe UI", 20)).place(x=879 , y=300)
    texto_irs = tk.CTkLabel(janela_solteiro_n_vale_cga_adse, text=("Retenção na fonte: {:.2f}€" .format(valor_irs)), font=("Segoe UI", 20)).place(x=879 , y=200)
    texto_ss = tk.CTkLabel(janela_solteiro_n_vale_cga_adse, text=("Taxa Social Única: {:.2f}€" .format(valor_ss)), font=("Segoe UI", 20)).place(x=879 , y=250)
    taxa_adse = tk.CTkLabel(janela_solteiro_n_vale_cga_adse, text=("Desconto ADSE: {:.2f}€" .format(valor_adse)), font=("Segoe UI", 20)).place(x=879 , y=350)
    valor_final = tk.CTkLabel(janela_solteiro_n_vale_cga_adse, text=( "Valor após descontos: {:.2f}€" .format(renumeracao_final)), font=("Segoe UI", 20), bg_color = "red").place(x=879 , y=450)

### FINAL - SAIR OU HISTORICO ###
    decidir_historico = tk.CTkLabel(janela_solteiro_n_vale_cga_adse, text=("Deseja adicionar está simulação ao histórico?" ), font=("Segoe UI", 20)).place(x=879, y=500)
    select_tabela_a = tk.CTkButton(janela_solteiro_n_vale_cga_adse, text="Sim",command=lambda: historico_ordenado(regime, situacao_fiscal, dependentes, contribuicao_social, adse, valor_alimentacao, dias_alimentacao, forma_pagamento, outros, renumeracao, valor_irs, valor_adse, valor_ss, renumeracao_final, invalidez),font=("Segoe UI", 20)).place(x=879, y=550)
    select_tabela_b = tk.CTkButton(janela_solteiro_n_vale_cga_adse, text="Não",command=lambda: reiniciar_programa(),font=("Segoe UI", 20)).place(x=1079, y=550)



def dependente_1t_n_vale_cga(janela_solteiro_n_vale):
    janela_solteiro_n_vale.withdraw()
    janela_solteiro_n_vale_cga = tk.CTkToplevel()
    janela_solteiro_n_vale_cga.geometry("1400x700")
    janela_solteiro_n_vale_cga.title("Simulação do ordenado liquido - Trabalhador Dependente - Casado - 1 Titular - Outras contribuições")
    texto_topo = tk.CTkLabel(janela_solteiro_n_vale_cga, text="Simulação do ordenado liquido\nTrabalhador Dependente\nCasado - 1 Titular\nOutras contribuições", font=("Segoe UI", 20)).place(x=550, y=0)
    texto_adse = tk.CTkLabel(janela_solteiro_n_vale_cga, text="É beneficiário da ADSE?", font=("Segoe UI", 20)).place(x=590, y=150)
    botao_sim = tk.CTkButton(janela_solteiro_n_vale_cga, text= "Sim", command=lambda: dependente_1t_n_vale_cga_adse(janela_solteiro_n_vale_cga), font=("Segoe UI", 20)).place(x=530, y=200)
    botao_nao = tk.CTkButton(janela_solteiro_n_vale_cga, text="Não", command=lambda: dependente_1t_n_vale_cga_resultado(janela_solteiro_n_vale_cga), font=("Segoe UI", 20)).place(x=730, y=200)

def dependente_1t_n_vale_ss_resultado(janela_solteiro_n_vale_ss):
    regime = 1
    situacao_fiscal = 2
    contribuicao_social = 1
    adse = 2
    forma_pagamento = 2
    valor_irs=0
    invalidez = 1
    valor_adse=0
    janela_solteiro_n_vale_ss.withdraw()
    janela_solteiro_n_vale_ss_resultado = tk.CTkToplevel()
    janela_solteiro_n_vale_ss_resultado.geometry("1400x700")
    janela_solteiro_n_vale_ss_resultado.title( "Simulação do ordenado liquido - Trabalhador Dependente - Solteiro - Resultado Final")
    texto_topo = tk.CTkLabel(janela_solteiro_n_vale_ss_resultado, text="Simulação do ordenado liquido\nTrabalhador Dependente\nSolteiro\nResultado Final", font=("Segoe UI", 20)).place(x=550, y=0)
    ordenado1 = float(renumera_log[0])
    dependentes = int(dependentes_log[0])
    alimentacao = float(alimentacao_log[0])
    dias_alimentacao = int(dias_log[0])
    outros = float(outros_log[0])
    if alimentacao <9.6:
        excedente_alimentacao = 0
    else:
        excedente_alimentacao = alimentacao-9.6
    valor_alimentacao = alimentacao*dias_alimentacao
    excedente_alimentacao_dias = excedente_alimentacao*dias_alimentacao
    renumeracao = ordenado1+excedente_alimentacao_dias+outros

    if renumeracao<=762:
        renumeracao_liquida = 762
        taxa = 0
        parcela_dependente = 0
        parcela_abater = 0

    else:
        valor_irs, parcela_abater, taxa, renumeracao_liquida, parcela_dependente = ordenado_casado_1t(dependentes, renumeracao)
    if valor_irs<0:
        valor_irs = 0
    else:
        valor_irs = valor_irs
    valor_ss = renumeracao*0.11
    renumeracao_final = renumeracao - valor_ss - valor_irs + valor_alimentacao


    ### SINTESE DE CARACTERISTICAS ###

    escrever_renumeracao = tk.CTkLabel(janela_solteiro_n_vale_ss_resultado, text=("Ordenado Base: {} €" .format(ordenado1)), font=("Segoe UI", 20)).place(x=150, y=100)
    escrever_regime = tk.CTkLabel(janela_solteiro_n_vale_ss_resultado, text=("Regime: Trabalhador Dependente"), font=("Segoe UI", 20)).place(x=150, y=150)
    escrever_fiscal = tk.CTkLabel(janela_solteiro_n_vale_ss_resultado, text = ("Situação Fiscal: Casado - 1 Titular"), font=("Segoe UI", 20)).place(x=150,y=200)
    escrever_dependentes = tk.CTkLabel(janela_solteiro_n_vale_ss_resultado, text=("Dependentes: {}".format(dependentes)), font=("Segoe UI", 20)).place(x=150, y=250)
    escrever_social = tk.CTkLabel(janela_solteiro_n_vale_ss_resultado, text=("Contribuição Social: Segurança Social"), font=("Segoe UI", 20)).place(x=150, y=300)
    escrever_adse = tk.CTkLabel(janela_solteiro_n_vale_ss_resultado, text=("ADSE: Não"), font=("Segoe UI", 20)).place(x=150, y=350)
    escrever_alimentacao = tk.CTkLabel(janela_solteiro_n_vale_ss_resultado, text=("Subsidio de Alimentação: {} €".format(valor_alimentacao)), font=("Segoe UI", 20)).place(x=150, y=400)
    escrever_dias = tk.CTkLabel(janela_solteiro_n_vale_ss_resultado, text=("Dias com susbsidio de alimentação: {}".format(dias_alimentacao)), font=("Segoe UI", 20)).place(x=150, y=450)
    escrever_pagamento = tk.CTkLabel(janela_solteiro_n_vale_ss_resultado, text=("Forma de pagamento do subsidio de alimentação: Vale/Cartão de Refeição"), font=("Segoe UI", 20)).place(x=150, y=500)
    escrever_outros = tk.CTkLabel(janela_solteiro_n_vale_ss_resultado, text=("Outros subsidios tributaveis: {} €".format(outros)), font=("Segoe UI", 20)).place(x=150, y=550)
    escrever_invalidez = tk.CTkLabel(janela_solteiro_n_vale_ss_resultado, text=("Invalidez ou incapacidade: Não"), font=("Segoe UI", 20)).place(x=150, y=600)

### APRESENTAÇÃO DOS VALORES ###
    texto_descontos = tk.CTkLabel(janela_solteiro_n_vale_ss_resultado, text=("Resumo dos descontos"), font=("Segoe UI", 20)) .place(x=879, y=150)
    texto_valor = tk.CTkLabel(janela_solteiro_n_vale_ss_resultado, text=("Valor tributável:{:.2f}€ " .format(renumeracao)), font=("Segoe UI", 20)).place(x=879 , y=300)
    texto_irs = tk.CTkLabel(janela_solteiro_n_vale_ss_resultado, text=("Retenção na fonte: {:.2f}€" .format(valor_irs)), font=("Segoe UI", 20)).place(x=879 , y=200)
    texto_ss = tk.CTkLabel(janela_solteiro_n_vale_ss_resultado, text=("Taxa Social Única: {:.2f}€" .format(valor_ss)), font=("Segoe UI", 20)).place(x=879 , y=250)
    valor_final = tk.CTkLabel(janela_solteiro_n_vale_ss_resultado, text=( "Valor após descontos: {:.2f}€" .format(renumeracao_final)), font=("Segoe UI", 20), bg_color = "red").place(x=879 , y=300)

### FINAL - SAIR OU HISTORICO ###
    decidir_historico = tk.CTkLabel(janela_solteiro_n_vale_ss_resultado, text=("Deseja adicionar está simulação ao histórico?" ), font=("Segoe UI", 20)).place(x=879, y=500)
    select_tabela_a = tk.CTkButton(janela_solteiro_n_vale_ss_resultado, text="Sim",command=lambda: historico_ordenado(regime, situacao_fiscal, dependentes, contribuicao_social, adse, valor_alimentacao, dias_alimentacao, forma_pagamento, outros, renumeracao, valor_irs, valor_adse, valor_ss, renumeracao_final, invalidez),font=("Segoe UI", 20)).place(x=879, y=550)
    select_tabela_b = tk.CTkButton(janela_solteiro_n_vale_ss_resultado, text="Não",command=lambda: reiniciar_programa(),font=("Segoe UI", 20)).place(x=1079, y=550)



def dependente_1t_n_vale_ss_adse(janela_solteiro_n_vale_ss):
    regime = 1
    situacao_fiscal = 2
    contribuicao_social = 1
    adse = 1
    forma_pagamento = 2
    valor_irs=0
    invalidez = 1
    janela_solteiro_n_vale_ss.withdraw()
    janela_solteiro_n_vale_ss_adse = tk.CTkToplevel()
    janela_solteiro_n_vale_ss_adse.geometry("1400x700")
    janela_solteiro_n_vale_ss_adse.title( "Simulação do ordenado liquido - Trabalhador Dependente - Casado - 1 Titular - Resultado Final")
    texto_topo = tk.CTkLabel(janela_solteiro_n_vale_ss_adse, text="Simulação do ordenado liquido\nTrabalhador Dependente\nCasado - 1 Titular\nResultado Final", font=("Segoe UI", 20)).place(x=550, y=0)
    ordenado1 = float(renumera_log[0])
    dependentes = int(dependentes_log[0])
    alimentacao = float(alimentacao_log[0])
    dias_alimentacao = int(dias_log[0])
    outros = float(outros_log[0])
    if alimentacao < 9.6:
        excedente_alimentacao = 0
    else:
        excedente_alimentacao = alimentacao-9.6
    valor_alimentacao = alimentacao*dias_alimentacao
    excedente_alimentacao_dias = excedente_alimentacao*dias_alimentacao
    renumeracao = ordenado1+excedente_alimentacao_dias+outros

    if renumeracao<=762:
        renumeracao_liquida = 762
        taxa = 0
        parcela_dependente = 0
        parcela_abater = 0

    else:
        valor_irs, parcela_abater, taxa, renumeracao_liquida, parcela_dependente = ordenado_casado_1t(dependentes, renumeracao)

    valor_ss = renumeracao*0.11
    valor_adse = renumeracao*0.035

    if valor_irs<0:
        valor_irs = 0
    else:
        valor_irs = valor_irs

    renumeracao_final = renumeracao - valor_adse - valor_ss - valor_irs+valor_alimentacao

    ### SINTESE DE CARACTERISTICAS ###

    escrever_renumeracao = tk.CTkLabel(janela_solteiro_n_vale_ss_adse, text=("Ordenado Base: {} €" .format(ordenado1)), font=("Segoe UI", 20)).place(x=150, y=100)
    escrever_regime = tk.CTkLabel(janela_solteiro_n_vale_ss_adse, text=("Regime: Trabalhador Dependente"), font=("Segoe UI", 20)).place(x=150, y=150)
    escrever_fiscal = tk.CTkLabel(janela_solteiro_n_vale_ss_adse, text = ("Situação Fiscal: Casado - 1 Titular"), font=("Segoe UI", 20)).place(x=150,y=200)
    escrever_dependentes = tk.CTkLabel(janela_solteiro_n_vale_ss_adse, text=("Dependentes: {}".format(dependentes)), font=("Segoe UI", 20)).place(x=150, y=250)
    escrever_social = tk.CTkLabel(janela_solteiro_n_vale_ss_adse, text=("Contribuição Social: Segurança Social"), font=("Segoe UI", 20)).place(x=150, y=300)
    escrever_adse = tk.CTkLabel(janela_solteiro_n_vale_ss_adse, text=("ADSE: Sim"), font=("Segoe UI", 20)).place(x=150, y=350)
    escrever_alimentacao = tk.CTkLabel(janela_solteiro_n_vale_ss_adse, text=("Subsidio de Alimentação: {} €".format(valor_alimentacao)), font=("Segoe UI", 20)).place(x=150, y=400)
    escrever_dias = tk.CTkLabel(janela_solteiro_n_vale_ss_adse, text=("Dias com susbsidio de alimentação: {}".format(dias_alimentacao)), font=("Segoe UI", 20)).place(x=150, y=450)
    escrever_pagamento = tk.CTkLabel(janela_solteiro_n_vale_ss_adse, text=("Forma de pagamento do subsidio de alimentação: Cartão/Vale de alimentação"), font=("Segoe UI", 20)).place(x=150, y=500)
    escrever_outros = tk.CTkLabel(janela_solteiro_n_vale_ss_adse, text=("Outros subsidios tributaveis: {} €".format(outros)), font=("Segoe UI", 20)).place(x=150, y=550)
    escrever_invalidez = tk.CTkLabel(janela_solteiro_n_vale_ss_adse, text=("Invalidez ou incapacidade: Não"), font=("Segoe UI", 20)).place(x=150, y=600)

### APRESENTAÇÃO DOS VALORES ###
    texto_descontos = tk.CTkLabel(janela_solteiro_n_vale_ss_adse, text=("Resumo dos descontos"), font=("Segoe UI", 20)) .place(x=879, y=150)
    texto_valor = tk.CTkLabel(janela_solteiro_n_vale_ss_adse, text=("Valor tributável:{:.2f}€ " .format(renumeracao)), font=("Segoe UI", 20)).place(x=879 , y=300)
    texto_irs = tk.CTkLabel(janela_solteiro_n_vale_ss_adse, text=("Retenção na fonte: {:.2f}€" .format(valor_irs)), font=("Segoe UI", 20)).place(x=879 , y=200)
    texto_ss = tk.CTkLabel(janela_solteiro_n_vale_ss_adse, text=("Taxa Social Única: {:.2f}€" .format(valor_ss)), font=("Segoe UI", 20)).place(x=879 , y=250)
    taxa_adse = tk.CTkLabel(janela_solteiro_n_vale_ss_adse, text=("Desconto ADSE: {:.2f}€" .format(valor_adse)), font=("Segoe UI", 20)).place(x=879 , y=350)
    valor_final = tk.CTkLabel(janela_solteiro_n_vale_ss_adse, text=( "Valor após descontos: {:.2f}€" .format(renumeracao_final)), font=("Segoe UI", 20), bg_color = "red").place(x=879 , y=450)

### FINAL - SAIR OU HISTORICO ###
    decidir_historico = tk.CTkLabel(janela_solteiro_n_vale_ss_adse, text=("Deseja adicionar está simulação ao histórico?" ), font=("Segoe UI", 20)).place(x=879, y=500)
    select_tabela_a = tk.CTkButton(janela_solteiro_n_vale_ss_adse, text="Sim",command=lambda: historico_ordenado(regime, situacao_fiscal, dependentes, contribuicao_social, adse, valor_alimentacao, dias_alimentacao, forma_pagamento, outros, renumeracao, valor_irs, valor_adse, valor_ss, renumeracao_final, invalidez),font=("Segoe UI", 20)).place(x=879, y=550)
    select_tabela_b = tk.CTkButton(janela_solteiro_n_vale_ss_adse, text="Não",command=lambda: reiniciar_programa(),font=("Segoe UI", 20)).place(x=1079, y=550)



def dependente_1t_n_vale_ss(janela_solteiro_n_vale):
    janela_solteiro_n_vale.withdraw()
    janela_solteiro_n_vale_ss = tk.CTkToplevel()
    janela_solteiro_n_vale_ss.geometry("1400x700")
    janela_solteiro_n_vale_ss.title("Simulação do ordenado liquido - Trabalhador Dependente - Casado - 1 Titular - Outras contribuições")
    texto_topo = tk.CTkLabel(janela_solteiro_n_vale_ss, text="Simulação do ordenado liquido\nTrabalhador Dependente\nCasado - 1 Titular\nOutras contribuições", font=("Segoe UI", 20)).place(x=550, y=0)
    texto_adse = tk.CTkLabel(janela_solteiro_n_vale_ss, text="É beneficiário da ADSE?", font=("Segoe UI", 20)).place(x=590, y=150)
    botao_sim = tk.CTkButton(janela_solteiro_n_vale_ss, text= "Sim", command=lambda: dependente_1t_n_vale_ss_adse(janela_solteiro_n_vale_ss), font=("Segoe UI", 20)).place(x=530, y=200)
    botao_nao = tk.CTkButton(janela_solteiro_n_vale_ss, text="Não", command=lambda: dependente_1t_n_vale_ss_resultado(janela_solteiro_n_vale_ss), font=("Segoe UI", 20)).place(x=730, y=200)




def dependente_1t_n_vale(janela_solteiro_n, pedir_outros, pedir_alimentacao, pedir_dias):
    alimentacao = float(pedir_alimentacao.get())
    alimentacao_log.append(alimentacao)
    dias = float(pedir_dias.get())
    dias_log.append(dias)
    outros = float(pedir_outros.get())
    outros_log.append(outros)
    janela_solteiro_n.withdraw()
    janela_solteiro_n_vale = tk.CTkToplevel()
    janela_solteiro_n_vale.geometry("1400x700")
    janela_solteiro_n_vale.title("Simulação do ordenado liquido - Trabalhador Dependente - Casado - 1 Titular - Outras contribuições")
    texto_topo = tk.CTkLabel(janela_solteiro_n_vale, text="Simulação do ordenado liquido\nTrabalhador Dependente\nCasado - 1 Titular\nOutras contribuições", font=("Segoe UI", 20)).place(x=550, y=0)
    texto_forma = tk.CTkLabel(janela_solteiro_n_vale, text = "Selecione a sua forma de contribuição social", font=("Segoe UI", 20)).place(x=510, y=150)
    botao_ss = tk.CTkButton(janela_solteiro_n_vale, text="Segurança Social", command=lambda:dependente_1t_n_vale_ss(janela_solteiro_n_vale), font=("Segoe UI", 20)) .place(x=606, y=200)
    botao_cga = tk.CTkButton(janela_solteiro_n_vale, text="Caixa Geral de Aposentações", command=lambda: dependente_1t_n_vale_cga(janela_solteiro_n_vale),  font=("Segoe UI",20)) .place(x=560, y=250)

def dependente_1t_n_dinheiro_ss_resultado(janela_solteiro_n_dinheiro_ss):
    regime = 1
    situacao_fiscal = 2
    contribuicao_social = 1
    adse = 2
    forma_pagamento = 1
    valor_irs=0
    invalidez = 1
    valor_adse=0
    janela_solteiro_n_dinheiro_ss.withdraw()
    janela_solteiro_n_dinheiro_ss_resultado = tk.CTkToplevel()
    janela_solteiro_n_dinheiro_ss_resultado.geometry("1400x700")
    janela_solteiro_n_dinheiro_ss_resultado.title( "Simulação do ordenado liquido - Trabalhador Dependente - Casado - 1 Titular - Resultado Final")
    texto_topo = tk.CTkLabel(janela_solteiro_n_dinheiro_ss_resultado, text="Simulação do ordenado liquido\nTrabalhador Dependente\nCasado - 1 Titular\nResultado Final", font=("Segoe UI", 20)).place(x=550, y=0)
    ordenado1 = float(renumera_log[0])
    dependentes = int(dependentes_log[0])
    alimentacao = float(alimentacao_log[0])
    dias_alimentacao = int(dias_log[0])
    outros = float(outros_log[0])
    if alimentacao < 6:
        excedente_alimentacao = 0
    else:
        excedente_alimentacao = alimentacao-6
    valor_alimentacao = alimentacao*dias_alimentacao
    excedente_alimentacao_dias = excedente_alimentacao*dias_alimentacao
    renumeracao = ordenado1+excedente_alimentacao_dias+outros

    if renumeracao<=762:
        renumeracao_liquida = 762
        taxa = 0
        parcela_dependente = 0
        parcela_abater = 0

    else:
        valor_irs, parcela_abater, taxa, renumeracao_liquida, parcela_dependente = ordenado_casado_1t(dependentes, renumeracao)
    if valor_irs<0:
        valor_irs = 0
    else:
        valor_irs = valor_irs
    valor_ss = renumeracao*0.11
    renumeracao_final = renumeracao - valor_ss - valor_irs + valor_alimentacao


    ### SINTESE DE CARACTERISTICAS ###

    escrever_renumeracao = tk.CTkLabel(janela_solteiro_n_dinheiro_ss_resultado, text=("Ordenado Base: {} €" .format(ordenado1)), font=("Segoe UI", 20)).place(x=150, y=100)
    escrever_regime = tk.CTkLabel(janela_solteiro_n_dinheiro_ss_resultado, text=("Regime: Trabalhador Dependente"), font=("Segoe UI", 20)).place(x=150, y=150)
    escrever_fiscal = tk.CTkLabel(janela_solteiro_n_dinheiro_ss_resultado, text = ("Situação Fiscal: Casado - 1 Titular"), font=("Segoe UI", 20)).place(x=150,y=200)
    escrever_dependentes = tk.CTkLabel(janela_solteiro_n_dinheiro_ss_resultado, text=("Dependentes: {}".format(dependentes)), font=("Segoe UI", 20)).place(x=150, y=250)
    escrever_social = tk.CTkLabel(janela_solteiro_n_dinheiro_ss_resultado, text=("Contribuição Social: Segurança Social"), font=("Segoe UI", 20)).place(x=150, y=300)
    escrever_adse = tk.CTkLabel(janela_solteiro_n_dinheiro_ss_resultado, text=("ADSE: Não"), font=("Segoe UI", 20)).place(x=150, y=350)
    escrever_alimentacao = tk.CTkLabel(janela_solteiro_n_dinheiro_ss_resultado, text=("Subsidio de Alimentação: {} €".format(valor_alimentacao)), font=("Segoe UI", 20)).place(x=150, y=400)
    escrever_dias = tk.CTkLabel(janela_solteiro_n_dinheiro_ss_resultado, text=("Dias com susbsidio de alimentação: {}".format(dias_alimentacao)), font=("Segoe UI", 20)).place(x=150, y=450)
    escrever_pagamento = tk.CTkLabel(janela_solteiro_n_dinheiro_ss_resultado, text=("Forma de pagamento do subsidio de alimentação: Dinheiro"), font=("Segoe UI", 20)).place(x=150, y=500)
    escrever_outros = tk.CTkLabel(janela_solteiro_n_dinheiro_ss_resultado, text=("Outros subsidios tributaveis: {} €".format(outros)), font=("Segoe UI", 20)).place(x=150, y=550)
    escrever_invalidez = tk.CTkLabel(janela_solteiro_n_dinheiro_ss_resultado, text=("Invalidez ou incapacidade: Não"), font=("Segoe UI", 20)).place(x=150, y=600)

### APRESENTAÇÃO DOS VALORES ###
    texto_descontos = tk.CTkLabel(janela_solteiro_n_dinheiro_ss_resultado, text=("Resumo dos descontos"), font=("Segoe UI", 20)) .place(x=879, y=150)
    texto_valor = tk.CTkLabel(janela_solteiro_n_dinheiro_ss_resultado, text=("Valor tributável:{:.2f}€ " .format(renumeracao)), font=("Segoe UI", 20)).place(x=879 , y=300)
    texto_irs = tk.CTkLabel(janela_solteiro_n_dinheiro_ss_resultado, text=("Retenção na fonte: {:.2f}€" .format(valor_irs)), font=("Segoe UI", 20)).place(x=879 , y=200)
    texto_ss = tk.CTkLabel(janela_solteiro_n_dinheiro_ss_resultado, text=("Taxa Social Única: {:.2f}€" .format(valor_ss)), font=("Segoe UI", 20)).place(x=879 , y=250)
    valor_final = tk.CTkLabel(janela_solteiro_n_dinheiro_ss_resultado, text=( "Valor após descontos: {:.2f}€" .format(renumeracao_final)), font=("Segoe UI", 20), bg_color = "red").place(x=879 , y=300)

### FINAL - SAIR OU HISTORICO ###
    decidir_historico = tk.CTkLabel(janela_solteiro_n_dinheiro_ss_resultado, text=("Deseja adicionar está simulação ao histórico?" ), font=("Segoe UI", 20)).place(x=879, y=500)
    select_tabela_a = tk.CTkButton(janela_solteiro_n_dinheiro_ss_resultado, text="Sim",command=lambda: historico_ordenado(regime, situacao_fiscal, dependentes, contribuicao_social, adse, valor_alimentacao, dias_alimentacao, forma_pagamento, outros, renumeracao, valor_irs, valor_adse, valor_ss, renumeracao_final, invalidez),font=("Segoe UI", 20)).place(x=879, y=550)
    select_tabela_b = tk.CTkButton(janela_solteiro_n_dinheiro_ss_resultado, text="Não",command=lambda: reiniciar_programa(),font=("Segoe UI", 20)).place(x=1079, y=550)



def dependente_1t_n_dinheiro_ss_adse(janela_solteiro_n_dinheiro_ss):
    regime = 1
    situacao_fiscal = 2
    contribuicao_social = 1
    adse = 1
    forma_pagamento = 1
    valor_irs=0
    invalidez = 1
    janela_solteiro_n_dinheiro_ss.withdraw()
    janela_solteiro_n_dinheiro_ss_adse = tk.CTkToplevel()
    janela_solteiro_n_dinheiro_ss_adse.geometry("1400x700")
    janela_solteiro_n_dinheiro_ss_adse.title( "Simulação do ordenado liquido - Trabalhador Dependente - Casado - 1 Titular - Resultado Final")
    texto_topo = tk.CTkLabel(janela_solteiro_n_dinheiro_ss_adse, text="Simulação do ordenado liquido\nTrabalhador Dependente\nCasado - 1 Titular\nResultado Final", font=("Segoe UI", 20)).place(x=550, y=0)
    ordenado1 = float(renumera_log[0])
    dependentes = int(dependentes_log[0])
    alimentacao = float(alimentacao_log[0])
    dias_alimentacao = int(dias_log[0])
    outros = float(outros_log[0])
    if alimentacao < 6:
        excedente_alimentacao = 0
    else:
        excedente_alimentacao = alimentacao-6
    valor_alimentacao = alimentacao*dias_alimentacao
    excedente_alimentacao_dias = excedente_alimentacao*dias_alimentacao
    renumeracao = ordenado1+excedente_alimentacao_dias+outros

    if renumeracao<=762:
        renumeracao_liquida = 762
        taxa = 0
        parcela_dependente = 0
        parcela_abater = 0

    else:
        valor_irs, parcela_abater, taxa, renumeracao_liquida, parcela_dependente = ordenado_casado_1t(dependentes, renumeracao)

    valor_ss = renumeracao*0.11
    valor_adse = renumeracao*0.035

    if valor_irs<0:
        valor_irs = 0
    else:
        valor_irs = valor_irs

    renumeracao_final = renumeracao - valor_adse - valor_ss - valor_irs+valor_alimentacao

    ### SINTESE DE CARACTERISTICAS ###

    escrever_renumeracao = tk.CTkLabel(janela_solteiro_n_dinheiro_ss_adse, text=("Ordenado Base: {} €" .format(ordenado1)), font=("Segoe UI", 20)).place(x=150, y=100)
    escrever_regime = tk.CTkLabel(janela_solteiro_n_dinheiro_ss_adse, text=("Regime: Trabalhador Dependente"), font=("Segoe UI", 20)).place(x=150, y=150)
    escrever_fiscal = tk.CTkLabel(janela_solteiro_n_dinheiro_ss_adse, text = ("Situação Fiscal: Casado - 1 Titular"), font=("Segoe UI", 20)).place(x=150,y=200)
    escrever_dependentes = tk.CTkLabel(janela_solteiro_n_dinheiro_ss_adse, text=("Dependentes: {}".format(dependentes)), font=("Segoe UI", 20)).place(x=150, y=250)
    escrever_social = tk.CTkLabel(janela_solteiro_n_dinheiro_ss_adse, text=("Contribuição Social: Segurança Social"), font=("Segoe UI", 20)).place(x=150, y=300)
    escrever_adse = tk.CTkLabel(janela_solteiro_n_dinheiro_ss_adse, text=("ADSE: Sim"), font=("Segoe UI", 20)).place(x=150, y=350)
    escrever_alimentacao = tk.CTkLabel(janela_solteiro_n_dinheiro_ss_adse, text=("Subsidio de Alimentação: {} €".format(valor_alimentacao)), font=("Segoe UI", 20)).place(x=150, y=400)
    escrever_dias = tk.CTkLabel(janela_solteiro_n_dinheiro_ss_adse, text=("Dias com susbsidio de alimentação: {}".format(dias_alimentacao)), font=("Segoe UI", 20)).place(x=150, y=450)
    escrever_pagamento = tk.CTkLabel(janela_solteiro_n_dinheiro_ss_adse, text=("Forma de pagamento do subsidio de alimentação: Dinheiro"), font=("Segoe UI", 20)).place(x=150, y=500)
    escrever_outros = tk.CTkLabel(janela_solteiro_n_dinheiro_ss_adse, text=("Outros subsidios tributaveis: {} €".format(outros)), font=("Segoe UI", 20)).place(x=150, y=550)
    escrever_invalidez = tk.CTkLabel(janela_solteiro_n_dinheiro_ss_adse, text=("Invalidez ou incapacidade: Não"), font=("Segoe UI", 20)).place(x=150, y=600)

### APRESENTAÇÃO DOS VALORES ###
    texto_descontos = tk.CTkLabel(janela_solteiro_n_dinheiro_ss_adse, text=("Resumo dos descontos"), font=("Segoe UI", 20)) .place(x=879, y=150)
    texto_valor = tk.CTkLabel(janela_solteiro_n_dinheiro_ss_adse, text=("Valor tributável:{:.2f}€ " .format(renumeracao)), font=("Segoe UI", 20)).place(x=879 , y=300)
    texto_irs = tk.CTkLabel(janela_solteiro_n_dinheiro_ss_adse, text=("Retenção na fonte: {:.2f}€" .format(valor_irs)), font=("Segoe UI", 20)).place(x=879 , y=200)
    texto_ss = tk.CTkLabel(janela_solteiro_n_dinheiro_ss_adse, text=("Taxa Social Única: {:.2f}€" .format(valor_ss)), font=("Segoe UI", 20)).place(x=879 , y=250)
    taxa_adse = tk.CTkLabel(janela_solteiro_n_dinheiro_ss_adse, text=("Desconto ADSE: {:.2f}€" .format(valor_adse)), font=("Segoe UI", 20)).place(x=879 , y=350)
    valor_final = tk.CTkLabel(janela_solteiro_n_dinheiro_ss_adse, text=( "Valor após descontos: {:.2f}€" .format(renumeracao_final)), font=("Segoe UI", 20), bg_color = "red").place(x=879 , y=450)

### FINAL - SAIR OU HISTORICO ###
    decidir_historico = tk.CTkLabel(janela_solteiro_n_dinheiro_ss_adse, text=("Deseja adicionar está simulação ao histórico?" ), font=("Segoe UI", 20)).place(x=879, y=500)
    select_tabela_a = tk.CTkButton(janela_solteiro_n_dinheiro_ss_adse, text="Sim",command=lambda: historico_ordenado(regime, situacao_fiscal, dependentes, contribuicao_social, adse, valor_alimentacao, dias_alimentacao, forma_pagamento, outros, renumeracao, valor_irs, valor_adse, valor_ss, renumeracao_final, invalidez),font=("Segoe UI", 20)).place(x=879, y=550)
    select_tabela_b = tk.CTkButton(janela_solteiro_n_dinheiro_ss_adse, text="Não",command=lambda: reiniciar_programa(),font=("Segoe UI", 20)).place(x=1079, y=550)



def dependente_1t_n_dinheiro_ss(janela_solteiro_n_dinheiro):
    janela_solteiro_n_dinheiro.withdraw()
    janela_solteiro_n_dinheiro_ss = tk.CTkToplevel()
    janela_solteiro_n_dinheiro_ss.geometry("1400x700")
    janela_solteiro_n_dinheiro_ss.title("Simulação do ordenado liquido - Trabalhador Dependente - Casado - 1 Titular - Outras contribuições")
    texto_topo = tk.CTkLabel(janela_solteiro_n_dinheiro_ss, text="Simulação do ordenado liquido\nTrabalhador Dependente\nCasado - 1 Titular\nOutras contribuições", font=("Segoe UI", 20)).place(x=550, y=0)
    texto_adse = tk.CTkLabel(janela_solteiro_n_dinheiro_ss, text="É beneficiário da ADSE?", font=("Segoe UI", 20)).place(x=590, y=150)
    botao_sim = tk.CTkButton(janela_solteiro_n_dinheiro_ss, text= "Sim", command=lambda: dependente_1t_n_dinheiro_ss_adse(janela_solteiro_n_dinheiro_ss), font=("Segoe UI", 20)).place(x=530, y=200)
    botao_nao = tk.CTkButton(janela_solteiro_n_dinheiro_ss, text="Não", command=lambda: dependente_1t_n_dinheiro_ss_resultado(janela_solteiro_n_dinheiro_ss), font=("Segoe UI", 20)).place(x=730, y=200)

#
def dependente_1t_n_dinheiro(janela_solteiro_n, pedir_outros, pedir_alimentacao, pedir_dias):
    alimentacao = float(pedir_alimentacao.get())
    alimentacao_log.append(alimentacao)
    dias = float(pedir_dias.get())
    dias_log.append(dias)
    outros = float(pedir_outros.get())
    outros_log.append(outros)
    janela_solteiro_n.withdraw()
    janela_solteiro_n_dinheiro = tk.CTkToplevel()
    janela_solteiro_n_dinheiro.geometry("1400x700")
    janela_solteiro_n_dinheiro.title("Simulação do ordenado liquido - Trabalhador Dependente - Casado - 1 Titular - Outras contribuições")
    texto_topo = tk.CTkLabel(janela_solteiro_n_dinheiro, text="Simulação do ordenado liquido\nTrabalhador Dependente\nCasado - 1 Titular\nOutras contribuições", font=("Segoe UI", 20)).place(x=550, y=0)
    texto_forma = tk.CTkLabel(janela_solteiro_n_dinheiro, text = "Selecione a sua forma de contribuição social", font=("Segoe UI", 20)).place(x=510, y=150)
    botao_ss = tk.CTkButton(janela_solteiro_n_dinheiro, text="Segurança Social", command=lambda:dependente_1t_n_dinheiro_ss(janela_solteiro_n_dinheiro), font=("Segoe UI", 20)) .place(x=606, y=200)
    botao_cga = tk.CTkButton(janela_solteiro_n_dinheiro, text="Caixa Geral de Aposentações", command=lambda: dependente_1t_n_dinheiro_cga(janela_solteiro_n_dinheiro),  font=("Segoe UI",20)) .place(x=560, y=250)


def dependente_1t_n_dinheiro_cga_resultado(janela_solteiro_n_dinheiro_cga):
    regime = 1
    situacao_fiscal = 2
    contribuicao_social = 2
    adse = 2
    forma_pagamento = 1
    valor_irs=0
    invalidez = 1
    valor_adse=0
    janela_solteiro_n_dinheiro_cga.withdraw()
    janela_solteiro_n_dinheiro_cga_resultado = tk.CTkToplevel()
    janela_solteiro_n_dinheiro_cga_resultado.geometry("1400x700")
    janela_solteiro_n_dinheiro_cga_resultado.title( "Simulação do ordenado liquido - Trabalhador Dependente - Casado - 1 Titular - Resultado Final")
    texto_topo = tk.CTkLabel(janela_solteiro_n_dinheiro_cga_resultado, text="Simulação do ordenado liquido\nTrabalhador Dependente\nCasado - 1 Titular\nResultado Final", font=("Segoe UI", 20)).place(x=550, y=0)
    ordenado1 = float(renumera_log[0])
    dependentes = int(dependentes_log[0])
    alimentacao = float(alimentacao_log[0])
    dias_alimentacao = int(dias_log[0])
    outros = float(outros_log[0])
    if alimentacao <6:
        excedente_alimentacao = 0
    else:
        excedente_alimentacao = alimentacao-6
    valor_alimentacao = alimentacao*dias_alimentacao
    excedente_alimentacao_dias = excedente_alimentacao*dias_alimentacao
    renumeracao = ordenado1+excedente_alimentacao_dias+outros

    if renumeracao<=762:
        renumeracao_liquida = 762
        taxa = 0
        parcela_dependente = 0
        parcela_abater = 0

    else:
        valor_irs, parcela_abater, taxa, renumeracao_liquida, parcela_dependente = ordenado_casado_1t(dependentes, renumeracao)
    if valor_irs<0:
        valor_irs = 0
    else:
        valor_irs = valor_irs
    valor_ss = renumeracao*0.11
    renumeracao_final = renumeracao - valor_ss - valor_irs + valor_alimentacao


    ### SINTESE DE CARACTERISTICAS ###

    escrever_renumeracao = tk.CTkLabel(janela_solteiro_n_dinheiro_cga_resultado, text=("Ordenado Base: {} €" .format(ordenado1)), font=("Segoe UI", 20)).place(x=150, y=100)
    escrever_regime = tk.CTkLabel(janela_solteiro_n_dinheiro_cga_resultado, text=("Regime: Trabalhador Dependente"), font=("Segoe UI", 20)).place(x=150, y=150)
    escrever_fiscal = tk.CTkLabel(janela_solteiro_n_dinheiro_cga_resultado, text = ("Situação Fiscal: Casado - 1 Titular"), font=("Segoe UI", 20)).place(x=150,y=200)
    escrever_dependentes = tk.CTkLabel(janela_solteiro_n_dinheiro_cga_resultado, text=("Dependentes: {}".format(dependentes)), font=("Segoe UI", 20)).place(x=150, y=250)
    escrever_social = tk.CTkLabel(janela_solteiro_n_dinheiro_cga_resultado, text=("Contribuição Social: Caixa Geral de Aposentações"), font=("Segoe UI", 20)).place(x=150, y=300)
    escrever_adse = tk.CTkLabel(janela_solteiro_n_dinheiro_cga_resultado, text=("ADSE: Não"), font=("Segoe UI", 20)).place(x=150, y=350)
    escrever_alimentacao = tk.CTkLabel(janela_solteiro_n_dinheiro_cga_resultado, text=("Subsidio de Alimentação: {} €".format(valor_alimentacao)), font=("Segoe UI", 20)).place(x=150, y=400)
    escrever_dias = tk.CTkLabel(janela_solteiro_n_dinheiro_cga_resultado, text=("Dias com susbsidio de alimentação: {}".format(dias_alimentacao)), font=("Segoe UI", 20)).place(x=150, y=450)
    escrever_pagamento = tk.CTkLabel(janela_solteiro_n_dinheiro_cga_resultado, text=("Forma de pagamento do subsidio de alimentação: Dinheiro"), font=("Segoe UI", 20)).place(x=150, y=500)
    escrever_outros = tk.CTkLabel(janela_solteiro_n_dinheiro_cga_resultado, text=("Outros subsidios tributaveis: {} €".format(outros)), font=("Segoe UI", 20)).place(x=150, y=550)
    escrever_invalidez = tk.CTkLabel(janela_solteiro_n_dinheiro_cga_resultado, text=("Invalidez ou incapacidade: Não"), font=("Segoe UI", 20)).place(x=150, y=600)

### APRESENTAÇÃO DOS VALORES ###
    texto_descontos = tk.CTkLabel(janela_solteiro_n_dinheiro_cga_resultado, text=("Resumo dos descontos"), font=("Segoe UI", 20)) .place(x=879, y=150)
    texto_valor = tk.CTkLabel(janela_solteiro_n_dinheiro_cga_resultado, text=("Valor tributável:{:.2f}€ " .format(renumeracao)), font=("Segoe UI", 20)).place(x=879 , y=300)
    texto_irs = tk.CTkLabel(janela_solteiro_n_dinheiro_cga_resultado, text=("Retenção na fonte: {:.2f}€" .format(valor_irs)), font=("Segoe UI", 20)).place(x=879 , y=200)
    texto_ss = tk.CTkLabel(janela_solteiro_n_dinheiro_cga_resultado, text=("Taxa Social Única: {:.2f}€" .format(valor_ss)), font=("Segoe UI", 20)).place(x=879 , y=250)
    valor_final = tk.CTkLabel(janela_solteiro_n_dinheiro_cga_resultado, text=( "Valor após descontos: {:.2f}€" .format(renumeracao_final)), font=("Segoe UI", 20), bg_color = "red").place(x=879 , y=300)

### FINAL - SAIR OU HISTORICO ###
    decidir_historico = tk.CTkLabel(janela_solteiro_n_dinheiro_cga_resultado, text=("Deseja adicionar está simulação ao histórico?" ), font=("Segoe UI", 20)).place(x=879, y=500)
    select_tabela_a = tk.CTkButton(janela_solteiro_n_dinheiro_cga_resultado, text="Sim",command=lambda: historico_ordenado(regime, situacao_fiscal, dependentes, contribuicao_social, adse, valor_alimentacao, dias_alimentacao, forma_pagamento, outros, renumeracao, valor_irs, valor_adse, valor_ss, renumeracao_final, invalidez),font=("Segoe UI", 20)).place(x=879, y=550)
    select_tabela_b = tk.CTkButton(janela_solteiro_n_dinheiro_cga_resultado, text="Não",command=lambda: reiniciar_programa(),font=("Segoe UI", 20)).place(x=1079, y=550)



def dependente_1t_n_dinheiro_cga_adse(janela_solteiro_n_dinheiro_cga):
    regime = 1
    situacao_fiscal = 2
    contribuicao_social = 2
    adse = 1
    forma_pagamento = 1
    valor_irs=0
    invalidez = 1
    janela_solteiro_n_dinheiro_cga.withdraw()
    janela_solteiro_n_dinheiro_cga_adse = tk.CTkToplevel()
    janela_solteiro_n_dinheiro_cga_adse.geometry("1400x700")
    janela_solteiro_n_dinheiro_cga_adse.title( "Simulação do ordenado liquido - Trabalhador Dependente - Casado - 1 Titular - Resultado Final")
    texto_topo = tk.CTkLabel(janela_solteiro_n_dinheiro_cga_adse, text="Simulação do ordenado liquido\nTrabalhador Dependente\nCasado - 1 Titular\nResultado Final", font=("Segoe UI", 20)).place(x=550, y=0)
    ordenado1 = float(renumera_log[0])
    dependentes = int(dependentes_log[0])
    alimentacao = float(alimentacao_log[0])
    dias_alimentacao = int(dias_log[0])
    outros = float(outros_log[0])
    if alimentacao < 6:
        excedente_alimentacao = 0
    else:
        excedente_alimentacao = alimentacao-6
    valor_alimentacao = alimentacao*dias_alimentacao
    excedente_alimentacao_dias = excedente_alimentacao*dias_alimentacao
    renumeracao = ordenado1+excedente_alimentacao_dias+outros

    if renumeracao<=762:
        renumeracao_liquida = 762
        taxa = 0
        parcela_dependente = 0
        parcela_abater = 0

    else:
        valor_irs, parcela_abater, taxa, renumeracao_liquida, parcela_dependente = ordenado_casado_1t(dependentes, renumeracao)

    valor_ss = renumeracao*0.11
    valor_adse = renumeracao*0.035
    if valor_irs<0:
        valor_irs = 0
    else:
        valor_irs = valor_irs
    renumeracao_final = renumeracao - valor_adse - valor_ss - valor_irs+valor_alimentacao

    ### SINTESE DE CARACTERISTICAS ###

    escrever_renumeracao = tk.CTkLabel(janela_solteiro_n_dinheiro_cga_adse, text=("Ordenado Base: {} €" .format(ordenado1)), font=("Segoe UI", 20)).place(x=150, y=100)
    escrever_regime = tk.CTkLabel(janela_solteiro_n_dinheiro_cga_adse, text=("Regime: Trabalhador Dependente"), font=("Segoe UI", 20)).place(x=150, y=150)
    escrever_fiscal = tk.CTkLabel(janela_solteiro_n_dinheiro_cga_adse, text = ("Situação Fiscal: Casado - 1 Titular"), font=("Segoe UI", 20)).place(x=150,y=200)
    escrever_dependentes = tk.CTkLabel(janela_solteiro_n_dinheiro_cga_adse, text=("Dependentes: {}".format(dependentes)), font=("Segoe UI", 20)).place(x=150, y=250)
    escrever_social = tk.CTkLabel(janela_solteiro_n_dinheiro_cga_adse, text=("Contribuição Social: Caixa Geral de Aposentações"), font=("Segoe UI", 20)).place(x=150, y=300)
    escrever_adse = tk.CTkLabel(janela_solteiro_n_dinheiro_cga_adse, text=("ADSE: Sim"), font=("Segoe UI", 20)).place(x=150, y=350)
    escrever_alimentacao = tk.CTkLabel(janela_solteiro_n_dinheiro_cga_adse, text=("Subsidio de Alimentação: {} €".format(valor_alimentacao)), font=("Segoe UI", 20)).place(x=150, y=400)
    escrever_dias = tk.CTkLabel(janela_solteiro_n_dinheiro_cga_adse, text=("Dias com susbsidio de alimentação: {}".format(dias_alimentacao)), font=("Segoe UI", 20)).place(x=150, y=450)
    escrever_pagamento = tk.CTkLabel(janela_solteiro_n_dinheiro_cga_adse, text=("Forma de pagamento do subsidio de alimentação: Dinheiro"), font=("Segoe UI", 20)).place(x=150, y=500)
    escrever_outros = tk.CTkLabel(janela_solteiro_n_dinheiro_cga_adse, text=("Outros subsidios tributaveis: {} €".format(outros)), font=("Segoe UI", 20)).place(x=150, y=550)
    escrever_invalidez = tk.CTkLabel(janela_solteiro_n_dinheiro_cga_adse, text=("Invalidez ou incapacidade: Não"), font=("Segoe UI", 20)).place(x=150, y=600)

### APRESENTAÇÃO DOS VALORES ###
    texto_descontos = tk.CTkLabel(janela_solteiro_n_dinheiro_cga_adse, text=("Resumo dos descontos"), font=("Segoe UI", 20)) .place(x=879, y=150)
    texto_valor = tk.CTkLabel(janela_solteiro_n_dinheiro_cga_adse, text=("Valor tributável:{:.2f}€ " .format(renumeracao)), font=("Segoe UI", 20)).place(x=879 , y=300)
    texto_irs = tk.CTkLabel(janela_solteiro_n_dinheiro_cga_adse, text=("Retenção na fonte: {:.2f}€" .format(valor_irs)), font=("Segoe UI", 20)).place(x=879 , y=200)
    texto_ss = tk.CTkLabel(janela_solteiro_n_dinheiro_cga_adse, text=("Taxa Social Única: {:.2f}€" .format(valor_ss)), font=("Segoe UI", 20)).place(x=879 , y=250)
    taxa_adse = tk.CTkLabel(janela_solteiro_n_dinheiro_cga_adse, text=("Desconto ADSE: {:.2f}€" .format(valor_adse)), font=("Segoe UI", 20)).place(x=879 , y=350)
    valor_final = tk.CTkLabel(janela_solteiro_n_dinheiro_cga_adse, text=( "Valor após descontos: {:.2f}€" .format(renumeracao_final)), font=("Segoe UI", 20), bg_color = "red").place(x=879 , y=450)

### FINAL - SAIR OU HISTORICO ###
    decidir_historico = tk.CTkLabel(janela_solteiro_n_dinheiro_cga_adse, text=("Deseja adicionar está simulação ao histórico?" ), font=("Segoe UI", 20)).place(x=879, y=500)
    select_tabela_a = tk.CTkButton(janela_solteiro_n_dinheiro_cga_adse, text="Sim",command=lambda: historico_ordenado(regime, situacao_fiscal, dependentes, contribuicao_social, adse, valor_alimentacao, dias_alimentacao, forma_pagamento, outros, renumeracao, valor_irs, valor_adse, valor_ss, renumeracao_final, invalidez),font=("Segoe UI", 20)).place(x=879, y=550)
    select_tabela_b = tk.CTkButton(janela_solteiro_n_dinheiro_cga_adse, text="Não",command=lambda: reiniciar_programa(),font=("Segoe UI", 20)).place(x=1079, y=550)



def dependente_1t_n_dinheiro_cga(janela_solteiro_n_dinheiro):
    janela_solteiro_n_dinheiro.withdraw()
    janela_solteiro_n_dinheiro_cga = tk.CTkToplevel()
    janela_solteiro_n_dinheiro_cga.geometry("1400x700")
    janela_solteiro_n_dinheiro_cga.title("Simulação do ordenado liquido - Trabalhador Dependente - Casado - 1 Titular - Outras contribuições")
    texto_topo = tk.CTkLabel(janela_solteiro_n_dinheiro_cga, text="Simulação do ordenado liquido\nTrabalhador Dependente\nCasado - 1 Titular\nOutras contribuições", font=("Segoe UI", 20)).place(x=550, y=0)
    texto_adse = tk.CTkLabel(janela_solteiro_n_dinheiro_cga, text="É beneficiário da ADSE?", font=("Segoe UI", 20)).place(x=590, y=150)
    botao_sim = tk.CTkButton(janela_solteiro_n_dinheiro_cga, text= "Sim", command=lambda: dependente_1t_n_dinheiro_cga_adse(janela_solteiro_n_dinheiro_cga), font=("Segoe UI", 20)).place(x=530, y=200)
    botao_nao = tk.CTkButton(janela_solteiro_n_dinheiro_cga, text="Não", command=lambda: dependente_1t_n_dinheiro_cga_resultado(janela_solteiro_n_dinheiro_cga), font=("Segoe UI", 20)).place(x=730, y=200)


def dependente_1t_n_dinheiro_ss_resultado(janela_solteiro_n_dinheiro_ss):
    regime = 1
    situacao_fiscal = 2
    contribuicao_social = 1
    adse = 2
    forma_pagamento = 1
    valor_irs=0
    invalidez = 1
    valor_adse=0
    janela_solteiro_n_dinheiro_ss.withdraw()
    janela_solteiro_n_dinheiro_ss_resultado = tk.CTkToplevel()
    janela_solteiro_n_dinheiro_ss_resultado.geometry("1400x700")
    janela_solteiro_n_dinheiro_ss_resultado.title( "Simulação do ordenado liquido - Trabalhador Dependente - Casado - 1 Titular - Resultado Final")
    texto_topo = tk.CTkLabel(janela_solteiro_n_dinheiro_ss_resultado, text="Simulação do ordenado liquido\nTrabalhador Dependente\nCasado - 1 Titular\nResultado Final", font=("Segoe UI", 20)).place(x=550, y=0)
    ordenado1 = float(renumera_log[0])
    dependentes = int(dependentes_log[0])
    alimentacao = float(alimentacao_log[0])
    dias_alimentacao = int(dias_log[0])
    outros = float(outros_log[0])
    if alimentacao <6:
        excedente_alimentacao = 0
    else:
        excedente_alimentacao = alimentacao-6
    valor_alimentacao = alimentacao*dias_alimentacao
    excedente_alimentacao_dias = excedente_alimentacao*dias_alimentacao
    renumeracao = ordenado1+excedente_alimentacao_dias+outros

    if renumeracao<=762:
        renumeracao_liquida = 762
        taxa = 0
        parcela_dependente = 0
        parcela_abater = 0

    else:
        valor_irs, parcela_abater, taxa, renumeracao_liquida, parcela_dependente = ordenado_casado_1t(dependentes, renumeracao)
    if valor_irs<0:
        valor_irs = 0
    else:
        valor_irs = valor_irs
    valor_ss = renumeracao*0.11
    renumeracao_final = renumeracao - valor_ss - valor_irs + valor_alimentacao


    ### SINTESE DE CARACTERISTICAS ###

    escrever_renumeracao = tk.CTkLabel(janela_solteiro_n_dinheiro_ss_resultado, text=("Ordenado Base: {} €" .format(ordenado1)), font=("Segoe UI", 20)).place(x=150, y=100)
    escrever_regime = tk.CTkLabel(janela_solteiro_n_dinheiro_ss_resultado, text=("Regime: Trabalhador Dependente"), font=("Segoe UI", 20)).place(x=150, y=150)
    escrever_fiscal = tk.CTkLabel(janela_solteiro_n_dinheiro_ss_resultado, text = ("Situação Fiscal: Casado - 1 Titular"), font=("Segoe UI", 20)).place(x=150,y=200)
    escrever_dependentes = tk.CTkLabel(janela_solteiro_n_dinheiro_ss_resultado, text=("Dependentes: {}".format(dependentes)), font=("Segoe UI", 20)).place(x=150, y=250)
    escrever_social = tk.CTkLabel(janela_solteiro_n_dinheiro_ss_resultado, text=("Contribuição Social: Segurança Social"), font=("Segoe UI", 20)).place(x=150, y=300)
    escrever_adse = tk.CTkLabel(janela_solteiro_n_dinheiro_ss_resultado, text=("ADSE: Não"), font=("Segoe UI", 20)).place(x=150, y=350)
    escrever_alimentacao = tk.CTkLabel(janela_solteiro_n_dinheiro_ss_resultado, text=("Subsidio de Alimentação: {} €".format(valor_alimentacao)), font=("Segoe UI", 20)).place(x=150, y=400)
    escrever_dias = tk.CTkLabel(janela_solteiro_n_dinheiro_ss_resultado, text=("Dias com susbsidio de alimentação: {}".format(dias_alimentacao)), font=("Segoe UI", 20)).place(x=150, y=450)
    escrever_pagamento = tk.CTkLabel(janela_solteiro_n_dinheiro_ss_resultado, text=("Forma de pagamento do subsidio de alimentação: Dinheiro"), font=("Segoe UI", 20)).place(x=150, y=500)
    escrever_outros = tk.CTkLabel(janela_solteiro_n_dinheiro_ss_resultado, text=("Outros subsidios tributaveis: {} €".format(outros)), font=("Segoe UI", 20)).place(x=150, y=550)
    escrever_invalidez = tk.CTkLabel(janela_solteiro_n_dinheiro_ss_resultado, text=("Invalidez ou incapacidade: Não"), font=("Segoe UI", 20)).place(x=150, y=600)

### APRESENTAÇÃO DOS VALORES ###
    texto_descontos = tk.CTkLabel(janela_solteiro_n_dinheiro_ss_resultado, text=("Resumo dos descontos"), font=("Segoe UI", 20)) .place(x=879, y=150)
    texto_valor = tk.CTkLabel(janela_solteiro_n_dinheiro_ss_resultado, text=("Valor tributável:{:.2f}€ " .format(renumeracao)), font=("Segoe UI", 20)).place(x=879 , y=300)
    texto_irs = tk.CTkLabel(janela_solteiro_n_dinheiro_ss_resultado, text=("Retenção na fonte: {:.2f}€" .format(valor_irs)), font=("Segoe UI", 20)).place(x=879 , y=200)
    texto_ss = tk.CTkLabel(janela_solteiro_n_dinheiro_ss_resultado, text=("Taxa Social Única: {:.2f}€" .format(valor_ss)), font=("Segoe UI", 20)).place(x=879 , y=250)
    valor_final = tk.CTkLabel(janela_solteiro_n_dinheiro_ss_resultado, text=( "Valor após descontos: {:.2f}€" .format(renumeracao_final)), font=("Segoe UI", 20), bg_color = "red").place(x=879 , y=300)

### FINAL - SAIR OU HISTORICO ###
    decidir_historico = tk.CTkLabel(janela_solteiro_n_dinheiro_ss_resultado, text=("Deseja adicionar está simulação ao histórico?" ), font=("Segoe UI", 20)).place(x=879, y=500)
    select_tabela_a = tk.CTkButton(janela_solteiro_n_dinheiro_ss_resultado, text="Sim",command=lambda: historico_ordenado(regime, situacao_fiscal, dependentes, contribuicao_social, adse, valor_alimentacao, dias_alimentacao, forma_pagamento, outros, renumeracao, valor_irs, valor_adse, valor_ss, renumeracao_final, invalidez),font=("Segoe UI", 20)).place(x=879, y=550)
    select_tabela_b = tk.CTkButton(janela_solteiro_n_dinheiro_ss_resultado, text="Não",command=lambda: reiniciar_programa(),font=("Segoe UI", 20)).place(x=1079, y=550)



def dependente_1t_n_dinheiro_ss_adse(janela_solteiro_n_dinheiro_ss):
    regime = 1
    situacao_fiscal = 2
    contribuicao_social = 1
    adse = 1
    forma_pagamento = 1
    valor_irs=0
    invalidez = 1
    janela_solteiro_n_dinheiro_ss.withdraw()
    janela_solteiro_n_dinheiro_ss_adse = tk.CTkToplevel()
    janela_solteiro_n_dinheiro_ss_adse.geometry("1400x700")
    janela_solteiro_n_dinheiro_ss_adse.title( "Simulação do ordenado liquido - Trabalhador Dependente - Casado - 1 Titular - Resultado Final")
    texto_topo = tk.CTkLabel(janela_solteiro_n_dinheiro_ss_adse, text="Simulação do ordenado liquido\nTrabalhador Dependente\nCasado - 1 Titular\nResultado Final", font=("Segoe UI", 20)).place(x=550, y=0)
    ordenado1 = float(renumera_log[0])
    dependentes = int(dependentes_log[0])
    alimentacao = float(alimentacao_log[0])
    dias_alimentacao = int(dias_log[0])
    outros = float(outros_log[0])
    if alimentacao < 6:
        excedente_alimentacao = 0
    else:
        excedente_alimentacao = alimentacao-6
    valor_alimentacao = alimentacao*dias_alimentacao
    excedente_alimentacao_dias = excedente_alimentacao*dias_alimentacao
    renumeracao = ordenado1+excedente_alimentacao_dias+outros

    if renumeracao<=762:
        renumeracao_liquida = 762
        taxa = 0
        parcela_dependente = 0
        parcela_abater = 0

    else:
        valor_irs, parcela_abater, taxa, renumeracao_liquida, parcela_dependente = ordenado_casado_1t(dependentes, renumeracao)

    valor_ss = renumeracao*0.11
    valor_adse = renumeracao*0.035

    if valor_irs<0:
        valor_irs = 0
    else:
        valor_irs = valor_irs

    renumeracao_final = renumeracao - valor_adse - valor_ss - valor_irs+valor_alimentacao

    ### SINTESE DE CARACTERISTICAS ###

    escrever_renumeracao = tk.CTkLabel(janela_solteiro_n_dinheiro_ss_adse, text=("Ordenado Base: {} €" .format(ordenado1)), font=("Segoe UI", 20)).place(x=150, y=100)
    escrever_regime = tk.CTkLabel(janela_solteiro_n_dinheiro_ss_adse, text=("Regime: Trabalhador Dependente"), font=("Segoe UI", 20)).place(x=150, y=150)
    escrever_fiscal = tk.CTkLabel(janela_solteiro_n_dinheiro_ss_adse, text = ("Situação Fiscal: Casado - 1 Titular"), font=("Segoe UI", 20)).place(x=150,y=200)
    escrever_dependentes = tk.CTkLabel(janela_solteiro_n_dinheiro_ss_adse, text=("Dependentes: {}".format(dependentes)), font=("Segoe UI", 20)).place(x=150, y=250)
    escrever_social = tk.CTkLabel(janela_solteiro_n_dinheiro_ss_adse, text=("Contribuição Social: Segurança Social"), font=("Segoe UI", 20)).place(x=150, y=300)
    escrever_adse = tk.CTkLabel(janela_solteiro_n_dinheiro_ss_adse, text=("ADSE: Sim"), font=("Segoe UI", 20)).place(x=150, y=350)
    escrever_alimentacao = tk.CTkLabel(janela_solteiro_n_dinheiro_ss_adse, text=("Subsidio de Alimentação: {} €".format(valor_alimentacao)), font=("Segoe UI", 20)).place(x=150, y=400)
    escrever_dias = tk.CTkLabel(janela_solteiro_n_dinheiro_ss_adse, text=("Dias com susbsidio de alimentação: {}".format(dias_alimentacao)), font=("Segoe UI", 20)).place(x=150, y=450)
    escrever_pagamento = tk.CTkLabel(janela_solteiro_n_dinheiro_ss_adse, text=("Forma de pagamento do subsidio de alimentação: Dinheiro"), font=("Segoe UI", 20)).place(x=150, y=500)
    escrever_outros = tk.CTkLabel(janela_solteiro_n_dinheiro_ss_adse, text=("Outros subsidios tributaveis: {} €".format(outros)), font=("Segoe UI", 20)).place(x=150, y=550)
    escrever_invalidez = tk.CTkLabel(janela_solteiro_n_dinheiro_ss_adse, text=("Invalidez ou incapacidade: Não"), font=("Segoe UI", 20)).place(x=150, y=600)

### APRESENTAÇÃO DOS VALORES ###
    texto_descontos = tk.CTkLabel(janela_solteiro_n_dinheiro_ss_adse, text=("Resumo dos descontos"), font=("Segoe UI", 20)) .place(x=879, y=150)
    texto_valor = tk.CTkLabel(janela_solteiro_n_dinheiro_ss_adse, text=("Valor tributável:{:.2f}€ " .format(renumeracao)), font=("Segoe UI", 20)).place(x=879 , y=300)
    texto_irs = tk.CTkLabel(janela_solteiro_n_dinheiro_ss_adse, text=("Retenção na fonte: {:.2f}€" .format(valor_irs)), font=("Segoe UI", 20)).place(x=879 , y=200)
    texto_ss = tk.CTkLabel(janela_solteiro_n_dinheiro_ss_adse, text=("Taxa Social Única: {:.2f}€" .format(valor_ss)), font=("Segoe UI", 20)).place(x=879 , y=250)
    taxa_adse = tk.CTkLabel(janela_solteiro_n_dinheiro_ss_adse, text=("Desconto ADSE: {:.2f}€" .format(valor_adse)), font=("Segoe UI", 20)).place(x=879 , y=350)
    valor_final = tk.CTkLabel(janela_solteiro_n_dinheiro_ss_adse, text=( "Valor após descontos: {:.2f}€" .format(renumeracao_final)), font=("Segoe UI", 20), bg_color = "red").place(x=879 , y=450)

### FINAL - SAIR OU HISTORICO ###
    decidir_historico = tk.CTkLabel(janela_solteiro_n_dinheiro_ss_adse, text=("Deseja adicionar está simulação ao histórico?" ), font=("Segoe UI", 20)).place(x=879, y=500)
    select_tabela_a = tk.CTkButton(janela_solteiro_n_dinheiro_ss_adse, text="Sim",command=lambda: historico_ordenado(regime, situacao_fiscal, dependentes, contribuicao_social, adse, valor_alimentacao, dias_alimentacao, forma_pagamento, outros, renumeracao, valor_irs, valor_adse, valor_ss, renumeracao_final, invalidez),font=("Segoe UI", 20)).place(x=879, y=550)
    select_tabela_b = tk.CTkButton(janela_solteiro_n_dinheiro_ss_adse, text="Não",command=lambda: reiniciar_programa(),font=("Segoe UI", 20)).place(x=1079, y=550)



def dependente_1t_n_dinheiro_ss(janela_solteiro_n_dinheiro):
    janela_solteiro_n_dinheiro.withdraw()
    janela_solteiro_n_dinheiro_ss = tk.CTkToplevel()
    janela_solteiro_n_dinheiro_ss.geometry("1400x700")
    janela_solteiro_n_dinheiro_ss.title("Simulação do ordenado liquido - Trabalhador Dependente - Casado - 1 Titular - Outras contribuições")
    texto_topo = tk.CTkLabel(janela_solteiro_n_dinheiro_ss, text="Simulação do ordenado liquido\nTrabalhador Dependente\nCasado - 1 Titular\nOutras contribuições", font=("Segoe UI", 20)).place(x=550, y=0)
    texto_adse = tk.CTkLabel(janela_solteiro_n_dinheiro_ss, text="É beneficiário da ADSE?", font=("Segoe UI", 20)).place(x=590, y=150)
    botao_sim = tk.CTkButton(janela_solteiro_n_dinheiro_ss, text= "Sim", command=lambda: dependente_1t_n_dinheiro_ss_adse(janela_solteiro_n_dinheiro_ss), font=("Segoe UI", 20)).place(x=530, y=200)
    botao_nao = tk.CTkButton(janela_solteiro_n_dinheiro_ss, text="Não", command=lambda: dependente_1t_n_dinheiro_ss_resultado(janela_solteiro_n_dinheiro_ss), font=("Segoe UI", 20)).place(x=730, y=200)


def dependente_1t_n_dinheiro(janela_solteiro_n, pedir_outros, pedir_alimentacao, pedir_dias):
    alimentacao = float(pedir_alimentacao.get())
    alimentacao_log.append(alimentacao)
    dias = float(pedir_dias.get())
    dias_log.append(dias)
    outros = float(pedir_outros.get())
    outros_log.append(outros)
    janela_solteiro_n.withdraw()
    janela_solteiro_n_dinheiro = tk.CTkToplevel()
    janela_solteiro_n_dinheiro.geometry("1400x700")
    janela_solteiro_n_dinheiro.title("Simulação do ordenado liquido - Trabalhador Dependente - Casado - 1 Titular - Outras contribuições")
    texto_topo = tk.CTkLabel(janela_solteiro_n_dinheiro, text="Simulação do ordenado liquido\nTrabalhador Dependente\nCasado - 1 Titular\nOutras contribuições", font=("Segoe UI", 20)).place(x=550, y=0)
    texto_forma = tk.CTkLabel(janela_solteiro_n_dinheiro, text = "Selecione a sua forma de contribuição social", font=("Segoe UI", 20)).place(x=510, y=150)
    botao_ss = tk.CTkButton(janela_solteiro_n_dinheiro, text="Segurança Social", command=lambda:dependente_1t_n_dinheiro_ss(janela_solteiro_n_dinheiro), font=("Segoe UI", 20)) .place(x=606, y=200)
    botao_cga = tk.CTkButton(janela_solteiro_n_dinheiro, text="Caixa Geral de Aposentações", command=lambda: dependente_1t_n_dinheiro_cga(janela_solteiro_n_dinheiro),  font=("Segoe UI",20)) .place(x=560, y=250)

def dependente_1t_n(janela_dependente_solteiro, pedir_renumeracao_base):

    ordenado2 = float(pedir_renumeracao_base.get())
    renumera_log.append(ordenado2)
    janela_dependente_solteiro.withdraw()
    janela_solteiro_n = tk.CTkToplevel()
    janela_solteiro_n.geometry("1400x700")
    janela_solteiro_n.title("Simulação do ordenado liquido - Trabalhador Dependente - Casado - 1 Titular - Subsidios")
    texto_topo = tk.CTkLabel(janela_solteiro_n,text="Simulação do ordenado liquido\nTrabalhador Dependente\nCasado - 1 Titular", font=("Segoe UI", 20)).place(x=550, y=0)
    texto_alimentacao = tk.CTkLabel(janela_solteiro_n,text="Insira o valor diário do subsidio de alimentação", font=("Segoe UI", 20)).place(x=490, y=100)
    pedir_alimentacao = tk.CTkEntry(janela_solteiro_n, placeholder_text= "Valor", font=("Segoe UI",20))
    pedir_alimentacao.place(x=636, y=150)
    texto_dias = tk.CTkLabel(janela_solteiro_n,text="Insira o número de dias com subsidio de alimentação", font=("Segoe UI", 20)).place(x=475, y=200)
    pedir_dias = tk.CTkEntry(janela_solteiro_n, placeholder_text="Dias", font=("Segoe UI", 20))
    pedir_dias.place(x=636, y=250)
    texto_outros = tk.CTkLabel(janela_solteiro_n, text = "Insira o valor de outros subsidios", font=("Segoe UI",20)) .place(x=550,y=300)
    pedir_outros = tk.CTkEntry(janela_solteiro_n, placeholder_text= "Valor", font=("Segoe UI",20))
    pedir_outros.place(x=636,y=350)
    texto_pag_alimentacao = tk.CTkLabel(janela_solteiro_n, text = "Selecione a forma de pagamento do subsidio de alimentacão", font=("Segoe UI", 20)) .place(x=450, y=400)
    botao_dinheiro = tk.CTkButton(janela_solteiro_n, text = "Dinheiro", font=("Segoe UI", 20), command=lambda: dependente_1t_n_dinheiro(janela_solteiro_n, pedir_outros, pedir_alimentacao, pedir_dias)) .place(x=490, y=450)
    botao_cartao = tk.CTkButton(janela_solteiro_n, text="Cartão/Vale de refeição", command=lambda:dependente_1t_n_vale(janela_solteiro_n, pedir_outros, pedir_alimentacao, pedir_dias),font=("Segoe UI", 20)) .place(x=690, y=450)

############################################ INVALIDEZ ####################


def dependente_1t_s_vale_cga_resultado(janela_solteiro_n_vale_cga):
    regime = 1
    situacao_fiscal = 2
    contribuicao_social = 2
    adse = 2
    forma_pagamento = 2
    valor_irs=0
    invalidez = 2
    valor_adse=0
    janela_solteiro_n_vale_cga.withdraw()
    janela_solteiro_n_vale_cga_resultado = tk.CTkToplevel()
    janela_solteiro_n_vale_cga_resultado.geometry("1400x700")
    janela_solteiro_n_vale_cga_resultado.title( "Simulação do ordenado liquido - Trabalhador Dependente - Casado - 1 Titular  - Resultado Final")
    texto_topo = tk.CTkLabel(janela_solteiro_n_vale_cga_resultado, text="Simulação do ordenado liquido\nTrabalhador Dependente\nCasado - 1 Titular\nResultado Final", font=("Segoe UI", 20)).place(x=550, y=0)
    ordenado1 = float(renumera_log[0])
    dependentes = int(dependentes_log[0])
    alimentacao = float(alimentacao_log[0])
    dias_alimentacao = int(dias_log[0])
    outros = float(outros_log[0])
    if alimentacao < 9.6:
        excedente_alimentacao = 0
    else:
        excedente_alimentacao = alimentacao-9.6
    valor_alimentacao = alimentacao*dias_alimentacao
    excedente_alimentacao_dias = excedente_alimentacao*dias_alimentacao
    renumeracao = ordenado1+excedente_alimentacao_dias+outros


    valor_irs, parcela_abater, taxa, renumeracao_liquida, parcela_dependente = ordenado_casado_1t_invalidez(dependentes, renumeracao)
    if valor_irs<0:
        valor_irs = 0
    else:
        valor_irs = valor_irs
    valor_ss = renumeracao*0.11
    renumeracao_final = renumeracao - valor_ss - valor_irs + valor_alimentacao


    ### SINTESE DE CARACTERISTICAS ###

    escrever_renumeracao = tk.CTkLabel(janela_solteiro_n_vale_cga_resultado, text=("Ordenado Base: {} €" .format(ordenado1)), font=("Segoe UI", 20)).place(x=150, y=100)
    escrever_regime = tk.CTkLabel(janela_solteiro_n_vale_cga_resultado, text=("Regime: Trabalhador Dependente"), font=("Segoe UI", 20)).place(x=150, y=150)
    escrever_fiscal = tk.CTkLabel(janela_solteiro_n_vale_cga_resultado, text = ("Situação Fiscal: Casado - 1 Titular"), font=("Segoe UI", 20)).place(x=150,y=200)
    escrever_dependentes = tk.CTkLabel(janela_solteiro_n_vale_cga_resultado, text=("Dependentes: {}".format(dependentes)), font=("Segoe UI", 20)).place(x=150, y=250)
    escrever_social = tk.CTkLabel(janela_solteiro_n_vale_cga_resultado, text=("Contribuição Social: Caixa Geral de Aposentações"), font=("Segoe UI", 20)).place(x=150, y=300)
    escrever_adse = tk.CTkLabel(janela_solteiro_n_vale_cga_resultado, text=("ADSE: Não"), font=("Segoe UI", 20)).place(x=150, y=350)
    escrever_alimentacao = tk.CTkLabel(janela_solteiro_n_vale_cga_resultado, text=("Subsidio de Alimentação: {} €".format(valor_alimentacao)), font=("Segoe UI", 20)).place(x=150, y=400)
    escrever_dias = tk.CTkLabel(janela_solteiro_n_vale_cga_resultado, text=("Dias com susbsidio de alimentação: {}".format(dias_alimentacao)), font=("Segoe UI", 20)).place(x=150, y=450)
    escrever_pagamento = tk.CTkLabel(janela_solteiro_n_vale_cga_resultado, text=("Forma de pagamento do subsidio de alimentação: Vale/Cartão de refeição"), font=("Segoe UI", 20)).place(x=150, y=500)
    escrever_outros = tk.CTkLabel(janela_solteiro_n_vale_cga_resultado, text=("Outros subsidios tributaveis: {} €".format(outros)), font=("Segoe UI", 20)).place(x=150, y=550)
    escrever_invalidez = tk.CTkLabel(janela_solteiro_n_vale_cga_resultado, text=("Invalidez ou incapacidade: Sim"), font=("Segoe UI", 20)).place(x=150, y=600)

### APRESENTAÇÃO DOS VALORES ###
    texto_descontos = tk.CTkLabel(janela_solteiro_n_vale_cga_resultado, text=("Resumo dos descontos"), font=("Segoe UI", 20)) .place(x=879, y=150)
    texto_valor = tk.CTkLabel(janela_solteiro_n_vale_cga_resultado, text=("Valor tributável:{:.2f}€ " .format(renumeracao)), font=("Segoe UI", 20)).place(x=879 , y=300)
    texto_irs = tk.CTkLabel(janela_solteiro_n_vale_cga_resultado, text=("Retenção na fonte: {:.2f}€" .format(valor_irs)), font=("Segoe UI", 20)).place(x=879 , y=200)
    texto_ss = tk.CTkLabel(janela_solteiro_n_vale_cga_resultado, text=("Taxa Social Única: {:.2f}€" .format(valor_ss)), font=("Segoe UI", 20)).place(x=879 , y=250)
    valor_final = tk.CTkLabel(janela_solteiro_n_vale_cga_resultado, text=( "Valor após descontos: {:.2f}€" .format(renumeracao_final)), font=("Segoe UI", 20), bg_color = "red").place(x=879 , y=300)

### FINAL - SAIR OU HISTORICO ###
    decidir_historico = tk.CTkLabel(janela_solteiro_n_vale_cga_resultado, text=("Deseja adicionar está simulação ao histórico?" ), font=("Segoe UI", 20)).place(x=879, y=500)
    select_tabela_a = tk.CTkButton(janela_solteiro_n_vale_cga_resultado, text="Sim",command=lambda: historico_ordenado(regime, situacao_fiscal, dependentes, contribuicao_social, adse, valor_alimentacao, dias_alimentacao, forma_pagamento, outros, renumeracao, valor_irs, valor_adse, valor_ss, renumeracao_final, invalidez),font=("Segoe UI", 20)).place(x=879, y=550)
    select_tabela_b = tk.CTkButton(janela_solteiro_n_vale_cga_resultado, text="Não",command=lambda: reiniciar_programa(),font=("Segoe UI", 20)).place(x=1079, y=550)



def dependente_1t_s_vale_cga_adse(janela_solteiro_n_vale_cga):
    regime = 1
    situacao_fiscal = 2
    contribuicao_social = 2
    adse = 1
    forma_pagamento = 2
    valor_irs=0
    invalidez = 2
    janela_solteiro_n_vale_cga.withdraw()
    janela_solteiro_n_vale_cga_adse = tk.CTkToplevel()
    janela_solteiro_n_vale_cga_adse.geometry("1400x700")
    janela_solteiro_n_vale_cga_adse.title( "Simulação do ordenado liquido - Trabalhador Dependente - Casado - 1 Titular  - Resultado Final")
    texto_topo = tk.CTkLabel(janela_solteiro_n_vale_cga_adse, text="Simulação do ordenado liquido\nTrabalhador Dependente\nCasado - 1 Titular\nResultado Final", font=("Segoe UI", 20)).place(x=550, y=0)
    ordenado1 = float(renumera_log[0])
    dependentes = int(dependentes_log[0])
    alimentacao = float(alimentacao_log[0])
    dias_alimentacao = int(dias_log[0])
    outros = float(outros_log[0])
    if alimentacao < 9.6:
        excedente_alimentacao = 0
    else:
        excedente_alimentacao = alimentacao-9.6
    valor_alimentacao = alimentacao*dias_alimentacao
    excedente_alimentacao_dias = excedente_alimentacao*dias_alimentacao
    renumeracao = ordenado1+excedente_alimentacao_dias+outros


    valor_irs, parcela_abater, taxa, renumeracao_liquida, parcela_dependente = ordenado_casado_1t_invalidez(dependentes, renumeracao)

    valor_ss = renumeracao*0.11
    valor_adse = renumeracao*0.035
    if valor_irs<0:
        valor_irs = 0
    else:
        valor_irs = valor_irs
    renumeracao_final = renumeracao - valor_adse - valor_ss - valor_irs+valor_alimentacao

    ### SINTESE DE CARACTERISTICAS ###

    escrever_renumeracao = tk.CTkLabel(janela_solteiro_n_vale_cga_adse, text=("Ordenado Base: {} €" .format(ordenado1)), font=("Segoe UI", 20)).place(x=150, y=100)
    escrever_regime = tk.CTkLabel(janela_solteiro_n_vale_cga_adse, text=("Regime: Trabalhador Dependente"), font=("Segoe UI", 20)).place(x=150, y=150)
    escrever_fiscal = tk.CTkLabel(janela_solteiro_n_vale_cga_adse, text = ("Situação Fiscal:  Casado - 1 Titular"), font=("Segoe UI", 20)).place(x=150,y=200)
    escrever_dependentes = tk.CTkLabel(janela_solteiro_n_vale_cga_adse, text=("Dependentes: {}".format(dependentes)), font=("Segoe UI", 20)).place(x=150, y=250)
    escrever_social = tk.CTkLabel(janela_solteiro_n_vale_cga_adse, text=("Contribuição Social: Caixa Geral de Aposentações"), font=("Segoe UI", 20)).place(x=150, y=300)
    escrever_adse = tk.CTkLabel(janela_solteiro_n_vale_cga_adse, text=("ADSE: Sim"), font=("Segoe UI", 20)).place(x=150, y=350)
    escrever_alimentacao = tk.CTkLabel(janela_solteiro_n_vale_cga_adse, text=("Subsidio de Alimentação: {} €".format(valor_alimentacao)), font=("Segoe UI", 20)).place(x=150, y=400)
    escrever_dias = tk.CTkLabel(janela_solteiro_n_vale_cga_adse, text=("Dias com susbsidio de alimentação: {}".format(dias_alimentacao)), font=("Segoe UI", 20)).place(x=150, y=450)
    escrever_pagamento = tk.CTkLabel(janela_solteiro_n_vale_cga_adse, text=("Forma de pagamento do subsidio de alimentação: Vale/Cartão de alimentação"), font=("Segoe UI", 20)).place(x=150, y=500)
    escrever_outros = tk.CTkLabel(janela_solteiro_n_vale_cga_adse, text=("Outros subsidios tributaveis: {} €".format(outros)), font=("Segoe UI", 20)).place(x=150, y=550)
    escrever_invalidez = tk.CTkLabel(janela_solteiro_n_vale_cga_adse, text=("Invalidez ou incapacidade: Sim"), font=("Segoe UI", 20)).place(x=150, y=600)

### APRESENTAÇÃO DOS VALORES ###
    texto_descontos = tk.CTkLabel(janela_solteiro_n_vale_cga_adse, text=("Resumo dos descontos"), font=("Segoe UI", 20)) .place(x=879, y=150)
    texto_valor = tk.CTkLabel(janela_solteiro_n_vale_cga_adse, text=("Valor tributável:{:.2f}€ " .format(renumeracao)), font=("Segoe UI", 20)).place(x=879 , y=300)
    texto_irs = tk.CTkLabel(janela_solteiro_n_vale_cga_adse, text=("Retenção na fonte: {:.2f}€" .format(valor_irs)), font=("Segoe UI", 20)).place(x=879 , y=200)
    texto_ss = tk.CTkLabel(janela_solteiro_n_vale_cga_adse, text=("Taxa Social Única: {:.2f}€" .format(valor_ss)), font=("Segoe UI", 20)).place(x=879 , y=250)
    taxa_adse = tk.CTkLabel(janela_solteiro_n_vale_cga_adse, text=("Desconto ADSE: {:.2f}€" .format(valor_adse)), font=("Segoe UI", 20)).place(x=879 , y=350)
    valor_final = tk.CTkLabel(janela_solteiro_n_vale_cga_adse, text=( "Valor após descontos: {:.2f}€" .format(renumeracao_final)), font=("Segoe UI", 20), bg_color = "red").place(x=879 , y=450)

### FINAL - SAIR OU HISTORICO ###
    decidir_historico = tk.CTkLabel(janela_solteiro_n_vale_cga_adse, text=("Deseja adicionar está simulação ao histórico?" ), font=("Segoe UI", 20)).place(x=879, y=500)
    select_tabela_a = tk.CTkButton(janela_solteiro_n_vale_cga_adse, text="Sim",command=lambda: historico_ordenado(regime, situacao_fiscal, dependentes, contribuicao_social, adse, valor_alimentacao, dias_alimentacao, forma_pagamento, outros, renumeracao, valor_irs, valor_adse, valor_ss, renumeracao_final, invalidez),font=("Segoe UI", 20)).place(x=879, y=550)
    select_tabela_b = tk.CTkButton(janela_solteiro_n_vale_cga_adse, text="Não",command=lambda: reiniciar_programa(),font=("Segoe UI", 20)).place(x=1079, y=550)



def dependente_1t_s_vale_cga(janela_solteiro_n_vale):
    janela_solteiro_n_vale.withdraw()
    janela_solteiro_n_vale_cga = tk.CTkToplevel()
    janela_solteiro_n_vale_cga.geometry("1400x700")
    janela_solteiro_n_vale_cga.title("Simulação do ordenado liquido - Trabalhador Dependente - Casado - 1 Titular  - Outras contribuições")
    texto_topo = tk.CTkLabel(janela_solteiro_n_vale_cga, text="Simulação do ordenado liquido\nTrabalhador Dependente\nCasado - 1 Titular\nOutras contribuições", font=("Segoe UI", 20)).place(x=550, y=0)
    texto_adse = tk.CTkLabel(janela_solteiro_n_vale_cga, text="É beneficiário da ADSE?", font=("Segoe UI", 20)).place(x=590, y=150)
    botao_sim = tk.CTkButton(janela_solteiro_n_vale_cga, text= "Sim", command=lambda: dependente_1t_s_vale_cga_adse(janela_solteiro_n_vale_cga), font=("Segoe UI", 20)).place(x=530, y=200)
    botao_nao = tk.CTkButton(janela_solteiro_n_vale_cga, text="Não", command=lambda: dependente_1t_s_vale_cga_resultado(janela_solteiro_n_vale_cga), font=("Segoe UI", 20)).place(x=730, y=200)

def dependente_1t_s_vale_ss_resultado(janela_solteiro_n_vale_ss):
    regime = 1
    situacao_fiscal = 2
    contribuicao_social = 1
    adse = 2
    forma_pagamento = 2
    valor_irs=0
    invalidez = 2
    valor_adse=0
    janela_solteiro_n_vale_ss.withdraw()
    janela_solteiro_n_vale_ss_resultado = tk.CTkToplevel()
    janela_solteiro_n_vale_ss_resultado.geometry("1400x700")
    janela_solteiro_n_vale_ss_resultado.title( "Simulação do ordenado liquido - Trabalhador Dependente - Casado - 1 Titular  - Resultado Final")
    texto_topo = tk.CTkLabel(janela_solteiro_n_vale_ss_resultado, text="Simulação do ordenado liquido\nTrabalhador Dependente\nCasado - 1 Titular \nResultado Final", font=("Segoe UI", 20)).place(x=550, y=0)
    ordenado1 = float(renumera_log[0])
    dependentes = int(dependentes_log[0])
    alimentacao = float(alimentacao_log[0])
    dias_alimentacao = int(dias_log[0])
    outros = float(outros_log[0])
    if alimentacao <9.6:
        excedente_alimentacao = 0
    else:
        excedente_alimentacao = alimentacao-9.6
    valor_alimentacao = alimentacao*dias_alimentacao
    excedente_alimentacao_dias = excedente_alimentacao*dias_alimentacao
    renumeracao = ordenado1+excedente_alimentacao_dias+outros


    valor_irs, parcela_abater, taxa, renumeracao_liquida, parcela_dependente = ordenado_casado_1t_invalidez(dependentes, renumeracao)
    if valor_irs<0:
        valor_irs = 0
    else:
        valor_irs = valor_irs
    valor_ss = renumeracao*0.11
    renumeracao_final = renumeracao - valor_ss - valor_irs + valor_alimentacao


    ### SINTESE DE CARACTERISTICAS ###

    escrever_renumeracao = tk.CTkLabel(janela_solteiro_n_vale_ss_resultado, text=("Ordenado Base: {} €" .format(ordenado1)), font=("Segoe UI", 20)).place(x=150, y=100)
    escrever_regime = tk.CTkLabel(janela_solteiro_n_vale_ss_resultado, text=("Regime: Trabalhador Dependente"), font=("Segoe UI", 20)).place(x=150, y=150)
    escrever_fiscal = tk.CTkLabel(janela_solteiro_n_vale_ss_resultado, text = ("Situação Fiscal:Casado - 1 Titular"), font=("Segoe UI", 20)).place(x=150,y=200)
    escrever_dependentes = tk.CTkLabel(janela_solteiro_n_vale_ss_resultado, text=("Dependentes: {}".format(dependentes)), font=("Segoe UI", 20)).place(x=150, y=250)
    escrever_social = tk.CTkLabel(janela_solteiro_n_vale_ss_resultado, text=("Contribuição Social: Segurança Social"), font=("Segoe UI", 20)).place(x=150, y=300)
    escrever_adse = tk.CTkLabel(janela_solteiro_n_vale_ss_resultado, text=("ADSE: Não"), font=("Segoe UI", 20)).place(x=150, y=350)
    escrever_alimentacao = tk.CTkLabel(janela_solteiro_n_vale_ss_resultado, text=("Subsidio de Alimentação: {} €".format(valor_alimentacao)), font=("Segoe UI", 20)).place(x=150, y=400)
    escrever_dias = tk.CTkLabel(janela_solteiro_n_vale_ss_resultado, text=("Dias com susbsidio de alimentação: {}".format(dias_alimentacao)), font=("Segoe UI", 20)).place(x=150, y=450)
    escrever_pagamento = tk.CTkLabel(janela_solteiro_n_vale_ss_resultado, text=("Forma de pagamento do subsidio de alimentação: Vale/Cartão de Refeição"), font=("Segoe UI", 20)).place(x=150, y=500)
    escrever_outros = tk.CTkLabel(janela_solteiro_n_vale_ss_resultado, text=("Outros subsidios tributaveis: {} €".format(outros)), font=("Segoe UI", 20)).place(x=150, y=550)
    escrever_invalidez = tk.CTkLabel(janela_solteiro_n_vale_ss_resultado, text=("Invalidez ou incapacidade: Sim"), font=("Segoe UI", 20)).place(x=150, y=600)

### APRESENTAÇÃO DOS VALORES ###
    texto_descontos = tk.CTkLabel(janela_solteiro_n_vale_ss_resultado, text=("Resumo dos descontos"), font=("Segoe UI", 20)) .place(x=879, y=150)
    texto_valor = tk.CTkLabel(janela_solteiro_n_vale_ss_resultado, text=("Valor tributável:{:.2f}€ " .format(renumeracao)), font=("Segoe UI", 20)).place(x=879 , y=300)
    texto_irs = tk.CTkLabel(janela_solteiro_n_vale_ss_resultado, text=("Retenção na fonte: {:.2f}€" .format(valor_irs)), font=("Segoe UI", 20)).place(x=879 , y=200)
    texto_ss = tk.CTkLabel(janela_solteiro_n_vale_ss_resultado, text=("Taxa Social Única: {:.2f}€" .format(valor_ss)), font=("Segoe UI", 20)).place(x=879 , y=250)
    valor_final = tk.CTkLabel(janela_solteiro_n_vale_ss_resultado, text=( "Valor após descontos: {:.2f}€" .format(renumeracao_final)), font=("Segoe UI", 20), bg_color = "red").place(x=879 , y=300)

### FINAL - SAIR OU HISTORICO ###
    decidir_historico = tk.CTkLabel(janela_solteiro_n_vale_ss_resultado, text=("Deseja adicionar está simulação ao histórico?" ), font=("Segoe UI", 20)).place(x=879, y=500)
    select_tabela_a = tk.CTkButton(janela_solteiro_n_vale_ss_resultado, text="Sim",command=lambda: historico_ordenado(regime, situacao_fiscal, dependentes, contribuicao_social, adse, valor_alimentacao, dias_alimentacao, forma_pagamento, outros, renumeracao, valor_irs, valor_adse, valor_ss, renumeracao_final, invalidez),font=("Segoe UI", 20)).place(x=879, y=550)
    select_tabela_b = tk.CTkButton(janela_solteiro_n_vale_ss_resultado, text="Não",command=lambda: reiniciar_programa(),font=("Segoe UI", 20)).place(x=1079, y=550)



def dependente_1t_s_vale_ss_adse(janela_solteiro_n_vale_ss):
    regime = 1
    situacao_fiscal = 2
    contribuicao_social = 1
    adse = 1
    forma_pagamento = 2
    valor_irs=0
    invalidez = 2
    janela_solteiro_n_vale_ss.withdraw()
    janela_solteiro_n_vale_ss_adse = tk.CTkToplevel()
    janela_solteiro_n_vale_ss_adse.geometry("1400x700")
    janela_solteiro_n_vale_ss_adse.title( "Simulação do ordenado liquido - Trabalhador Dependente - Casado - 1 Titular  - Resultado Final")
    texto_topo = tk.CTkLabel(janela_solteiro_n_vale_ss_adse, text="Simulação do ordenado liquido\nTrabalhador Dependente\nCasado - 1 Titular \nResultado Final", font=("Segoe UI", 20)).place(x=550, y=0)
    ordenado1 = float(renumera_log[0])
    dependentes = int(dependentes_log[0])
    alimentacao = float(alimentacao_log[0])
    dias_alimentacao = int(dias_log[0])
    outros = float(outros_log[0])
    if alimentacao < 9.6:
        excedente_alimentacao = 0
    else:
        excedente_alimentacao = alimentacao-9.6
    valor_alimentacao = alimentacao*dias_alimentacao
    excedente_alimentacao_dias = excedente_alimentacao*dias_alimentacao
    renumeracao = ordenado1+excedente_alimentacao_dias+outros


    valor_irs, parcela_abater, taxa, renumeracao_liquida, parcela_dependente = ordenado_casado_1t_invalidez(dependentes, renumeracao)

    valor_ss = renumeracao*0.11
    valor_adse = renumeracao*0.035

    if valor_irs<0:
        valor_irs = 0
    else:
        valor_irs = valor_irs

    renumeracao_final = renumeracao - valor_adse - valor_ss - valor_irs+valor_alimentacao

    ### SINTESE DE CARACTERISTICAS ###

    escrever_renumeracao = tk.CTkLabel(janela_solteiro_n_vale_ss_adse, text=("Ordenado Base: {} €" .format(ordenado1)), font=("Segoe UI", 20)).place(x=150, y=100)
    escrever_regime = tk.CTkLabel(janela_solteiro_n_vale_ss_adse, text=("Regime: Trabalhador Dependente"), font=("Segoe UI", 20)).place(x=150, y=150)
    escrever_fiscal = tk.CTkLabel(janela_solteiro_n_vale_ss_adse, text = ("Situação Fiscal: Casado - 1 Titular"), font=("Segoe UI", 20)).place(x=150,y=200)
    escrever_dependentes = tk.CTkLabel(janela_solteiro_n_vale_ss_adse, text=("Dependentes: {}".format(dependentes)), font=("Segoe UI", 20)).place(x=150, y=250)
    escrever_social = tk.CTkLabel(janela_solteiro_n_vale_ss_adse, text=("Contribuição Social: Segurança Social"), font=("Segoe UI", 20)).place(x=150, y=300)
    escrever_adse = tk.CTkLabel(janela_solteiro_n_vale_ss_adse, text=("ADSE: Sim"), font=("Segoe UI", 20)).place(x=150, y=350)
    escrever_alimentacao = tk.CTkLabel(janela_solteiro_n_vale_ss_adse, text=("Subsidio de Alimentação: {} €".format(valor_alimentacao)), font=("Segoe UI", 20)).place(x=150, y=400)
    escrever_dias = tk.CTkLabel(janela_solteiro_n_vale_ss_adse, text=("Dias com susbsidio de alimentação: {}".format(dias_alimentacao)), font=("Segoe UI", 20)).place(x=150, y=450)
    escrever_pagamento = tk.CTkLabel(janela_solteiro_n_vale_ss_adse, text=("Forma de pagamento do subsidio de alimentação: Cartão/Vale de alimentação"), font=("Segoe UI", 20)).place(x=150, y=500)
    escrever_outros = tk.CTkLabel(janela_solteiro_n_vale_ss_adse, text=("Outros subsidios tributaveis: {} €".format(outros)), font=("Segoe UI", 20)).place(x=150, y=550)
    escrever_invalidez = tk.CTkLabel(janela_solteiro_n_vale_ss_adse, text=("Invalidez ou incapacidade: Sim"), font=("Segoe UI", 20)).place(x=150, y=600)

### APRESENTAÇÃO DOS VALORES ###
    texto_descontos = tk.CTkLabel(janela_solteiro_n_vale_ss_adse, text=("Resumo dos descontos"), font=("Segoe UI", 20)) .place(x=879, y=150)
    texto_valor = tk.CTkLabel(janela_solteiro_n_vale_ss_adse, text=("Valor tributável:{:.2f}€ " .format(renumeracao)), font=("Segoe UI", 20)).place(x=879 , y=300)
    texto_irs = tk.CTkLabel(janela_solteiro_n_vale_ss_adse, text=("Retenção na fonte: {:.2f}€" .format(valor_irs)), font=("Segoe UI", 20)).place(x=879 , y=200)
    texto_ss = tk.CTkLabel(janela_solteiro_n_vale_ss_adse, text=("Taxa Social Única: {:.2f}€" .format(valor_ss)), font=("Segoe UI", 20)).place(x=879 , y=250)
    taxa_adse = tk.CTkLabel(janela_solteiro_n_vale_ss_adse, text=("Desconto ADSE: {:.2f}€" .format(valor_adse)), font=("Segoe UI", 20)).place(x=879 , y=350)
    valor_final = tk.CTkLabel(janela_solteiro_n_vale_ss_adse, text=( "Valor após descontos: {:.2f}€" .format(renumeracao_final)), font=("Segoe UI", 20), bg_color = "red").place(x=879 , y=450)

### FINAL - SAIR OU HISTORICO ###
    decidir_historico = tk.CTkLabel(janela_solteiro_n_vale_ss_adse, text=("Deseja adicionar está simulação ao histórico?" ), font=("Segoe UI", 20)).place(x=879, y=500)
    select_tabela_a = tk.CTkButton(janela_solteiro_n_vale_ss_adse, text="Sim",command=lambda: historico_ordenado(regime, situacao_fiscal, dependentes, contribuicao_social, adse, valor_alimentacao, dias_alimentacao, forma_pagamento, outros, renumeracao, valor_irs, valor_adse, valor_ss, renumeracao_final, invalidez),font=("Segoe UI", 20)).place(x=879, y=550)
    select_tabela_b = tk.CTkButton(janela_solteiro_n_vale_ss_adse, text="Não",command=lambda: reiniciar_programa(),font=("Segoe UI", 20)).place(x=1079, y=550)



def dependente_1t_s_vale_ss(janela_solteiro_n_vale):
    janela_solteiro_n_vale.withdraw()
    janela_solteiro_n_vale_ss = tk.CTkToplevel()
    janela_solteiro_n_vale_ss.geometry("1400x700")
    janela_solteiro_n_vale_ss.title("Simulação do ordenado liquido - Trabalhador Dependente - Casado - 1 Titular  - Outras contribuições")
    texto_topo = tk.CTkLabel(janela_solteiro_n_vale_ss, text="Simulação do ordenado liquido\nTrabalhador Dependente\nCasado - 1 Titular\nOutras contribuições", font=("Segoe UI", 20)).place(x=550, y=0)
    texto_adse = tk.CTkLabel(janela_solteiro_n_vale_ss, text="É beneficiário da ADSE?", font=("Segoe UI", 20)).place(x=590, y=150)
    botao_sim = tk.CTkButton(janela_solteiro_n_vale_ss, text= "Sim", command=lambda: dependente_1t_s_vale_ss_adse(janela_solteiro_n_vale_ss), font=("Segoe UI", 20)).place(x=530, y=200)
    botao_nao = tk.CTkButton(janela_solteiro_n_vale_ss, text="Não", command=lambda: dependente_1t_s_vale_ss_resultado(janela_solteiro_n_vale_ss), font=("Segoe UI", 20)).place(x=730, y=200)




def dependente_1t_s_vale(janela_solteiro_n, pedir_outros, pedir_alimentacao, pedir_dias):
    alimentacao = float(pedir_alimentacao.get())
    alimentacao_log.append(alimentacao)
    dias = float(pedir_dias.get())
    dias_log.append(dias)
    outros = float(pedir_outros.get())
    outros_log.append(outros)
    janela_solteiro_n.withdraw()
    janela_solteiro_n_vale = tk.CTkToplevel()
    janela_solteiro_n_vale.geometry("1400x700")
    janela_solteiro_n_vale.title("Simulação do ordenado liquido - Trabalhador Dependente - Casado - 1 Titular  - Outras contribuições")
    texto_topo = tk.CTkLabel(janela_solteiro_n_vale, text="Simulação do ordenado liquido\nTrabalhador Dependente\nCasado - 1 Titular \nOutras contribuições", font=("Segoe UI", 20)).place(x=550, y=0)
    texto_forma = tk.CTkLabel(janela_solteiro_n_vale, text = "Selecione a sua forma de contribuição social", font=("Segoe UI", 20)).place(x=510, y=150)
    botao_ss = tk.CTkButton(janela_solteiro_n_vale, text="Segurança Social", command=lambda:dependente_1t_s_vale_ss(janela_solteiro_n_vale), font=("Segoe UI", 20)) .place(x=606, y=200)
    botao_cga = tk.CTkButton(janela_solteiro_n_vale, text="Caixa Geral de Aposentações", command=lambda: dependente_1t_s_vale_cga(janela_solteiro_n_vale),  font=("Segoe UI",20)) .place(x=560, y=250)



def dependente_1t_s_dinheiro_ss_resultado(janela_solteiro_n_dinheiro_ss):
    regime = 1
    situacao_fiscal = 2
    contribuicao_social = 1
    adse = 2
    forma_pagamento = 1
    valor_irs=0
    invalidez = 2
    valor_adse=0
    janela_solteiro_n_dinheiro_ss.withdraw()
    janela_solteiro_n_dinheiro_ss_resultado = tk.CTkToplevel()
    janela_solteiro_n_dinheiro_ss_resultado.geometry("1400x700")
    janela_solteiro_n_dinheiro_ss_resultado.title( "Simulação do ordenado liquido - Trabalhador Dependente - Casado - 1 Titular  - Resultado Final")
    texto_topo = tk.CTkLabel(janela_solteiro_n_dinheiro_ss_resultado, text="Simulação do ordenado liquido\nTrabalhador Dependente\nCasado - 1 Titular \nResultado Final", font=("Segoe UI", 20)).place(x=550, y=0)
    ordenado1 = float(renumera_log[0])
    dependentes = int(dependentes_log[0])
    alimentacao = float(alimentacao_log[0])
    dias_alimentacao = int(dias_log[0])
    outros = float(outros_log[0])
    if alimentacao < 6:
        excedente_alimentacao = 0
    else:
        excedente_alimentacao = alimentacao-6
    valor_alimentacao = alimentacao*dias_alimentacao
    excedente_alimentacao_dias = excedente_alimentacao*dias_alimentacao
    renumeracao = ordenado1+excedente_alimentacao_dias+outros

    valor_irs, parcela_abater, taxa, renumeracao_liquida, parcela_dependente = ordenado_casado_1t_invalidez(dependentes, renumeracao)
    if valor_irs<0:
        valor_irs = 0
    else:
        valor_irs = valor_irs
    valor_ss = renumeracao*0.11
    renumeracao_final = renumeracao - valor_ss - valor_irs + valor_alimentacao


    ### SINTESE DE CARACTERISTICAS ###

    escrever_renumeracao = tk.CTkLabel(janela_solteiro_n_dinheiro_ss_resultado, text=("Ordenado Base: {} €" .format(ordenado1)), font=("Segoe UI", 20)).place(x=150, y=100)
    escrever_regime = tk.CTkLabel(janela_solteiro_n_dinheiro_ss_resultado, text=("Regime: Trabalhador Dependente"), font=("Segoe UI", 20)).place(x=150, y=150)
    escrever_fiscal = tk.CTkLabel(janela_solteiro_n_dinheiro_ss_resultado, text = ("Situação Fiscal: Casado - 1 Titular"), font=("Segoe UI", 20)).place(x=150,y=200)
    escrever_dependentes = tk.CTkLabel(janela_solteiro_n_dinheiro_ss_resultado, text=("Dependentes: {}".format(dependentes)), font=("Segoe UI", 20)).place(x=150, y=250)
    escrever_social = tk.CTkLabel(janela_solteiro_n_dinheiro_ss_resultado, text=("Contribuição Social: Segurança Social"), font=("Segoe UI", 20)).place(x=150, y=300)
    escrever_adse = tk.CTkLabel(janela_solteiro_n_dinheiro_ss_resultado, text=("ADSE: Não"), font=("Segoe UI", 20)).place(x=150, y=350)
    escrever_alimentacao = tk.CTkLabel(janela_solteiro_n_dinheiro_ss_resultado, text=("Subsidio de Alimentação: {} €".format(valor_alimentacao)), font=("Segoe UI", 20)).place(x=150, y=400)
    escrever_dias = tk.CTkLabel(janela_solteiro_n_dinheiro_ss_resultado, text=("Dias com susbsidio de alimentação: {}".format(dias_alimentacao)), font=("Segoe UI", 20)).place(x=150, y=450)
    escrever_pagamento = tk.CTkLabel(janela_solteiro_n_dinheiro_ss_resultado, text=("Forma de pagamento do subsidio de alimentação: Dinheiro"), font=("Segoe UI", 20)).place(x=150, y=500)
    escrever_outros = tk.CTkLabel(janela_solteiro_n_dinheiro_ss_resultado, text=("Outros subsidios tributaveis: {} €".format(outros)), font=("Segoe UI", 20)).place(x=150, y=550)
    escrever_invalidez = tk.CTkLabel(janela_solteiro_n_dinheiro_ss_resultado, text=("Invalidez ou incapacidade: Sim"), font=("Segoe UI", 20)).place(x=150, y=600)

### APRESENTAÇÃO DOS VALORES ###
    texto_descontos = tk.CTkLabel(janela_solteiro_n_dinheiro_ss_resultado, text=("Resumo dos descontos"), font=("Segoe UI", 20)) .place(x=879, y=150)
    texto_valor = tk.CTkLabel(janela_solteiro_n_dinheiro_ss_resultado, text=("Valor tributável:{:.2f}€ " .format(renumeracao)), font=("Segoe UI", 20)).place(x=879 , y=300)
    texto_irs = tk.CTkLabel(janela_solteiro_n_dinheiro_ss_resultado, text=("Retenção na fonte: {:.2f}€" .format(valor_irs)), font=("Segoe UI", 20)).place(x=879 , y=200)
    texto_ss = tk.CTkLabel(janela_solteiro_n_dinheiro_ss_resultado, text=("Taxa Social Única: {:.2f}€" .format(valor_ss)), font=("Segoe UI", 20)).place(x=879 , y=250)
    valor_final = tk.CTkLabel(janela_solteiro_n_dinheiro_ss_resultado, text=( "Valor após descontos: {:.2f}€" .format(renumeracao_final)), font=("Segoe UI", 20), bg_color = "red").place(x=879 , y=300)

### FINAL - SAIR OU HISTORICO ###
    decidir_historico = tk.CTkLabel(janela_solteiro_n_dinheiro_ss_resultado, text=("Deseja adicionar está simulação ao histórico?" ), font=("Segoe UI", 20)).place(x=879, y=500)
    select_tabela_a = tk.CTkButton(janela_solteiro_n_dinheiro_ss_resultado, text="Sim",command=lambda: historico_ordenado(regime, situacao_fiscal, dependentes, contribuicao_social, adse, valor_alimentacao, dias_alimentacao, forma_pagamento, outros, renumeracao, valor_irs, valor_adse, valor_ss, renumeracao_final, invalidez),font=("Segoe UI", 20)).place(x=879, y=550)
    select_tabela_b = tk.CTkButton(janela_solteiro_n_dinheiro_ss_resultado, text="Não",command=lambda: reiniciar_programa(),font=("Segoe UI", 20)).place(x=1079, y=550)



def dependente_1t_s_dinheiro_ss_adse(janela_solteiro_n_dinheiro_ss):
    regime = 1
    situacao_fiscal = 2
    contribuicao_social = 1
    adse = 1
    forma_pagamento = 1
    valor_irs=0
    invalidez = 2
    janela_solteiro_n_dinheiro_ss.withdraw()
    janela_solteiro_n_dinheiro_ss_adse = tk.CTkToplevel()
    janela_solteiro_n_dinheiro_ss_adse.geometry("1400x700")
    janela_solteiro_n_dinheiro_ss_adse.title( "Simulação do ordenado liquido - Trabalhador Dependente - Casado - 1 Titular  - Resultado Final")
    texto_topo = tk.CTkLabel(janela_solteiro_n_dinheiro_ss_adse, text="Simulação do ordenado liquido\nTrabalhador Dependente\nCasado - 1 Titular \nResultado Final", font=("Segoe UI", 20)).place(x=550, y=0)
    ordenado1 = float(renumera_log[0])
    dependentes = int(dependentes_log[0])
    alimentacao = float(alimentacao_log[0])
    dias_alimentacao = int(dias_log[0])
    outros = float(outros_log[0])
    if alimentacao < 6:
        excedente_alimentacao = 0
    else:
        excedente_alimentacao = alimentacao-6
    valor_alimentacao = alimentacao*dias_alimentacao
    excedente_alimentacao_dias = excedente_alimentacao*dias_alimentacao
    renumeracao = ordenado1+excedente_alimentacao_dias+outros


    valor_irs, parcela_abater, taxa, renumeracao_liquida, parcela_dependente = ordenado_casado_1t_invalidez(dependentes, renumeracao)

    valor_ss = renumeracao*0.11
    valor_adse = renumeracao*0.035

    if valor_irs<0:
        valor_irs = 0
    else:
        valor_irs = valor_irs

    renumeracao_final = renumeracao - valor_adse - valor_ss - valor_irs+valor_alimentacao

    ### SINTESE DE CARACTERISTICAS ###

    escrever_renumeracao = tk.CTkLabel(janela_solteiro_n_dinheiro_ss_adse, text=("Ordenado Base: {} €" .format(ordenado1)), font=("Segoe UI", 20)).place(x=150, y=100)
    escrever_regime = tk.CTkLabel(janela_solteiro_n_dinheiro_ss_adse, text=("Regime: Trabalhador Dependente"), font=("Segoe UI", 20)).place(x=150, y=150)
    escrever_fiscal = tk.CTkLabel(janela_solteiro_n_dinheiro_ss_adse, text = ("Situação Fiscal: Casado - 1 Titular"), font=("Segoe UI", 20)).place(x=150,y=200)
    escrever_dependentes = tk.CTkLabel(janela_solteiro_n_dinheiro_ss_adse, text=("Dependentes: {}".format(dependentes)), font=("Segoe UI", 20)).place(x=150, y=250)
    escrever_social = tk.CTkLabel(janela_solteiro_n_dinheiro_ss_adse, text=("Contribuição Social: Segurança Social"), font=("Segoe UI", 20)).place(x=150, y=300)
    escrever_adse = tk.CTkLabel(janela_solteiro_n_dinheiro_ss_adse, text=("ADSE: Sim"), font=("Segoe UI", 20)).place(x=150, y=350)
    escrever_alimentacao = tk.CTkLabel(janela_solteiro_n_dinheiro_ss_adse, text=("Subsidio de Alimentação: {} €".format(valor_alimentacao)), font=("Segoe UI", 20)).place(x=150, y=400)
    escrever_dias = tk.CTkLabel(janela_solteiro_n_dinheiro_ss_adse, text=("Dias com susbsidio de alimentação: {}".format(dias_alimentacao)), font=("Segoe UI", 20)).place(x=150, y=450)
    escrever_pagamento = tk.CTkLabel(janela_solteiro_n_dinheiro_ss_adse, text=("Forma de pagamento do subsidio de alimentação: Dinheiro"), font=("Segoe UI", 20)).place(x=150, y=500)
    escrever_outros = tk.CTkLabel(janela_solteiro_n_dinheiro_ss_adse, text=("Outros subsidios tributaveis: {} €".format(outros)), font=("Segoe UI", 20)).place(x=150, y=550)
    escrever_invalidez = tk.CTkLabel(janela_solteiro_n_dinheiro_ss_adse, text=("Invalidez ou incapacidade: Sim"), font=("Segoe UI", 20)).place(x=150, y=600)

### APRESENTAÇÃO DOS VALORES ###
    texto_descontos = tk.CTkLabel(janela_solteiro_n_dinheiro_ss_adse, text=("Resumo dos descontos"), font=("Segoe UI", 20)) .place(x=879, y=150)
    texto_valor = tk.CTkLabel(janela_solteiro_n_dinheiro_ss_adse, text=("Valor tributável:{:.2f}€ " .format(renumeracao)), font=("Segoe UI", 20)).place(x=879 , y=300)
    texto_irs = tk.CTkLabel(janela_solteiro_n_dinheiro_ss_adse, text=("Retenção na fonte: {:.2f}€" .format(valor_irs)), font=("Segoe UI", 20)).place(x=879 , y=200)
    texto_ss = tk.CTkLabel(janela_solteiro_n_dinheiro_ss_adse, text=("Taxa Social Única: {:.2f}€" .format(valor_ss)), font=("Segoe UI", 20)).place(x=879 , y=250)
    taxa_adse = tk.CTkLabel(janela_solteiro_n_dinheiro_ss_adse, text=("Desconto ADSE: {:.2f}€" .format(valor_adse)), font=("Segoe UI", 20)).place(x=879 , y=350)
    valor_final = tk.CTkLabel(janela_solteiro_n_dinheiro_ss_adse, text=( "Valor após descontos: {:.2f}€" .format(renumeracao_final)), font=("Segoe UI", 20), bg_color = "red").place(x=879 , y=450)

### FINAL - SAIR OU HISTORICO ###
    decidir_historico = tk.CTkLabel(janela_solteiro_n_dinheiro_ss_adse, text=("Deseja adicionar está simulação ao histórico?" ), font=("Segoe UI", 20)).place(x=879, y=500)
    select_tabela_a = tk.CTkButton(janela_solteiro_n_dinheiro_ss_adse, text="Sim",command=lambda: historico_ordenado(regime, situacao_fiscal, dependentes, contribuicao_social, adse, valor_alimentacao, dias_alimentacao, forma_pagamento, outros, renumeracao, valor_irs, valor_adse, valor_ss, renumeracao_final, invalidez),font=("Segoe UI", 20)).place(x=879, y=550)
    select_tabela_b = tk.CTkButton(janela_solteiro_n_dinheiro_ss_adse, text="Não",command=lambda: reiniciar_programa(),font=("Segoe UI", 20)).place(x=1079, y=550)



def dependente_1t_s_dinheiro_ss(janela_solteiro_n_dinheiro):
    janela_solteiro_n_dinheiro.withdraw()
    janela_solteiro_n_dinheiro_ss = tk.CTkToplevel()
    janela_solteiro_n_dinheiro_ss.geometry("1400x700")
    janela_solteiro_n_dinheiro_ss.title("Simulação do ordenado liquido - Trabalhador Dependente - Casado - 1 Titular  - Outras contribuições")
    texto_topo = tk.CTkLabel(janela_solteiro_n_dinheiro_ss, text="Simulação do ordenado liquido\nTrabalhador Dependente\nCasado - 1 Titular \nOutras contribuições", font=("Segoe UI", 20)).place(x=550, y=0)
    texto_adse = tk.CTkLabel(janela_solteiro_n_dinheiro_ss, text="É beneficiário da ADSE?", font=("Segoe UI", 20)).place(x=590, y=150)
    botao_sim = tk.CTkButton(janela_solteiro_n_dinheiro_ss, text= "Sim", command=lambda: dependente_1t_s_dinheiro_ss_adse(janela_solteiro_n_dinheiro_ss), font=("Segoe UI", 20)).place(x=530, y=200)
    botao_nao = tk.CTkButton(janela_solteiro_n_dinheiro_ss, text="Não", command=lambda: dependente_1t_s_dinheiro_ss_resultado(janela_solteiro_n_dinheiro_ss), font=("Segoe UI", 20)).place(x=730, y=200)


def dependente_1t_s_dinheiro(janela_solteiro_n, pedir_outros, pedir_alimentacao, pedir_dias):
    alimentacao = float(pedir_alimentacao.get())
    alimentacao_log.append(alimentacao)
    dias = float(pedir_dias.get())
    dias_log.append(dias)
    outros = float(pedir_outros.get())
    outros_log.append(outros)
    janela_solteiro_n.withdraw()
    janela_solteiro_n_dinheiro = tk.CTkToplevel()
    janela_solteiro_n_dinheiro.geometry("1400x700")
    janela_solteiro_n_dinheiro.title("Simulação do ordenado liquido - Trabalhador Dependente - Casado - 1 Titular  - Outras contribuições")
    texto_topo = tk.CTkLabel(janela_solteiro_n_dinheiro, text="Simulação do ordenado liquido\nTrabalhador Dependente\nCasado - 1 Titular \nOutras contribuições", font=("Segoe UI", 20)).place(x=550, y=0)
    texto_forma = tk.CTkLabel(janela_solteiro_n_dinheiro, text = "Selecione a sua forma de contribuição social", font=("Segoe UI", 20)).place(x=510, y=150)
    botao_ss = tk.CTkButton(janela_solteiro_n_dinheiro, text="Segurança Social", command=lambda:dependente_1t_s_dinheiro_ss(janela_solteiro_n_dinheiro), font=("Segoe UI", 20)) .place(x=606, y=200)
    botao_cga = tk.CTkButton(janela_solteiro_n_dinheiro, text="Caixa Geral de Aposentações", command=lambda: dependente_1t_s_dinheiro_cga(janela_solteiro_n_dinheiro),  font=("Segoe UI",20)) .place(x=560, y=250)


def dependente_1t_s_dinheiro_cga_resultado(janela_solteiro_n_dinheiro_cga):
    regime = 1
    situacao_fiscal = 2
    contribuicao_social = 2
    adse = 2
    forma_pagamento = 1
    valor_irs=0
    invalidez = 2
    valor_adse=0
    janela_solteiro_n_dinheiro_cga.withdraw()
    janela_solteiro_n_dinheiro_cga_resultado = tk.CTkToplevel()
    janela_solteiro_n_dinheiro_cga_resultado.geometry("1400x700")
    janela_solteiro_n_dinheiro_cga_resultado.title( "Simulação do ordenado liquido - Trabalhador Dependente - Casado - 1 Titular  - Resultado Final")
    texto_topo = tk.CTkLabel(janela_solteiro_n_dinheiro_cga_resultado, text="Simulação do ordenado liquido\nTrabalhador Dependente\nCasado - 1 Titular \nResultado Final", font=("Segoe UI", 20)).place(x=550, y=0)
    ordenado1 = float(renumera_log[0])
    dependentes = int(dependentes_log[0])
    alimentacao = float(alimentacao_log[0])
    dias_alimentacao = int(dias_log[0])
    outros = float(outros_log[0])
    if alimentacao <6:
        excedente_alimentacao = 0
    else:
        excedente_alimentacao = alimentacao-6
    valor_alimentacao = alimentacao*dias_alimentacao
    excedente_alimentacao_dias = excedente_alimentacao*dias_alimentacao
    renumeracao = ordenado1+excedente_alimentacao_dias+outros


    valor_irs, parcela_abater, taxa, renumeracao_liquida, parcela_dependente = ordenado_casado_1t_invalidez(dependentes, renumeracao)
    if valor_irs<0:
        valor_irs = 0
    else:
        valor_irs = valor_irs
    valor_ss = renumeracao*0.11
    renumeracao_final = renumeracao - valor_ss - valor_irs + valor_alimentacao


    ### SINTESE DE CARACTERISTICAS ###

    escrever_renumeracao = tk.CTkLabel(janela_solteiro_n_dinheiro_cga_resultado, text=("Ordenado Base: {} €" .format(ordenado1)), font=("Segoe UI", 20)).place(x=150, y=100)
    escrever_regime = tk.CTkLabel(janela_solteiro_n_dinheiro_cga_resultado, text=("Regime: Trabalhador Dependente"), font=("Segoe UI", 20)).place(x=150, y=150)
    escrever_fiscal = tk.CTkLabel(janela_solteiro_n_dinheiro_cga_resultado, text = ("Situação Fiscal: Casado - 1 Titular"), font=("Segoe UI", 20)).place(x=150,y=200)
    escrever_dependentes = tk.CTkLabel(janela_solteiro_n_dinheiro_cga_resultado, text=("Dependentes: {}".format(dependentes)), font=("Segoe UI", 20)).place(x=150, y=250)
    escrever_social = tk.CTkLabel(janela_solteiro_n_dinheiro_cga_resultado, text=("Contribuição Social: Caixa Geral de Aposentações"), font=("Segoe UI", 20)).place(x=150, y=300)
    escrever_adse = tk.CTkLabel(janela_solteiro_n_dinheiro_cga_resultado, text=("ADSE: Não"), font=("Segoe UI", 20)).place(x=150, y=350)
    escrever_alimentacao = tk.CTkLabel(janela_solteiro_n_dinheiro_cga_resultado, text=("Subsidio de Alimentação: {} €".format(valor_alimentacao)), font=("Segoe UI", 20)).place(x=150, y=400)
    escrever_dias = tk.CTkLabel(janela_solteiro_n_dinheiro_cga_resultado, text=("Dias com susbsidio de alimentação: {}".format(dias_alimentacao)), font=("Segoe UI", 20)).place(x=150, y=450)
    escrever_pagamento = tk.CTkLabel(janela_solteiro_n_dinheiro_cga_resultado, text=("Forma de pagamento do subsidio de alimentação: Dinheiro"), font=("Segoe UI", 20)).place(x=150, y=500)
    escrever_outros = tk.CTkLabel(janela_solteiro_n_dinheiro_cga_resultado, text=("Outros subsidios tributaveis: {} €".format(outros)), font=("Segoe UI", 20)).place(x=150, y=550)
    escrever_invalidez = tk.CTkLabel(janela_solteiro_n_dinheiro_cga_resultado, text=("Invalidez ou incapacidade: Sim"), font=("Segoe UI", 20)).place(x=150, y=600)

### APRESENTAÇÃO DOS VALORES ###
    texto_descontos = tk.CTkLabel(janela_solteiro_n_dinheiro_cga_resultado, text=("Resumo dos descontos"), font=("Segoe UI", 20)) .place(x=879, y=150)
    texto_valor = tk.CTkLabel(janela_solteiro_n_dinheiro_cga_resultado, text=("Valor tributável:{:.2f}€ " .format(renumeracao)), font=("Segoe UI", 20)).place(x=879 , y=300)
    texto_irs = tk.CTkLabel(janela_solteiro_n_dinheiro_cga_resultado, text=("Retenção na fonte: {:.2f}€" .format(valor_irs)), font=("Segoe UI", 20)).place(x=879 , y=200)
    texto_ss = tk.CTkLabel(janela_solteiro_n_dinheiro_cga_resultado, text=("Taxa Social Única: {:.2f}€" .format(valor_ss)), font=("Segoe UI", 20)).place(x=879 , y=250)
    valor_final = tk.CTkLabel(janela_solteiro_n_dinheiro_cga_resultado, text=( "Valor após descontos: {:.2f}€" .format(renumeracao_final)), font=("Segoe UI", 20), bg_color = "red").place(x=879 , y=300)

### FINAL - SAIR OU HISTORICO ###
    decidir_historico = tk.CTkLabel(janela_solteiro_n_dinheiro_cga_resultado, text=("Deseja adicionar está simulação ao histórico?" ), font=("Segoe UI", 20)).place(x=879, y=500)
    select_tabela_a = tk.CTkButton(janela_solteiro_n_dinheiro_cga_resultado, text="Sim",command=lambda: historico_ordenado(regime, situacao_fiscal, dependentes, contribuicao_social, adse, valor_alimentacao, dias_alimentacao, forma_pagamento, outros, renumeracao, valor_irs, valor_adse, valor_ss, renumeracao_final, invalidez),font=("Segoe UI", 20)).place(x=879, y=550)
    select_tabela_b = tk.CTkButton(janela_solteiro_n_dinheiro_cga_resultado, text="Não",command=lambda: reiniciar_programa(),font=("Segoe UI", 20)).place(x=1079, y=550)


def dependente_1t_s_dinheiro_cga_adse(janela_solteiro_n_dinheiro_cga):
    regime = 1
    situacao_fiscal = 2
    contribuicao_social = 2
    adse = 1
    forma_pagamento = 1
    valor_irs=0
    invalidez = 2
    janela_solteiro_n_dinheiro_cga.withdraw()
    janela_solteiro_n_dinheiro_cga_adse = tk.CTkToplevel()
    janela_solteiro_n_dinheiro_cga_adse.geometry("1400x700")
    janela_solteiro_n_dinheiro_cga_adse.title( "Simulação do ordenado liquido - Trabalhador Dependente - Casado - 1 Titular - Resultado Final")
    texto_topo = tk.CTkLabel(janela_solteiro_n_dinheiro_cga_adse, text="Simulação do ordenado liquido\nTrabalhador Dependente\nCasado - 1 Titular \nResultado Final", font=("Segoe UI", 20)).place(x=550, y=0)
    ordenado1 = float(renumera_log[0])
    dependentes = int(dependentes_log[0])
    alimentacao = float(alimentacao_log[0])
    dias_alimentacao = int(dias_log[0])
    outros = float(outros_log[0])
    if alimentacao < 6:
        excedente_alimentacao = 0
    else:
        excedente_alimentacao = alimentacao-6
    valor_alimentacao = alimentacao*dias_alimentacao
    excedente_alimentacao_dias = excedente_alimentacao*dias_alimentacao
    renumeracao = ordenado1+excedente_alimentacao_dias+outros


    valor_irs, parcela_abater, taxa, renumeracao_liquida, parcela_dependente = ordenado_casado_1t_invalidez (dependentes, renumeracao)

    valor_ss = renumeracao*0.11
    valor_adse = renumeracao*0.035
    if valor_irs<0:
        valor_irs = 0
    else:
        valor_irs = valor_irs
    renumeracao_final = renumeracao - valor_adse - valor_ss - valor_irs+valor_alimentacao

    ### SINTESE DE CARACTERISTICAS ###

    escrever_renumeracao = tk.CTkLabel(janela_solteiro_n_dinheiro_cga_adse, text=("Ordenado Base: {} €" .format(ordenado1)), font=("Segoe UI", 20)).place(x=150, y=100)
    escrever_regime = tk.CTkLabel(janela_solteiro_n_dinheiro_cga_adse, text=("Regime: Trabalhador Dependente"), font=("Segoe UI", 20)).place(x=150, y=150)
    escrever_fiscal = tk.CTkLabel(janela_solteiro_n_dinheiro_cga_adse, text = ("Situação Fiscal: Casado - 1 Titular"), font=("Segoe UI", 20)).place(x=150,y=200)
    escrever_dependentes = tk.CTkLabel(janela_solteiro_n_dinheiro_cga_adse, text=("Dependentes: {}".format(dependentes)), font=("Segoe UI", 20)).place(x=150, y=250)
    escrever_social = tk.CTkLabel(janela_solteiro_n_dinheiro_cga_adse, text=("Contribuição Social: Caixa Geral de Aposentações"), font=("Segoe UI", 20)).place(x=150, y=300)
    escrever_adse = tk.CTkLabel(janela_solteiro_n_dinheiro_cga_adse, text=("ADSE: Sim"), font=("Segoe UI", 20)).place(x=150, y=350)
    escrever_alimentacao = tk.CTkLabel(janela_solteiro_n_dinheiro_cga_adse, text=("Subsidio de Alimentação: {} €".format(valor_alimentacao)), font=("Segoe UI", 20)).place(x=150, y=400)
    escrever_dias = tk.CTkLabel(janela_solteiro_n_dinheiro_cga_adse, text=("Dias com susbsidio de alimentação: {}".format(dias_alimentacao)), font=("Segoe UI", 20)).place(x=150, y=450)
    escrever_pagamento = tk.CTkLabel(janela_solteiro_n_dinheiro_cga_adse, text=("Forma de pagamento do subsidio de alimentação: Dinheiro"), font=("Segoe UI", 20)).place(x=150, y=500)
    escrever_outros = tk.CTkLabel(janela_solteiro_n_dinheiro_cga_adse, text=("Outros subsidios tributaveis: {} €".format(outros)), font=("Segoe UI", 20)).place(x=150, y=550)
    escrever_invalidez = tk.CTkLabel(janela_solteiro_n_dinheiro_cga_adse, text=("Invalidez ou incapacidade: Sim"), font=("Segoe UI", 20)).place(x=150, y=600)

### APRESENTAÇÃO DOS VALORES ###
    texto_descontos = tk.CTkLabel(janela_solteiro_n_dinheiro_cga_adse, text=("Resumo dos descontos"), font=("Segoe UI", 20)) .place(x=879, y=150)
    texto_valor = tk.CTkLabel(janela_solteiro_n_dinheiro_cga_adse, text=("Valor tributável:{:.2f}€ " .format(renumeracao)), font=("Segoe UI", 20)).place(x=879 , y=300)
    texto_irs = tk.CTkLabel(janela_solteiro_n_dinheiro_cga_adse, text=("Retenção na fonte: {:.2f}€" .format(valor_irs)), font=("Segoe UI", 20)).place(x=879 , y=200)
    texto_ss = tk.CTkLabel(janela_solteiro_n_dinheiro_cga_adse, text=("Taxa Social Única: {:.2f}€" .format(valor_ss)), font=("Segoe UI", 20)).place(x=879 , y=250)
    taxa_adse = tk.CTkLabel(janela_solteiro_n_dinheiro_cga_adse, text=("Desconto ADSE: {:.2f}€" .format(valor_adse)), font=("Segoe UI", 20)).place(x=879 , y=350)
    valor_final = tk.CTkLabel(janela_solteiro_n_dinheiro_cga_adse, text=( "Valor após descontos: {:.2f}€" .format(renumeracao_final)), font=("Segoe UI", 20), bg_color = "red").place(x=879 , y=450)

### FINAL - SAIR OU HISTORICO ###
    decidir_historico = tk.CTkLabel(janela_solteiro_n_dinheiro_cga_adse, text=("Deseja adicionar está simulação ao histórico?" ), font=("Segoe UI", 20)).place(x=879, y=500)
    select_tabela_a = tk.CTkButton(janela_solteiro_n_dinheiro_cga_adse, text="Sim",command=lambda: historico_ordenado(regime, situacao_fiscal, dependentes, contribuicao_social, adse, valor_alimentacao, dias_alimentacao, forma_pagamento, outros, renumeracao, valor_irs, valor_adse, valor_ss, renumeracao_final, invalidez),font=("Segoe UI", 20)).place(x=879, y=550)
    select_tabela_b = tk.CTkButton(janela_solteiro_n_dinheiro_cga_adse, text="Não",command=lambda: reiniciar_programa(),font=("Segoe UI", 20)).place(x=1079, y=550)

def dependente_1t_s_dinheiro_cga(janela_solteiro_n_dinheiro):
    janela_solteiro_n_dinheiro.withdraw()
    janela_solteiro_n_dinheiro_cga = tk.CTkToplevel()
    janela_solteiro_n_dinheiro_cga.geometry("1400x700")
    janela_solteiro_n_dinheiro_cga.title("Simulação do ordenado liquido - Trabalhador Dependente - Casado - 1 Titular - Outras contribuições")
    texto_topo = tk.CTkLabel(janela_solteiro_n_dinheiro_cga, text="Simulação do ordenado liquido\nTrabalhador Dependente\nCasado - 1 Titular\nOutras contribuições", font=("Segoe UI", 20)).place(x=550, y=0)
    texto_adse = tk.CTkLabel(janela_solteiro_n_dinheiro_cga, text="É beneficiário da ADSE?", font=("Segoe UI", 20)).place(x=590, y=150)
    botao_sim = tk.CTkButton(janela_solteiro_n_dinheiro_cga, text= "Sim", command=lambda: dependente_1t_s_dinheiro_cga_adse(janela_solteiro_n_dinheiro_cga), font=("Segoe UI", 20)).place(x=530, y=200)
    botao_nao = tk.CTkButton(janela_solteiro_n_dinheiro_cga, text="Não", command=lambda: dependente_1t_s_dinheiro_cga_resultado(janela_solteiro_n_dinheiro_cga), font=("Segoe UI", 20)).place(x=730, y=200)


def dependente_1t_s_dinheiro_ss_resultado(janela_solteiro_n_dinheiro_ss):
    regime = 1
    situacao_fiscal = 2
    contribuicao_social = 1
    adse = 2
    forma_pagamento = 1
    valor_irs=0
    invalidez = 2
    valor_adse=0
    janela_solteiro_n_dinheiro_ss.withdraw()
    janela_solteiro_n_dinheiro_ss_resultado = tk.CTkToplevel()
    janela_solteiro_n_dinheiro_ss_resultado.geometry("1400x700")
    janela_solteiro_n_dinheiro_ss_resultado.title( "Simulação do ordenado liquido - Trabalhador Dependente - Casado - 1 Titular - Resultado Final")
    texto_topo = tk.CTkLabel(janela_solteiro_n_dinheiro_ss_resultado, text="Simulação do ordenado liquido\nTrabalhador Dependente\nCasado - 1 Titular\nResultado Final", font=("Segoe UI", 20)).place(x=550, y=0)
    ordenado1 = float(renumera_log[0])
    dependentes = int(dependentes_log[0])
    alimentacao = float(alimentacao_log[0])
    dias_alimentacao = int(dias_log[0])
    outros = float(outros_log[0])
    if alimentacao <6:
        excedente_alimentacao = 0
    else:
        excedente_alimentacao = alimentacao-6
    valor_alimentacao = alimentacao*dias_alimentacao
    excedente_alimentacao_dias = excedente_alimentacao*dias_alimentacao
    renumeracao = ordenado1+excedente_alimentacao_dias+outros


    valor_irs, parcela_abater, taxa, renumeracao_liquida, parcela_dependente = ordenado_casado_1t_invalidez(dependentes, renumeracao)
    if valor_irs<0:
        valor_irs = 0
    else:
        valor_irs = valor_irs
    valor_ss = renumeracao*0.11
    renumeracao_final = renumeracao - valor_ss - valor_irs + valor_alimentacao


    ### SINTESE DE CARACTERISTICAS ###

    escrever_renumeracao = tk.CTkLabel(janela_solteiro_n_dinheiro_ss_resultado, text=("Ordenado Base: {} €" .format(ordenado1)), font=("Segoe UI", 20)).place(x=150, y=100)
    escrever_regime = tk.CTkLabel(janela_solteiro_n_dinheiro_ss_resultado, text=("Regime: Trabalhador Dependente"), font=("Segoe UI", 20)).place(x=150, y=150)
    escrever_fiscal = tk.CTkLabel(janela_solteiro_n_dinheiro_ss_resultado, text = ("Situação Fiscal:  Casado - 1 Titular"), font=("Segoe UI", 20)).place(x=150,y=200)
    escrever_dependentes = tk.CTkLabel(janela_solteiro_n_dinheiro_ss_resultado, text=("Dependentes: {}".format(dependentes)), font=("Segoe UI", 20)).place(x=150, y=250)
    escrever_social = tk.CTkLabel(janela_solteiro_n_dinheiro_ss_resultado, text=("Contribuição Social: Segurança Social"), font=("Segoe UI", 20)).place(x=150, y=300)
    escrever_adse = tk.CTkLabel(janela_solteiro_n_dinheiro_ss_resultado, text=("ADSE: Não"), font=("Segoe UI", 20)).place(x=150, y=350)
    escrever_alimentacao = tk.CTkLabel(janela_solteiro_n_dinheiro_ss_resultado, text=("Subsidio de Alimentação: {} €".format(valor_alimentacao)), font=("Segoe UI", 20)).place(x=150, y=400)
    escrever_dias = tk.CTkLabel(janela_solteiro_n_dinheiro_ss_resultado, text=("Dias com susbsidio de alimentação: {}".format(dias_alimentacao)), font=("Segoe UI", 20)).place(x=150, y=450)
    escrever_pagamento = tk.CTkLabel(janela_solteiro_n_dinheiro_ss_resultado, text=("Forma de pagamento do subsidio de alimentação: Dinheiro"), font=("Segoe UI", 20)).place(x=150, y=500)
    escrever_outros = tk.CTkLabel(janela_solteiro_n_dinheiro_ss_resultado, text=("Outros subsidios tributaveis: {} €".format(outros)), font=("Segoe UI", 20)).place(x=150, y=550)
    escrever_invalidez = tk.CTkLabel(janela_solteiro_n_dinheiro_ss_resultado, text=("Invalidez ou incapacidade: Sim"), font=("Segoe UI", 20)).place(x=150, y=600)

### APRESENTAÇÃO DOS VALORES ###
    texto_descontos = tk.CTkLabel(janela_solteiro_n_dinheiro_ss_resultado, text=("Resumo dos descontos"), font=("Segoe UI", 20)) .place(x=879, y=150)
    texto_valor = tk.CTkLabel(janela_solteiro_n_dinheiro_ss_resultado, text=("Valor tributável:{:.2f}€ " .format(renumeracao)), font=("Segoe UI", 20)).place(x=879 , y=300)
    texto_irs = tk.CTkLabel(janela_solteiro_n_dinheiro_ss_resultado, text=("Retenção na fonte: {:.2f}€" .format(valor_irs)), font=("Segoe UI", 20)).place(x=879 , y=200)
    texto_ss = tk.CTkLabel(janela_solteiro_n_dinheiro_ss_resultado, text=("Taxa Social Única: {:.2f}€" .format(valor_ss)), font=("Segoe UI", 20)).place(x=879 , y=250)
    valor_final = tk.CTkLabel(janela_solteiro_n_dinheiro_ss_resultado, text=( "Valor após descontos: {:.2f}€" .format(renumeracao_final)), font=("Segoe UI", 20), bg_color = "red").place(x=879 , y=300)

### FINAL - SAIR OU HISTORICO ###
    decidir_historico = tk.CTkLabel(janela_solteiro_n_dinheiro_ss_resultado, text=("Deseja adicionar está simulação ao histórico?" ), font=("Segoe UI", 20)).place(x=879, y=500)
    select_tabela_a = tk.CTkButton(janela_solteiro_n_dinheiro_ss_resultado, text="Sim",command=lambda: historico_ordenado(regime, situacao_fiscal, dependentes, contribuicao_social, adse, valor_alimentacao, dias_alimentacao, forma_pagamento, outros, renumeracao, valor_irs, valor_adse, valor_ss, renumeracao_final, invalidez),font=("Segoe UI", 20)).place(x=879, y=550)
    select_tabela_b = tk.CTkButton(janela_solteiro_n_dinheiro_ss_resultado, text="Não",command=lambda: reiniciar_programa(),font=("Segoe UI", 20)).place(x=1079, y=550)


def dependente_1t_dinheiro_ss_adse(janela_solteiro_n_dinheiro_ss):
    regime = 1
    situacao_fiscal = 2
    contribuicao_social = 1
    adse = 1
    forma_pagamento = 1
    valor_irs=0
    invalidez = 2
    janela_solteiro_n_dinheiro_ss.withdraw()
    janela_solteiro_n_dinheiro_ss_adse = tk.CTkToplevel()
    janela_solteiro_n_dinheiro_ss_adse.geometry("1400x700")
    janela_solteiro_n_dinheiro_ss_adse.title( "Simulação do ordenado liquido - Trabalhador Dependente - Casado - 1 Titular - Resultado Final")
    texto_topo = tk.CTkLabel(janela_solteiro_n_dinheiro_ss_adse, text="Simulação do ordenado liquido\nTrabalhador Dependente\nCasado - 1 Titular\nResultado Final", font=("Segoe UI", 20)).place(x=550, y=0)
    ordenado1 = float(renumera_log[0])
    dependentes = int(dependentes_log[0])
    alimentacao = float(alimentacao_log[0])
    dias_alimentacao = int(dias_log[0])
    outros = float(outros_log[0])
    if alimentacao < 6:
        excedente_alimentacao = 0
    else:
        excedente_alimentacao = alimentacao-6
    valor_alimentacao = alimentacao*dias_alimentacao
    excedente_alimentacao_dias = excedente_alimentacao*dias_alimentacao
    renumeracao = ordenado1+excedente_alimentacao_dias+outros

    valor_irs, parcela_abater, taxa, renumeracao_liquida, parcela_dependente = ordenado_casado_1t_invalidez (dependentes, renumeracao)

    valor_ss = renumeracao*0.11
    valor_adse = renumeracao*0.035

    if valor_irs<0:
        valor_irs = 0
    else:
        valor_irs = valor_irs

    renumeracao_final = renumeracao - valor_adse - valor_ss - valor_irs+valor_alimentacao

    ### SINTESE DE CARACTERISTICAS ###

    escrever_renumeracao = tk.CTkLabel(janela_solteiro_n_dinheiro_ss_adse, text=("Ordenado Base: {} €" .format(ordenado1)), font=("Segoe UI", 20)).place(x=150, y=100)
    escrever_regime = tk.CTkLabel(janela_solteiro_n_dinheiro_ss_adse, text=("Regime: Trabalhador Dependente"), font=("Segoe UI", 20)).place(x=150, y=150)
    escrever_fiscal = tk.CTkLabel(janela_solteiro_n_dinheiro_ss_adse, text = ("Situação Fiscal: Casado - 1 Titular"), font=("Segoe UI", 20)).place(x=150,y=200)
    escrever_dependentes = tk.CTkLabel(janela_solteiro_n_dinheiro_ss_adse, text=("Dependentes: {}".format(dependentes)), font=("Segoe UI", 20)).place(x=150, y=250)
    escrever_social = tk.CTkLabel(janela_solteiro_n_dinheiro_ss_adse, text=("Contribuição Social: Segurança Social"), font=("Segoe UI", 20)).place(x=150, y=300)
    escrever_adse = tk.CTkLabel(janela_solteiro_n_dinheiro_ss_adse, text=("ADSE: Sim"), font=("Segoe UI", 20)).place(x=150, y=350)
    escrever_alimentacao = tk.CTkLabel(janela_solteiro_n_dinheiro_ss_adse, text=("Subsidio de Alimentação: {} €".format(valor_alimentacao)), font=("Segoe UI", 20)).place(x=150, y=400)
    escrever_dias = tk.CTkLabel(janela_solteiro_n_dinheiro_ss_adse, text=("Dias com susbsidio de alimentação: {}".format(dias_alimentacao)), font=("Segoe UI", 20)).place(x=150, y=450)
    escrever_pagamento = tk.CTkLabel(janela_solteiro_n_dinheiro_ss_adse, text=("Forma de pagamento do subsidio de alimentação: Dinheiro"), font=("Segoe UI", 20)).place(x=150, y=500)
    escrever_outros = tk.CTkLabel(janela_solteiro_n_dinheiro_ss_adse, text=("Outros subsidios tributaveis: {} €".format(outros)), font=("Segoe UI", 20)).place(x=150, y=550)
    escrever_invalidez = tk.CTkLabel(janela_solteiro_n_dinheiro_ss_adse, text=("Invalidez ou incapacidade: Sim"), font=("Segoe UI", 20)).place(x=150, y=600)

### APRESENTAÇÃO DOS VALORES ###
    texto_descontos = tk.CTkLabel(janela_solteiro_n_dinheiro_ss_adse, text=("Resumo dos descontos"), font=("Segoe UI", 20)) .place(x=879, y=150)
    texto_valor = tk.CTkLabel(janela_solteiro_n_dinheiro_ss_adse, text=("Valor tributável:{:.2f}€ " .format(renumeracao)), font=("Segoe UI", 20)).place(x=879 , y=300)
    texto_irs = tk.CTkLabel(janela_solteiro_n_dinheiro_ss_adse, text=("Retenção na fonte: {:.2f}€" .format(valor_irs)), font=("Segoe UI", 20)).place(x=879 , y=200)
    texto_ss = tk.CTkLabel(janela_solteiro_n_dinheiro_ss_adse, text=("Taxa Social Única: {:.2f}€" .format(valor_ss)), font=("Segoe UI", 20)).place(x=879 , y=250)
    taxa_adse = tk.CTkLabel(janela_solteiro_n_dinheiro_ss_adse, text=("Desconto ADSE: {:.2f}€" .format(valor_adse)), font=("Segoe UI", 20)).place(x=879 , y=350)
    valor_final = tk.CTkLabel(janela_solteiro_n_dinheiro_ss_adse, text=( "Valor após descontos: {:.2f}€" .format(renumeracao_final)), font=("Segoe UI", 20), bg_color = "red").place(x=879 , y=450)

### FINAL - SAIR OU HISTORICO ###
    decidir_historico = tk.CTkLabel(janela_solteiro_n_dinheiro_ss_adse, text=("Deseja adicionar está simulação ao histórico?" ), font=("Segoe UI", 20)).place(x=879, y=500)
    select_tabela_a = tk.CTkButton(janela_solteiro_n_dinheiro_ss_adse, text="Sim",command=lambda: historico_ordenado(regime, situacao_fiscal, dependentes, contribuicao_social, adse, valor_alimentacao, dias_alimentacao, forma_pagamento, outros, renumeracao, valor_irs, valor_adse, valor_ss, renumeracao_final, invalidez),font=("Segoe UI", 20)).place(x=879, y=550)
    select_tabela_b = tk.CTkButton(janela_solteiro_n_dinheiro_ss_adse, text="Não",command=lambda: reiniciar_programa(),font=("Segoe UI", 20)).place(x=1079, y=550)


def dependente_1t_dinheiro_ss(janela_solteiro_n_dinheiro):
    janela_solteiro_n_dinheiro.withdraw()
    janela_solteiro_n_dinheiro_ss = tk.CTkToplevel()
    janela_solteiro_n_dinheiro_ss.geometry("1400x700")
    janela_solteiro_n_dinheiro_ss.title("Simulação do ordenado liquido - Trabalhador Dependente - Casado - 1 Titular - Outras contribuições")
    texto_topo = tk.CTkLabel(janela_solteiro_n_dinheiro_ss, text="Simulação do ordenado liquido\nTrabalhador Dependente\nSolteiro\nOutras contribuições", font=("Segoe UI", 20)).place(x=550, y=0)
    texto_adse = tk.CTkLabel(janela_solteiro_n_dinheiro_ss, text="É beneficiário da ADSE?", font=("Segoe UI", 20)).place(x=590, y=150)
    botao_sim = tk.CTkButton(janela_solteiro_n_dinheiro_ss, text= "Sim", command=lambda: dependente_1t_s_dinheiro_ss_adse(janela_solteiro_n_dinheiro_ss), font=("Segoe UI", 20)).place(x=530, y=200)
    botao_nao = tk.CTkButton(janela_solteiro_n_dinheiro_ss, text="Não", command=lambda: dependente_1t_s_dinheiro_ss_resultado(janela_solteiro_n_dinheiro_ss), font=("Segoe UI", 20)).place(x=730, y=200)


def dependente_1t_s_dinheiro(janela_solteiro_n, pedir_outros, pedir_alimentacao, pedir_dias):
    alimentacao = float(pedir_alimentacao.get())
    alimentacao_log.append(alimentacao)
    dias = float(pedir_dias.get())
    dias_log.append(dias)
    outros = float(pedir_outros.get())
    outros_log.append(outros)
    janela_solteiro_n.withdraw()
    janela_solteiro_n_dinheiro = tk.CTkToplevel()
    janela_solteiro_n_dinheiro.geometry("1400x700")
    janela_solteiro_n_dinheiro.title("Simulação do ordenado liquido - Trabalhador Dependente - Casado - 1 Titular - Outras contribuições")
    texto_topo = tk.CTkLabel(janela_solteiro_n_dinheiro, text="Simulação do ordenado liquido\nTrabalhador Dependente\nCasado - 1 Titular\nOutras contribuições", font=("Segoe UI", 20)).place(x=550, y=0)
    texto_forma = tk.CTkLabel(janela_solteiro_n_dinheiro, text = "Selecione a sua forma de contribuição social", font=("Segoe UI", 20)).place(x=510, y=150)
    botao_ss = tk.CTkButton(janela_solteiro_n_dinheiro, text="Segurança Social", command=lambda:dependente_1t_s_dinheiro_ss(janela_solteiro_n_dinheiro), font=("Segoe UI", 20)) .place(x=606, y=200)
    botao_cga = tk.CTkButton(janela_solteiro_n_dinheiro, text="Caixa Geral de Aposentações", command=lambda: dependente_1t_s_dinheiro_cga(janela_solteiro_n_dinheiro),  font=("Segoe UI",20)) .place(x=560, y=250)

def dependente_1t_s(janela_dependente_solteiro, pedir_renumeracao_base):

    ordenado2 = float(pedir_renumeracao_base.get())
    renumera_log.append(ordenado2)
    janela_dependente_solteiro.withdraw()
    janela_solteiro_n = tk.CTkToplevel()
    janela_solteiro_n.geometry("1400x700")
    janela_solteiro_n.title("Simulação do ordenado liquido - Trabalhador Dependente - Casado - 1 Titular - Subsidios")
    texto_topo = tk.CTkLabel(janela_solteiro_n,text="Simulação do ordenado liquido\nTrabalhador Dependente\nCasado - 1 Titular", font=("Segoe UI", 20)).place(x=550, y=0)
    texto_alimentacao = tk.CTkLabel(janela_solteiro_n,text="Insira o valor diário do subsidio de alimentação", font=("Segoe UI", 20)).place(x=490, y=100)
    pedir_alimentacao = tk.CTkEntry(janela_solteiro_n, placeholder_text= "Valor", font=("Segoe UI",20))
    pedir_alimentacao.place(x=636, y=150)
    texto_dias = tk.CTkLabel(janela_solteiro_n,text="Insira o número de dias com subsidio de alimentação", font=("Segoe UI", 20)).place(x=475, y=200)
    pedir_dias = tk.CTkEntry(janela_solteiro_n, placeholder_text="Dias", font=("Segoe UI", 20))
    pedir_dias.place(x=636, y=250)
    texto_outros = tk.CTkLabel(janela_solteiro_n, text = "Insira o valor de outros subsidios", font=("Segoe UI",20)) .place(x=550,y=300)
    pedir_outros = tk.CTkEntry(janela_solteiro_n, placeholder_text= "Valor", font=("Segoe UI",20))
    pedir_outros.place(x=636,y=350)
    texto_pag_alimentacao = tk.CTkLabel(janela_solteiro_n, text = "Selecione a forma de pagamento do subsidio de alimentacão", font=("Segoe UI", 20)) .place(x=450, y=400)
    botao_dinheiro = tk.CTkButton(janela_solteiro_n, text = "Dinheiro", font=("Segoe UI", 20), command=lambda: dependente_1t_s_dinheiro(janela_solteiro_n, pedir_outros, pedir_alimentacao, pedir_dias)) .place(x=490, y=450)
    botao_cartao = tk.CTkButton(janela_solteiro_n, text="Cartão/Vale de refeição", command=lambda:dependente_1t_s_vale(janela_solteiro_n, pedir_outros, pedir_alimentacao, pedir_dias),font=("Segoe UI", 20)) .place(x=690, y=450)


def dependente_1t(janela_dependente, pedir_dependentes):
    janela_dependente.withdraw()
    dependentes_log.append(pedir_dependentes.get())
    janela_dependente_solteiro=tk.CTkToplevel()
    janela_dependente_solteiro.title("Simulação do ordenado liquido - Trabalhador Dependente - Casado - 1 Titular")
    janela_dependente_solteiro.geometry("1400x700")
    texto_topo = tk.CTkLabel(janela_dependente_solteiro, text = "Simulação do ordenado liquido\nTrabalhador Dependente\nCasado - 1 Titular", font = ("Segoe UI", 20)) .place(x=560, y=0)
    texto_renumeracao_base = tk.CTkLabel(janela_dependente_solteiro, text = "Insira a sua renumeração base", font = ("Segoe UI", 20)) .place(x=569, y=100)
    pedir_renumeracao_base = tk.CTkEntry(janela_dependente_solteiro, placeholder_text = "Renumeração base", font = ("Segoe UI",20))
    pedir_renumeracao_base.place(x=616, y=150)
    texto_invalidez= tk.CTkLabel(janela_dependente_solteiro, text = "Possui algum tipo de invalidez (deficiencia)?", font = ("Segoe UI",20)) .place(x=524, y=200)
    sim_invalidez = tk.CTkButton(janela_dependente_solteiro, text = "Sim", font=("Sego UI",20), command = lambda: dependente_1t_s(janela_dependente_solteiro, pedir_renumeracao_base)). place(x = 626, y=250)
    nao_invalidez = tk.CTkButton(janela_dependente_solteiro, text = "Não", font=("Sego UI",20), command=lambda:dependente_1t_n(janela_dependente_solteiro, pedir_renumeracao_base)). place(x=626, y=300)






### DEPENDENTE ###

def dependente_solteiro_n_vale_cga_resultado(janela_solteiro_n_vale_cga):
    regime = 1
    situacao_fiscal = 1
    contribuicao_social = 2
    adse = 2
    forma_pagamento = 2
    valor_irs=0
    invalidez = 1
    valor_adse=0
    janela_solteiro_n_vale_cga.withdraw()
    janela_solteiro_n_vale_cga_resultado = tk.CTkToplevel()
    janela_solteiro_n_vale_cga_resultado.geometry("1400x700")
    janela_solteiro_n_vale_cga_resultado.title( "Simulação do ordenado liquido - Trabalhador Dependente - Solteiro - Resultado Final")
    texto_topo = tk.CTkLabel(janela_solteiro_n_vale_cga_resultado, text="Simulação do ordenado liquido\nTrabalhador Dependente\nSolteiro\nResultado Final", font=("Segoe UI", 20)).place(x=550, y=0)
    ordenado1 = float(renumera_log[0])
    dependentes = int(dependentes_log[0])
    alimentacao = float(alimentacao_log[0])
    dias_alimentacao = int(dias_log[0])
    outros = float(outros_log[0])
    if alimentacao < 9.6:
        excedente_alimentacao = 0
    else:
        excedente_alimentacao = alimentacao-9.6
    valor_alimentacao = alimentacao*dias_alimentacao
    excedente_alimentacao_dias = excedente_alimentacao*dias_alimentacao
    renumeracao = ordenado1+excedente_alimentacao_dias+outros

    if renumeracao<=762:
        renumeracao_liquida = 762
        taxa = 0
        parcela_dependente = 0
        parcela_abater = 0

    else:
        valor_irs, parcela_abater, taxa, renumeracao_liquida, parcela_dependente = ordenado_dependente_solteiro(dependentes, renumeracao)
    if valor_irs<0:
        valor_irs = 0
    else:
        valor_irs = valor_irs
    valor_ss = renumeracao*0.11
    renumeracao_final = renumeracao - valor_ss - valor_irs + valor_alimentacao


    ### SINTESE DE CARACTERISTICAS ###

    escrever_renumeracao = tk.CTkLabel(janela_solteiro_n_vale_cga_resultado, text=("Ordenado Base: {} €" .format(ordenado1)), font=("Segoe UI", 20)).place(x=150, y=100)
    escrever_regime = tk.CTkLabel(janela_solteiro_n_vale_cga_resultado, text=("Regime: Trabalhador Dependente"), font=("Segoe UI", 20)).place(x=150, y=150)
    escrever_fiscal = tk.CTkLabel(janela_solteiro_n_vale_cga_resultado, text = ("Situação Fiscal: Solteiro"), font=("Segoe UI", 20)).place(x=150,y=200)
    escrever_dependentes = tk.CTkLabel(janela_solteiro_n_vale_cga_resultado, text=("Dependentes: {}".format(dependentes)), font=("Segoe UI", 20)).place(x=150, y=250)
    escrever_social = tk.CTkLabel(janela_solteiro_n_vale_cga_resultado, text=("Contribuição Social: Caixa Geral de Aposentações"), font=("Segoe UI", 20)).place(x=150, y=300)
    escrever_adse = tk.CTkLabel(janela_solteiro_n_vale_cga_resultado, text=("ADSE: Não"), font=("Segoe UI", 20)).place(x=150, y=350)
    escrever_alimentacao = tk.CTkLabel(janela_solteiro_n_vale_cga_resultado, text=("Subsidio de Alimentação: {} €".format(valor_alimentacao)), font=("Segoe UI", 20)).place(x=150, y=400)
    escrever_dias = tk.CTkLabel(janela_solteiro_n_vale_cga_resultado, text=("Dias com susbsidio de alimentação: {}".format(dias_alimentacao)), font=("Segoe UI", 20)).place(x=150, y=450)
    escrever_pagamento = tk.CTkLabel(janela_solteiro_n_vale_cga_resultado, text=("Forma de pagamento do subsidio de alimentação: Vale/Cartão de refeição"), font=("Segoe UI", 20)).place(x=150, y=500)
    escrever_outros = tk.CTkLabel(janela_solteiro_n_vale_cga_resultado, text=("Outros subsidios tributaveis: {} €".format(outros)), font=("Segoe UI", 20)).place(x=150, y=550)
    escrever_invalidez = tk.CTkLabel(janela_solteiro_n_vale_cga_resultado, text=("Invalidez ou incapacidade: Não"), font=("Segoe UI", 20)).place(x=150, y=600)

### APRESENTAÇÃO DOS VALORES ###
    texto_descontos = tk.CTkLabel(janela_solteiro_n_vale_cga_resultado, text=("Resumo dos descontos"), font=("Segoe UI", 20)) .place(x=879, y=150)
    texto_valor = tk.CTkLabel(janela_solteiro_n_vale_cga_resultado, text=("Valor tributável:{:.2f}€ " .format(renumeracao)), font=("Segoe UI", 20)).place(x=879 , y=300)
    texto_irs = tk.CTkLabel(janela_solteiro_n_vale_cga_resultado, text=("Retenção na fonte: {:.2f}€" .format(valor_irs)), font=("Segoe UI", 20)).place(x=879 , y=200)
    texto_ss = tk.CTkLabel(janela_solteiro_n_vale_cga_resultado, text=("Taxa Social Única: {:.2f}€" .format(valor_ss)), font=("Segoe UI", 20)).place(x=879 , y=250)
    valor_final = tk.CTkLabel(janela_solteiro_n_vale_cga_resultado, text=( "Valor após descontos: {:.2f}€" .format(renumeracao_final)), font=("Segoe UI", 20), bg_color = "red").place(x=879 , y=300)

### FINAL - SAIR OU HISTORICO ###
    decidir_historico = tk.CTkLabel(janela_solteiro_n_vale_cga_resultado, text=("Deseja adicionar está simulação ao histórico?" ), font=("Segoe UI", 20)).place(x=879, y=500)
    select_tabela_a = tk.CTkButton(janela_solteiro_n_vale_cga_resultado, text="Sim",command=lambda: historico_ordenado(regime, situacao_fiscal, dependentes, contribuicao_social, adse, valor_alimentacao, dias_alimentacao, forma_pagamento, outros, renumeracao, valor_irs, valor_adse, valor_ss, renumeracao_final, invalidez),font=("Segoe UI", 20)).place(x=879, y=550)
    select_tabela_b = tk.CTkButton(janela_solteiro_n_vale_cga_resultado, text="Não",command=lambda: reiniciar_programa(),font=("Segoe UI", 20)).place(x=1079, y=550)



def dependente_solteiro_n_vale_cga_adse(janela_solteiro_n_vale_cga):
    regime = 1
    situacao_fiscal = 1
    contribuicao_social = 2
    adse = 1
    forma_pagamento = 2
    valor_irs=0
    invalidez = 1
    janela_solteiro_n_vale_cga.withdraw()
    janela_solteiro_n_vale_cga_adse = tk.CTkToplevel()
    janela_solteiro_n_vale_cga_adse.geometry("1400x700")
    janela_solteiro_n_vale_cga_adse.title( "Simulação do ordenado liquido - Trabalhador Dependente - Solteiro - Resultado Final")
    texto_topo = tk.CTkLabel(janela_solteiro_n_vale_cga_adse, text="Simulação do ordenado liquido\nTrabalhador Dependente\nSolteiro\nResultado Final", font=("Segoe UI", 20)).place(x=550, y=0)
    ordenado1 = float(renumera_log[0])
    dependentes = int(dependentes_log[0])
    alimentacao = float(alimentacao_log[0])
    dias_alimentacao = int(dias_log[0])
    outros = float(outros_log[0])
    if alimentacao < 9.6:
        excedente_alimentacao = 0
    else:
        excedente_alimentacao = alimentacao-9.6
    valor_alimentacao = alimentacao*dias_alimentacao
    excedente_alimentacao_dias = excedente_alimentacao*dias_alimentacao
    renumeracao = ordenado1+excedente_alimentacao_dias+outros

    if renumeracao<=762:
        renumeracao_liquida = 762
        taxa = 0
        parcela_dependente = 0
        parcela_abater = 0

    else:
        valor_irs, parcela_abater, taxa, renumeracao_liquida, parcela_dependente = ordenado_dependente_solteiro(dependentes, renumeracao)

    valor_ss = renumeracao*0.11
    valor_adse = renumeracao*0.035
    if valor_irs<0:
        valor_irs = 0
    else:
        valor_irs = valor_irs
    renumeracao_final = renumeracao - valor_adse - valor_ss - valor_irs+valor_alimentacao

    ### SINTESE DE CARACTERISTICAS ###

    escrever_renumeracao = tk.CTkLabel(janela_solteiro_n_vale_cga_adse, text=("Ordenado Base: {} €" .format(ordenado1)), font=("Segoe UI", 20)).place(x=150, y=100)
    escrever_regime = tk.CTkLabel(janela_solteiro_n_vale_cga_adse, text=("Regime: Trabalhador Dependente"), font=("Segoe UI", 20)).place(x=150, y=150)
    escrever_fiscal = tk.CTkLabel(janela_solteiro_n_vale_cga_adse, text = ("Situação Fiscal: Solteiro"), font=("Segoe UI", 20)).place(x=150,y=200)
    escrever_dependentes = tk.CTkLabel(janela_solteiro_n_vale_cga_adse, text=("Dependentes: {}".format(dependentes)), font=("Segoe UI", 20)).place(x=150, y=250)
    escrever_social = tk.CTkLabel(janela_solteiro_n_vale_cga_adse, text=("Contribuição Social: Caixa Geral de Aposentações"), font=("Segoe UI", 20)).place(x=150, y=300)
    escrever_adse = tk.CTkLabel(janela_solteiro_n_vale_cga_adse, text=("ADSE: Sim"), font=("Segoe UI", 20)).place(x=150, y=350)
    escrever_alimentacao = tk.CTkLabel(janela_solteiro_n_vale_cga_adse, text=("Subsidio de Alimentação: {} €".format(valor_alimentacao)), font=("Segoe UI", 20)).place(x=150, y=400)
    escrever_dias = tk.CTkLabel(janela_solteiro_n_vale_cga_adse, text=("Dias com susbsidio de alimentação: {}".format(dias_alimentacao)), font=("Segoe UI", 20)).place(x=150, y=450)
    escrever_pagamento = tk.CTkLabel(janela_solteiro_n_vale_cga_adse, text=("Forma de pagamento do subsidio de alimentação: Vale/Cartão de alimentação"), font=("Segoe UI", 20)).place(x=150, y=500)
    escrever_outros = tk.CTkLabel(janela_solteiro_n_vale_cga_adse, text=("Outros subsidios tributaveis: {} €".format(outros)), font=("Segoe UI", 20)).place(x=150, y=550)
    escrever_invalidez = tk.CTkLabel(janela_solteiro_n_vale_cga_adse, text=("Invalidez ou incapacidade: Não"), font=("Segoe UI", 20)).place(x=150, y=600)

### APRESENTAÇÃO DOS VALORES ###
    texto_descontos = tk.CTkLabel(janela_solteiro_n_vale_cga_adse, text=("Resumo dos descontos"), font=("Segoe UI", 20)) .place(x=879, y=150)
    texto_valor = tk.CTkLabel(janela_solteiro_n_vale_cga_adse, text=("Valor tributável:{:.2f}€ " .format(renumeracao)), font=("Segoe UI", 20)).place(x=879 , y=300)
    texto_irs = tk.CTkLabel(janela_solteiro_n_vale_cga_adse, text=("Retenção na fonte: {:.2f}€" .format(valor_irs)), font=("Segoe UI", 20)).place(x=879 , y=200)
    texto_ss = tk.CTkLabel(janela_solteiro_n_vale_cga_adse, text=("Taxa Social Única: {:.2f}€" .format(valor_ss)), font=("Segoe UI", 20)).place(x=879 , y=250)
    taxa_adse = tk.CTkLabel(janela_solteiro_n_vale_cga_adse, text=("Desconto ADSE: {:.2f}€" .format(valor_adse)), font=("Segoe UI", 20)).place(x=879 , y=350)
    valor_final = tk.CTkLabel(janela_solteiro_n_vale_cga_adse, text=( "Valor após descontos: {:.2f}€" .format(renumeracao_final)), font=("Segoe UI", 20), bg_color = "red").place(x=879 , y=450)

### FINAL - SAIR OU HISTORICO ###
    decidir_historico = tk.CTkLabel(janela_solteiro_n_vale_cga_adse, text=("Deseja adicionar está simulação ao histórico?" ), font=("Segoe UI", 20)).place(x=879, y=500)
    select_tabela_a = tk.CTkButton(janela_solteiro_n_vale_cga_adse, text="Sim",command=lambda: historico_ordenado(regime, situacao_fiscal, dependentes, contribuicao_social, adse, valor_alimentacao, dias_alimentacao, forma_pagamento, outros, renumeracao, valor_irs, valor_adse, valor_ss, renumeracao_final, invalidez),font=("Segoe UI", 20)).place(x=879, y=550)
    select_tabela_b = tk.CTkButton(janela_solteiro_n_vale_cga_adse, text="Não",command=lambda: reiniciar_programa(),font=("Segoe UI", 20)).place(x=1079, y=550)



def dependente_solteiro_n_vale_cga(janela_solteiro_n_vale):
    janela_solteiro_n_vale.withdraw()
    janela_solteiro_n_vale_cga = tk.CTkToplevel()
    janela_solteiro_n_vale_cga.geometry("1400x700")
    janela_solteiro_n_vale_cga.title("Simulação do ordenado liquido - Trabalhador Dependente - Solteiro - Outras contribuições")
    texto_topo = tk.CTkLabel(janela_solteiro_n_vale_cga, text="Simulação do ordenado liquido\nTrabalhador Dependente\nSolteiro\nOutras contribuições", font=("Segoe UI", 20)).place(x=550, y=0)
    texto_adse = tk.CTkLabel(janela_solteiro_n_vale_cga, text="É beneficiário da ADSE?", font=("Segoe UI", 20)).place(x=590, y=150)
    botao_sim = tk.CTkButton(janela_solteiro_n_vale_cga, text= "Sim", command=lambda: dependente_solteiro_n_vale_cga_adse(janela_solteiro_n_vale_cga), font=("Segoe UI", 20)).place(x=530, y=200)
    botao_nao = tk.CTkButton(janela_solteiro_n_vale_cga, text="Não", command=lambda: dependente_solteiro_n_vale_cga_resultado(janela_solteiro_n_vale_cga), font=("Segoe UI", 20)).place(x=730, y=200)

def dependente_solteiro_n_vale_ss_resultado(janela_solteiro_n_vale_ss):
    regime = 1
    situacao_fiscal = 1
    contribuicao_social = 1
    adse = 2
    forma_pagamento = 2
    valor_irs=0
    invalidez = 1
    valor_adse=0
    janela_solteiro_n_vale_ss.withdraw()
    janela_solteiro_n_vale_ss_resultado = tk.CTkToplevel()
    janela_solteiro_n_vale_ss_resultado.geometry("1400x700")
    janela_solteiro_n_vale_ss_resultado.title( "Simulação do ordenado liquido - Trabalhador Dependente - Solteiro - Resultado Final")
    texto_topo = tk.CTkLabel(janela_solteiro_n_vale_ss_resultado, text="Simulação do ordenado liquido\nTrabalhador Dependente\nSolteiro\nResultado Final", font=("Segoe UI", 20)).place(x=550, y=0)
    ordenado1 = float(renumera_log[0])
    dependentes = int(dependentes_log[0])
    alimentacao = float(alimentacao_log[0])
    dias_alimentacao = int(dias_log[0])
    outros = float(outros_log[0])
    if alimentacao <9.6:
        excedente_alimentacao = 0
    else:
        excedente_alimentacao = alimentacao-9.6
    valor_alimentacao = alimentacao*dias_alimentacao
    excedente_alimentacao_dias = excedente_alimentacao*dias_alimentacao
    renumeracao = ordenado1+excedente_alimentacao_dias+outros

    if renumeracao<=762:
        renumeracao_liquida = 762
        taxa = 0
        parcela_dependente = 0
        parcela_abater = 0

    else:
        valor_irs, parcela_abater, taxa, renumeracao_liquida, parcela_dependente = ordenado_dependente_solteiro(dependentes, renumeracao)
    if valor_irs<0:
        valor_irs = 0
    else:
        valor_irs = valor_irs
    valor_ss = renumeracao*0.11
    renumeracao_final = renumeracao - valor_ss - valor_irs + valor_alimentacao


    ### SINTESE DE CARACTERISTICAS ###

    escrever_renumeracao = tk.CTkLabel(janela_solteiro_n_vale_ss_resultado, text=("Ordenado Base: {} €" .format(ordenado1)), font=("Segoe UI", 20)).place(x=150, y=100)
    escrever_regime = tk.CTkLabel(janela_solteiro_n_vale_ss_resultado, text=("Regime: Trabalhador Dependente"), font=("Segoe UI", 20)).place(x=150, y=150)
    escrever_fiscal = tk.CTkLabel(janela_solteiro_n_vale_ss_resultado, text = ("Situação Fiscal: Solteiro"), font=("Segoe UI", 20)).place(x=150,y=200)
    escrever_dependentes = tk.CTkLabel(janela_solteiro_n_vale_ss_resultado, text=("Dependentes: {}".format(dependentes)), font=("Segoe UI", 20)).place(x=150, y=250)
    escrever_social = tk.CTkLabel(janela_solteiro_n_vale_ss_resultado, text=("Contribuição Social: Segurança Social"), font=("Segoe UI", 20)).place(x=150, y=300)
    escrever_adse = tk.CTkLabel(janela_solteiro_n_vale_ss_resultado, text=("ADSE: Não"), font=("Segoe UI", 20)).place(x=150, y=350)
    escrever_alimentacao = tk.CTkLabel(janela_solteiro_n_vale_ss_resultado, text=("Subsidio de Alimentação: {} €".format(valor_alimentacao)), font=("Segoe UI", 20)).place(x=150, y=400)
    escrever_dias = tk.CTkLabel(janela_solteiro_n_vale_ss_resultado, text=("Dias com susbsidio de alimentação: {}".format(dias_alimentacao)), font=("Segoe UI", 20)).place(x=150, y=450)
    escrever_pagamento = tk.CTkLabel(janela_solteiro_n_vale_ss_resultado, text=("Forma de pagamento do subsidio de alimentação: Vale/Cartão de Refeição"), font=("Segoe UI", 20)).place(x=150, y=500)
    escrever_outros = tk.CTkLabel(janela_solteiro_n_vale_ss_resultado, text=("Outros subsidios tributaveis: {} €".format(outros)), font=("Segoe UI", 20)).place(x=150, y=550)
    escrever_invalidez = tk.CTkLabel(janela_solteiro_n_vale_ss_resultado, text=("Invalidez ou incapacidade: Não"), font=("Segoe UI", 20)).place(x=150, y=600)

### APRESENTAÇÃO DOS VALORES ###
    texto_descontos = tk.CTkLabel(janela_solteiro_n_vale_ss_resultado, text=("Resumo dos descontos"), font=("Segoe UI", 20)) .place(x=879, y=150)
    texto_valor = tk.CTkLabel(janela_solteiro_n_vale_ss_resultado, text=("Valor tributável:{:.2f}€ " .format(renumeracao)), font=("Segoe UI", 20)).place(x=879 , y=300)
    texto_irs = tk.CTkLabel(janela_solteiro_n_vale_ss_resultado, text=("Retenção na fonte: {:.2f}€" .format(valor_irs)), font=("Segoe UI", 20)).place(x=879 , y=200)
    texto_ss = tk.CTkLabel(janela_solteiro_n_vale_ss_resultado, text=("Taxa Social Única: {:.2f}€" .format(valor_ss)), font=("Segoe UI", 20)).place(x=879 , y=250)
    valor_final = tk.CTkLabel(janela_solteiro_n_vale_ss_resultado, text=( "Valor após descontos: {:.2f}€" .format(renumeracao_final)), font=("Segoe UI", 20), bg_color = "red").place(x=879 , y=300)

### FINAL - SAIR OU HISTORICO ###
    decidir_historico = tk.CTkLabel(janela_solteiro_n_vale_ss_resultado, text=("Deseja adicionar está simulação ao histórico?" ), font=("Segoe UI", 20)).place(x=879, y=500)
    select_tabela_a = tk.CTkButton(janela_solteiro_n_vale_ss_resultado, text="Sim",command=lambda: historico_ordenado(regime, situacao_fiscal, dependentes, contribuicao_social, adse, valor_alimentacao, dias_alimentacao, forma_pagamento, outros, renumeracao, valor_irs, valor_adse, valor_ss, renumeracao_final, invalidez),font=("Segoe UI", 20)).place(x=879, y=550)
    select_tabela_b = tk.CTkButton(janela_solteiro_n_vale_ss_resultado, text="Não",command=lambda: reiniciar_programa(),font=("Segoe UI", 20)).place(x=1079, y=550)



def dependente_solteiro_n_vale_ss_adse(janela_solteiro_n_vale_ss):
    regime = 1
    situacao_fiscal = 1
    contribuicao_social = 1
    adse = 1
    forma_pagamento = 2
    valor_irs=0
    invalidez = 1
    janela_solteiro_n_vale_ss.withdraw()
    janela_solteiro_n_vale_ss_adse = tk.CTkToplevel()
    janela_solteiro_n_vale_ss_adse.geometry("1400x700")
    janela_solteiro_n_vale_ss_adse.title( "Simulação do ordenado liquido - Trabalhador Dependente - Solteiro - Resultado Final")
    texto_topo = tk.CTkLabel(janela_solteiro_n_vale_ss_adse, text="Simulação do ordenado liquido\nTrabalhador Dependente\nSolteiro\nResultado Final", font=("Segoe UI", 20)).place(x=550, y=0)
    ordenado1 = float(renumera_log[0])
    dependentes = int(dependentes_log[0])
    alimentacao = float(alimentacao_log[0])
    dias_alimentacao = int(dias_log[0])
    outros = float(outros_log[0])
    if alimentacao < 9.6:
        excedente_alimentacao = 0
    else:
        excedente_alimentacao = alimentacao-9.6
    valor_alimentacao = alimentacao*dias_alimentacao
    excedente_alimentacao_dias = excedente_alimentacao*dias_alimentacao
    renumeracao = ordenado1+excedente_alimentacao_dias+outros

    if renumeracao<=762:
        renumeracao_liquida = 762
        taxa = 0
        parcela_dependente = 0
        parcela_abater = 0

    else:
        valor_irs, parcela_abater, taxa, renumeracao_liquida, parcela_dependente = ordenado_dependente_solteiro(dependentes, renumeracao)

    valor_ss = renumeracao*0.11
    valor_adse = renumeracao*0.035

    if valor_irs<0:
        valor_irs = 0
    else:
        valor_irs = valor_irs

    renumeracao_final = renumeracao - valor_adse - valor_ss - valor_irs+valor_alimentacao

    ### SINTESE DE CARACTERISTICAS ###

    escrever_renumeracao = tk.CTkLabel(janela_solteiro_n_vale_ss_adse, text=("Ordenado Base: {} €" .format(ordenado1)), font=("Segoe UI", 20)).place(x=150, y=100)
    escrever_regime = tk.CTkLabel(janela_solteiro_n_vale_ss_adse, text=("Regime: Trabalhador Dependente"), font=("Segoe UI", 20)).place(x=150, y=150)
    escrever_fiscal = tk.CTkLabel(janela_solteiro_n_vale_ss_adse, text = ("Situação Fiscal: Solteiro"), font=("Segoe UI", 20)).place(x=150,y=200)
    escrever_dependentes = tk.CTkLabel(janela_solteiro_n_vale_ss_adse, text=("Dependentes: {}".format(dependentes)), font=("Segoe UI", 20)).place(x=150, y=250)
    escrever_social = tk.CTkLabel(janela_solteiro_n_vale_ss_adse, text=("Contribuição Social: Segurança Social"), font=("Segoe UI", 20)).place(x=150, y=300)
    escrever_adse = tk.CTkLabel(janela_solteiro_n_vale_ss_adse, text=("ADSE: Sim"), font=("Segoe UI", 20)).place(x=150, y=350)
    escrever_alimentacao = tk.CTkLabel(janela_solteiro_n_vale_ss_adse, text=("Subsidio de Alimentação: {} €".format(valor_alimentacao)), font=("Segoe UI", 20)).place(x=150, y=400)
    escrever_dias = tk.CTkLabel(janela_solteiro_n_vale_ss_adse, text=("Dias com susbsidio de alimentação: {}".format(dias_alimentacao)), font=("Segoe UI", 20)).place(x=150, y=450)
    escrever_pagamento = tk.CTkLabel(janela_solteiro_n_vale_ss_adse, text=("Forma de pagamento do subsidio de alimentação: Cartão/Vale de alimentação"), font=("Segoe UI", 20)).place(x=150, y=500)
    escrever_outros = tk.CTkLabel(janela_solteiro_n_vale_ss_adse, text=("Outros subsidios tributaveis: {} €".format(outros)), font=("Segoe UI", 20)).place(x=150, y=550)
    escrever_invalidez = tk.CTkLabel(janela_solteiro_n_vale_ss_adse, text=("Invalidez ou incapacidade: Não"), font=("Segoe UI", 20)).place(x=150, y=600)

### APRESENTAÇÃO DOS VALORES ###
    texto_descontos = tk.CTkLabel(janela_solteiro_n_vale_ss_adse, text=("Resumo dos descontos"), font=("Segoe UI", 20)) .place(x=879, y=150)
    texto_valor = tk.CTkLabel(janela_solteiro_n_vale_ss_adse, text=("Valor tributável:{:.2f}€ " .format(renumeracao)), font=("Segoe UI", 20)).place(x=879 , y=300)
    texto_irs = tk.CTkLabel(janela_solteiro_n_vale_ss_adse, text=("Retenção na fonte: {:.2f}€" .format(valor_irs)), font=("Segoe UI", 20)).place(x=879 , y=200)
    texto_ss = tk.CTkLabel(janela_solteiro_n_vale_ss_adse, text=("Taxa Social Única: {:.2f}€" .format(valor_ss)), font=("Segoe UI", 20)).place(x=879 , y=250)
    taxa_adse = tk.CTkLabel(janela_solteiro_n_vale_ss_adse, text=("Desconto ADSE: {:.2f}€" .format(valor_adse)), font=("Segoe UI", 20)).place(x=879 , y=350)
    valor_final = tk.CTkLabel(janela_solteiro_n_vale_ss_adse, text=( "Valor após descontos: {:.2f}€" .format(renumeracao_final)), font=("Segoe UI", 20), bg_color = "red").place(x=879 , y=450)

### FINAL - SAIR OU HISTORICO ###
    decidir_historico = tk.CTkLabel(janela_solteiro_n_vale_ss_adse, text=("Deseja adicionar está simulação ao histórico?" ), font=("Segoe UI", 20)).place(x=879, y=500)
    select_tabela_a = tk.CTkButton(janela_solteiro_n_vale_ss_adse, text="Sim",command=lambda: historico_ordenado(regime, situacao_fiscal, dependentes, contribuicao_social, adse, valor_alimentacao, dias_alimentacao, forma_pagamento, outros, renumeracao, valor_irs, valor_adse, valor_ss, renumeracao_final, invalidez),font=("Segoe UI", 20)).place(x=879, y=550)
    select_tabela_b = tk.CTkButton(janela_solteiro_n_vale_ss_adse, text="Não",command=lambda: reiniciar_programa(),font=("Segoe UI", 20)).place(x=1079, y=550)



def dependente_solteiro_n_vale_ss(janela_solteiro_n_vale):
    janela_solteiro_n_vale.withdraw()
    janela_solteiro_n_vale_ss = tk.CTkToplevel()
    janela_solteiro_n_vale_ss.geometry("1400x700")
    janela_solteiro_n_vale_ss.title("Simulação do ordenado liquido - Trabalhador Dependente - Solteiro - Outras contribuições")
    texto_topo = tk.CTkLabel(janela_solteiro_n_vale_ss, text="Simulação do ordenado liquido\nTrabalhador Dependente\nSolteiro\nOutras contribuições", font=("Segoe UI", 20)).place(x=550, y=0)
    texto_adse = tk.CTkLabel(janela_solteiro_n_vale_ss, text="É beneficiário da ADSE?", font=("Segoe UI", 20)).place(x=590, y=150)
    botao_sim = tk.CTkButton(janela_solteiro_n_vale_ss, text= "Sim", command=lambda: dependente_solteiro_n_vale_ss_adse(janela_solteiro_n_vale_ss), font=("Segoe UI", 20)).place(x=530, y=200)
    botao_nao = tk.CTkButton(janela_solteiro_n_vale_ss, text="Não", command=lambda: dependente_solteiro_n_vale_ss_resultado(janela_solteiro_n_vale_ss), font=("Segoe UI", 20)).place(x=730, y=200)




def dependente_solteiro_n_vale(janela_solteiro_n, pedir_outros, pedir_alimentacao, pedir_dias):
    alimentacao = float(pedir_alimentacao.get())
    alimentacao_log.append(alimentacao)
    dias = float(pedir_dias.get())
    dias_log.append(dias)
    outros = float(pedir_outros.get())
    outros_log.append(outros)
    janela_solteiro_n.withdraw()
    janela_solteiro_n_vale = tk.CTkToplevel()
    janela_solteiro_n_vale.geometry("1400x700")
    janela_solteiro_n_vale.title("Simulação do ordenado liquido - Trabalhador Dependente - Solteiro - Outras contribuições")
    texto_topo = tk.CTkLabel(janela_solteiro_n_vale, text="Simulação do ordenado liquido\nTrabalhador Dependente\nSolteiro\nOutras contribuições", font=("Segoe UI", 20)).place(x=550, y=0)
    texto_forma = tk.CTkLabel(janela_solteiro_n_vale, text = "Selecione a sua forma de contribuição social", font=("Segoe UI", 20)).place(x=510, y=150)
    botao_ss = tk.CTkButton(janela_solteiro_n_vale, text="Segurança Social", command=lambda:dependente_solteiro_n_vale_ss(janela_solteiro_n_vale), font=("Segoe UI", 20)) .place(x=606, y=200)
    botao_cga = tk.CTkButton(janela_solteiro_n_vale, text="Caixa Geral de Aposentações", command=lambda: dependente_solteiro_n_vale_cga(janela_solteiro_n_vale),  font=("Segoe UI",20)) .place(x=560, y=250)




def dependente_solteiro_n_dinheiro_ss_resultado(janela_solteiro_n_dinheiro_ss):
    regime = 1
    situacao_fiscal = 1
    contribuicao_social = 1
    adse = 2
    forma_pagamento = 1
    valor_irs=0
    invalidez = 1
    valor_adse=0
    janela_solteiro_n_dinheiro_ss.withdraw()
    janela_solteiro_n_dinheiro_ss_resultado = tk.CTkToplevel()
    janela_solteiro_n_dinheiro_ss_resultado.geometry("1400x700")
    janela_solteiro_n_dinheiro_ss_resultado.title( "Simulação do ordenado liquido - Trabalhador Dependente - Solteiro - Resultado Final")
    texto_topo = tk.CTkLabel(janela_solteiro_n_dinheiro_ss_resultado, text="Simulação do ordenado liquido\nTrabalhador Dependente\nSolteiro\nResultado Final", font=("Segoe UI", 20)).place(x=550, y=0)
    ordenado1 = float(renumera_log[0])
    dependentes = int(dependentes_log[0])
    alimentacao = float(alimentacao_log[0])
    dias_alimentacao = int(dias_log[0])
    outros = float(outros_log[0])
    if alimentacao < 6:
        excedente_alimentacao = 0
    else:
        excedente_alimentacao = alimentacao-6
    valor_alimentacao = alimentacao*dias_alimentacao
    excedente_alimentacao_dias = excedente_alimentacao*dias_alimentacao
    renumeracao = ordenado1+excedente_alimentacao_dias+outros

    if renumeracao<=762:
        renumeracao_liquida = 762
        taxa = 0
        parcela_dependente = 0
        parcela_abater = 0

    else:
        valor_irs, parcela_abater, taxa, renumeracao_liquida, parcela_dependente = ordenado_dependente_solteiro(dependentes, renumeracao)
    if valor_irs<0:
        valor_irs = 0
    else:
        valor_irs = valor_irs
    valor_ss = renumeracao*0.11
    renumeracao_final = renumeracao - valor_ss - valor_irs + valor_alimentacao


    ### SINTESE DE CARACTERISTICAS ###

    escrever_renumeracao = tk.CTkLabel(janela_solteiro_n_dinheiro_ss_resultado, text=("Ordenado Base: {} €" .format(ordenado1)), font=("Segoe UI", 20)).place(x=150, y=100)
    escrever_regime = tk.CTkLabel(janela_solteiro_n_dinheiro_ss_resultado, text=("Regime: Trabalhador Dependente"), font=("Segoe UI", 20)).place(x=150, y=150)
    escrever_fiscal = tk.CTkLabel(janela_solteiro_n_dinheiro_ss_resultado, text = ("Situação Fiscal: Solteiro"), font=("Segoe UI", 20)).place(x=150,y=200)
    escrever_dependentes = tk.CTkLabel(janela_solteiro_n_dinheiro_ss_resultado, text=("Dependentes: {}".format(dependentes)), font=("Segoe UI", 20)).place(x=150, y=250)
    escrever_social = tk.CTkLabel(janela_solteiro_n_dinheiro_ss_resultado, text=("Contribuição Social: Segurança Social"), font=("Segoe UI", 20)).place(x=150, y=300)
    escrever_adse = tk.CTkLabel(janela_solteiro_n_dinheiro_ss_resultado, text=("ADSE: Não"), font=("Segoe UI", 20)).place(x=150, y=350)
    escrever_alimentacao = tk.CTkLabel(janela_solteiro_n_dinheiro_ss_resultado, text=("Subsidio de Alimentação: {} €".format(valor_alimentacao)), font=("Segoe UI", 20)).place(x=150, y=400)
    escrever_dias = tk.CTkLabel(janela_solteiro_n_dinheiro_ss_resultado, text=("Dias com susbsidio de alimentação: {}".format(dias_alimentacao)), font=("Segoe UI", 20)).place(x=150, y=450)
    escrever_pagamento = tk.CTkLabel(janela_solteiro_n_dinheiro_ss_resultado, text=("Forma de pagamento do subsidio de alimentação: Dinheiro"), font=("Segoe UI", 20)).place(x=150, y=500)
    escrever_outros = tk.CTkLabel(janela_solteiro_n_dinheiro_ss_resultado, text=("Outros subsidios tributaveis: {} €".format(outros)), font=("Segoe UI", 20)).place(x=150, y=550)
    escrever_invalidez = tk.CTkLabel(janela_solteiro_n_dinheiro_ss_resultado, text=("Invalidez ou incapacidade: Não"), font=("Segoe UI", 20)).place(x=150, y=600)

### APRESENTAÇÃO DOS VALORES ###
    texto_descontos = tk.CTkLabel(janela_solteiro_n_dinheiro_ss_resultado, text=("Resumo dos descontos"), font=("Segoe UI", 20)) .place(x=879, y=150)
    texto_valor = tk.CTkLabel(janela_solteiro_n_dinheiro_ss_resultado, text=("Valor tributável:{:.2f}€ " .format(renumeracao)), font=("Segoe UI", 20)).place(x=879 , y=300)
    texto_irs = tk.CTkLabel(janela_solteiro_n_dinheiro_ss_resultado, text=("Retenção na fonte: {:.2f}€" .format(valor_irs)), font=("Segoe UI", 20)).place(x=879 , y=200)
    texto_ss = tk.CTkLabel(janela_solteiro_n_dinheiro_ss_resultado, text=("Taxa Social Única: {:.2f}€" .format(valor_ss)), font=("Segoe UI", 20)).place(x=879 , y=250)
    valor_final = tk.CTkLabel(janela_solteiro_n_dinheiro_ss_resultado, text=( "Valor após descontos: {:.2f}€" .format(renumeracao_final)), font=("Segoe UI", 20), bg_color = "red").place(x=879 , y=300)

### FINAL - SAIR OU HISTORICO ###
    decidir_historico = tk.CTkLabel(janela_solteiro_n_dinheiro_ss_resultado, text=("Deseja adicionar está simulação ao histórico?" ), font=("Segoe UI", 20)).place(x=879, y=500)
    select_tabela_a = tk.CTkButton(janela_solteiro_n_dinheiro_ss_resultado, text="Sim",command=lambda: historico_ordenado(regime, situacao_fiscal, dependentes, contribuicao_social, adse, valor_alimentacao, dias_alimentacao, forma_pagamento, outros, renumeracao, valor_irs, valor_adse, valor_ss, renumeracao_final, invalidez),font=("Segoe UI", 20)).place(x=879, y=550)
    select_tabela_b = tk.CTkButton(janela_solteiro_n_dinheiro_ss_resultado, text="Não",command=lambda: reiniciar_programa(),font=("Segoe UI", 20)).place(x=1079, y=550)



def dependente_solteiro_n_dinheiro_ss_adse(janela_solteiro_n_dinheiro_ss):
    regime = 1
    situacao_fiscal = 1
    contribuicao_social = 1
    adse = 1
    forma_pagamento = 1
    valor_irs=0
    invalidez = 1
    janela_solteiro_n_dinheiro_ss.withdraw()
    janela_solteiro_n_dinheiro_ss_adse = tk.CTkToplevel()
    janela_solteiro_n_dinheiro_ss_adse.geometry("1400x700")
    janela_solteiro_n_dinheiro_ss_adse.title( "Simulação do ordenado liquido - Trabalhador Dependente - Solteiro - Resultado Final")
    texto_topo = tk.CTkLabel(janela_solteiro_n_dinheiro_ss_adse, text="Simulação do ordenado liquido\nTrabalhador Dependente\nSolteiro\nResultado Final", font=("Segoe UI", 20)).place(x=550, y=0)
    ordenado1 = float(renumera_log[0])
    dependentes = int(dependentes_log[0])
    alimentacao = float(alimentacao_log[0])
    dias_alimentacao = int(dias_log[0])
    outros = float(outros_log[0])
    if alimentacao < 6:
        excedente_alimentacao = 0
    else:
        excedente_alimentacao = alimentacao-6
    valor_alimentacao = alimentacao*dias_alimentacao
    excedente_alimentacao_dias = excedente_alimentacao*dias_alimentacao
    renumeracao = ordenado1+excedente_alimentacao_dias+outros

    if renumeracao<=762:
        renumeracao_liquida = 762
        taxa = 0
        parcela_dependente = 0
        parcela_abater = 0

    else:
        valor_irs, parcela_abater, taxa, renumeracao_liquida, parcela_dependente = ordenado_dependente_solteiro(dependentes, renumeracao)

    valor_ss = renumeracao*0.11
    valor_adse = renumeracao*0.035

    if valor_irs<0:
        valor_irs = 0
    else:
        valor_irs = valor_irs

    renumeracao_final = renumeracao - valor_adse - valor_ss - valor_irs+valor_alimentacao

    ### SINTESE DE CARACTERISTICAS ###

    escrever_renumeracao = tk.CTkLabel(janela_solteiro_n_dinheiro_ss_adse, text=("Ordenado Base: {} €" .format(ordenado1)), font=("Segoe UI", 20)).place(x=150, y=100)
    escrever_regime = tk.CTkLabel(janela_solteiro_n_dinheiro_ss_adse, text=("Regime: Trabalhador Dependente"), font=("Segoe UI", 20)).place(x=150, y=150)
    escrever_fiscal = tk.CTkLabel(janela_solteiro_n_dinheiro_ss_adse, text = ("Situação Fiscal: Solteiro"), font=("Segoe UI", 20)).place(x=150,y=200)
    escrever_dependentes = tk.CTkLabel(janela_solteiro_n_dinheiro_ss_adse, text=("Dependentes: {}".format(dependentes)), font=("Segoe UI", 20)).place(x=150, y=250)
    escrever_social = tk.CTkLabel(janela_solteiro_n_dinheiro_ss_adse, text=("Contribuição Social: Segurança Social"), font=("Segoe UI", 20)).place(x=150, y=300)
    escrever_adse = tk.CTkLabel(janela_solteiro_n_dinheiro_ss_adse, text=("ADSE: Sim"), font=("Segoe UI", 20)).place(x=150, y=350)
    escrever_alimentacao = tk.CTkLabel(janela_solteiro_n_dinheiro_ss_adse, text=("Subsidio de Alimentação: {} €".format(valor_alimentacao)), font=("Segoe UI", 20)).place(x=150, y=400)
    escrever_dias = tk.CTkLabel(janela_solteiro_n_dinheiro_ss_adse, text=("Dias com susbsidio de alimentação: {}".format(dias_alimentacao)), font=("Segoe UI", 20)).place(x=150, y=450)
    escrever_pagamento = tk.CTkLabel(janela_solteiro_n_dinheiro_ss_adse, text=("Forma de pagamento do subsidio de alimentação: Dinheiro"), font=("Segoe UI", 20)).place(x=150, y=500)
    escrever_outros = tk.CTkLabel(janela_solteiro_n_dinheiro_ss_adse, text=("Outros subsidios tributaveis: {} €".format(outros)), font=("Segoe UI", 20)).place(x=150, y=550)
    escrever_invalidez = tk.CTkLabel(janela_solteiro_n_dinheiro_ss_adse, text=("Invalidez ou incapacidade: Não"), font=("Segoe UI", 20)).place(x=150, y=600)

### APRESENTAÇÃO DOS VALORES ###
    texto_descontos = tk.CTkLabel(janela_solteiro_n_dinheiro_ss_adse, text=("Resumo dos descontos"), font=("Segoe UI", 20)) .place(x=879, y=150)
    texto_valor = tk.CTkLabel(janela_solteiro_n_dinheiro_ss_adse, text=("Valor tributável:{:.2f}€ " .format(renumeracao)), font=("Segoe UI", 20)).place(x=879 , y=300)
    texto_irs = tk.CTkLabel(janela_solteiro_n_dinheiro_ss_adse, text=("Retenção na fonte: {:.2f}€" .format(valor_irs)), font=("Segoe UI", 20)).place(x=879 , y=200)
    texto_ss = tk.CTkLabel(janela_solteiro_n_dinheiro_ss_adse, text=("Taxa Social Única: {:.2f}€" .format(valor_ss)), font=("Segoe UI", 20)).place(x=879 , y=250)
    taxa_adse = tk.CTkLabel(janela_solteiro_n_dinheiro_ss_adse, text=("Desconto ADSE: {:.2f}€" .format(valor_adse)), font=("Segoe UI", 20)).place(x=879 , y=350)
    valor_final = tk.CTkLabel(janela_solteiro_n_dinheiro_ss_adse, text=( "Valor após descontos: {:.2f}€" .format(renumeracao_final)), font=("Segoe UI", 20), bg_color = "red").place(x=879 , y=450)

### FINAL - SAIR OU HISTORICO ###
    decidir_historico = tk.CTkLabel(janela_solteiro_n_dinheiro_ss_adse, text=("Deseja adicionar está simulação ao histórico?" ), font=("Segoe UI", 20)).place(x=879, y=500)
    select_tabela_a = tk.CTkButton(janela_solteiro_n_dinheiro_ss_adse, text="Sim",command=lambda: historico_ordenado(regime, situacao_fiscal, dependentes, contribuicao_social, adse, valor_alimentacao, dias_alimentacao, forma_pagamento, outros, renumeracao, valor_irs, valor_adse, valor_ss, renumeracao_final, invalidez),font=("Segoe UI", 20)).place(x=879, y=550)
    select_tabela_b = tk.CTkButton(janela_solteiro_n_dinheiro_ss_adse, text="Não",command=lambda: reiniciar_programa(),font=("Segoe UI", 20)).place(x=1079, y=550)



def dependente_solteiro_n_dinheiro_ss(janela_solteiro_n_dinheiro):
    janela_solteiro_n_dinheiro.withdraw()
    janela_solteiro_n_dinheiro_ss = tk.CTkToplevel()
    janela_solteiro_n_dinheiro_ss.geometry("1400x700")
    janela_solteiro_n_dinheiro_ss.title("Simulação do ordenado liquido - Trabalhador Dependente - Solteiro - Outras contribuições")
    texto_topo = tk.CTkLabel(janela_solteiro_n_dinheiro_ss, text="Simulação do ordenado liquido\nTrabalhador Dependente\nSolteiro\nOutras contribuições", font=("Segoe UI", 20)).place(x=550, y=0)
    texto_adse = tk.CTkLabel(janela_solteiro_n_dinheiro_ss, text="É beneficiário da ADSE?", font=("Segoe UI", 20)).place(x=590, y=150)
    botao_sim = tk.CTkButton(janela_solteiro_n_dinheiro_ss, text= "Sim", command=lambda: dependente_solteiro_n_dinheiro_ss_adse(janela_solteiro_n_dinheiro_ss), font=("Segoe UI", 20)).place(x=530, y=200)
    botao_nao = tk.CTkButton(janela_solteiro_n_dinheiro_ss, text="Não", command=lambda: dependente_solteiro_n_dinheiro_ss_resultado(janela_solteiro_n_dinheiro_ss), font=("Segoe UI", 20)).place(x=730, y=200)

#
def dependente_solteiro_n_dinheiro(janela_solteiro_n, pedir_outros, pedir_alimentacao, pedir_dias):
    alimentacao = float(pedir_alimentacao.get())
    alimentacao_log.append(alimentacao)
    dias = float(pedir_dias.get())
    dias_log.append(dias)
    outros = float(pedir_outros.get())
    outros_log.append(outros)
    janela_solteiro_n.withdraw()
    janela_solteiro_n_dinheiro = tk.CTkToplevel()
    janela_solteiro_n_dinheiro.geometry("1400x700")
    janela_solteiro_n_dinheiro.title("Simulação do ordenado liquido - Trabalhador Dependente - Solteiro - Outras contribuições")
    texto_topo = tk.CTkLabel(janela_solteiro_n_dinheiro, text="Simulação do ordenado liquido\nTrabalhador Dependente\nSolteiro\nOutras contribuições", font=("Segoe UI", 20)).place(x=550, y=0)
    texto_forma = tk.CTkLabel(janela_solteiro_n_dinheiro, text = "Selecione a sua forma de contribuição social", font=("Segoe UI", 20)).place(x=510, y=150)
    botao_ss = tk.CTkButton(janela_solteiro_n_dinheiro, text="Segurança Social", command=lambda:dependente_solteiro_n_dinheiro_ss(janela_solteiro_n_dinheiro), font=("Segoe UI", 20)) .place(x=606, y=200)
    botao_cga = tk.CTkButton(janela_solteiro_n_dinheiro, text="Caixa Geral de Aposentações", command=lambda: dependente_solteiro_n_dinheiro_cga(janela_solteiro_n_dinheiro),  font=("Segoe UI",20)) .place(x=560, y=250)


def dependente_solteiro_n_dinheiro_cga_resultado(janela_solteiro_n_dinheiro_cga):
    regime = 1
    situacao_fiscal = 1
    contribuicao_social = 2
    adse = 2
    forma_pagamento = 1
    valor_irs=0
    invalidez = 1
    valor_adse=0
    janela_solteiro_n_dinheiro_cga.withdraw()
    janela_solteiro_n_dinheiro_cga_resultado = tk.CTkToplevel()
    janela_solteiro_n_dinheiro_cga_resultado.geometry("1400x700")
    janela_solteiro_n_dinheiro_cga_resultado.title( "Simulação do ordenado liquido - Trabalhador Dependente - Solteiro - Resultado Final")
    texto_topo = tk.CTkLabel(janela_solteiro_n_dinheiro_cga_resultado, text="Simulação do ordenado liquido\nTrabalhador Dependente\nSolteiro\nResultado Final", font=("Segoe UI", 20)).place(x=550, y=0)
    ordenado1 = float(renumera_log[0])
    dependentes = int(dependentes_log[0])
    alimentacao = float(alimentacao_log[0])
    dias_alimentacao = int(dias_log[0])
    outros = float(outros_log[0])
    if alimentacao <6:
        excedente_alimentacao = 0
    else:
        excedente_alimentacao = alimentacao-6
    valor_alimentacao = alimentacao*dias_alimentacao
    excedente_alimentacao_dias = excedente_alimentacao*dias_alimentacao
    renumeracao = ordenado1+excedente_alimentacao_dias+outros

    if renumeracao<=762:
        renumeracao_liquida = 762
        taxa = 0
        parcela_dependente = 0
        parcela_abater = 0

    else:
        valor_irs, parcela_abater, taxa, renumeracao_liquida, parcela_dependente = ordenado_dependente_solteiro(dependentes, renumeracao)
    if valor_irs<0:
        valor_irs = 0
    else:
        valor_irs = valor_irs
    valor_ss = renumeracao*0.11
    renumeracao_final = renumeracao - valor_ss - valor_irs + valor_alimentacao


    ### SINTESE DE CARACTERISTICAS ###

    escrever_renumeracao = tk.CTkLabel(janela_solteiro_n_dinheiro_cga_resultado, text=("Ordenado Base: {} €" .format(ordenado1)), font=("Segoe UI", 20)).place(x=150, y=100)
    escrever_regime = tk.CTkLabel(janela_solteiro_n_dinheiro_cga_resultado, text=("Regime: Trabalhador Dependente"), font=("Segoe UI", 20)).place(x=150, y=150)
    escrever_fiscal = tk.CTkLabel(janela_solteiro_n_dinheiro_cga_resultado, text = ("Situação Fiscal: Solteiro"), font=("Segoe UI", 20)).place(x=150,y=200)
    escrever_dependentes = tk.CTkLabel(janela_solteiro_n_dinheiro_cga_resultado, text=("Dependentes: {}".format(dependentes)), font=("Segoe UI", 20)).place(x=150, y=250)
    escrever_social = tk.CTkLabel(janela_solteiro_n_dinheiro_cga_resultado, text=("Contribuição Social: Caixa Geral de Aposentações"), font=("Segoe UI", 20)).place(x=150, y=300)
    escrever_adse = tk.CTkLabel(janela_solteiro_n_dinheiro_cga_resultado, text=("ADSE: Não"), font=("Segoe UI", 20)).place(x=150, y=350)
    escrever_alimentacao = tk.CTkLabel(janela_solteiro_n_dinheiro_cga_resultado, text=("Subsidio de Alimentação: {} €".format(valor_alimentacao)), font=("Segoe UI", 20)).place(x=150, y=400)
    escrever_dias = tk.CTkLabel(janela_solteiro_n_dinheiro_cga_resultado, text=("Dias com susbsidio de alimentação: {}".format(dias_alimentacao)), font=("Segoe UI", 20)).place(x=150, y=450)
    escrever_pagamento = tk.CTkLabel(janela_solteiro_n_dinheiro_cga_resultado, text=("Forma de pagamento do subsidio de alimentação: Dinheiro"), font=("Segoe UI", 20)).place(x=150, y=500)
    escrever_outros = tk.CTkLabel(janela_solteiro_n_dinheiro_cga_resultado, text=("Outros subsidios tributaveis: {} €".format(outros)), font=("Segoe UI", 20)).place(x=150, y=550)
    escrever_invalidez = tk.CTkLabel(janela_solteiro_n_dinheiro_cga_resultado, text=("Invalidez ou incapacidade: Não"), font=("Segoe UI", 20)).place(x=150, y=600)

### APRESENTAÇÃO DOS VALORES ###
    texto_descontos = tk.CTkLabel(janela_solteiro_n_dinheiro_cga_resultado, text=("Resumo dos descontos"), font=("Segoe UI", 20)) .place(x=879, y=150)
    texto_valor = tk.CTkLabel(janela_solteiro_n_dinheiro_cga_resultado, text=("Valor tributável:{:.2f}€ " .format(renumeracao)), font=("Segoe UI", 20)).place(x=879 , y=300)
    texto_irs = tk.CTkLabel(janela_solteiro_n_dinheiro_cga_resultado, text=("Retenção na fonte: {:.2f}€" .format(valor_irs)), font=("Segoe UI", 20)).place(x=879 , y=200)
    texto_ss = tk.CTkLabel(janela_solteiro_n_dinheiro_cga_resultado, text=("Taxa Social Única: {:.2f}€" .format(valor_ss)), font=("Segoe UI", 20)).place(x=879 , y=250)
    valor_final = tk.CTkLabel(janela_solteiro_n_dinheiro_cga_resultado, text=( "Valor após descontos: {:.2f}€" .format(renumeracao_final)), font=("Segoe UI", 20), bg_color = "red").place(x=879 , y=300)

### FINAL - SAIR OU HISTORICO ###
    decidir_historico = tk.CTkLabel(janela_solteiro_n_dinheiro_cga_resultado, text=("Deseja adicionar está simulação ao histórico?" ), font=("Segoe UI", 20)).place(x=879, y=500)
    select_tabela_a = tk.CTkButton(janela_solteiro_n_dinheiro_cga_resultado, text="Sim",command=lambda: historico_ordenado(regime, situacao_fiscal, dependentes, contribuicao_social, adse, valor_alimentacao, dias_alimentacao, forma_pagamento, outros, renumeracao, valor_irs, valor_adse, valor_ss, renumeracao_final, invalidez),font=("Segoe UI", 20)).place(x=879, y=550)
    select_tabela_b = tk.CTkButton(janela_solteiro_n_dinheiro_cga_resultado, text="Não",command=lambda: reiniciar_programa(),font=("Segoe UI", 20)).place(x=1079, y=550)



def dependente_solteiro_n_dinheiro_cga_adse(janela_solteiro_n_dinheiro_cga):
    regime = 1
    situacao_fiscal = 1
    contribuicao_social = 2
    adse = 1
    forma_pagamento = 1
    valor_irs=0
    invalidez = 1
    janela_solteiro_n_dinheiro_cga.withdraw()
    janela_solteiro_n_dinheiro_cga_adse = tk.CTkToplevel()
    janela_solteiro_n_dinheiro_cga_adse.geometry("1400x700")
    janela_solteiro_n_dinheiro_cga_adse.title( "Simulação do ordenado liquido - Trabalhador Dependente - Solteiro - Resultado Final")
    texto_topo = tk.CTkLabel(janela_solteiro_n_dinheiro_cga_adse, text="Simulação do ordenado liquido\nTrabalhador Dependente\nSolteiro\nResultado Final", font=("Segoe UI", 20)).place(x=550, y=0)
    ordenado1 = float(renumera_log[0])
    dependentes = int(dependentes_log[0])
    alimentacao = float(alimentacao_log[0])
    dias_alimentacao = int(dias_log[0])
    outros = float(outros_log[0])
    if alimentacao < 6:
        excedente_alimentacao = 0
    else:
        excedente_alimentacao = alimentacao-6
    valor_alimentacao = alimentacao*dias_alimentacao
    excedente_alimentacao_dias = excedente_alimentacao*dias_alimentacao
    renumeracao = ordenado1+excedente_alimentacao_dias+outros

    if renumeracao<=762:
        renumeracao_liquida = 762
        taxa = 0
        parcela_dependente = 0
        parcela_abater = 0

    else:
        valor_irs, parcela_abater, taxa, renumeracao_liquida, parcela_dependente = ordenado_dependente_solteiro(dependentes, renumeracao)

    valor_ss = renumeracao*0.11
    valor_adse = renumeracao*0.035
    if valor_irs<0:
        valor_irs = 0
    else:
        valor_irs = valor_irs
    renumeracao_final = renumeracao - valor_adse - valor_ss - valor_irs+valor_alimentacao

    ### SINTESE DE CARACTERISTICAS ###

    escrever_renumeracao = tk.CTkLabel(janela_solteiro_n_dinheiro_cga_adse, text=("Ordenado Base: {} €" .format(ordenado1)), font=("Segoe UI", 20)).place(x=150, y=100)
    escrever_regime = tk.CTkLabel(janela_solteiro_n_dinheiro_cga_adse, text=("Regime: Trabalhador Dependente"), font=("Segoe UI", 20)).place(x=150, y=150)
    escrever_fiscal = tk.CTkLabel(janela_solteiro_n_dinheiro_cga_adse, text = ("Situação Fiscal: Solteiro"), font=("Segoe UI", 20)).place(x=150,y=200)
    escrever_dependentes = tk.CTkLabel(janela_solteiro_n_dinheiro_cga_adse, text=("Dependentes: {}".format(dependentes)), font=("Segoe UI", 20)).place(x=150, y=250)
    escrever_social = tk.CTkLabel(janela_solteiro_n_dinheiro_cga_adse, text=("Contribuição Social: Caixa Geral de Aposentações"), font=("Segoe UI", 20)).place(x=150, y=300)
    escrever_adse = tk.CTkLabel(janela_solteiro_n_dinheiro_cga_adse, text=("ADSE: Sim"), font=("Segoe UI", 20)).place(x=150, y=350)
    escrever_alimentacao = tk.CTkLabel(janela_solteiro_n_dinheiro_cga_adse, text=("Subsidio de Alimentação: {} €".format(valor_alimentacao)), font=("Segoe UI", 20)).place(x=150, y=400)
    escrever_dias = tk.CTkLabel(janela_solteiro_n_dinheiro_cga_adse, text=("Dias com susbsidio de alimentação: {}".format(dias_alimentacao)), font=("Segoe UI", 20)).place(x=150, y=450)
    escrever_pagamento = tk.CTkLabel(janela_solteiro_n_dinheiro_cga_adse, text=("Forma de pagamento do subsidio de alimentação: Dinheiro"), font=("Segoe UI", 20)).place(x=150, y=500)
    escrever_outros = tk.CTkLabel(janela_solteiro_n_dinheiro_cga_adse, text=("Outros subsidios tributaveis: {} €".format(outros)), font=("Segoe UI", 20)).place(x=150, y=550)
    escrever_invalidez = tk.CTkLabel(janela_solteiro_n_dinheiro_cga_adse, text=("Invalidez ou incapacidade: Não"), font=("Segoe UI", 20)).place(x=150, y=600)

### APRESENTAÇÃO DOS VALORES ###
    texto_descontos = tk.CTkLabel(janela_solteiro_n_dinheiro_cga_adse, text=("Resumo dos descontos"), font=("Segoe UI", 20)) .place(x=879, y=150)
    texto_valor = tk.CTkLabel(janela_solteiro_n_dinheiro_cga_adse, text=("Valor tributável:{:.2f}€ " .format(renumeracao)), font=("Segoe UI", 20)).place(x=879 , y=300)
    texto_irs = tk.CTkLabel(janela_solteiro_n_dinheiro_cga_adse, text=("Retenção na fonte: {:.2f}€" .format(valor_irs)), font=("Segoe UI", 20)).place(x=879 , y=200)
    texto_ss = tk.CTkLabel(janela_solteiro_n_dinheiro_cga_adse, text=("Taxa Social Única: {:.2f}€" .format(valor_ss)), font=("Segoe UI", 20)).place(x=879 , y=250)
    taxa_adse = tk.CTkLabel(janela_solteiro_n_dinheiro_cga_adse, text=("Desconto ADSE: {:.2f}€" .format(valor_adse)), font=("Segoe UI", 20)).place(x=879 , y=350)
    valor_final = tk.CTkLabel(janela_solteiro_n_dinheiro_cga_adse, text=( "Valor após descontos: {:.2f}€" .format(renumeracao_final)), font=("Segoe UI", 20), bg_color = "red").place(x=879 , y=450)

### FINAL - SAIR OU HISTORICO ###
    decidir_historico = tk.CTkLabel(janela_solteiro_n_dinheiro_cga_adse, text=("Deseja adicionar está simulação ao histórico?" ), font=("Segoe UI", 20)).place(x=879, y=500)
    select_tabela_a = tk.CTkButton(janela_solteiro_n_dinheiro_cga_adse, text="Sim",command=lambda: historico_ordenado(regime, situacao_fiscal, dependentes, contribuicao_social, adse, valor_alimentacao, dias_alimentacao, forma_pagamento, outros, renumeracao, valor_irs, valor_adse, valor_ss, renumeracao_final, invalidez),font=("Segoe UI", 20)).place(x=879, y=550)
    select_tabela_b = tk.CTkButton(janela_solteiro_n_dinheiro_cga_adse, text="Não",command=lambda: reiniciar_programa(),font=("Segoe UI", 20)).place(x=1079, y=550)



def dependente_solteiro_n_dinheiro_cga(janela_solteiro_n_dinheiro):
    janela_solteiro_n_dinheiro.withdraw()
    janela_solteiro_n_dinheiro_cga = tk.CTkToplevel()
    janela_solteiro_n_dinheiro_cga.geometry("1400x700")
    janela_solteiro_n_dinheiro_cga.title("Simulação do ordenado liquido - Trabalhador Dependente - Solteiro - Outras contribuições")
    texto_topo = tk.CTkLabel(janela_solteiro_n_dinheiro_cga, text="Simulação do ordenado liquido\nTrabalhador Dependente\nSolteiro\nOutras contribuições", font=("Segoe UI", 20)).place(x=550, y=0)
    texto_adse = tk.CTkLabel(janela_solteiro_n_dinheiro_cga, text="É beneficiário da ADSE?", font=("Segoe UI", 20)).place(x=590, y=150)
    botao_sim = tk.CTkButton(janela_solteiro_n_dinheiro_cga, text= "Sim", command=lambda: dependente_solteiro_n_dinheiro_cga_adse(janela_solteiro_n_dinheiro_cga), font=("Segoe UI", 20)).place(x=530, y=200)
    botao_nao = tk.CTkButton(janela_solteiro_n_dinheiro_cga, text="Não", command=lambda: dependente_solteiro_n_dinheiro_cga_resultado(janela_solteiro_n_dinheiro_cga), font=("Segoe UI", 20)).place(x=730, y=200)


def dependente_solteiro_n_dinheiro_ss_resultado(janela_solteiro_n_dinheiro_ss):
    regime = 1
    situacao_fiscal = 1
    contribuicao_social = 1
    adse = 2
    forma_pagamento = 1
    valor_irs=0
    invalidez = 1
    valor_adse=0
    janela_solteiro_n_dinheiro_ss.withdraw()
    janela_solteiro_n_dinheiro_ss_resultado = tk.CTkToplevel()
    janela_solteiro_n_dinheiro_ss_resultado.geometry("1400x700")
    janela_solteiro_n_dinheiro_ss_resultado.title( "Simulação do ordenado liquido - Trabalhador Dependente - Solteiro - Resultado Final")
    texto_topo = tk.CTkLabel(janela_solteiro_n_dinheiro_ss_resultado, text="Simulação do ordenado liquido\nTrabalhador Dependente\nSolteiro\nResultado Final", font=("Segoe UI", 20)).place(x=550, y=0)
    ordenado1 = float(renumera_log[0])
    dependentes = int(dependentes_log[0])
    alimentacao = float(alimentacao_log[0])
    dias_alimentacao = int(dias_log[0])
    outros = float(outros_log[0])
    if alimentacao <6:
        excedente_alimentacao = 0
    else:
        excedente_alimentacao = alimentacao-6
    valor_alimentacao = alimentacao*dias_alimentacao
    excedente_alimentacao_dias = excedente_alimentacao*dias_alimentacao
    renumeracao = ordenado1+excedente_alimentacao_dias+outros

    if renumeracao<=762:
        renumeracao_liquida = 762
        taxa = 0
        parcela_dependente = 0
        parcela_abater = 0

    else:
        valor_irs, parcela_abater, taxa, renumeracao_liquida, parcela_dependente = ordenado_dependente_solteiro(dependentes, renumeracao)
    if valor_irs<0:
        valor_irs = 0
    else:
        valor_irs = valor_irs
    valor_ss = renumeracao*0.11
    renumeracao_final = renumeracao - valor_ss - valor_irs + valor_alimentacao


    ### SINTESE DE CARACTERISTICAS ###

    escrever_renumeracao = tk.CTkLabel(janela_solteiro_n_dinheiro_ss_resultado, text=("Ordenado Base: {} €" .format(ordenado1)), font=("Segoe UI", 20)).place(x=150, y=100)
    escrever_regime = tk.CTkLabel(janela_solteiro_n_dinheiro_ss_resultado, text=("Regime: Trabalhador Dependente"), font=("Segoe UI", 20)).place(x=150, y=150)
    escrever_fiscal = tk.CTkLabel(janela_solteiro_n_dinheiro_ss_resultado, text = ("Situação Fiscal: Solteiro"), font=("Segoe UI", 20)).place(x=150,y=200)
    escrever_dependentes = tk.CTkLabel(janela_solteiro_n_dinheiro_ss_resultado, text=("Dependentes: {}".format(dependentes)), font=("Segoe UI", 20)).place(x=150, y=250)
    escrever_social = tk.CTkLabel(janela_solteiro_n_dinheiro_ss_resultado, text=("Contribuição Social: Segurança Social"), font=("Segoe UI", 20)).place(x=150, y=300)
    escrever_adse = tk.CTkLabel(janela_solteiro_n_dinheiro_ss_resultado, text=("ADSE: Não"), font=("Segoe UI", 20)).place(x=150, y=350)
    escrever_alimentacao = tk.CTkLabel(janela_solteiro_n_dinheiro_ss_resultado, text=("Subsidio de Alimentação: {} €".format(valor_alimentacao)), font=("Segoe UI", 20)).place(x=150, y=400)
    escrever_dias = tk.CTkLabel(janela_solteiro_n_dinheiro_ss_resultado, text=("Dias com susbsidio de alimentação: {}".format(dias_alimentacao)), font=("Segoe UI", 20)).place(x=150, y=450)
    escrever_pagamento = tk.CTkLabel(janela_solteiro_n_dinheiro_ss_resultado, text=("Forma de pagamento do subsidio de alimentação: Dinheiro"), font=("Segoe UI", 20)).place(x=150, y=500)
    escrever_outros = tk.CTkLabel(janela_solteiro_n_dinheiro_ss_resultado, text=("Outros subsidios tributaveis: {} €".format(outros)), font=("Segoe UI", 20)).place(x=150, y=550)
    escrever_invalidez = tk.CTkLabel(janela_solteiro_n_dinheiro_ss_resultado, text=("Invalidez ou incapacidade: Não"), font=("Segoe UI", 20)).place(x=150, y=600)

### APRESENTAÇÃO DOS VALORES ###
    texto_descontos = tk.CTkLabel(janela_solteiro_n_dinheiro_ss_resultado, text=("Resumo dos descontos"), font=("Segoe UI", 20)) .place(x=879, y=150)
    texto_valor = tk.CTkLabel(janela_solteiro_n_dinheiro_ss_resultado, text=("Valor tributável:{:.2f}€ " .format(renumeracao)), font=("Segoe UI", 20)).place(x=879 , y=300)
    texto_irs = tk.CTkLabel(janela_solteiro_n_dinheiro_ss_resultado, text=("Retenção na fonte: {:.2f}€" .format(valor_irs)), font=("Segoe UI", 20)).place(x=879 , y=200)
    texto_ss = tk.CTkLabel(janela_solteiro_n_dinheiro_ss_resultado, text=("Taxa Social Única: {:.2f}€" .format(valor_ss)), font=("Segoe UI", 20)).place(x=879 , y=250)
    valor_final = tk.CTkLabel(janela_solteiro_n_dinheiro_ss_resultado, text=( "Valor após descontos: {:.2f}€" .format(renumeracao_final)), font=("Segoe UI", 20), bg_color = "red").place(x=879 , y=300)

### FINAL - SAIR OU HISTORICO ###
    decidir_historico = tk.CTkLabel(janela_solteiro_n_dinheiro_ss_resultado, text=("Deseja adicionar está simulação ao histórico?" ), font=("Segoe UI", 20)).place(x=879, y=500)
    select_tabela_a = tk.CTkButton(janela_solteiro_n_dinheiro_ss_resultado, text="Sim",command=lambda: historico_ordenado(regime, situacao_fiscal, dependentes, contribuicao_social, adse, valor_alimentacao, dias_alimentacao, forma_pagamento, outros, renumeracao, valor_irs, valor_adse, valor_ss, renumeracao_final, invalidez),font=("Segoe UI", 20)).place(x=879, y=550)
    select_tabela_b = tk.CTkButton(janela_solteiro_n_dinheiro_ss_resultado, text="Não",command=lambda: reiniciar_programa(),font=("Segoe UI", 20)).place(x=1079, y=550)



def dependente_solteiro_n_dinheiro_ss_adse(janela_solteiro_n_dinheiro_ss):
    regime = 1
    situacao_fiscal = 1
    contribuicao_social = 1
    adse = 1
    forma_pagamento = 1
    valor_irs=0
    invalidez = 1
    janela_solteiro_n_dinheiro_ss.withdraw()
    janela_solteiro_n_dinheiro_ss_adse = tk.CTkToplevel()
    janela_solteiro_n_dinheiro_ss_adse.geometry("1400x700")
    janela_solteiro_n_dinheiro_ss_adse.title( "Simulação do ordenado liquido - Trabalhador Dependente - Solteiro - Resultado Final")
    texto_topo = tk.CTkLabel(janela_solteiro_n_dinheiro_ss_adse, text="Simulação do ordenado liquido\nTrabalhador Dependente\nSolteiro\nResultado Final", font=("Segoe UI", 20)).place(x=550, y=0)
    ordenado1 = float(renumera_log[0])
    dependentes = int(dependentes_log[0])
    alimentacao = float(alimentacao_log[0])
    dias_alimentacao = int(dias_log[0])
    outros = float(outros_log[0])
    if alimentacao < 6:
        excedente_alimentacao = 0
    else:
        excedente_alimentacao = alimentacao-6
    valor_alimentacao = alimentacao*dias_alimentacao
    excedente_alimentacao_dias = excedente_alimentacao*dias_alimentacao
    renumeracao = ordenado1+excedente_alimentacao_dias+outros

    if renumeracao<=762:
        renumeracao_liquida = 762
        taxa = 0
        parcela_dependente = 0
        parcela_abater = 0

    else:
        valor_irs, parcela_abater, taxa, renumeracao_liquida, parcela_dependente = ordenado_dependente_solteiro(dependentes, renumeracao)

    valor_ss = renumeracao*0.11
    valor_adse = renumeracao*0.035

    if valor_irs<0:
        valor_irs = 0
    else:
        valor_irs = valor_irs

    renumeracao_final = renumeracao - valor_adse - valor_ss - valor_irs+valor_alimentacao

    ### SINTESE DE CARACTERISTICAS ###

    escrever_renumeracao = tk.CTkLabel(janela_solteiro_n_dinheiro_ss_adse, text=("Ordenado Base: {} €" .format(ordenado1)), font=("Segoe UI", 20)).place(x=150, y=100)
    escrever_regime = tk.CTkLabel(janela_solteiro_n_dinheiro_ss_adse, text=("Regime: Trabalhador Dependente"), font=("Segoe UI", 20)).place(x=150, y=150)
    escrever_fiscal = tk.CTkLabel(janela_solteiro_n_dinheiro_ss_adse, text = ("Situação Fiscal: Solteiro"), font=("Segoe UI", 20)).place(x=150,y=200)
    escrever_dependentes = tk.CTkLabel(janela_solteiro_n_dinheiro_ss_adse, text=("Dependentes: {}".format(dependentes)), font=("Segoe UI", 20)).place(x=150, y=250)
    escrever_social = tk.CTkLabel(janela_solteiro_n_dinheiro_ss_adse, text=("Contribuição Social: Segurança Social"), font=("Segoe UI", 20)).place(x=150, y=300)
    escrever_adse = tk.CTkLabel(janela_solteiro_n_dinheiro_ss_adse, text=("ADSE: Sim"), font=("Segoe UI", 20)).place(x=150, y=350)
    escrever_alimentacao = tk.CTkLabel(janela_solteiro_n_dinheiro_ss_adse, text=("Subsidio de Alimentação: {} €".format(valor_alimentacao)), font=("Segoe UI", 20)).place(x=150, y=400)
    escrever_dias = tk.CTkLabel(janela_solteiro_n_dinheiro_ss_adse, text=("Dias com susbsidio de alimentação: {}".format(dias_alimentacao)), font=("Segoe UI", 20)).place(x=150, y=450)
    escrever_pagamento = tk.CTkLabel(janela_solteiro_n_dinheiro_ss_adse, text=("Forma de pagamento do subsidio de alimentação: Dinheiro"), font=("Segoe UI", 20)).place(x=150, y=500)
    escrever_outros = tk.CTkLabel(janela_solteiro_n_dinheiro_ss_adse, text=("Outros subsidios tributaveis: {} €".format(outros)), font=("Segoe UI", 20)).place(x=150, y=550)
    escrever_invalidez = tk.CTkLabel(janela_solteiro_n_dinheiro_ss_adse, text=("Invalidez ou incapacidade: Não"), font=("Segoe UI", 20)).place(x=150, y=600)

### APRESENTAÇÃO DOS VALORES ###
    texto_descontos = tk.CTkLabel(janela_solteiro_n_dinheiro_ss_adse, text=("Resumo dos descontos"), font=("Segoe UI", 20)) .place(x=879, y=150)
    texto_valor = tk.CTkLabel(janela_solteiro_n_dinheiro_ss_adse, text=("Valor tributável:{:.2f}€ " .format(renumeracao)), font=("Segoe UI", 20)).place(x=879 , y=300)
    texto_irs = tk.CTkLabel(janela_solteiro_n_dinheiro_ss_adse, text=("Retenção na fonte: {:.2f}€" .format(valor_irs)), font=("Segoe UI", 20)).place(x=879 , y=200)
    texto_ss = tk.CTkLabel(janela_solteiro_n_dinheiro_ss_adse, text=("Taxa Social Única: {:.2f}€" .format(valor_ss)), font=("Segoe UI", 20)).place(x=879 , y=250)
    taxa_adse = tk.CTkLabel(janela_solteiro_n_dinheiro_ss_adse, text=("Desconto ADSE: {:.2f}€" .format(valor_adse)), font=("Segoe UI", 20)).place(x=879 , y=350)
    valor_final = tk.CTkLabel(janela_solteiro_n_dinheiro_ss_adse, text=( "Valor após descontos: {:.2f}€" .format(renumeracao_final)), font=("Segoe UI", 20), bg_color = "red").place(x=879 , y=450)

### FINAL - SAIR OU HISTORICO ###
    decidir_historico = tk.CTkLabel(janela_solteiro_n_dinheiro_ss_adse, text=("Deseja adicionar está simulação ao histórico?" ), font=("Segoe UI", 20)).place(x=879, y=500)
    select_tabela_a = tk.CTkButton(janela_solteiro_n_dinheiro_ss_adse, text="Sim",command=lambda: historico_ordenado(regime, situacao_fiscal, dependentes, contribuicao_social, adse, valor_alimentacao, dias_alimentacao, forma_pagamento, outros, renumeracao, valor_irs, valor_adse, valor_ss, renumeracao_final, invalidez),font=("Segoe UI", 20)).place(x=879, y=550)
    select_tabela_b = tk.CTkButton(janela_solteiro_n_dinheiro_ss_adse, text="Não",command=lambda: reiniciar_programa(),font=("Segoe UI", 20)).place(x=1079, y=550)



def dependente_solteiro_n_dinheiro_ss(janela_solteiro_n_dinheiro):
    janela_solteiro_n_dinheiro.withdraw()
    janela_solteiro_n_dinheiro_ss = tk.CTkToplevel()
    janela_solteiro_n_dinheiro_ss.geometry("1400x700")
    janela_solteiro_n_dinheiro_ss.title("Simulação do ordenado liquido - Trabalhador Dependente - Solteiro - Outras contribuições")
    texto_topo = tk.CTkLabel(janela_solteiro_n_dinheiro_ss, text="Simulação do ordenado liquido\nTrabalhador Dependente\nSolteiro\nOutras contribuições", font=("Segoe UI", 20)).place(x=550, y=0)
    texto_adse = tk.CTkLabel(janela_solteiro_n_dinheiro_ss, text="É beneficiário da ADSE?", font=("Segoe UI", 20)).place(x=590, y=150)
    botao_sim = tk.CTkButton(janela_solteiro_n_dinheiro_ss, text= "Sim", command=lambda: dependente_solteiro_n_dinheiro_ss_adse(janela_solteiro_n_dinheiro_ss), font=("Segoe UI", 20)).place(x=530, y=200)
    botao_nao = tk.CTkButton(janela_solteiro_n_dinheiro_ss, text="Não", command=lambda: dependente_solteiro_n_dinheiro_ss_resultado(janela_solteiro_n_dinheiro_ss), font=("Segoe UI", 20)).place(x=730, y=200)


def dependente_solteiro_n_dinheiro(janela_solteiro_n, pedir_outros, pedir_alimentacao, pedir_dias):
    alimentacao = float(pedir_alimentacao.get())
    alimentacao_log.append(alimentacao)
    dias = float(pedir_dias.get())
    dias_log.append(dias)
    outros = float(pedir_outros.get())
    outros_log.append(outros)
    janela_solteiro_n.withdraw()
    janela_solteiro_n_dinheiro = tk.CTkToplevel()
    janela_solteiro_n_dinheiro.geometry("1400x700")
    janela_solteiro_n_dinheiro.title("Simulação do ordenado liquido - Trabalhador Dependente - Solteiro - Outras contribuições")
    texto_topo = tk.CTkLabel(janela_solteiro_n_dinheiro, text="Simulação do ordenado liquido\nTrabalhador Dependente\nSolteiro\nOutras contribuições", font=("Segoe UI", 20)).place(x=550, y=0)
    texto_forma = tk.CTkLabel(janela_solteiro_n_dinheiro, text = "Selecione a sua forma de contribuição social", font=("Segoe UI", 20)).place(x=510, y=150)
    botao_ss = tk.CTkButton(janela_solteiro_n_dinheiro, text="Segurança Social", command=lambda:dependente_solteiro_n_dinheiro_ss(janela_solteiro_n_dinheiro), font=("Segoe UI", 20)) .place(x=606, y=200)
    botao_cga = tk.CTkButton(janela_solteiro_n_dinheiro, text="Caixa Geral de Aposentações", command=lambda: dependente_solteiro_n_dinheiro_cga(janela_solteiro_n_dinheiro),  font=("Segoe UI",20)) .place(x=560, y=250)

def dependente_solteiro_n(janela_dependente_solteiro, pedir_renumeracao_base):

    ordenado2 = float(pedir_renumeracao_base.get())
    renumera_log.append(ordenado2)
    janela_dependente_solteiro.withdraw()
    janela_solteiro_n = tk.CTkToplevel()
    janela_solteiro_n.geometry("1400x700")
    janela_solteiro_n.title("Simulação do ordenado liquido - Trabalhador Dependente - Solteiro - Subsidios")
    texto_topo = tk.CTkLabel(janela_solteiro_n,text="Simulação do ordenado liquido\nTrabalhador Dependente\nSolteiro", font=("Segoe UI", 20)).place(x=550, y=0)
    texto_alimentacao = tk.CTkLabel(janela_solteiro_n,text="Insira o valor diário do subsidio de alimentação", font=("Segoe UI", 20)).place(x=490, y=100)
    pedir_alimentacao = tk.CTkEntry(janela_solteiro_n, placeholder_text= "Valor", font=("Segoe UI",20))
    pedir_alimentacao.place(x=636, y=150)
    texto_dias = tk.CTkLabel(janela_solteiro_n,text="Insira o número de dias com subsidio de alimentação", font=("Segoe UI", 20)).place(x=475, y=200)
    pedir_dias = tk.CTkEntry(janela_solteiro_n, placeholder_text="Dias", font=("Segoe UI", 20))
    pedir_dias.place(x=636, y=250)
    texto_outros = tk.CTkLabel(janela_solteiro_n, text = "Insira o valor de outros subsidios", font=("Segoe UI",20)) .place(x=550,y=300)
    pedir_outros = tk.CTkEntry(janela_solteiro_n, placeholder_text= "Valor", font=("Segoe UI",20))
    pedir_outros.place(x=636,y=350)
    texto_pag_alimentacao = tk.CTkLabel(janela_solteiro_n, text = "Selecione a forma de pagamento do subsidio de alimentacão", font=("Segoe UI", 20)) .place(x=450, y=400)
    botao_dinheiro = tk.CTkButton(janela_solteiro_n, text = "Dinheiro", font=("Segoe UI", 20), command=lambda: dependente_solteiro_n_dinheiro(janela_solteiro_n, pedir_outros, pedir_alimentacao, pedir_dias)) .place(x=490, y=450)
    botao_cartao = tk.CTkButton(janela_solteiro_n, text="Cartão/Vale de refeição", command=lambda:dependente_solteiro_n_vale(janela_solteiro_n, pedir_outros, pedir_alimentacao, pedir_dias),font=("Segoe UI", 20)) .place(x=690, y=450)

############################################ INVALIDEZ ####################


def dependente_solteiro_s_vale_cga_resultado(janela_solteiro_n_vale_cga):
    regime = 1
    situacao_fiscal = 1
    contribuicao_social = 2
    adse = 2
    forma_pagamento = 2
    valor_irs=0
    invalidez = 2
    valor_adse=0
    janela_solteiro_n_vale_cga.withdraw()
    janela_solteiro_n_vale_cga_resultado = tk.CTkToplevel()
    janela_solteiro_n_vale_cga_resultado.geometry("1400x700")
    janela_solteiro_n_vale_cga_resultado.title( "Simulação do ordenado liquido - Trabalhador Dependente - Solteiro - Resultado Final")
    texto_topo = tk.CTkLabel(janela_solteiro_n_vale_cga_resultado, text="Simulação do ordenado liquido\nTrabalhador Dependente\nSolteiro\nResultado Final", font=("Segoe UI", 20)).place(x=550, y=0)
    ordenado1 = float(renumera_log[0])
    dependentes = int(dependentes_log[0])
    alimentacao = float(alimentacao_log[0])
    dias_alimentacao = int(dias_log[0])
    outros = float(outros_log[0])
    if alimentacao < 9.6:
        excedente_alimentacao = 0
    else:
        excedente_alimentacao = alimentacao-9.6
    valor_alimentacao = alimentacao*dias_alimentacao
    excedente_alimentacao_dias = excedente_alimentacao*dias_alimentacao
    renumeracao = ordenado1+excedente_alimentacao_dias+outros


    valor_irs, parcela_abater, taxa, renumeracao_liquida, parcela_dependente = ordenado_dependente_solteiro_invalidez(dependentes, renumeracao)
    if valor_irs<0:
        valor_irs = 0
    else:
        valor_irs = valor_irs
    valor_ss = renumeracao*0.11
    renumeracao_final = renumeracao - valor_ss - valor_irs + valor_alimentacao


    ### SINTESE DE CARACTERISTICAS ###

    escrever_renumeracao = tk.CTkLabel(janela_solteiro_n_vale_cga_resultado, text=("Ordenado Base: {} €" .format(ordenado1)), font=("Segoe UI", 20)).place(x=150, y=100)
    escrever_regime = tk.CTkLabel(janela_solteiro_n_vale_cga_resultado, text=("Regime: Trabalhador Dependente"), font=("Segoe UI", 20)).place(x=150, y=150)
    escrever_fiscal = tk.CTkLabel(janela_solteiro_n_vale_cga_resultado, text = ("Situação Fiscal: Solteiro"), font=("Segoe UI", 20)).place(x=150,y=200)
    escrever_dependentes = tk.CTkLabel(janela_solteiro_n_vale_cga_resultado, text=("Dependentes: {}".format(dependentes)), font=("Segoe UI", 20)).place(x=150, y=250)
    escrever_social = tk.CTkLabel(janela_solteiro_n_vale_cga_resultado, text=("Contribuição Social: Caixa Geral de Aposentações"), font=("Segoe UI", 20)).place(x=150, y=300)
    escrever_adse = tk.CTkLabel(janela_solteiro_n_vale_cga_resultado, text=("ADSE: Não"), font=("Segoe UI", 20)).place(x=150, y=350)
    escrever_alimentacao = tk.CTkLabel(janela_solteiro_n_vale_cga_resultado, text=("Subsidio de Alimentação: {} €".format(valor_alimentacao)), font=("Segoe UI", 20)).place(x=150, y=400)
    escrever_dias = tk.CTkLabel(janela_solteiro_n_vale_cga_resultado, text=("Dias com susbsidio de alimentação: {}".format(dias_alimentacao)), font=("Segoe UI", 20)).place(x=150, y=450)
    escrever_pagamento = tk.CTkLabel(janela_solteiro_n_vale_cga_resultado, text=("Forma de pagamento do subsidio de alimentação: Vale/Cartão de refeição"), font=("Segoe UI", 20)).place(x=150, y=500)
    escrever_outros = tk.CTkLabel(janela_solteiro_n_vale_cga_resultado, text=("Outros subsidios tributaveis: {} €".format(outros)), font=("Segoe UI", 20)).place(x=150, y=550)
    escrever_invalidez = tk.CTkLabel(janela_solteiro_n_vale_cga_resultado, text=("Invalidez ou incapacidade: Sim"), font=("Segoe UI", 20)).place(x=150, y=600)

### APRESENTAÇÃO DOS VALORES ###
    texto_descontos = tk.CTkLabel(janela_solteiro_n_vale_cga_resultado, text=("Resumo dos descontos"), font=("Segoe UI", 20)) .place(x=879, y=150)
    texto_valor = tk.CTkLabel(janela_solteiro_n_vale_cga_resultado, text=("Valor tributável:{:.2f}€ " .format(renumeracao)), font=("Segoe UI", 20)).place(x=879 , y=300)
    texto_irs = tk.CTkLabel(janela_solteiro_n_vale_cga_resultado, text=("Retenção na fonte: {:.2f}€" .format(valor_irs)), font=("Segoe UI", 20)).place(x=879 , y=200)
    texto_ss = tk.CTkLabel(janela_solteiro_n_vale_cga_resultado, text=("Taxa Social Única: {:.2f}€" .format(valor_ss)), font=("Segoe UI", 20)).place(x=879 , y=250)
    valor_final = tk.CTkLabel(janela_solteiro_n_vale_cga_resultado, text=( "Valor após descontos: {:.2f}€" .format(renumeracao_final)), font=("Segoe UI", 20), bg_color = "red").place(x=879 , y=300)

### FINAL - SAIR OU HISTORICO ###
    decidir_historico = tk.CTkLabel(janela_solteiro_n_vale_cga_resultado, text=("Deseja adicionar está simulação ao histórico?" ), font=("Segoe UI", 20)).place(x=879, y=500)
    select_tabela_a = tk.CTkButton(janela_solteiro_n_vale_cga_resultado, text="Sim",command=lambda: historico_ordenado(regime, situacao_fiscal, dependentes, contribuicao_social, adse, valor_alimentacao, dias_alimentacao, forma_pagamento, outros, renumeracao, valor_irs, valor_adse, valor_ss, renumeracao_final, invalidez),font=("Segoe UI", 20)).place(x=879, y=550)
    select_tabela_b = tk.CTkButton(janela_solteiro_n_vale_cga_resultado, text="Não",command=lambda: reiniciar_programa(),font=("Segoe UI", 20)).place(x=1079, y=550)



def dependente_solteiro_s_vale_cga_adse(janela_solteiro_n_vale_cga):
    regime = 1
    situacao_fiscal = 1
    contribuicao_social = 2
    adse = 1
    forma_pagamento = 2
    valor_irs=0
    invalidez = 2
    janela_solteiro_n_vale_cga.withdraw()
    janela_solteiro_n_vale_cga_adse = tk.CTkToplevel()
    janela_solteiro_n_vale_cga_adse.geometry("1400x700")
    janela_solteiro_n_vale_cga_adse.title( "Simulação do ordenado liquido - Trabalhador Dependente - Solteiro - Resultado Final")
    texto_topo = tk.CTkLabel(janela_solteiro_n_vale_cga_adse, text="Simulação do ordenado liquido\nTrabalhador Dependente\nSolteiro\nResultado Final", font=("Segoe UI", 20)).place(x=550, y=0)
    ordenado1 = float(renumera_log[0])
    dependentes = int(dependentes_log[0])
    alimentacao = float(alimentacao_log[0])
    dias_alimentacao = int(dias_log[0])
    outros = float(outros_log[0])
    if alimentacao < 9.6:
        excedente_alimentacao = 0
    else:
        excedente_alimentacao = alimentacao-9.6
    valor_alimentacao = alimentacao*dias_alimentacao
    excedente_alimentacao_dias = excedente_alimentacao*dias_alimentacao
    renumeracao = ordenado1+excedente_alimentacao_dias+outros


    valor_irs, parcela_abater, taxa, renumeracao_liquida, parcela_dependente = ordenado_dependente_solteiro_invalidez(dependentes, renumeracao)

    valor_ss = renumeracao*0.11
    valor_adse = renumeracao*0.035
    if valor_irs<0:
        valor_irs = 0
    else:
        valor_irs = valor_irs
    renumeracao_final = renumeracao - valor_adse - valor_ss - valor_irs+valor_alimentacao

    ### SINTESE DE CARACTERISTICAS ###

    escrever_renumeracao = tk.CTkLabel(janela_solteiro_n_vale_cga_adse, text=("Ordenado Base: {} €" .format(ordenado1)), font=("Segoe UI", 20)).place(x=150, y=100)
    escrever_regime = tk.CTkLabel(janela_solteiro_n_vale_cga_adse, text=("Regime: Trabalhador Dependente"), font=("Segoe UI", 20)).place(x=150, y=150)
    escrever_fiscal = tk.CTkLabel(janela_solteiro_n_vale_cga_adse, text = ("Situação Fiscal: Solteiro"), font=("Segoe UI", 20)).place(x=150,y=200)
    escrever_dependentes = tk.CTkLabel(janela_solteiro_n_vale_cga_adse, text=("Dependentes: {}".format(dependentes)), font=("Segoe UI", 20)).place(x=150, y=250)
    escrever_social = tk.CTkLabel(janela_solteiro_n_vale_cga_adse, text=("Contribuição Social: Caixa Geral de Aposentações"), font=("Segoe UI", 20)).place(x=150, y=300)
    escrever_adse = tk.CTkLabel(janela_solteiro_n_vale_cga_adse, text=("ADSE: Sim"), font=("Segoe UI", 20)).place(x=150, y=350)
    escrever_alimentacao = tk.CTkLabel(janela_solteiro_n_vale_cga_adse, text=("Subsidio de Alimentação: {} €".format(valor_alimentacao)), font=("Segoe UI", 20)).place(x=150, y=400)
    escrever_dias = tk.CTkLabel(janela_solteiro_n_vale_cga_adse, text=("Dias com susbsidio de alimentação: {}".format(dias_alimentacao)), font=("Segoe UI", 20)).place(x=150, y=450)
    escrever_pagamento = tk.CTkLabel(janela_solteiro_n_vale_cga_adse, text=("Forma de pagamento do subsidio de alimentação: Vale/Cartão de alimentação"), font=("Segoe UI", 20)).place(x=150, y=500)
    escrever_outros = tk.CTkLabel(janela_solteiro_n_vale_cga_adse, text=("Outros subsidios tributaveis: {} €".format(outros)), font=("Segoe UI", 20)).place(x=150, y=550)
    escrever_invalidez = tk.CTkLabel(janela_solteiro_n_vale_cga_adse, text=("Invalidez ou incapacidade: Sim"), font=("Segoe UI", 20)).place(x=150, y=600)

### APRESENTAÇÃO DOS VALORES ###
    texto_descontos = tk.CTkLabel(janela_solteiro_n_vale_cga_adse, text=("Resumo dos descontos"), font=("Segoe UI", 20)) .place(x=879, y=150)
    texto_valor = tk.CTkLabel(janela_solteiro_n_vale_cga_adse, text=("Valor tributável:{:.2f}€ " .format(renumeracao)), font=("Segoe UI", 20)).place(x=879 , y=300)
    texto_irs = tk.CTkLabel(janela_solteiro_n_vale_cga_adse, text=("Retenção na fonte: {:.2f}€" .format(valor_irs)), font=("Segoe UI", 20)).place(x=879 , y=200)
    texto_ss = tk.CTkLabel(janela_solteiro_n_vale_cga_adse, text=("Taxa Social Única: {:.2f}€" .format(valor_ss)), font=("Segoe UI", 20)).place(x=879 , y=250)
    taxa_adse = tk.CTkLabel(janela_solteiro_n_vale_cga_adse, text=("Desconto ADSE: {:.2f}€" .format(valor_adse)), font=("Segoe UI", 20)).place(x=879 , y=350)
    valor_final = tk.CTkLabel(janela_solteiro_n_vale_cga_adse, text=( "Valor após descontos: {:.2f}€" .format(renumeracao_final)), font=("Segoe UI", 20), bg_color = "red").place(x=879 , y=450)

### FINAL - SAIR OU HISTORICO ###
    decidir_historico = tk.CTkLabel(janela_solteiro_n_vale_cga_adse, text=("Deseja adicionar está simulação ao histórico?" ), font=("Segoe UI", 20)).place(x=879, y=500)
    select_tabela_a = tk.CTkButton(janela_solteiro_n_vale_cga_adse, text="Sim",command=lambda: historico_ordenado(regime, situacao_fiscal, dependentes, contribuicao_social, adse, valor_alimentacao, dias_alimentacao, forma_pagamento, outros, renumeracao, valor_irs, valor_adse, valor_ss, renumeracao_final, invalidez),font=("Segoe UI", 20)).place(x=879, y=550)
    select_tabela_b = tk.CTkButton(janela_solteiro_n_vale_cga_adse, text="Não",command=lambda: reiniciar_programa(),font=("Segoe UI", 20)).place(x=1079, y=550)



def dependente_solteiro_s_vale_cga(janela_solteiro_n_vale):
    janela_solteiro_n_vale.withdraw()
    janela_solteiro_n_vale_cga = tk.CTkToplevel()
    janela_solteiro_n_vale_cga.geometry("1400x700")
    janela_solteiro_n_vale_cga.title("Simulação do ordenado liquido - Trabalhador Dependente - Solteiro - Outras contribuições")
    texto_topo = tk.CTkLabel(janela_solteiro_n_vale_cga, text="Simulação do ordenado liquido\nTrabalhador Dependente\nSolteiro\nOutras contribuições", font=("Segoe UI", 20)).place(x=550, y=0)
    texto_adse = tk.CTkLabel(janela_solteiro_n_vale_cga, text="É beneficiário da ADSE?", font=("Segoe UI", 20)).place(x=590, y=150)
    botao_sim = tk.CTkButton(janela_solteiro_n_vale_cga, text= "Sim", command=lambda: dependente_solteiro_s_vale_cga_adse(janela_solteiro_n_vale_cga), font=("Segoe UI", 20)).place(x=530, y=200)
    botao_nao = tk.CTkButton(janela_solteiro_n_vale_cga, text="Não", command=lambda: dependente_solteiro_s_vale_cga_resultado(janela_solteiro_n_vale_cga), font=("Segoe UI", 20)).place(x=730, y=200)

def dependente_solteiro_s_vale_ss_resultado(janela_solteiro_n_vale_ss):
    regime = 1
    situacao_fiscal = 1
    contribuicao_social = 1
    adse = 2
    forma_pagamento = 2
    valor_irs=0
    invalidez = 2
    valor_adse=0
    janela_solteiro_n_vale_ss.withdraw()
    janela_solteiro_n_vale_ss_resultado = tk.CTkToplevel()
    janela_solteiro_n_vale_ss_resultado.geometry("1400x700")
    janela_solteiro_n_vale_ss_resultado.title( "Simulação do ordenado liquido - Trabalhador Dependente - Solteiro - Resultado Final")
    texto_topo = tk.CTkLabel(janela_solteiro_n_vale_ss_resultado, text="Simulação do ordenado liquido\nTrabalhador Dependente\nSolteiro\nResultado Final", font=("Segoe UI", 20)).place(x=550, y=0)
    ordenado1 = float(renumera_log[0])
    dependentes = int(dependentes_log[0])
    alimentacao = float(alimentacao_log[0])
    dias_alimentacao = int(dias_log[0])
    outros = float(outros_log[0])
    if alimentacao <9.6:
        excedente_alimentacao = 0
    else:
        excedente_alimentacao = alimentacao-9.6
    valor_alimentacao = alimentacao*dias_alimentacao
    excedente_alimentacao_dias = excedente_alimentacao*dias_alimentacao
    renumeracao = ordenado1+excedente_alimentacao_dias+outros


    valor_irs, parcela_abater, taxa, renumeracao_liquida, parcela_dependente = ordenado_dependente_solteiro_invalidez(dependentes, renumeracao)
    if valor_irs<0:
        valor_irs = 0
    else:
        valor_irs = valor_irs
    valor_ss = renumeracao*0.11
    renumeracao_final = renumeracao - valor_ss - valor_irs + valor_alimentacao


    ### SINTESE DE CARACTERISTICAS ###

    escrever_renumeracao = tk.CTkLabel(janela_solteiro_n_vale_ss_resultado, text=("Ordenado Base: {} €" .format(ordenado1)), font=("Segoe UI", 20)).place(x=150, y=100)
    escrever_regime = tk.CTkLabel(janela_solteiro_n_vale_ss_resultado, text=("Regime: Trabalhador Dependente"), font=("Segoe UI", 20)).place(x=150, y=150)
    escrever_fiscal = tk.CTkLabel(janela_solteiro_n_vale_ss_resultado, text = ("Situação Fiscal: Solteiro"), font=("Segoe UI", 20)).place(x=150,y=200)
    escrever_dependentes = tk.CTkLabel(janela_solteiro_n_vale_ss_resultado, text=("Dependentes: {}".format(dependentes)), font=("Segoe UI", 20)).place(x=150, y=250)
    escrever_social = tk.CTkLabel(janela_solteiro_n_vale_ss_resultado, text=("Contribuição Social: Segurança Social"), font=("Segoe UI", 20)).place(x=150, y=300)
    escrever_adse = tk.CTkLabel(janela_solteiro_n_vale_ss_resultado, text=("ADSE: Não"), font=("Segoe UI", 20)).place(x=150, y=350)
    escrever_alimentacao = tk.CTkLabel(janela_solteiro_n_vale_ss_resultado, text=("Subsidio de Alimentação: {} €".format(valor_alimentacao)), font=("Segoe UI", 20)).place(x=150, y=400)
    escrever_dias = tk.CTkLabel(janela_solteiro_n_vale_ss_resultado, text=("Dias com susbsidio de alimentação: {}".format(dias_alimentacao)), font=("Segoe UI", 20)).place(x=150, y=450)
    escrever_pagamento = tk.CTkLabel(janela_solteiro_n_vale_ss_resultado, text=("Forma de pagamento do subsidio de alimentação: Vale/Cartão de Refeição"), font=("Segoe UI", 20)).place(x=150, y=500)
    escrever_outros = tk.CTkLabel(janela_solteiro_n_vale_ss_resultado, text=("Outros subsidios tributaveis: {} €".format(outros)), font=("Segoe UI", 20)).place(x=150, y=550)
    escrever_invalidez = tk.CTkLabel(janela_solteiro_n_vale_ss_resultado, text=("Invalidez ou incapacidade: Sim"), font=("Segoe UI", 20)).place(x=150, y=600)

### APRESENTAÇÃO DOS VALORES ###
    texto_descontos = tk.CTkLabel(janela_solteiro_n_vale_ss_resultado, text=("Resumo dos descontos"), font=("Segoe UI", 20)) .place(x=879, y=150)
    texto_valor = tk.CTkLabel(janela_solteiro_n_vale_ss_resultado, text=("Valor tributável:{:.2f}€ " .format(renumeracao)), font=("Segoe UI", 20)).place(x=879 , y=300)
    texto_irs = tk.CTkLabel(janela_solteiro_n_vale_ss_resultado, text=("Retenção na fonte: {:.2f}€" .format(valor_irs)), font=("Segoe UI", 20)).place(x=879 , y=200)
    texto_ss = tk.CTkLabel(janela_solteiro_n_vale_ss_resultado, text=("Taxa Social Única: {:.2f}€" .format(valor_ss)), font=("Segoe UI", 20)).place(x=879 , y=250)
    valor_final = tk.CTkLabel(janela_solteiro_n_vale_ss_resultado, text=( "Valor após descontos: {:.2f}€" .format(renumeracao_final)), font=("Segoe UI", 20), bg_color = "red").place(x=879 , y=300)

### FINAL - SAIR OU HISTORICO ###
    decidir_historico = tk.CTkLabel(janela_solteiro_n_vale_ss_resultado, text=("Deseja adicionar está simulação ao histórico?" ), font=("Segoe UI", 20)).place(x=879, y=500)
    select_tabela_a = tk.CTkButton(janela_solteiro_n_vale_ss_resultado, text="Sim",command=lambda: historico_ordenado(regime, situacao_fiscal, dependentes, contribuicao_social, adse, valor_alimentacao, dias_alimentacao, forma_pagamento, outros, renumeracao, valor_irs, valor_adse, valor_ss, renumeracao_final, invalidez),font=("Segoe UI", 20)).place(x=879, y=550)
    select_tabela_b = tk.CTkButton(janela_solteiro_n_vale_ss_resultado, text="Não",command=lambda: reiniciar_programa(),font=("Segoe UI", 20)).place(x=1079, y=550)



def dependente_solteiro_s_vale_ss_adse(janela_solteiro_n_vale_ss):
    regime = 1
    situacao_fiscal = 1
    contribuicao_social = 1
    adse = 1
    forma_pagamento = 2
    valor_irs=0
    invalidez = 2
    janela_solteiro_n_vale_ss.withdraw()
    janela_solteiro_n_vale_ss_adse = tk.CTkToplevel()
    janela_solteiro_n_vale_ss_adse.geometry("1400x700")
    janela_solteiro_n_vale_ss_adse.title( "Simulação do ordenado liquido - Trabalhador Dependente - Solteiro - Resultado Final")
    texto_topo = tk.CTkLabel(janela_solteiro_n_vale_ss_adse, text="Simulação do ordenado liquido\nTrabalhador Dependente\nSolteiro\nResultado Final", font=("Segoe UI", 20)).place(x=550, y=0)
    ordenado1 = float(renumera_log[0])
    dependentes = int(dependentes_log[0])
    alimentacao = float(alimentacao_log[0])
    dias_alimentacao = int(dias_log[0])
    outros = float(outros_log[0])
    if alimentacao < 9.6:
        excedente_alimentacao = 0
    else:
        excedente_alimentacao = alimentacao-9.6
    valor_alimentacao = alimentacao*dias_alimentacao
    excedente_alimentacao_dias = excedente_alimentacao*dias_alimentacao
    renumeracao = ordenado1+excedente_alimentacao_dias+outros


    valor_irs, parcela_abater, taxa, renumeracao_liquida, parcela_dependente = ordenado_dependente_solteiro_invalidez(dependentes, renumeracao)

    valor_ss = renumeracao*0.11
    valor_adse = renumeracao*0.035

    if valor_irs<0:
        valor_irs = 0
    else:
        valor_irs = valor_irs

    renumeracao_final = renumeracao - valor_adse - valor_ss - valor_irs+valor_alimentacao

    ### SINTESE DE CARACTERISTICAS ###

    escrever_renumeracao = tk.CTkLabel(janela_solteiro_n_vale_ss_adse, text=("Ordenado Base: {} €" .format(ordenado1)), font=("Segoe UI", 20)).place(x=150, y=100)
    escrever_regime = tk.CTkLabel(janela_solteiro_n_vale_ss_adse, text=("Regime: Trabalhador Dependente"), font=("Segoe UI", 20)).place(x=150, y=150)
    escrever_fiscal = tk.CTkLabel(janela_solteiro_n_vale_ss_adse, text = ("Situação Fiscal: Solteiro"), font=("Segoe UI", 20)).place(x=150,y=200)
    escrever_dependentes = tk.CTkLabel(janela_solteiro_n_vale_ss_adse, text=("Dependentes: {}".format(dependentes)), font=("Segoe UI", 20)).place(x=150, y=250)
    escrever_social = tk.CTkLabel(janela_solteiro_n_vale_ss_adse, text=("Contribuição Social: Segurança Social"), font=("Segoe UI", 20)).place(x=150, y=300)
    escrever_adse = tk.CTkLabel(janela_solteiro_n_vale_ss_adse, text=("ADSE: Sim"), font=("Segoe UI", 20)).place(x=150, y=350)
    escrever_alimentacao = tk.CTkLabel(janela_solteiro_n_vale_ss_adse, text=("Subsidio de Alimentação: {} €".format(valor_alimentacao)), font=("Segoe UI", 20)).place(x=150, y=400)
    escrever_dias = tk.CTkLabel(janela_solteiro_n_vale_ss_adse, text=("Dias com susbsidio de alimentação: {}".format(dias_alimentacao)), font=("Segoe UI", 20)).place(x=150, y=450)
    escrever_pagamento = tk.CTkLabel(janela_solteiro_n_vale_ss_adse, text=("Forma de pagamento do subsidio de alimentação: Cartão/Vale de alimentação"), font=("Segoe UI", 20)).place(x=150, y=500)
    escrever_outros = tk.CTkLabel(janela_solteiro_n_vale_ss_adse, text=("Outros subsidios tributaveis: {} €".format(outros)), font=("Segoe UI", 20)).place(x=150, y=550)
    escrever_invalidez = tk.CTkLabel(janela_solteiro_n_vale_ss_adse, text=("Invalidez ou incapacidade: Sim"), font=("Segoe UI", 20)).place(x=150, y=600)

### APRESENTAÇÃO DOS VALORES ###
    texto_descontos = tk.CTkLabel(janela_solteiro_n_vale_ss_adse, text=("Resumo dos descontos"), font=("Segoe UI", 20)) .place(x=879, y=150)
    texto_valor = tk.CTkLabel(janela_solteiro_n_vale_ss_adse, text=("Valor tributável:{:.2f}€ " .format(renumeracao)), font=("Segoe UI", 20)).place(x=879 , y=300)
    texto_irs = tk.CTkLabel(janela_solteiro_n_vale_ss_adse, text=("Retenção na fonte: {:.2f}€" .format(valor_irs)), font=("Segoe UI", 20)).place(x=879 , y=200)
    texto_ss = tk.CTkLabel(janela_solteiro_n_vale_ss_adse, text=("Taxa Social Única: {:.2f}€" .format(valor_ss)), font=("Segoe UI", 20)).place(x=879 , y=250)
    taxa_adse = tk.CTkLabel(janela_solteiro_n_vale_ss_adse, text=("Desconto ADSE: {:.2f}€" .format(valor_adse)), font=("Segoe UI", 20)).place(x=879 , y=350)
    valor_final = tk.CTkLabel(janela_solteiro_n_vale_ss_adse, text=( "Valor após descontos: {:.2f}€" .format(renumeracao_final)), font=("Segoe UI", 20), bg_color = "red").place(x=879 , y=450)

### FINAL - SAIR OU HISTORICO ###
    decidir_historico = tk.CTkLabel(janela_solteiro_n_vale_ss_adse, text=("Deseja adicionar está simulação ao histórico?" ), font=("Segoe UI", 20)).place(x=879, y=500)
    select_tabela_a = tk.CTkButton(janela_solteiro_n_vale_ss_adse, text="Sim",command=lambda: historico_ordenado(regime, situacao_fiscal, dependentes, contribuicao_social, adse, valor_alimentacao, dias_alimentacao, forma_pagamento, outros, renumeracao, valor_irs, valor_adse, valor_ss, renumeracao_final, invalidez),font=("Segoe UI", 20)).place(x=879, y=550)
    select_tabela_b = tk.CTkButton(janela_solteiro_n_vale_ss_adse, text="Não",command=lambda: reiniciar_programa(),font=("Segoe UI", 20)).place(x=1079, y=550)



def dependente_solteiro_s_vale_ss(janela_solteiro_n_vale):
    janela_solteiro_n_vale.withdraw()
    janela_solteiro_n_vale_ss = tk.CTkToplevel()
    janela_solteiro_n_vale_ss.geometry("1400x700")
    janela_solteiro_n_vale_ss.title("Simulação do ordenado liquido - Trabalhador Dependente - Solteiro - Outras contribuições")
    texto_topo = tk.CTkLabel(janela_solteiro_n_vale_ss, text="Simulação do ordenado liquido\nTrabalhador Dependente\nSolteiro\nOutras contribuições", font=("Segoe UI", 20)).place(x=550, y=0)
    texto_adse = tk.CTkLabel(janela_solteiro_n_vale_ss, text="É beneficiário da ADSE?", font=("Segoe UI", 20)).place(x=590, y=150)
    botao_sim = tk.CTkButton(janela_solteiro_n_vale_ss, text= "Sim", command=lambda: dependente_solteiro_s_vale_ss_adse(janela_solteiro_n_vale_ss), font=("Segoe UI", 20)).place(x=530, y=200)
    botao_nao = tk.CTkButton(janela_solteiro_n_vale_ss, text="Não", command=lambda: dependente_solteiro_s_vale_ss_resultado(janela_solteiro_n_vale_ss), font=("Segoe UI", 20)).place(x=730, y=200)




def dependente_solteiro_s_vale(janela_solteiro_n, pedir_outros, pedir_alimentacao, pedir_dias):
    alimentacao = float(pedir_alimentacao.get())
    alimentacao_log.append(alimentacao)
    dias = float(pedir_dias.get())
    dias_log.append(dias)
    outros = float(pedir_outros.get())
    outros_log.append(outros)
    janela_solteiro_n.withdraw()
    janela_solteiro_n_vale = tk.CTkToplevel()
    janela_solteiro_n_vale.geometry("1400x700")
    janela_solteiro_n_vale.title("Simulação do ordenado liquido - Trabalhador Dependente - Solteiro - Outras contribuições")
    texto_topo = tk.CTkLabel(janela_solteiro_n_vale, text="Simulação do ordenado liquido\nTrabalhador Dependente\nSolteiro\nOutras contribuições", font=("Segoe UI", 20)).place(x=550, y=0)
    texto_forma = tk.CTkLabel(janela_solteiro_n_vale, text = "Selecione a sua forma de contribuição social", font=("Segoe UI", 20)).place(x=510, y=150)
    botao_ss = tk.CTkButton(janela_solteiro_n_vale, text="Segurança Social", command=lambda:dependente_solteiro_s_vale_ss(janela_solteiro_n_vale), font=("Segoe UI", 20)) .place(x=606, y=200)
    botao_cga = tk.CTkButton(janela_solteiro_n_vale, text="Caixa Geral de Aposentações", command=lambda: dependente_solteiro_s_vale_cga(janela_solteiro_n_vale),  font=("Segoe UI",20)) .place(x=560, y=250)



def dependente_solteiro_s_dinheiro_ss_resultado(janela_solteiro_n_dinheiro_ss):
    regime = 1
    situacao_fiscal = 1
    contribuicao_social = 1
    adse = 2
    forma_pagamento = 1
    valor_irs=0
    invalidez = 2
    valor_adse=0
    janela_solteiro_n_dinheiro_ss.withdraw()
    janela_solteiro_n_dinheiro_ss_resultado = tk.CTkToplevel()
    janela_solteiro_n_dinheiro_ss_resultado.geometry("1400x700")
    janela_solteiro_n_dinheiro_ss_resultado.title( "Simulação do ordenado liquido - Trabalhador Dependente - Solteiro - Resultado Final")
    texto_topo = tk.CTkLabel(janela_solteiro_n_dinheiro_ss_resultado, text="Simulação do ordenado liquido\nTrabalhador Dependente\nSolteiro\nResultado Final", font=("Segoe UI", 20)).place(x=550, y=0)
    ordenado1 = float(renumera_log[0])
    dependentes = int(dependentes_log[0])
    alimentacao = float(alimentacao_log[0])
    dias_alimentacao = int(dias_log[0])
    outros = float(outros_log[0])
    if alimentacao < 6:
        excedente_alimentacao = 0
    else:
        excedente_alimentacao = alimentacao-6
    valor_alimentacao = alimentacao*dias_alimentacao
    excedente_alimentacao_dias = excedente_alimentacao*dias_alimentacao
    renumeracao = ordenado1+excedente_alimentacao_dias+outros

    valor_irs, parcela_abater, taxa, renumeracao_liquida, parcela_dependente = ordenado_dependente_solteiro_invalidez(dependentes, renumeracao)
    if valor_irs<0:
        valor_irs = 0
    else:
        valor_irs = valor_irs
    valor_ss = renumeracao*0.11
    renumeracao_final = renumeracao - valor_ss - valor_irs + valor_alimentacao


    ### SINTESE DE CARACTERISTICAS ###

    escrever_renumeracao = tk.CTkLabel(janela_solteiro_n_dinheiro_ss_resultado, text=("Ordenado Base: {} €" .format(ordenado1)), font=("Segoe UI", 20)).place(x=150, y=100)
    escrever_regime = tk.CTkLabel(janela_solteiro_n_dinheiro_ss_resultado, text=("Regime: Trabalhador Dependente"), font=("Segoe UI", 20)).place(x=150, y=150)
    escrever_fiscal = tk.CTkLabel(janela_solteiro_n_dinheiro_ss_resultado, text = ("Situação Fiscal: Solteiro"), font=("Segoe UI", 20)).place(x=150,y=200)
    escrever_dependentes = tk.CTkLabel(janela_solteiro_n_dinheiro_ss_resultado, text=("Dependentes: {}".format(dependentes)), font=("Segoe UI", 20)).place(x=150, y=250)
    escrever_social = tk.CTkLabel(janela_solteiro_n_dinheiro_ss_resultado, text=("Contribuição Social: Segurança Social"), font=("Segoe UI", 20)).place(x=150, y=300)
    escrever_adse = tk.CTkLabel(janela_solteiro_n_dinheiro_ss_resultado, text=("ADSE: Não"), font=("Segoe UI", 20)).place(x=150, y=350)
    escrever_alimentacao = tk.CTkLabel(janela_solteiro_n_dinheiro_ss_resultado, text=("Subsidio de Alimentação: {} €".format(valor_alimentacao)), font=("Segoe UI", 20)).place(x=150, y=400)
    escrever_dias = tk.CTkLabel(janela_solteiro_n_dinheiro_ss_resultado, text=("Dias com susbsidio de alimentação: {}".format(dias_alimentacao)), font=("Segoe UI", 20)).place(x=150, y=450)
    escrever_pagamento = tk.CTkLabel(janela_solteiro_n_dinheiro_ss_resultado, text=("Forma de pagamento do subsidio de alimentação: Dinheiro"), font=("Segoe UI", 20)).place(x=150, y=500)
    escrever_outros = tk.CTkLabel(janela_solteiro_n_dinheiro_ss_resultado, text=("Outros subsidios tributaveis: {} €".format(outros)), font=("Segoe UI", 20)).place(x=150, y=550)
    escrever_invalidez = tk.CTkLabel(janela_solteiro_n_dinheiro_ss_resultado, text=("Invalidez ou incapacidade: Sim"), font=("Segoe UI", 20)).place(x=150, y=600)

### APRESENTAÇÃO DOS VALORES ###
    texto_descontos = tk.CTkLabel(janela_solteiro_n_dinheiro_ss_resultado, text=("Resumo dos descontos"), font=("Segoe UI", 20)) .place(x=879, y=150)
    texto_valor = tk.CTkLabel(janela_solteiro_n_dinheiro_ss_resultado, text=("Valor tributável:{:.2f}€ " .format(renumeracao)), font=("Segoe UI", 20)).place(x=879 , y=300)
    texto_irs = tk.CTkLabel(janela_solteiro_n_dinheiro_ss_resultado, text=("Retenção na fonte: {:.2f}€" .format(valor_irs)), font=("Segoe UI", 20)).place(x=879 , y=200)
    texto_ss = tk.CTkLabel(janela_solteiro_n_dinheiro_ss_resultado, text=("Taxa Social Única: {:.2f}€" .format(valor_ss)), font=("Segoe UI", 20)).place(x=879 , y=250)
    valor_final = tk.CTkLabel(janela_solteiro_n_dinheiro_ss_resultado, text=( "Valor após descontos: {:.2f}€" .format(renumeracao_final)), font=("Segoe UI", 20), bg_color = "red").place(x=879 , y=300)

### FINAL - SAIR OU HISTORICO ###
    decidir_historico = tk.CTkLabel(janela_solteiro_n_dinheiro_ss_resultado, text=("Deseja adicionar está simulação ao histórico?" ), font=("Segoe UI", 20)).place(x=879, y=500)
    select_tabela_a = tk.CTkButton(janela_solteiro_n_dinheiro_ss_resultado, text="Sim",command=lambda: historico_ordenado(regime, situacao_fiscal, dependentes, contribuicao_social, adse, valor_alimentacao, dias_alimentacao, forma_pagamento, outros, renumeracao, valor_irs, valor_adse, valor_ss, renumeracao_final, invalidez),font=("Segoe UI", 20)).place(x=879, y=550)
    select_tabela_b = tk.CTkButton(janela_solteiro_n_dinheiro_ss_resultado, text="Não",command=lambda: reiniciar_programa(),font=("Segoe UI", 20)).place(x=1079, y=550)



def dependente_solteiro_s_dinheiro_ss_adse(janela_solteiro_n_dinheiro_ss):
    regime = 1
    situacao_fiscal = 1
    contribuicao_social = 1
    adse = 1
    forma_pagamento = 1
    valor_irs=0
    invalidez = 2
    janela_solteiro_n_dinheiro_ss.withdraw()
    janela_solteiro_n_dinheiro_ss_adse = tk.CTkToplevel()
    janela_solteiro_n_dinheiro_ss_adse.geometry("1400x700")
    janela_solteiro_n_dinheiro_ss_adse.title( "Simulação do ordenado liquido - Trabalhador Dependente - Solteiro - Resultado Final")
    texto_topo = tk.CTkLabel(janela_solteiro_n_dinheiro_ss_adse, text="Simulação do ordenado liquido\nTrabalhador Dependente\nSolteiro\nResultado Final", font=("Segoe UI", 20)).place(x=550, y=0)
    ordenado1 = float(renumera_log[0])
    dependentes = int(dependentes_log[0])
    alimentacao = float(alimentacao_log[0])
    dias_alimentacao = int(dias_log[0])
    outros = float(outros_log[0])
    if alimentacao < 6:
        excedente_alimentacao = 0
    else:
        excedente_alimentacao = alimentacao-6
    valor_alimentacao = alimentacao*dias_alimentacao
    excedente_alimentacao_dias = excedente_alimentacao*dias_alimentacao
    renumeracao = ordenado1+excedente_alimentacao_dias+outros


    valor_irs, parcela_abater, taxa, renumeracao_liquida, parcela_dependente = ordenado_dependente_solteiro_invalidez(dependentes, renumeracao)

    valor_ss = renumeracao*0.11
    valor_adse = renumeracao*0.035

    if valor_irs<0:
        valor_irs = 0
    else:
        valor_irs = valor_irs

    renumeracao_final = renumeracao - valor_adse - valor_ss - valor_irs+valor_alimentacao

    ### SINTESE DE CARACTERISTICAS ###

    escrever_renumeracao = tk.CTkLabel(janela_solteiro_n_dinheiro_ss_adse, text=("Ordenado Base: {} €" .format(ordenado1)), font=("Segoe UI", 20)).place(x=150, y=100)
    escrever_regime = tk.CTkLabel(janela_solteiro_n_dinheiro_ss_adse, text=("Regime: Trabalhador Dependente"), font=("Segoe UI", 20)).place(x=150, y=150)
    escrever_fiscal = tk.CTkLabel(janela_solteiro_n_dinheiro_ss_adse, text = ("Situação Fiscal: Solteiro"), font=("Segoe UI", 20)).place(x=150,y=200)
    escrever_dependentes = tk.CTkLabel(janela_solteiro_n_dinheiro_ss_adse, text=("Dependentes: {}".format(dependentes)), font=("Segoe UI", 20)).place(x=150, y=250)
    escrever_social = tk.CTkLabel(janela_solteiro_n_dinheiro_ss_adse, text=("Contribuição Social: Segurança Social"), font=("Segoe UI", 20)).place(x=150, y=300)
    escrever_adse = tk.CTkLabel(janela_solteiro_n_dinheiro_ss_adse, text=("ADSE: Sim"), font=("Segoe UI", 20)).place(x=150, y=350)
    escrever_alimentacao = tk.CTkLabel(janela_solteiro_n_dinheiro_ss_adse, text=("Subsidio de Alimentação: {} €".format(valor_alimentacao)), font=("Segoe UI", 20)).place(x=150, y=400)
    escrever_dias = tk.CTkLabel(janela_solteiro_n_dinheiro_ss_adse, text=("Dias com susbsidio de alimentação: {}".format(dias_alimentacao)), font=("Segoe UI", 20)).place(x=150, y=450)
    escrever_pagamento = tk.CTkLabel(janela_solteiro_n_dinheiro_ss_adse, text=("Forma de pagamento do subsidio de alimentação: Dinheiro"), font=("Segoe UI", 20)).place(x=150, y=500)
    escrever_outros = tk.CTkLabel(janela_solteiro_n_dinheiro_ss_adse, text=("Outros subsidios tributaveis: {} €".format(outros)), font=("Segoe UI", 20)).place(x=150, y=550)
    escrever_invalidez = tk.CTkLabel(janela_solteiro_n_dinheiro_ss_adse, text=("Invalidez ou incapacidade: Sim"), font=("Segoe UI", 20)).place(x=150, y=600)

### APRESENTAÇÃO DOS VALORES ###
    texto_descontos = tk.CTkLabel(janela_solteiro_n_dinheiro_ss_adse, text=("Resumo dos descontos"), font=("Segoe UI", 20)) .place(x=879, y=150)
    texto_valor = tk.CTkLabel(janela_solteiro_n_dinheiro_ss_adse, text=("Valor tributável:{:.2f}€ " .format(renumeracao)), font=("Segoe UI", 20)).place(x=879 , y=300)
    texto_irs = tk.CTkLabel(janela_solteiro_n_dinheiro_ss_adse, text=("Retenção na fonte: {:.2f}€" .format(valor_irs)), font=("Segoe UI", 20)).place(x=879 , y=200)
    texto_ss = tk.CTkLabel(janela_solteiro_n_dinheiro_ss_adse, text=("Taxa Social Única: {:.2f}€" .format(valor_ss)), font=("Segoe UI", 20)).place(x=879 , y=250)
    taxa_adse = tk.CTkLabel(janela_solteiro_n_dinheiro_ss_adse, text=("Desconto ADSE: {:.2f}€" .format(valor_adse)), font=("Segoe UI", 20)).place(x=879 , y=350)
    valor_final = tk.CTkLabel(janela_solteiro_n_dinheiro_ss_adse, text=( "Valor após descontos: {:.2f}€" .format(renumeracao_final)), font=("Segoe UI", 20), bg_color = "red").place(x=879 , y=450)

### FINAL - SAIR OU HISTORICO ###
    decidir_historico = tk.CTkLabel(janela_solteiro_n_dinheiro_ss_adse, text=("Deseja adicionar está simulação ao histórico?" ), font=("Segoe UI", 20)).place(x=879, y=500)
    select_tabela_a = tk.CTkButton(janela_solteiro_n_dinheiro_ss_adse, text="Sim",command=lambda: historico_ordenado(regime, situacao_fiscal, dependentes, contribuicao_social, adse, valor_alimentacao, dias_alimentacao, forma_pagamento, outros, renumeracao, valor_irs, valor_adse, valor_ss, renumeracao_final, invalidez),font=("Segoe UI", 20)).place(x=879, y=550)
    select_tabela_b = tk.CTkButton(janela_solteiro_n_dinheiro_ss_adse, text="Não",command=lambda: reiniciar_programa(),font=("Segoe UI", 20)).place(x=1079, y=550)



def dependente_solteiro_s_dinheiro_ss(janela_solteiro_n_dinheiro):
    janela_solteiro_n_dinheiro.withdraw()
    janela_solteiro_n_dinheiro_ss = tk.CTkToplevel()
    janela_solteiro_n_dinheiro_ss.geometry("1400x700")
    janela_solteiro_n_dinheiro_ss.title("Simulação do ordenado liquido - Trabalhador Dependente - Solteiro - Outras contribuições")
    texto_topo = tk.CTkLabel(janela_solteiro_n_dinheiro_ss, text="Simulação do ordenado liquido\nTrabalhador Dependente\nSolteiro\nOutras contribuições", font=("Segoe UI", 20)).place(x=550, y=0)
    texto_adse = tk.CTkLabel(janela_solteiro_n_dinheiro_ss, text="É beneficiário da ADSE?", font=("Segoe UI", 20)).place(x=590, y=150)
    botao_sim = tk.CTkButton(janela_solteiro_n_dinheiro_ss, text= "Sim", command=lambda: dependente_solteiro_s_dinheiro_ss_adse(janela_solteiro_n_dinheiro_ss), font=("Segoe UI", 20)).place(x=530, y=200)
    botao_nao = tk.CTkButton(janela_solteiro_n_dinheiro_ss, text="Não", command=lambda: dependente_solteiro_s_dinheiro_ss_resultado(janela_solteiro_n_dinheiro_ss), font=("Segoe UI", 20)).place(x=730, y=200)


def dependente_solteiro_s_dinheiro(janela_solteiro_n, pedir_outros, pedir_alimentacao, pedir_dias):
    alimentacao = float(pedir_alimentacao.get())
    alimentacao_log.append(alimentacao)
    dias = float(pedir_dias.get())
    dias_log.append(dias)
    outros = float(pedir_outros.get())
    outros_log.append(outros)
    janela_solteiro_n.withdraw()
    janela_solteiro_n_dinheiro = tk.CTkToplevel()
    janela_solteiro_n_dinheiro.geometry("1400x700")
    janela_solteiro_n_dinheiro.title("Simulação do ordenado liquido - Trabalhador Dependente - Solteiro - Outras contribuições")
    texto_topo = tk.CTkLabel(janela_solteiro_n_dinheiro, text="Simulação do ordenado liquido\nTrabalhador Dependente\nSolteiro\nOutras contribuições", font=("Segoe UI", 20)).place(x=550, y=0)
    texto_forma = tk.CTkLabel(janela_solteiro_n_dinheiro, text = "Selecione a sua forma de contribuição social", font=("Segoe UI", 20)).place(x=510, y=150)
    botao_ss = tk.CTkButton(janela_solteiro_n_dinheiro, text="Segurança Social", command=lambda:dependente_solteiro_s_dinheiro_ss(janela_solteiro_n_dinheiro), font=("Segoe UI", 20)) .place(x=606, y=200)
    botao_cga = tk.CTkButton(janela_solteiro_n_dinheiro, text="Caixa Geral de Aposentações", command=lambda: dependente_solteiro_s_dinheiro_cga(janela_solteiro_n_dinheiro),  font=("Segoe UI",20)) .place(x=560, y=250)


def dependente_solteiro_s_dinheiro_cga_resultado(janela_solteiro_n_dinheiro_cga):
    regime = 1
    situacao_fiscal = 1
    contribuicao_social = 2
    adse = 2
    forma_pagamento = 1
    valor_irs=0
    invalidez = 2
    valor_adse=0
    janela_solteiro_n_dinheiro_cga.withdraw()
    janela_solteiro_n_dinheiro_cga_resultado = tk.CTkToplevel()
    janela_solteiro_n_dinheiro_cga_resultado.geometry("1400x700")
    janela_solteiro_n_dinheiro_cga_resultado.title( "Simulação do ordenado liquido - Trabalhador Dependente - Solteiro - Resultado Final")
    texto_topo = tk.CTkLabel(janela_solteiro_n_dinheiro_cga_resultado, text="Simulação do ordenado liquido\nTrabalhador Dependente\nSolteiro\nResultado Final", font=("Segoe UI", 20)).place(x=550, y=0)
    ordenado1 = float(renumera_log[0])
    dependentes = int(dependentes_log[0])
    alimentacao = float(alimentacao_log[0])
    dias_alimentacao = int(dias_log[0])
    outros = float(outros_log[0])
    if alimentacao <6:
        excedente_alimentacao = 0
    else:
        excedente_alimentacao = alimentacao-6
    valor_alimentacao = alimentacao*dias_alimentacao
    excedente_alimentacao_dias = excedente_alimentacao*dias_alimentacao
    renumeracao = ordenado1+excedente_alimentacao_dias+outros


    valor_irs, parcela_abater, taxa, renumeracao_liquida, parcela_dependente = ordenado_dependente_solteiro_invalidez(dependentes, renumeracao)
    if valor_irs<0:
        valor_irs = 0
    else:
        valor_irs = valor_irs
    valor_ss = renumeracao*0.11
    renumeracao_final = renumeracao - valor_ss - valor_irs + valor_alimentacao


    ### SINTESE DE CARACTERISTICAS ###

    escrever_renumeracao = tk.CTkLabel(janela_solteiro_n_dinheiro_cga_resultado, text=("Ordenado Base: {} €" .format(ordenado1)), font=("Segoe UI", 20)).place(x=150, y=100)
    escrever_regime = tk.CTkLabel(janela_solteiro_n_dinheiro_cga_resultado, text=("Regime: Trabalhador Dependente"), font=("Segoe UI", 20)).place(x=150, y=150)
    escrever_fiscal = tk.CTkLabel(janela_solteiro_n_dinheiro_cga_resultado, text = ("Situação Fiscal: Solteiro"), font=("Segoe UI", 20)).place(x=150,y=200)
    escrever_dependentes = tk.CTkLabel(janela_solteiro_n_dinheiro_cga_resultado, text=("Dependentes: {}".format(dependentes)), font=("Segoe UI", 20)).place(x=150, y=250)
    escrever_social = tk.CTkLabel(janela_solteiro_n_dinheiro_cga_resultado, text=("Contribuição Social: Caixa Geral de Aposentações"), font=("Segoe UI", 20)).place(x=150, y=300)
    escrever_adse = tk.CTkLabel(janela_solteiro_n_dinheiro_cga_resultado, text=("ADSE: Não"), font=("Segoe UI", 20)).place(x=150, y=350)
    escrever_alimentacao = tk.CTkLabel(janela_solteiro_n_dinheiro_cga_resultado, text=("Subsidio de Alimentação: {} €".format(valor_alimentacao)), font=("Segoe UI", 20)).place(x=150, y=400)
    escrever_dias = tk.CTkLabel(janela_solteiro_n_dinheiro_cga_resultado, text=("Dias com susbsidio de alimentação: {}".format(dias_alimentacao)), font=("Segoe UI", 20)).place(x=150, y=450)
    escrever_pagamento = tk.CTkLabel(janela_solteiro_n_dinheiro_cga_resultado, text=("Forma de pagamento do subsidio de alimentação: Dinheiro"), font=("Segoe UI", 20)).place(x=150, y=500)
    escrever_outros = tk.CTkLabel(janela_solteiro_n_dinheiro_cga_resultado, text=("Outros subsidios tributaveis: {} €".format(outros)), font=("Segoe UI", 20)).place(x=150, y=550)
    escrever_invalidez = tk.CTkLabel(janela_solteiro_n_dinheiro_cga_resultado, text=("Invalidez ou incapacidade: Sim"), font=("Segoe UI", 20)).place(x=150, y=600)

### APRESENTAÇÃO DOS VALORES ###
    texto_descontos = tk.CTkLabel(janela_solteiro_n_dinheiro_cga_resultado, text=("Resumo dos descontos"), font=("Segoe UI", 20)) .place(x=879, y=150)
    texto_valor = tk.CTkLabel(janela_solteiro_n_dinheiro_cga_resultado, text=("Valor tributável:{:.2f}€ " .format(renumeracao)), font=("Segoe UI", 20)).place(x=879 , y=300)
    texto_irs = tk.CTkLabel(janela_solteiro_n_dinheiro_cga_resultado, text=("Retenção na fonte: {:.2f}€" .format(valor_irs)), font=("Segoe UI", 20)).place(x=879 , y=200)
    texto_ss = tk.CTkLabel(janela_solteiro_n_dinheiro_cga_resultado, text=("Taxa Social Única: {:.2f}€" .format(valor_ss)), font=("Segoe UI", 20)).place(x=879 , y=250)
    valor_final = tk.CTkLabel(janela_solteiro_n_dinheiro_cga_resultado, text=( "Valor após descontos: {:.2f}€" .format(renumeracao_final)), font=("Segoe UI", 20), bg_color = "red").place(x=879 , y=300)

### FINAL - SAIR OU HISTORICO ###
    decidir_historico = tk.CTkLabel(janela_solteiro_n_dinheiro_cga_resultado, text=("Deseja adicionar está simulação ao histórico?" ), font=("Segoe UI", 20)).place(x=879, y=500)
    select_tabela_a = tk.CTkButton(janela_solteiro_n_dinheiro_cga_resultado, text="Sim",command=lambda: historico_ordenado(regime, situacao_fiscal, dependentes, contribuicao_social, adse, valor_alimentacao, dias_alimentacao, forma_pagamento, outros, renumeracao, valor_irs, valor_adse, valor_ss, renumeracao_final, invalidez),font=("Segoe UI", 20)).place(x=879, y=550)
    select_tabela_b = tk.CTkButton(janela_solteiro_n_dinheiro_cga_resultado, text="Não",command=lambda: reiniciar_programa(),font=("Segoe UI", 20)).place(x=1079, y=550)


def dependente_solteiro_s_dinheiro_cga_adse(janela_solteiro_n_dinheiro_cga):
    regime = 1
    situacao_fiscal = 1
    contribuicao_social = 2
    adse = 1
    forma_pagamento = 1
    valor_irs=0
    invalidez = 2
    janela_solteiro_n_dinheiro_cga.withdraw()
    janela_solteiro_n_dinheiro_cga_adse = tk.CTkToplevel()
    janela_solteiro_n_dinheiro_cga_adse.geometry("1400x700")
    janela_solteiro_n_dinheiro_cga_adse.title( "Simulação do ordenado liquido - Trabalhador Dependente - Solteiro - Resultado Final")
    texto_topo = tk.CTkLabel(janela_solteiro_n_dinheiro_cga_adse, text="Simulação do ordenado liquido\nTrabalhador Dependente\nSolteiro\nResultado Final", font=("Segoe UI", 20)).place(x=550, y=0)
    ordenado1 = float(renumera_log[0])
    dependentes = int(dependentes_log[0])
    alimentacao = float(alimentacao_log[0])
    dias_alimentacao = int(dias_log[0])
    outros = float(outros_log[0])
    if alimentacao < 6:
        excedente_alimentacao = 0
    else:
        excedente_alimentacao = alimentacao-6
    valor_alimentacao = alimentacao*dias_alimentacao
    excedente_alimentacao_dias = excedente_alimentacao*dias_alimentacao
    renumeracao = ordenado1+excedente_alimentacao_dias+outros


    valor_irs, parcela_abater, taxa, renumeracao_liquida, parcela_dependente = ordenado_dependente_solteiro_invalidez(dependentes, renumeracao)

    valor_ss = renumeracao*0.11
    valor_adse = renumeracao*0.035
    if valor_irs<0:
        valor_irs = 0
    else:
        valor_irs = valor_irs
    renumeracao_final = renumeracao - valor_adse - valor_ss - valor_irs+valor_alimentacao

    ### SINTESE DE CARACTERISTICAS ###

    escrever_renumeracao = tk.CTkLabel(janela_solteiro_n_dinheiro_cga_adse, text=("Ordenado Base: {} €" .format(ordenado1)), font=("Segoe UI", 20)).place(x=150, y=100)
    escrever_regime = tk.CTkLabel(janela_solteiro_n_dinheiro_cga_adse, text=("Regime: Trabalhador Dependente"), font=("Segoe UI", 20)).place(x=150, y=150)
    escrever_fiscal = tk.CTkLabel(janela_solteiro_n_dinheiro_cga_adse, text = ("Situação Fiscal: Solteiro"), font=("Segoe UI", 20)).place(x=150,y=200)
    escrever_dependentes = tk.CTkLabel(janela_solteiro_n_dinheiro_cga_adse, text=("Dependentes: {}".format(dependentes)), font=("Segoe UI", 20)).place(x=150, y=250)
    escrever_social = tk.CTkLabel(janela_solteiro_n_dinheiro_cga_adse, text=("Contribuição Social: Caixa Geral de Aposentações"), font=("Segoe UI", 20)).place(x=150, y=300)
    escrever_adse = tk.CTkLabel(janela_solteiro_n_dinheiro_cga_adse, text=("ADSE: Sim"), font=("Segoe UI", 20)).place(x=150, y=350)
    escrever_alimentacao = tk.CTkLabel(janela_solteiro_n_dinheiro_cga_adse, text=("Subsidio de Alimentação: {} €".format(valor_alimentacao)), font=("Segoe UI", 20)).place(x=150, y=400)
    escrever_dias = tk.CTkLabel(janela_solteiro_n_dinheiro_cga_adse, text=("Dias com susbsidio de alimentação: {}".format(dias_alimentacao)), font=("Segoe UI", 20)).place(x=150, y=450)
    escrever_pagamento = tk.CTkLabel(janela_solteiro_n_dinheiro_cga_adse, text=("Forma de pagamento do subsidio de alimentação: Dinheiro"), font=("Segoe UI", 20)).place(x=150, y=500)
    escrever_outros = tk.CTkLabel(janela_solteiro_n_dinheiro_cga_adse, text=("Outros subsidios tributaveis: {} €".format(outros)), font=("Segoe UI", 20)).place(x=150, y=550)
    escrever_invalidez = tk.CTkLabel(janela_solteiro_n_dinheiro_cga_adse, text=("Invalidez ou incapacidade: Não"), font=("Segoe UI", 20)).place(x=150, y=600)

### APRESENTAÇÃO DOS VALORES ###
    texto_descontos = tk.CTkLabel(janela_solteiro_n_dinheiro_cga_adse, text=("Resumo dos descontos"), font=("Segoe UI", 20)) .place(x=879, y=150)
    texto_valor = tk.CTkLabel(janela_solteiro_n_dinheiro_cga_adse, text=("Valor tributável:{:.2f}€ " .format(renumeracao)), font=("Segoe UI", 20)).place(x=879 , y=300)
    texto_irs = tk.CTkLabel(janela_solteiro_n_dinheiro_cga_adse, text=("Retenção na fonte: {:.2f}€" .format(valor_irs)), font=("Segoe UI", 20)).place(x=879 , y=200)
    texto_ss = tk.CTkLabel(janela_solteiro_n_dinheiro_cga_adse, text=("Taxa Social Única: {:.2f}€" .format(valor_ss)), font=("Segoe UI", 20)).place(x=879 , y=250)
    taxa_adse = tk.CTkLabel(janela_solteiro_n_dinheiro_cga_adse, text=("Desconto ADSE: {:.2f}€" .format(valor_adse)), font=("Segoe UI", 20)).place(x=879 , y=350)
    valor_final = tk.CTkLabel(janela_solteiro_n_dinheiro_cga_adse, text=( "Valor após descontos: {:.2f}€" .format(renumeracao_final)), font=("Segoe UI", 20), bg_color = "red").place(x=879 , y=450)

### FINAL - SAIR OU HISTORICO ###
    decidir_historico = tk.CTkLabel(janela_solteiro_n_dinheiro_cga_adse, text=("Deseja adicionar está simulação ao histórico?" ), font=("Segoe UI", 20)).place(x=879, y=500)
    select_tabela_a = tk.CTkButton(janela_solteiro_n_dinheiro_cga_adse, text="Sim",command=lambda: historico_ordenado(regime, situacao_fiscal, dependentes, contribuicao_social, adse, valor_alimentacao, dias_alimentacao, forma_pagamento, outros, renumeracao, valor_irs, valor_adse, valor_ss, renumeracao_final, invalidez),font=("Segoe UI", 20)).place(x=879, y=550)
    select_tabela_b = tk.CTkButton(janela_solteiro_n_dinheiro_cga_adse, text="Não",command=lambda: reiniciar_programa(),font=("Segoe UI", 20)).place(x=1079, y=550)

def dependente_solteiro_s_dinheiro_cga(janela_solteiro_n_dinheiro):
    janela_solteiro_n_dinheiro.withdraw()
    janela_solteiro_n_dinheiro_cga = tk.CTkToplevel()
    janela_solteiro_n_dinheiro_cga.geometry("1400x700")
    janela_solteiro_n_dinheiro_cga.title("Simulação do ordenado liquido - Trabalhador Dependente - Solteiro - Outras contribuições")
    texto_topo = tk.CTkLabel(janela_solteiro_n_dinheiro_cga, text="Simulação do ordenado liquido\nTrabalhador Dependente\nSolteiro\nOutras contribuições", font=("Segoe UI", 20)).place(x=550, y=0)
    texto_adse = tk.CTkLabel(janela_solteiro_n_dinheiro_cga, text="É beneficiário da ADSE?", font=("Segoe UI", 20)).place(x=590, y=150)
    botao_sim = tk.CTkButton(janela_solteiro_n_dinheiro_cga, text= "Sim", command=lambda: dependente_solteiro_s_dinheiro_cga_adse(janela_solteiro_n_dinheiro_cga), font=("Segoe UI", 20)).place(x=530, y=200)
    botao_nao = tk.CTkButton(janela_solteiro_n_dinheiro_cga, text="Não", command=lambda: dependente_solteiro_s_dinheiro_cga_resultado(janela_solteiro_n_dinheiro_cga), font=("Segoe UI", 20)).place(x=730, y=200)


def dependente_solteiro_s_dinheiro_ss_resultado(janela_solteiro_n_dinheiro_ss):
    regime = 1
    situacao_fiscal = 1
    contribuicao_social = 1
    adse = 2
    forma_pagamento = 1
    valor_irs=0
    invalidez = 2
    valor_adse=0
    janela_solteiro_n_dinheiro_ss.withdraw()
    janela_solteiro_n_dinheiro_ss_resultado = tk.CTkToplevel()
    janela_solteiro_n_dinheiro_ss_resultado.geometry("1400x700")
    janela_solteiro_n_dinheiro_ss_resultado.title( "Simulação do ordenado liquido - Trabalhador Dependente - Solteiro - Resultado Final")
    texto_topo = tk.CTkLabel(janela_solteiro_n_dinheiro_ss_resultado, text="Simulação do ordenado liquido\nTrabalhador Dependente\nSolteiro\nResultado Final", font=("Segoe UI", 20)).place(x=550, y=0)
    ordenado1 = float(renumera_log[0])
    dependentes = int(dependentes_log[0])
    alimentacao = float(alimentacao_log[0])
    dias_alimentacao = int(dias_log[0])
    outros = float(outros_log[0])
    if alimentacao <6:
        excedente_alimentacao = 0
    else:
        excedente_alimentacao = alimentacao-6
    valor_alimentacao = alimentacao*dias_alimentacao
    excedente_alimentacao_dias = excedente_alimentacao*dias_alimentacao
    renumeracao = ordenado1+excedente_alimentacao_dias+outros


    valor_irs, parcela_abater, taxa, renumeracao_liquida, parcela_dependente = ordenado_dependente_solteiro_invalidez(dependentes, renumeracao)
    if valor_irs<0:
        valor_irs = 0
    else:
        valor_irs = valor_irs
    valor_ss = renumeracao*0.11
    renumeracao_final = renumeracao - valor_ss - valor_irs + valor_alimentacao


    ### SINTESE DE CARACTERISTICAS ###

    escrever_renumeracao = tk.CTkLabel(janela_solteiro_n_dinheiro_ss_resultado, text=("Ordenado Base: {} €" .format(ordenado1)), font=("Segoe UI", 20)).place(x=150, y=100)
    escrever_regime = tk.CTkLabel(janela_solteiro_n_dinheiro_ss_resultado, text=("Regime: Trabalhador Dependente"), font=("Segoe UI", 20)).place(x=150, y=150)
    escrever_fiscal = tk.CTkLabel(janela_solteiro_n_dinheiro_ss_resultado, text = ("Situação Fiscal: Solteiro"), font=("Segoe UI", 20)).place(x=150,y=200)
    escrever_dependentes = tk.CTkLabel(janela_solteiro_n_dinheiro_ss_resultado, text=("Dependentes: {}".format(dependentes)), font=("Segoe UI", 20)).place(x=150, y=250)
    escrever_social = tk.CTkLabel(janela_solteiro_n_dinheiro_ss_resultado, text=("Contribuição Social: Segurança Social"), font=("Segoe UI", 20)).place(x=150, y=300)
    escrever_adse = tk.CTkLabel(janela_solteiro_n_dinheiro_ss_resultado, text=("ADSE: Não"), font=("Segoe UI", 20)).place(x=150, y=350)
    escrever_alimentacao = tk.CTkLabel(janela_solteiro_n_dinheiro_ss_resultado, text=("Subsidio de Alimentação: {} €".format(valor_alimentacao)), font=("Segoe UI", 20)).place(x=150, y=400)
    escrever_dias = tk.CTkLabel(janela_solteiro_n_dinheiro_ss_resultado, text=("Dias com susbsidio de alimentação: {}".format(dias_alimentacao)), font=("Segoe UI", 20)).place(x=150, y=450)
    escrever_pagamento = tk.CTkLabel(janela_solteiro_n_dinheiro_ss_resultado, text=("Forma de pagamento do subsidio de alimentação: Dinheiro"), font=("Segoe UI", 20)).place(x=150, y=500)
    escrever_outros = tk.CTkLabel(janela_solteiro_n_dinheiro_ss_resultado, text=("Outros subsidios tributaveis: {} €".format(outros)), font=("Segoe UI", 20)).place(x=150, y=550)
    escrever_invalidez = tk.CTkLabel(janela_solteiro_n_dinheiro_ss_resultado, text=("Invalidez ou incapacidade: Sim"), font=("Segoe UI", 20)).place(x=150, y=600)

### APRESENTAÇÃO DOS VALORES ###
    texto_descontos = tk.CTkLabel(janela_solteiro_n_dinheiro_ss_resultado, text=("Resumo dos descontos"), font=("Segoe UI", 20)) .place(x=879, y=150)
    texto_valor = tk.CTkLabel(janela_solteiro_n_dinheiro_ss_resultado, text=("Valor tributável:{:.2f}€ " .format(renumeracao)), font=("Segoe UI", 20)).place(x=879 , y=300)
    texto_irs = tk.CTkLabel(janela_solteiro_n_dinheiro_ss_resultado, text=("Retenção na fonte: {:.2f}€" .format(valor_irs)), font=("Segoe UI", 20)).place(x=879 , y=200)
    texto_ss = tk.CTkLabel(janela_solteiro_n_dinheiro_ss_resultado, text=("Taxa Social Única: {:.2f}€" .format(valor_ss)), font=("Segoe UI", 20)).place(x=879 , y=250)
    valor_final = tk.CTkLabel(janela_solteiro_n_dinheiro_ss_resultado, text=( "Valor após descontos: {:.2f}€" .format(renumeracao_final)), font=("Segoe UI", 20), bg_color = "red").place(x=879 , y=300)

### FINAL - SAIR OU HISTORICO ###
    decidir_historico = tk.CTkLabel(janela_solteiro_n_dinheiro_ss_resultado, text=("Deseja adicionar está simulação ao histórico?" ), font=("Segoe UI", 20)).place(x=879, y=500)
    select_tabela_a = tk.CTkButton(janela_solteiro_n_dinheiro_ss_resultado, text="Sim",command=lambda: historico_ordenado(regime, situacao_fiscal, dependentes, contribuicao_social, adse, valor_alimentacao, dias_alimentacao, forma_pagamento, outros, renumeracao, valor_irs, valor_adse, valor_ss, renumeracao_final, invalidez),font=("Segoe UI", 20)).place(x=879, y=550)
    select_tabela_b = tk.CTkButton(janela_solteiro_n_dinheiro_ss_resultado, text="Não",command=lambda: reiniciar_programa(),font=("Segoe UI", 20)).place(x=1079, y=550)


def dependente_solteiro_s_dinheiro_ss_adse(janela_solteiro_n_dinheiro_ss):
    regime = 1
    situacao_fiscal = 1
    contribuicao_social = 1
    adse = 1
    forma_pagamento = 1
    valor_irs=0
    invalidez = 2
    janela_solteiro_n_dinheiro_ss.withdraw()
    janela_solteiro_n_dinheiro_ss_adse = tk.CTkToplevel()
    janela_solteiro_n_dinheiro_ss_adse.geometry("1400x700")
    janela_solteiro_n_dinheiro_ss_adse.title( "Simulação do ordenado liquido - Trabalhador Dependente - Solteiro - Resultado Final")
    texto_topo = tk.CTkLabel(janela_solteiro_n_dinheiro_ss_adse, text="Simulação do ordenado liquido\nTrabalhador Dependente\nSolteiro\nResultado Final", font=("Segoe UI", 20)).place(x=550, y=0)
    ordenado1 = float(renumera_log[0])
    dependentes = int(dependentes_log[0])
    alimentacao = float(alimentacao_log[0])
    dias_alimentacao = int(dias_log[0])
    outros = float(outros_log[0])
    if alimentacao < 6:
        excedente_alimentacao = 0
    else:
        excedente_alimentacao = alimentacao-6
    valor_alimentacao = alimentacao*dias_alimentacao
    excedente_alimentacao_dias = excedente_alimentacao*dias_alimentacao
    renumeracao = ordenado1+excedente_alimentacao_dias+outros

    valor_irs, parcela_abater, taxa, renumeracao_liquida, parcela_dependente = ordenado_dependente_solteiro_invalidez(dependentes, renumeracao)

    valor_ss = renumeracao*0.11
    valor_adse = renumeracao*0.035

    if valor_irs<0:
        valor_irs = 0
    else:
        valor_irs = valor_irs

    renumeracao_final = renumeracao - valor_adse - valor_ss - valor_irs+valor_alimentacao

    ### SINTESE DE CARACTERISTICAS ###

    escrever_renumeracao = tk.CTkLabel(janela_solteiro_n_dinheiro_ss_adse, text=("Ordenado Base: {} €" .format(ordenado1)), font=("Segoe UI", 20)).place(x=150, y=100)
    escrever_regime = tk.CTkLabel(janela_solteiro_n_dinheiro_ss_adse, text=("Regime: Trabalhador Dependente"), font=("Segoe UI", 20)).place(x=150, y=150)
    escrever_fiscal = tk.CTkLabel(janela_solteiro_n_dinheiro_ss_adse, text = ("Situação Fiscal: Solteiro"), font=("Segoe UI", 20)).place(x=150,y=200)
    escrever_dependentes = tk.CTkLabel(janela_solteiro_n_dinheiro_ss_adse, text=("Dependentes: {}".format(dependentes)), font=("Segoe UI", 20)).place(x=150, y=250)
    escrever_social = tk.CTkLabel(janela_solteiro_n_dinheiro_ss_adse, text=("Contribuição Social: Segurança Social"), font=("Segoe UI", 20)).place(x=150, y=300)
    escrever_adse = tk.CTkLabel(janela_solteiro_n_dinheiro_ss_adse, text=("ADSE: Sim"), font=("Segoe UI", 20)).place(x=150, y=350)
    escrever_alimentacao = tk.CTkLabel(janela_solteiro_n_dinheiro_ss_adse, text=("Subsidio de Alimentação: {} €".format(valor_alimentacao)), font=("Segoe UI", 20)).place(x=150, y=400)
    escrever_dias = tk.CTkLabel(janela_solteiro_n_dinheiro_ss_adse, text=("Dias com susbsidio de alimentação: {}".format(dias_alimentacao)), font=("Segoe UI", 20)).place(x=150, y=450)
    escrever_pagamento = tk.CTkLabel(janela_solteiro_n_dinheiro_ss_adse, text=("Forma de pagamento do subsidio de alimentação: Dinheiro"), font=("Segoe UI", 20)).place(x=150, y=500)
    escrever_outros = tk.CTkLabel(janela_solteiro_n_dinheiro_ss_adse, text=("Outros subsidios tributaveis: {} €".format(outros)), font=("Segoe UI", 20)).place(x=150, y=550)
    escrever_invalidez = tk.CTkLabel(janela_solteiro_n_dinheiro_ss_adse, text=("Invalidez ou incapacidade: Sim"), font=("Segoe UI", 20)).place(x=150, y=600)

### APRESENTAÇÃO DOS VALORES ###
    texto_descontos = tk.CTkLabel(janela_solteiro_n_dinheiro_ss_adse, text=("Resumo dos descontos"), font=("Segoe UI", 20)) .place(x=879, y=150)
    texto_valor = tk.CTkLabel(janela_solteiro_n_dinheiro_ss_adse, text=("Valor tributável:{:.2f}€ " .format(renumeracao)), font=("Segoe UI", 20)).place(x=879 , y=300)
    texto_irs = tk.CTkLabel(janela_solteiro_n_dinheiro_ss_adse, text=("Retenção na fonte: {:.2f}€" .format(valor_irs)), font=("Segoe UI", 20)).place(x=879 , y=200)
    texto_ss = tk.CTkLabel(janela_solteiro_n_dinheiro_ss_adse, text=("Taxa Social Única: {:.2f}€" .format(valor_ss)), font=("Segoe UI", 20)).place(x=879 , y=250)
    taxa_adse = tk.CTkLabel(janela_solteiro_n_dinheiro_ss_adse, text=("Desconto ADSE: {:.2f}€" .format(valor_adse)), font=("Segoe UI", 20)).place(x=879 , y=350)
    valor_final = tk.CTkLabel(janela_solteiro_n_dinheiro_ss_adse, text=( "Valor após descontos: {:.2f}€" .format(renumeracao_final)), font=("Segoe UI", 20), bg_color = "red").place(x=879 , y=450)

### FINAL - SAIR OU HISTORICO ###
    decidir_historico = tk.CTkLabel(janela_solteiro_n_dinheiro_ss_adse, text=("Deseja adicionar está simulação ao histórico?" ), font=("Segoe UI", 20)).place(x=879, y=500)
    select_tabela_a = tk.CTkButton(janela_solteiro_n_dinheiro_ss_adse, text="Sim",command=lambda: historico_ordenado(regime, situacao_fiscal, dependentes, contribuicao_social, adse, valor_alimentacao, dias_alimentacao, forma_pagamento, outros, renumeracao, valor_irs, valor_adse, valor_ss, renumeracao_final, invalidez),font=("Segoe UI", 20)).place(x=879, y=550)
    select_tabela_b = tk.CTkButton(janela_solteiro_n_dinheiro_ss_adse, text="Não",command=lambda: reiniciar_programa(),font=("Segoe UI", 20)).place(x=1079, y=550)


def dependente_solteiro_s_dinheiro_ss(janela_solteiro_n_dinheiro):
    janela_solteiro_n_dinheiro.withdraw()
    janela_solteiro_n_dinheiro_ss = tk.CTkToplevel()
    janela_solteiro_n_dinheiro_ss.geometry("1400x700")
    janela_solteiro_n_dinheiro_ss.title("Simulação do ordenado liquido - Trabalhador Dependente - Solteiro - Outras contribuições")
    texto_topo = tk.CTkLabel(janela_solteiro_n_dinheiro_ss, text="Simulação do ordenado liquido\nTrabalhador Dependente\nSolteiro\nOutras contribuições", font=("Segoe UI", 20)).place(x=550, y=0)
    texto_adse = tk.CTkLabel(janela_solteiro_n_dinheiro_ss, text="É beneficiário da ADSE?", font=("Segoe UI", 20)).place(x=590, y=150)
    botao_sim = tk.CTkButton(janela_solteiro_n_dinheiro_ss, text= "Sim", command=lambda: dependente_solteiro_s_dinheiro_ss_adse(janela_solteiro_n_dinheiro_ss), font=("Segoe UI", 20)).place(x=530, y=200)
    botao_nao = tk.CTkButton(janela_solteiro_n_dinheiro_ss, text="Não", command=lambda: dependente_solteiro_s_dinheiro_ss_resultado(janela_solteiro_n_dinheiro_ss), font=("Segoe UI", 20)).place(x=730, y=200)


def dependente_solteiro_s_dinheiro(janela_solteiro_n, pedir_outros, pedir_alimentacao, pedir_dias):
    alimentacao = float(pedir_alimentacao.get())
    alimentacao_log.append(alimentacao)
    dias = float(pedir_dias.get())
    dias_log.append(dias)
    outros = float(pedir_outros.get())
    outros_log.append(outros)
    janela_solteiro_n.withdraw()
    janela_solteiro_n_dinheiro = tk.CTkToplevel()
    janela_solteiro_n_dinheiro.geometry("1400x700")
    janela_solteiro_n_dinheiro.title("Simulação do ordenado liquido - Trabalhador Dependente - Solteiro - Outras contribuições")
    texto_topo = tk.CTkLabel(janela_solteiro_n_dinheiro, text="Simulação do ordenado liquido\nTrabalhador Dependente\nSolteiro\nOutras contribuições", font=("Segoe UI", 20)).place(x=550, y=0)
    texto_forma = tk.CTkLabel(janela_solteiro_n_dinheiro, text = "Selecione a sua forma de contribuição social", font=("Segoe UI", 20)).place(x=510, y=150)
    botao_ss = tk.CTkButton(janela_solteiro_n_dinheiro, text="Segurança Social", command=lambda:dependente_solteiro_s_dinheiro_ss(janela_solteiro_n_dinheiro), font=("Segoe UI", 20)) .place(x=606, y=200)
    botao_cga = tk.CTkButton(janela_solteiro_n_dinheiro, text="Caixa Geral de Aposentações", command=lambda: dependente_solteiro_s_dinheiro_cga(janela_solteiro_n_dinheiro),  font=("Segoe UI",20)) .place(x=560, y=250)

def dependente_solteiro_s(janela_dependente_solteiro, pedir_renumeracao_base):

    ordenado2 = float(pedir_renumeracao_base.get())
    renumera_log.append(ordenado2)
    janela_dependente_solteiro.withdraw()
    janela_solteiro_n = tk.CTkToplevel()
    janela_solteiro_n.geometry("1400x700")
    janela_solteiro_n.title("Simulação do ordenado liquido - Trabalhador Dependente - Solteiro - Subsidios")
    texto_topo = tk.CTkLabel(janela_solteiro_n,text="Simulação do ordenado liquido\nTrabalhador Dependente\nSolteiro", font=("Segoe UI", 20)).place(x=550, y=0)
    texto_alimentacao = tk.CTkLabel(janela_solteiro_n,text="Insira o valor diário do subsidio de alimentação", font=("Segoe UI", 20)).place(x=490, y=100)
    pedir_alimentacao = tk.CTkEntry(janela_solteiro_n, placeholder_text= "Valor", font=("Segoe UI",20))
    pedir_alimentacao.place(x=636, y=150)
    texto_dias = tk.CTkLabel(janela_solteiro_n,text="Insira o número de dias com subsidio de alimentação", font=("Segoe UI", 20)).place(x=475, y=200)
    pedir_dias = tk.CTkEntry(janela_solteiro_n, placeholder_text="Dias", font=("Segoe UI", 20))
    pedir_dias.place(x=636, y=250)
    texto_outros = tk.CTkLabel(janela_solteiro_n, text = "Insira o valor de outros subsidios", font=("Segoe UI",20)) .place(x=550,y=300)
    pedir_outros = tk.CTkEntry(janela_solteiro_n, placeholder_text= "Valor", font=("Segoe UI",20))
    pedir_outros.place(x=636,y=350)
    texto_pag_alimentacao = tk.CTkLabel(janela_solteiro_n, text = "Selecione a forma de pagamento do subsidio de alimentacão", font=("Segoe UI", 20)) .place(x=450, y=400)
    botao_dinheiro = tk.CTkButton(janela_solteiro_n, text = "Dinheiro", font=("Segoe UI", 20), command=lambda: dependente_solteiro_s_dinheiro(janela_solteiro_n, pedir_outros, pedir_alimentacao, pedir_dias)) .place(x=490, y=450)
    botao_cartao = tk.CTkButton(janela_solteiro_n, text="Cartão/Vale de refeição", command=lambda:dependente_solteiro_s_vale(janela_solteiro_n, pedir_outros, pedir_alimentacao, pedir_dias),font=("Segoe UI", 20)) .place(x=690, y=450)


def dependente_solteiro(janela_dependente, pedir_dependentes):
    janela_dependente.withdraw()
    dependentes_log.append(pedir_dependentes.get())
    janela_dependente_solteiro=tk.CTkToplevel()
    janela_dependente_solteiro.title("Simulação do ordenado liquido - Trabalhador Dependente - Solteiro")
    janela_dependente_solteiro.geometry("1400x700")
    texto_topo = tk.CTkLabel(janela_dependente_solteiro, text = "Simulação do ordenado liquido\nTrabalhador Dependente\nSolteiro", font = ("Segoe UI", 20)) .place(x=560, y=0)
    texto_renumeracao_base = tk.CTkLabel(janela_dependente_solteiro, text = "Insira a sua renumeração base", font = ("Segoe UI", 20)) .place(x=569, y=100)
    pedir_renumeracao_base = tk.CTkEntry(janela_dependente_solteiro, placeholder_text = "Renumeração base", font = ("Segoe UI",20))
    pedir_renumeracao_base.place(x=616, y=150)
    texto_invalidez= tk.CTkLabel(janela_dependente_solteiro, text = "Possui algum tipo de invalidez (deficiencia)?", font = ("Segoe UI",20)) .place(x=524, y=200)
    sim_invalidez = tk.CTkButton(janela_dependente_solteiro, text = "Sim", font=("Sego UI",20), command = lambda: dependente_solteiro_s(janela_dependente_solteiro, pedir_renumeracao_base)). place(x = 626, y=250)
    nao_invalidez = tk.CTkButton(janela_dependente_solteiro, text = "Não", font=("Sego UI",20), command=lambda:dependente_solteiro_n(janela_dependente_solteiro, pedir_renumeracao_base)). place(x=626, y=300)

def dependente(janela_dados):
    janela_dados.withdraw()
    janela_dependente = tk.CTkToplevel()
    janela_dependente.title("Simulação do ordenado liquido - Trabalhador Dependente")
    janela_dependente.geometry("1400x700")
    texto_topo = tk.CTkLabel(janela_dependente, text = "Simulação do Ordenado Liquido\nTrabalhador Dependente", font=("Segoe UI", 20)) .place(x= 550, y=0)
    texto_dependentes  = tk.CTkLabel(janela_dependente, text = "Insira a quantidade de dependentes", font=("Segoe UI", 20)) .place(x=540, y=150)
    pedir_dependentes = tk.CTkEntry(janela_dependente, placeholder_text= "Dependentes", font=("Segoe UI", 20))
    pedir_dependentes.place(x=616, y=200)
    texto_situacao_fiscal= tk.CTkLabel(janela_dependente, text = "Selecione a sua situação fiscal", font=("Segoe UI", 20)) .place(x=560,y=250)
    botao_solteiro = tk.CTkButton(janela_dependente, text = "Solteiro", font=("Segoe UI", 20), command=lambda: dependente_solteiro(janela_dependente, pedir_dependentes)) .place(x=616, y=300)
    botao_casado_1t = tk.CTkButton(janela_dependente, text = "Casado - 1 Titular", font=("Segoe UI", 20), command=lambda: dependente_1t(janela_dependente, pedir_dependentes) ) .place(x=610, y=350)
    botao_casado_2t = tk.CTkButton(janela_dependente, text="Casado - 2 Titulares", command= lambda:dependente_2t(janela_dependente, pedir_dependentes), font=("Segoe UI", 20)).place(x=600, y=400)

########################################################################

def historico_pensao(situacao_fiscal, invalidez, renumeracao, valor_irs,  renumeracao_final):
    data_atual = datetime.today().date()
    data_atual_formatada = "{}/{}/{}" .format(data_atual.day, data_atual.month, data_atual.year)
    hora_atual = datetime.now().time()
    f = open("historico.txt", "a+")
    f.write("--- SIMULAÇÃO DOS IMPOSTOS SOBRE OS RENDIMENTOS 2023 2ºSEMESTRE ---\n")

    f.write("Simulação realizada no dia {} ás {}\n".format(data_atual_formatada, hora_atual))
    f.write(" --- Caracterização ---\n")
    f.write("Pensionista\n")
    if situacao_fiscal == 1:
        f.write("Situação Fiscal: Solteiro\n")
    elif situacao_fiscal == 2:
        f.write("Situação Fiscal: Casado: 1 titular\n")
    else:
        f.write("Situação Fiscal: Casado: 2 titular\n")
    if invalidez == 1:
        f.write("Invalidez, defeciencia ou incapacidade: Não\n")
    elif invalidez == 2:
        f.write("Invalidez, deficiencia ou incapacidade: Sim\n")
    else:
        f.write("Invalidez, deficiencia ou incapacidade: Sim, das forças armadas\n")
    f.write("--- Resumo dos descontos ---\n")
    f.write("Valor tributável: {:.2f}€\n".format(renumeracao))
    f.write("Retenção na fonte: {:.2f}€\n".format(valor_irs))
    f.write("Valor após descontos: {:.2f}€\n".format(renumeracao_final))
    f.write("----------------------------------------------------------------\n")
    f.close()
    os.system(f'start notepad {historico}')
    reiniciar_programa()

def pensionista_2t_solteiro_invalidez_fa(janela_reformado_solteiro):
    situacao_fiscal = 1
    valor_irs=0
    invalidez = 3

    janela_reformado_solteiro.withdraw()
    janela_reforma_n = tk.CTkToplevel()
    janela_reforma_n.geometry("1400x700")
    janela_reforma_n.title( "Simulação do ordenado liquido - Pensionista - Solteiro ou Casado 2 Titulares - Resultado Final")
    texto_topo = tk.CTkLabel(janela_reforma_n, text="Simulação do ordenado liquido\nPensionista\nSolteiro ou Casado 2 Titulares\nResultado Final", font=("Segoe UI", 20)).place(x=550, y=0)
    renumeracao = float(renumera_log[0])
    ordenado1=renumeracao


    valor_irs, parcela_abater, taxa, renumeracao_liquida = pensao_solteiro_casado_2t_deficiente_fa(renumeracao)
    if valor_irs<0:
        valor_irs = 0
    else:
        valor_irs = valor_irs
    renumeracao_final = renumeracao - valor_irs


    ### SINTESE DE CARACTERISTICAS ###

    escrever_renumeracao = tk.CTkLabel(janela_reforma_n, text=("Ordenado Base: {} €" .format(ordenado1)), font=("Segoe UI", 20)).place(x=150, y=150)
    escrever_regime = tk.CTkLabel(janela_reforma_n, text=("Regime: Pensionista"), font=("Segoe UI", 20)).place(x=150, y=200)
    escrever_fiscal = tk.CTkLabel(janela_reforma_n, text = ("Situação Fiscal: Solteiro ou Casado 2 titulares"), font=("Segoe UI", 20)).place(x=150,y=250)
    escrever_invalidez = tk.CTkLabel(janela_reforma_n, text=("Invalidez ou incapacidade: Sim, das forças armadas"), font=("Segoe UI", 20)).place(x=150, y=300)

### APRESENTAÇÃO DOS VALORES ###
    texto_descontos = tk.CTkLabel(janela_reforma_n, text=("Resumo dos descontos"), font=("Segoe UI", 20)) .place(x=879, y=150)
    texto_valor = tk.CTkLabel(janela_reforma_n, text=("Valor tributável:{:.2f}€ " .format(renumeracao)), font=("Segoe UI", 20)).place(x=879 , y=200)
    texto_irs = tk.CTkLabel(janela_reforma_n, text=("Retenção na fonte: {:.2f}€" .format(valor_irs)), font=("Segoe UI", 20)).place(x=879 , y=250)
    valor_final = tk.CTkLabel(janela_reforma_n, text=( "Valor após descontos: {:.2f}€" .format(renumeracao_final)), font=("Segoe UI", 20), bg_color = "red").place(x=879 , y=350)

### FINAL - SAIR OU HISTORICO ###
    decidir_historico = tk.CTkLabel(janela_reforma_n, text=("Deseja adicionar está simulação ao histórico?" ), font=("Segoe UI", 20)).place(x=879, y=500)
    select_tabela_a = tk.CTkButton(janela_reforma_n, text="Sim",command=lambda: historico_pensao(situacao_fiscal, invalidez, renumeracao, valor_irs,  renumeracao_final),font=("Segoe UI", 20)).place(x=879, y=550)
    select_tabela_b = tk.CTkButton(janela_reforma_n, text="Não",command=lambda: reiniciar_programa(),font=("Segoe UI", 20)).place(x=1079, y=550)


def pensionista_2t_solteiro_invalidez(janela_reformado_solteiro):
    situacao_fiscal = 1
    valor_irs=0
    invalidez = 2

    janela_reformado_solteiro.withdraw()
    janela_reforma_n = tk.CTkToplevel()
    janela_reforma_n.geometry("1400x700")
    janela_reforma_n.title( "Simulação do ordenado liquido - Pensionista - Solteiro ou Casado 2 Titulares - Resultado Final")
    texto_topo = tk.CTkLabel(janela_reforma_n, text="Simulação do ordenado liquido\nPensionista\nSolteiro ou Casado 2 Titulares\nResultado Final", font=("Segoe UI", 20)).place(x=550, y=0)
    renumeracao = float(renumera_log[0])
    ordenado1=renumeracao


    valor_irs, parcela_abater, taxa, renumeracao_liquida = pensao_solteiro_casado_2t_deficiente(renumeracao)
    if valor_irs<0:
        valor_irs = 0
    else:
        valor_irs = valor_irs
    renumeracao_final = renumeracao - valor_irs


    ### SINTESE DE CARACTERISTICAS ###

    escrever_renumeracao = tk.CTkLabel(janela_reforma_n, text=("Ordenado Base: {} €" .format(ordenado1)), font=("Segoe UI", 20)).place(x=150, y=150)
    escrever_regime = tk.CTkLabel(janela_reforma_n, text=("Regime: Pensionista"), font=("Segoe UI", 20)).place(x=150, y=200)
    escrever_fiscal = tk.CTkLabel(janela_reforma_n, text = ("Situação Fiscal: Solteiro ou Casado 2 titulares"), font=("Segoe UI", 20)).place(x=150,y=250)
    escrever_invalidez = tk.CTkLabel(janela_reforma_n, text=("Invalidez ou incapacidade: Sim"), font=("Segoe UI", 20)).place(x=150, y=300)

### APRESENTAÇÃO DOS VALORES ###
    texto_descontos = tk.CTkLabel(janela_reforma_n, text=("Resumo dos descontos"), font=("Segoe UI", 20)) .place(x=879, y=150)
    texto_valor = tk.CTkLabel(janela_reforma_n, text=("Valor tributável:{:.2f}€ " .format(renumeracao)), font=("Segoe UI", 20)).place(x=879 , y=200)
    texto_irs = tk.CTkLabel(janela_reforma_n, text=("Retenção na fonte: {:.2f}€" .format(valor_irs)), font=("Segoe UI", 20)).place(x=879 , y=250)
    valor_final = tk.CTkLabel(janela_reforma_n, text=( "Valor após descontos: {:.2f}€" .format(renumeracao_final)), font=("Segoe UI", 20), bg_color = "red").place(x=879 , y=350)

### FINAL - SAIR OU HISTORICO ###
    decidir_historico = tk.CTkLabel(janela_reforma_n, text=("Deseja adicionar está simulação ao histórico?" ), font=("Segoe UI", 20)).place(x=879, y=500)
    select_tabela_a = tk.CTkButton(janela_reforma_n, text="Sim",command=lambda:historico_pensao(situacao_fiscal, invalidez, renumeracao, valor_irs,  renumeracao_final),font=("Segoe UI", 20)).place(x=879, y=550)
    select_tabela_b = tk.CTkButton(janela_reforma_n, text="Não",command=lambda: reiniciar_programa(),font=("Segoe UI", 20)).place(x=1079, y=550)

def pensionista_2t_solteiro(janela_reformado_solteiro):
    situacao_fiscal = 1
    valor_irs=0
    invalidez = 1

    janela_reformado_solteiro.withdraw()
    janela_reforma_n = tk.CTkToplevel()
    janela_reforma_n.geometry("1400x700")
    janela_reforma_n.title( "Simulação do ordenado liquido - Pensionista - Solteiro ou Casado 2 Titulares - Resultado Final")
    texto_topo = tk.CTkLabel(janela_reforma_n, text="Simulação do ordenado liquido\nPensionista\nSolteiro ou Casado 2 Titulares\nResultado Final", font=("Segoe UI", 20)).place(x=550, y=0)
    renumeracao = float(renumera_log[0])
    ordenado1=renumeracao


    valor_irs, parcela_abater, taxa, renumeracao_liquida = pensao_solteiro_casado_2t(renumeracao)
    if valor_irs<0:
        valor_irs = 0
    else:
        valor_irs = valor_irs
    renumeracao_final = renumeracao - valor_irs


    ### SINTESE DE CARACTERISTICAS ###

    escrever_renumeracao = tk.CTkLabel(janela_reforma_n, text=("Ordenado Base: {} €" .format(ordenado1)), font=("Segoe UI", 20)).place(x=150, y=150)
    escrever_regime = tk.CTkLabel(janela_reforma_n, text=("Regime: Pensionista"), font=("Segoe UI", 20)).place(x=150, y=200)
    escrever_fiscal = tk.CTkLabel(janela_reforma_n, text = ("Situação Fiscal: Solteiro ou Casado 2 titulares"), font=("Segoe UI", 20)).place(x=150,y=250)
    escrever_invalidez = tk.CTkLabel(janela_reforma_n, text=("Invalidez ou incapacidade: Não"), font=("Segoe UI", 20)).place(x=150, y=300)

### APRESENTAÇÃO DOS VALORES ###
    texto_descontos = tk.CTkLabel(janela_reforma_n, text=("Resumo dos descontos"), font=("Segoe UI", 20)) .place(x=879, y=150)
    texto_valor = tk.CTkLabel(janela_reforma_n, text=("Valor tributável:{:.2f}€ " .format(renumeracao)), font=("Segoe UI", 20)).place(x=879 , y=200)
    texto_irs = tk.CTkLabel(janela_reforma_n, text=("Retenção na fonte: {:.2f}€" .format(valor_irs)), font=("Segoe UI", 20)).place(x=879 , y=250)
    valor_final = tk.CTkLabel(janela_reforma_n, text=( "Valor após descontos: {:.2f}€" .format(renumeracao_final)), font=("Segoe UI", 20), bg_color = "red").place(x=879 , y=350)

### FINAL - SAIR OU HISTORICO ###
    decidir_historico = tk.CTkLabel(janela_reforma_n, text=("Deseja adicionar está simulação ao histórico?" ), font=("Segoe UI", 20)).place(x=879, y=500)
    select_tabela_a = tk.CTkButton(janela_reforma_n, text="Sim",command=lambda: historico_pensao(situacao_fiscal, invalidez, renumeracao, valor_irs,  renumeracao_final),font=("Segoe UI", 20)).place(x=879, y=550)
    select_tabela_b = tk.CTkButton(janela_reforma_n, text="Não",command=lambda: reiniciar_programa(),font=("Segoe UI", 20)).place(x=1079, y=550)


def reformado_solteiro_2t(janela_reforma, pedir_renumeracao_base):
    janela_reforma.withdraw()
    renumera_log.append(pedir_renumeracao_base.get())
    janela_reformado_solteiro=tk.CTkToplevel()
    janela_reformado_solteiro.title("Simulação do ordenado liquido - Pensionista - Solteiro ou Casado: 2 Titulares")
    janela_reformado_solteiro.geometry("1400x700")
    texto_topo = tk.CTkLabel(janela_reformado_solteiro, text = "Simulação do ordenado liquido\nPensionista\nSolteiro ou Casado: 2 Titulares", font = ("Segoe UI", 20)) .place(x=560, y=0)

    texto_invalidez= tk.CTkLabel(janela_reformado_solteiro, text = "Possui algum tipo de invalidez (deficiencia)?", font = ("Segoe UI",20)) .place(x=524, y=200)
    sim_invalidez = tk.CTkButton(janela_reformado_solteiro, text = "Sim", font=("Segoe UI",20), command = lambda: pensionista_2t_solteiro_invalidez(janela_reformado_solteiro)). place(x = 626, y=250)
    nao_invalidez = tk.CTkButton(janela_reformado_solteiro, text = "Não", font=("Segoe UI",20), command=lambda:pensionista_2t_solteiro(janela_reformado_solteiro)). place(x=626, y=300)
    sim_invalidez_fa = tk.CTkButton(janela_reformado_solteiro, text="Sim, das forças armadas", font=("Sego UI", 20), command=lambda: pensionista_2t_solteiro_invalidez_fa(janela_reformado_solteiro)).place(x=626, y=350)

########################################################################################################################################

def pensionista_1t_invalidez_fa(janela_reformado_1t):
    situacao_fiscal = 2
    valor_irs = 0
    invalidez = 3

    janela_reformado_1t.withdraw()
    janela_reforma_n = tk.CTkToplevel()
    janela_reforma_n.geometry("1400x700")
    janela_reforma_n.title("Simulação do ordenado liquido - Pensionista - Casado: 1 Titular - Resultado Final")
    texto_topo = tk.CTkLabel(janela_reforma_n,text="Simulação do ordenado liquido\nPensionista\nCasado: 1 Titular\nResultado Final", font=("Segoe UI", 20)).place(x=550, y=0)
    renumeracao = float(renumera_log[0])
    ordenado1 = renumeracao

    valor_irs, parcela_abater, taxa, renumeracao_liquida = pensao_casado_1t_deficiente_fa(renumeracao)
    if valor_irs < 0:
        valor_irs = 0
    else:
        valor_irs = valor_irs
    renumeracao_final = renumeracao - valor_irs

    ### SINTESE DE CARACTERISTICAS ###

    escrever_renumeracao = tk.CTkLabel(janela_reforma_n, text=("Ordenado Base: {} €".format(ordenado1)),font=("Segoe UI", 20)).place(x=150, y=150)
    escrever_regime = tk.CTkLabel(janela_reforma_n, text=("Regime: Pensionista"), font=("Segoe UI", 20)).place(x=150, y=200)
    escrever_fiscal = tk.CTkLabel(janela_reforma_n, text=("Situação Fiscal: Casado 1 titular"), font=("Segoe UI", 20)).place(x=150, y=250)
    escrever_invalidez = tk.CTkLabel(janela_reforma_n, text=("Invalidez ou incapacidade: Sim, das forças armadas"), font=("Segoe UI", 20)).place(x=150, y=300)

    ### APRESENTAÇÃO DOS VALORES ###
    texto_descontos = tk.CTkLabel(janela_reforma_n, text=("Resumo dos descontos"), font=("Segoe UI", 20)).place(x=879, y=150)
    texto_valor = tk.CTkLabel(janela_reforma_n, text=("Valor tributável:{:.2f}€ ".format(renumeracao)), font=("Segoe UI", 20)).place(x=879, y=200)
    texto_irs = tk.CTkLabel(janela_reforma_n, text=("Retenção na fonte: {:.2f}€".format(valor_irs)), font=("Segoe UI", 20)).place(x=879, y=250)
    valor_final = tk.CTkLabel(janela_reforma_n, text=("Valor após descontos: {:.2f}€".format(renumeracao_final)),font=("Segoe UI", 20), bg_color="red").place(x=879, y=350)

### FINAL - SAIR OU HISTORICO ###
    decidir_historico = tk.CTkLabel(janela_reforma_n, text=("Deseja adicionar está simulação ao histórico?"),font=("Segoe UI", 20)).place(x=879, y=500)
    select_tabela_a = tk.CTkButton(janela_reforma_n, text="Sim", command=lambda: historico_pensao(situacao_fiscal, invalidez, renumeracao, valor_irs,  renumeracao_final),font=("Segoe UI", 20)).place(x=879, y=550)
    select_tabela_b = tk.CTkButton(janela_reforma_n, text="Não", command=lambda: reiniciar_programa(),font=("Segoe UI", 20)).place(x=1079, y=550)

def pensionista_1t_invalidez(janela_reformado_1t):
    situacao_fiscal = 2
    valor_irs = 0
    invalidez = 2

    janela_reformado_1t.withdraw()
    janela_reforma_n = tk.CTkToplevel()
    janela_reforma_n.geometry("1400x700")
    janela_reforma_n.title("Simulação do ordenado liquido - Pensionista - Casado 1 Titular - Resultado Final")
    texto_topo = tk.CTkLabel(janela_reforma_n, text="Simulação do ordenado liquido\nPensionista\nSolteiro ou Casado 2 Titulares\nResultado Final", font=("Segoe UI", 20)).place(x=550, y=0)
    renumeracao = float(renumera_log[0])
    ordenado1 = renumeracao

    valor_irs, parcela_abater, taxa, renumeracao_liquida = pensao_casado_1t_deficiente(renumeracao)
    if valor_irs < 0:
        valor_irs = 0
    else:
        valor_irs = valor_irs
    renumeracao_final = renumeracao - valor_irs

### SINTESE DE CARACTERISTICAS ###
    escrever_renumeracao = tk.CTkLabel(janela_reforma_n, text=("Ordenado Base: {} €".format(ordenado1)),font=("Segoe UI", 20)).place(x=150, y=150)
    escrever_regime = tk.CTkLabel(janela_reforma_n, text=("Regime: Pensionista"), font=("Segoe UI", 20)).place(x=150, y=200)
    escrever_fiscal = tk.CTkLabel(janela_reforma_n, text=("Situação Fiscal: Casado 1 titular"), font=("Segoe UI", 20)).place(x=150, y=250)
    escrever_invalidez = tk.CTkLabel(janela_reforma_n, text=("Invalidez ou incapacidade: Sim"), font=("Segoe UI", 20)).place(x=150, y=300)

### APRESENTAÇÃO DOS VALORES ###
    texto_descontos = tk.CTkLabel(janela_reforma_n, text=("Resumo dos descontos"), font=("Segoe UI", 20)).place(x=879, y=150)
    texto_valor = tk.CTkLabel(janela_reforma_n, text=("Valor tributável:{:.2f}€ ".format(renumeracao)), font=("Segoe UI", 20)).place(x=879, y=200)
    texto_irs = tk.CTkLabel(janela_reforma_n, text=("Retenção na fonte: {:.2f}€".format(valor_irs)), font=("Segoe UI", 20)).place(x=879, y=250)
    valor_final = tk.CTkLabel(janela_reforma_n, text=("Valor após descontos: {:.2f}€".format(renumeracao_final)),font=("Segoe UI", 20), bg_color="red").place(x=879, y=350)

### FINAL - SAIR OU HISTORICO ###
    decidir_historico = tk.CTkLabel(janela_reforma_n, text=("Deseja adicionar está simulação ao histórico?"), font=("Segoe UI", 20)).place(x=879, y=500)
    select_tabela_a = tk.CTkButton(janela_reforma_n, text="Sim", command=lambda: historico_pensao(situacao_fiscal, invalidez, renumeracao, valor_irs,  renumeracao_final), font=("Segoe UI", 20)).place(x=879, y=550)
    select_tabela_b = tk.CTkButton(janela_reforma_n, text="Não", command=lambda: reiniciar_programa(), font=("Segoe UI", 20)).place(x=1079, y=550)

def pensionista_1t(janela_reformado_1t):
    situacao_fiscal = 2
    valor_irs = 0
    invalidez = 1

    janela_reformado_1t.withdraw()
    janela_reforma_n = tk.CTkToplevel()
    janela_reforma_n.geometry("1400x700")
    janela_reforma_n.title("Simulação do ordenado liquido - Pensionista - Casado 1 Titular - Resultado Final")
    texto_topo = tk.CTkLabel(janela_reforma_n, text="Simulação do ordenado liquido\nPensionista\nCasado: 1 Titular\nResultado Final", font=("Segoe UI", 20)).place(x=550, y=0)
    renumeracao = float(renumera_log[0])
    ordenado1 = renumeracao

    valor_irs, parcela_abater, taxa, renumeracao_liquida = pensao_casado_1t(renumeracao)
    if valor_irs < 0:
        valor_irs = 0
    else:
        valor_irs = valor_irs
    renumeracao_final = renumeracao - valor_irs

### SINTESE DE CARACTERISTICAS ###

    escrever_renumeracao = tk.CTkLabel(janela_reforma_n, text=("Ordenado Base: {} €".format(ordenado1)), font=("Segoe UI", 20)).place(x=150, y=150)
    escrever_regime = tk.CTkLabel(janela_reforma_n, text=("Regime: Pensionista"), font=("Segoe UI", 20)).place(x=150, y=200)
    escrever_fiscal = tk.CTkLabel(janela_reforma_n, text=("Situação Fiscal: Casado 1 titular"), font=("Segoe UI", 20)).place(x=150, y=250)
    escrever_invalidez = tk.CTkLabel(janela_reforma_n, text=("Invalidez ou incapacidade: Não"),font=("Segoe UI", 20)).place(x=150, y=300)

### APRESENTAÇÃO DOS VALORES ###
    texto_descontos = tk.CTkLabel(janela_reforma_n, text=("Resumo dos descontos"), font=("Segoe UI", 20)).place(x=879, y=150)
    texto_valor = tk.CTkLabel(janela_reforma_n, text=("Valor tributável:{:.2f}€ ".format(renumeracao)), font=("Segoe UI", 20)).place(x=879, y=200)
    texto_irs = tk.CTkLabel(janela_reforma_n, text=("Retenção na fonte: {:.2f}€".format(valor_irs)), font=("Segoe UI", 20)).place(x=879, y=250)
    valor_final = tk.CTkLabel(janela_reforma_n, text=("Valor após descontos: {:.2f}€".format(renumeracao_final)), font=("Segoe UI", 20), bg_color="red").place(x=879, y=350)

### FINAL - SAIR OU HISTORICO ###
    decidir_historico = tk.CTkLabel(janela_reforma_n, text=("Deseja adicionar está simulação ao histórico?"),font=("Segoe UI", 20)).place(x=879, y=500)
    select_tabela_a = tk.CTkButton(janela_reforma_n, text="Sim",  command=lambda: historico_pensao(situacao_fiscal, invalidez, renumeracao, valor_irs,  renumeracao_final), font=("Segoe UI", 20)) .place(x=879, y=550)
    select_tabela_b = tk.CTkButton(janela_reforma_n, text="Não", command=lambda: reiniciar_programa(), font=("Segoe UI", 20)).place(x=1079, y=550)

def reformado_casado_1t(janela_reforma, pedir_renumeracao_base):
    janela_reforma.withdraw()
    renumera_log.append(pedir_renumeracao_base.get())
    janela_reformado_1t = tk.CTkToplevel()
    janela_reformado_1t.title("Simulação do ordenado liquido - Pensionista - Casado: 1 Titular")
    janela_reformado_1t.geometry("1400x700")
    texto_topo = tk.CTkLabel(janela_reformado_1t, text="Simulação do ordenado liquido\nPensionista\nCasado: 1 Titulares", font=("Segoe UI", 20)).place(x=560, y=0)
    texto_invalidez = tk.CTkLabel(janela_reformado_1t, text="Possui algum tipo de invalidez (deficiencia)?", font=("Segoe UI", 20)).place(x=524, y=200)
    sim_invalidez = tk.CTkButton(janela_reformado_1t, text="Sim", font=("Segoe UI", 20), command=lambda:pensionista_1t_invalidez_fa(janela_reformado_1t)).place(x=626, y=250)
    nao_invalidez = tk.CTkButton(janela_reformado_1t, text="Não", font=("Segoe UI", 20), command=lambda: pensionista_1t(janela_reformado_1t)).place(x=626, y=300)
    sim_invalidez_fa = tk.CTkButton(janela_reformado_1t, text="Sim, das forças armadas", font=("Sego UI", 20),command=lambda: pensionista_1t(janela_reformado_1t)).place(x=626, y=350)

############################################################################################################################################


def pensionista(janela_dados):
    janela_dados.withdraw()
    janela_reforma = tk.CTkToplevel()
    janela_reforma.title("Simulação do ordenado liquido - Pensionista")
    janela_reforma.geometry("1400x700")
    texto_topo = tk.CTkLabel(janela_reforma, text = "Simulação do Ordenado Liquido\nPensionista", font=("Segoe UI", 20)) .place(x= 550, y=0)
    texto_renumeracao_base = tk.CTkLabel(janela_reforma, text = "Insira a sua renumeração base", font = ("Segoe UI", 20)) .place(x=569, y=100)
    pedir_renumeracao_base = tk.CTkEntry(janela_reforma, placeholder_text = "Renumeração base", font = ("Segoe UI",20))
    pedir_renumeracao_base.place(x=616, y=150)
    texto_situacao_fiscal= tk.CTkLabel(janela_reforma, text = "Selecione a sua situação fiscal", font=("Segoe UI", 20)) .place(x=560,y=200)
    botao_solteiro = tk.CTkButton(janela_reforma, text = "Solteiro", font=("Segoe UI", 20), command=lambda: reformado_solteiro_2t(janela_reforma, pedir_renumeracao_base) ).place(x=616, y=250)
    botao_casado_1t = tk.CTkButton(janela_reforma, text = "Casado - 1 Titular", font=("Segoe UI", 20), command=lambda: reformado_casado_1t(janela_reforma, pedir_renumeracao_base)) .place(x=610, y=300)
    botao_casado_2t = tk.CTkButton(janela_reforma, text="Casado - 2 Titulares", command= lambda:reformado_solteiro_2t(janela_reforma, pedir_renumeracao_base), font=("Segoe UI", 20)).place(x=600, y=350)



def ordenado(inicio):
    inicio.withdraw()
    janela_dados =tk.CTkToplevel()
    janela_dados.title ("Simulação do Ordenado Líquido")
    janela_dados.geometry("1400x700")
    texto_topo= tk.CTkLabel(janela_dados, text="Simulação do Ordenado Líquido", font=("Segoe UI", 20))  .place(x=550, y=0)

    texto_regime = tk.CTkLabel(janela_dados, text="Selecione o regime: ", font = ("Segoe UI", 20)) .place(x=610,y=150)

    escolher_td = tk.CTkButton(janela_dados, text="Trabalhador dependente", command=lambda: dependente(janela_dados), font=("Segoe UI", 20)).place(x=578, y=200)
    escolher_pensionista = tk.CTkButton(janela_dados, text="Pensionista", command=lambda: pensionista(janela_dados), font=("Segoe UI", 20)).place(x=627, y=270)


    janela_dados.mainloop()

##########################################
def historico_irs(quociente_familiar, rendimento_conjunto,dependentes, deducoes_coleta,coleta_final):
    data_atual = datetime.today().date()
    data_atual_formatada = "{}/{}/{}".format(data_atual.day, data_atual.month, data_atual.year)
    hora_atual = datetime.now().time()
    f = open("historico.txt", "a+")
    f.write("--- SIMULAÇÃO DO IMPOSTO SOBRE OS RENDIMENTOS DE PESSOAS SINGULARES 2023 ---\n")
    f.write("Simulação realizada no dia {} ás {}\n".format(data_atual_formatada, hora_atual))
    f.write(" --- Informações ---\n")
    if quociente_familiar == 1:
        f.write("Situação Fiscal: Solteiro \n")
    else:
        f.write("Situação Fiscal: Casado\n")
    f.write("Rendimento Global: {} €\n" .format(rendimento_conjunto))
    f.write("Dependentes: {}\n".format(dependentes))
    f.write("Deduções á coleta: {:.2f} €\n" .format(deducoes_coleta))
    f.write("--- Resultado ---\n")
    if coleta_final < 0:
        f.write("Resultado: Receber :{:.2f}€ \n" .format(abs(coleta_final)))
    elif coleta_final>0:
        f.write( "Resultado: Pagar {:.2f}€\n" .format(coleta_final))
    else:
        f.write("Resultado: ISENTO\n" .format(coleta_final))

    f.write("----------------------------------------------------------------\n")
    f.close()
    os.system(f'start notepad {historico}')
    reiniciar_programa()

def irs_solteiros_resultado(janela_deducoes, pedir_automovel,pedir_gerais_familiares, pedir_saude,  pedir_educacao, pedir_habitacao,pedir_lares,pedir_moto, pedir_restaurantes, pedir_cabeleireiros, pedir_veterinario, pedir_transportes, pedir_ginasios, pedir_jornais):
    dependentes = int(dependentes_log[0])
    valor_ss1 = float(ss_log[0])
    quociente_familiar = 1
    rendimento_anual_a=renumeracao_log[0]
    retencoes_fonte_a = retencao_log[0]
    automoveis = float(pedir_automovel.get())
    gerais_familiares = float(pedir_gerais_familiares.get())
    saude = float(pedir_saude.get())
    educacao = float(pedir_educacao.get())
    habitacao = float(pedir_habitacao.get())
    lares = float(pedir_lares.get())
    motociclos = float(pedir_moto.get())
    restauracao = float(pedir_restaurantes.get())
    cabeleireiros = float(pedir_cabeleireiros.get())
    veterinarios = float(pedir_veterinario.get())
    transportes = float(pedir_transportes.get())
    ginasios = float(pedir_ginasios.get())
    jornais = float(pedir_jornais.get())
    valor_ss2=0
    rendimento_anual_b = 0
    retencoes_fonte_b = 0
    janela_deducoes.withdraw()
    janela_casados_resultados = tk.CTkToplevel()
    janela_casados_resultados.title("Simulação do Imposto sobre o Rendimento de Pessoas Singulares - Solteiro")
    janela_casados_resultados.geometry("1400x700")
    texto_topo = tk.CTkLabel(janela_casados_resultados, text="Simulação do Imposto sobre o Rendimento de Pessoas Singulares\nSolteiro", font=("Segoe UI", 20)).place(x=445, y=0)
    coleta_final, rendimento_conjunto, deducoes_coleta = irs.irs(gerais_familiares, valor_ss1, valor_ss2, quociente_familiar, dependentes, rendimento_anual_a, rendimento_anual_b, saude, educacao, habitacao, lares, automoveis, motociclos, restauracao, cabeleireiros, veterinarios, transportes, ginasios, jornais,retencoes_fonte_a, retencoes_fonte_b)

    ### SINTESE DE CARACTERISTICAS ###

    escrever_renumeracao = tk.CTkLabel(janela_casados_resultados, text=("Rendimento Global: {:.2f} €" .format(rendimento_conjunto)), font=("Segoe UI", 20)).place(x=150, y=150)

    escrever_fiscal = tk.CTkLabel(janela_casados_resultados, text = ("Situação Fiscal: Solteiro"), font=("Segoe UI", 20)).place(x=150,y=200)
    escrever_dependentes = tk.CTkLabel(janela_casados_resultados, text=("Dependentes: {}".format(dependentes)), font=("Segoe UI", 20)).place(x=150, y=250)
    escrever_deducoes = tk.CTkLabel(janela_casados_resultados, text=("Deduções á coleta: {:.2f} €" .format(deducoes_coleta)), font=("Segoe UI", 20)).place(x=150, y=300)

    if coleta_final < 0:
        texto_valor = tk.CTkLabel(janela_casados_resultados, text=("Resultado: Receber {:.2f}€ " .format(abs(coleta_final))), font=("Segoe UI", 20), bg_color = "red").place(x=879 , y=300)
    elif coleta_final>0:
        texto_valor= tk.CTkLabel(janela_casados_resultados, text=( "Resultado: Pagar {:.2f}€" .format(coleta_final)), font=("Segoe UI", 20), bg_color = "red").place(x=879 , y=300)
    else:
        texto_valor = tk.CTkLabel(janela_casados_resultados, text=( "Resultado: ISENTO" .format(coleta_final)), font=("Segoe UI", 20), bg_color = "red").place(x=879 , y=300)

### FINAL - SAIR OU HISTORICO ###
    decidir_historico = tk.CTkLabel(janela_casados_resultados, text=("Deseja adicionar está simulação ao histórico?" ), font=("Segoe UI", 20)).place(x=879, y=500)
    select_tabela_a = tk.CTkButton(janela_casados_resultados, text="Sim",font=("Segoe UI", 20), command=lambda: historico_irs(quociente_familiar, rendimento_conjunto,dependentes, deducoes_coleta,coleta_final)).place(x=879, y=550)
    select_tabela_b = tk.CTkButton(janela_casados_resultados, text="Não",command=lambda: reiniciar_programa(),font=("Segoe UI", 20)).place(x=1079, y=550)



def irs_casados_resultado(janela_deducoes, pedir_automovel,pedir_gerais_familiares, pedir_saude,  pedir_educacao, pedir_habitacao,pedir_lares,pedir_moto, pedir_restaurantes, pedir_cabeleireiros, pedir_veterinario, pedir_transportes, pedir_ginasios, pedir_jornais):
    dependentes = int(dependentes_log[0])
    valor_ss1 = float(ss_log[0])
    valor_ss2 = float(ss_log[1])
    quociente_familiar = 2
    rendimento_anual_a=renumeracao_log[0]
    rendimento_anual_b=renumeracao_log[1]
    retencoes_fonte_a = retencao_log[0]
    retencoes_fonte_b = retencao_log[1]
    automoveis = float(pedir_automovel.get())
    gerais_familiares = float(pedir_gerais_familiares.get())
    saude = float(pedir_saude.get())
    educacao = float(pedir_educacao.get())
    habitacao = float(pedir_habitacao.get())
    lares = float(pedir_lares.get())
    motociclos = float(pedir_moto.get())
    restauracao = float(pedir_restaurantes.get())
    cabeleireiros = float(pedir_cabeleireiros.get())
    veterinarios = float(pedir_veterinario.get())
    transportes = float(pedir_transportes.get())
    ginasios = float(pedir_ginasios.get())
    jornais = float(pedir_jornais.get())
    janela_deducoes.withdraw()
    janela_casados_resultados = tk.CTkToplevel()
    janela_casados_resultados.title("Simulação do Imposto sobre o Rendimento de Pessoas Singulares - Casado")
    janela_casados_resultados.geometry("1400x700")
    texto_topo = tk.CTkLabel(janela_casados_resultados, text="Simulação do Imposto sobre o Rendimento de Pessoas Singulares\nCasado", font=("Segoe UI", 20)).place(x=445, y=0)
    coleta_final, rendimento_conjunto, deducoes_coleta = irs.irs(gerais_familiares, valor_ss1, valor_ss2, quociente_familiar, dependentes, rendimento_anual_a, rendimento_anual_b, saude, educacao, habitacao, lares, automoveis, motociclos, restauracao, cabeleireiros, veterinarios, transportes, ginasios, jornais,retencoes_fonte_a, retencoes_fonte_b)

    ### SINTESE DE CARACTERISTICAS ###

    escrever_renumeracao = tk.CTkLabel(janela_casados_resultados, text=("Rendimento Global: {} €" .format(rendimento_conjunto)), font=("Segoe UI", 20)).place(x=150, y=150)

    escrever_fiscal = tk.CTkLabel(janela_casados_resultados, text = ("Situação Fiscal: Casado"), font=("Segoe UI", 20)).place(x=150,y=200)
    escrever_dependentes = tk.CTkLabel(janela_casados_resultados, text=("Dependentes: {}".format(dependentes)), font=("Segoe UI", 20)).place(x=150, y=250)
    escrever_deducoes = tk.CTkLabel(janela_casados_resultados, text=("Deduções á coleta: {:.2f} €" .format(deducoes_coleta)), font=("Segoe UI", 20)).place(x=150, y=300)

    if coleta_final < 0:
        texto_valor = tk.CTkLabel(janela_casados_resultados, text=("Resultado: Receber {:.2f}€ " .format(abs(coleta_final))), font=("Segoe UI", 20), bg_color = "red").place(x=879 , y=300)
    elif coleta_final>0:
        texto_valor= tk.CTkLabel(janela_casados_resultados, text=( "Resultado: Pagar {:.2f}€" .format(coleta_final)), font=("Segoe UI", 20), bg_color = "red").place(x=879 , y=300)
    else:
        texto_valor = tk.CTkLabel(janela_casados_resultados, text=( "Resultado: ISENTO" .format(coleta_final)), font=("Segoe UI", 20), bg_color = "red").place(x=879 , y=300)

### FINAL - SAIR OU HISTORICO ###
    decidir_historico = tk.CTkLabel(janela_casados_resultados, text=("Deseja adicionar está simulação ao histórico?" ), font=("Segoe UI", 20)).place(x=879, y=500)
    select_tabela_a = tk.CTkButton(janela_casados_resultados, text="Sim",font=("Segoe UI", 20), command=lambda: historico_irs(quociente_familiar, rendimento_conjunto,dependentes, deducoes_coleta,coleta_final)).place(x=879, y=550)
    select_tabela_b = tk.CTkButton(janela_casados_resultados, text="Não",command=lambda: reiniciar_programa(),font=("Segoe UI", 20)).place(x=1079, y=550)




def deducoes_solteiro(janela_rendimento_a, pedir_rendimento_a, pedir_ss_a, pedir_rentencao_a):
    renumeracao_log.append(float(pedir_rendimento_a.get()))
    retencao_log.append(float(pedir_rentencao_a.get()))
    ss_log.append(float(pedir_ss_a.get()))
    janela_rendimento_a.withdraw()
    janela_deducoes = tk.CTkToplevel()
    janela_deducoes.title("Simulação do Imposto sobre o Rendimento de Pessoas Singulares - Solteiro")
    janela_deducoes.geometry("1400x700")
    texto_topo = tk.CTkLabel(janela_deducoes, text="Preencha as caixas com os valores das deduções especificas",    font=("Segoe UI", 20)).place(x=445, y=0)

    automovel = tk.CTkImage(dark_image =Image.open("Automoveis.png"), size = (100,100))
    imagem_automovel = tk.CTkLabel(janela_deducoes, image = automovel, text = "") .place(x=300, y=50)
    pedir_automovel = tk.CTkEntry(janela_deducoes, placeholder_text = ("Valor"), font = ("Segoe UI", 20 ))
    pedir_automovel.place(x=280, y=150)
    gerais_familiares = tk.CTkImage(dark_image =Image.open("despesas_gerais.png"), size = (100,100))
    imagem_gerais_familiares = tk.CTkLabel(janela_deducoes, image = gerais_familiares, text = "") .place(x=630, y=50)
    pedir_gerais_familiares = tk.CTkEntry(janela_deducoes, placeholder_text = ("Valor"), font = ("Segoe UI", 20 ))
    pedir_gerais_familiares.place(x=610, y=150)
    saude = tk.CTkImage(dark_image =Image.open("Saude.png"), size = (100,100))
    imagem_saude = tk.CTkLabel(janela_deducoes, image = saude, text = "") .place(x=1000, y=50)
    pedir_saude = tk.CTkEntry(janela_deducoes, placeholder_text = ("Valor"), font = ("Segoe UI", 20 ))
    pedir_saude.place(x=980, y=150)

    educacao= tk.CTkImage(dark_image =Image.open("Educacao.png"), size = (100,100))
    imagem_educacao = tk.CTkLabel(janela_deducoes, image = educacao, text = "") .place(x=300, y=200)
    pedir_educacao = tk.CTkEntry(janela_deducoes, placeholder_text = ("Valor"), font = ("Segoe UI", 20 ))
    pedir_educacao.place(x=280, y=300)
    habitacao = tk.CTkImage(dark_image=Image.open("Casa.png"), size=(100, 100))
    imagem_habitacao = tk.CTkLabel(janela_deducoes, image=habitacao, text="").place(x=630, y=200)
    pedir_habitacao = tk.CTkEntry(janela_deducoes, placeholder_text=("Valor"), font=("Segoe UI", 20))
    pedir_habitacao.place(x=610, y=300)
    lares = tk.CTkImage(dark_image=Image.open("Lares.png"), size=(100, 100))
    imagem_lares = tk.CTkLabel(janela_deducoes, image=lares, text="").place(x=1000, y=200)
    pedir_lares = tk.CTkEntry(janela_deducoes, placeholder_text=("Valor"), font=("Segoe UI", 20))
    pedir_lares.place(x=980, y=300)


    moto= tk.CTkImage(dark_image =Image.open("Motociclos.png"), size = (100,100))
    imagem_moto = tk.CTkLabel(janela_deducoes, image = moto, text = "") .place(x=300, y=350)
    pedir_moto = tk.CTkEntry(janela_deducoes, placeholder_text = ("Valor"), font = ("Segoe UI", 20 ))
    pedir_moto.place(x=280, y=450)
    restaurantes = tk.CTkImage(dark_image=Image.open("restauracao-alojamento (2).png"), size=(100, 100))
    imagem_restaurantes = tk.CTkLabel(janela_deducoes, image=restaurantes, text="").place(x=630, y=350)
    pedir_restaurantes = tk.CTkEntry(janela_deducoes, placeholder_text=("Valor"), font=("Segoe UI", 20))
    pedir_restaurantes.place(x=610, y=450)
    cabeleireiros = tk.CTkImage(dark_image=Image.open("cabeleireiros.png"), size=(100, 100))
    imagem_cabeleireiros = tk.CTkLabel(janela_deducoes, image=cabeleireiros, text="").place(x=1000, y=350)
    pedir_cabeleireiros = tk.CTkEntry(janela_deducoes, placeholder_text=("Valor"), font=("Segoe UI", 20))
    pedir_cabeleireiros.place(x=980, y=450)

    veterinario = tk.CTkImage(dark_image =Image.open("Veterinario.png"), size = (100,100))
    imagem_veterinario = tk.CTkLabel(janela_deducoes, image = veterinario, text = "") .place(x=80, y=500)
    pedir_veterinario = tk.CTkEntry(janela_deducoes, placeholder_text = ("Valor"), font = ("Segoe UI", 20 ))
    pedir_veterinario.place(x=60, y=600)
    transportes = tk.CTkImage(dark_image=Image.open("Passes Mensais.png"), size=(100, 100))
    imagem_transportes = tk.CTkLabel(janela_deducoes, image=transportes, text="").place(x=460, y=500)
    pedir_transportes = tk.CTkEntry(janela_deducoes, placeholder_text=("Valor"), font=("Segoe UI", 20))
    pedir_transportes.place(x=440, y=600)
    ginasios = tk.CTkImage(dark_image=Image.open("Ginasios.png"), size=(100, 100))
    imagem_ginasios = tk.CTkLabel(janela_deducoes, image=ginasios, text="").place(x=840, y=500)
    pedir_ginasios = tk.CTkEntry(janela_deducoes, placeholder_text=("Valor"), font=("Segoe UI", 20))
    pedir_ginasios.place(x=820, y=600)
    jornais = tk.CTkImage(dark_image=Image.open("Jornais.png"), size=(100, 100))
    imagem_jornais = tk.CTkLabel(janela_deducoes, image=jornais, text="").place(x=1180, y=500)
    pedir_jornais = tk.CTkEntry(janela_deducoes, placeholder_text=("Valor"), font=("Segoe UI", 20))
    pedir_jornais.place(x=1160, y=600)
    botao_confirmar = tk.CTkButton(janela_deducoes, text = "Confirmar", font =("Segoe UI", 20), command=lambda: irs_solteiros_resultado(janela_deducoes, pedir_automovel,pedir_gerais_familiares, pedir_saude,  pedir_educacao, pedir_habitacao,pedir_lares,pedir_moto, pedir_restaurantes, pedir_cabeleireiros, pedir_veterinario, pedir_transportes, pedir_ginasios, pedir_jornais)) .place(x=630, y= 650)


def deducoes_casados(janela_rendimento_b, pedir_rendimento_b, pedir_ss_b, pedir_rentencao_b):
    renumeracao_log.append(float(pedir_rendimento_b.get()))
    retencao_log.append(float(pedir_rentencao_b.get()))
    ss_log.append(float(pedir_ss_b.get()))
    janela_rendimento_b.withdraw()
    janela_deducoes = tk.CTkToplevel()
    janela_deducoes.title("Simulação do Imposto sobre o Rendimento de Pessoas Singulares - Casado")
    janela_deducoes.geometry("1400x700")
    texto_topo = tk.CTkLabel(janela_deducoes, text="Preencha as caixas com os valores das deduções especificas",    font=("Segoe UI", 20)).place(x=445, y=0)

    automovel = tk.CTkImage(dark_image =Image.open("Automoveis.png"), size = (100,100))
    imagem_automovel = tk.CTkLabel(janela_deducoes, image = automovel, text = "") .place(x=300, y=50)
    pedir_automovel = tk.CTkEntry(janela_deducoes, placeholder_text = ("Valor"), font = ("Segoe UI", 20 ))
    pedir_automovel.place(x=280, y=150)
    gerais_familiares = tk.CTkImage(dark_image =Image.open("despesas_gerais.png"), size = (100,100))
    imagem_gerais_familiares = tk.CTkLabel(janela_deducoes, image = gerais_familiares, text = "") .place(x=630, y=50)
    pedir_gerais_familiares = tk.CTkEntry(janela_deducoes, placeholder_text = ("Valor"), font = ("Segoe UI", 20 ))
    pedir_gerais_familiares.place(x=610, y=150)
    saude = tk.CTkImage(dark_image =Image.open("Saude.png"), size = (100,100))
    imagem_saude = tk.CTkLabel(janela_deducoes, image = saude, text = "") .place(x=1000, y=50)
    pedir_saude = tk.CTkEntry(janela_deducoes, placeholder_text = ("Valor"), font = ("Segoe UI", 20 ))
    pedir_saude.place(x=980, y=150)

    educacao= tk.CTkImage(dark_image =Image.open("Educacao.png"), size = (100,100))
    imagem_educacao = tk.CTkLabel(janela_deducoes, image = educacao, text = "") .place(x=300, y=200)
    pedir_educacao = tk.CTkEntry(janela_deducoes, placeholder_text = ("Valor"), font = ("Segoe UI", 20 ))
    pedir_educacao.place(x=280, y=300)
    habitacao = tk.CTkImage(dark_image=Image.open("Casa.png"), size=(100, 100))
    imagem_habitacao = tk.CTkLabel(janela_deducoes, image=habitacao, text="").place(x=630, y=200)
    pedir_habitacao = tk.CTkEntry(janela_deducoes, placeholder_text=("Valor"), font=("Segoe UI", 20))
    pedir_habitacao.place(x=610, y=300)
    lares = tk.CTkImage(dark_image=Image.open("Lares.png"), size=(100, 100))
    imagem_lares = tk.CTkLabel(janela_deducoes, image=lares, text="").place(x=1000, y=200)
    pedir_lares = tk.CTkEntry(janela_deducoes, placeholder_text=("Valor"), font=("Segoe UI", 20))
    pedir_lares.place(x=980, y=300)


    moto= tk.CTkImage(dark_image =Image.open("Motociclos.png"), size = (100,100))
    imagem_moto = tk.CTkLabel(janela_deducoes, image = moto, text = "") .place(x=300, y=350)
    pedir_moto = tk.CTkEntry(janela_deducoes, placeholder_text = ("Valor"), font = ("Segoe UI", 20 ))
    pedir_moto.place(x=280, y=450)
    restaurantes = tk.CTkImage(dark_image=Image.open("restauracao-alojamento (2).png"), size=(100, 100))
    imagem_restaurantes = tk.CTkLabel(janela_deducoes, image=restaurantes, text="").place(x=630, y=350)
    pedir_restaurantes = tk.CTkEntry(janela_deducoes, placeholder_text=("Valor"), font=("Segoe UI", 20))
    pedir_restaurantes.place(x=610, y=450)
    cabeleireiros = tk.CTkImage(dark_image=Image.open("cabeleireiros.png"), size=(100, 100))
    imagem_cabeleireiros = tk.CTkLabel(janela_deducoes, image=cabeleireiros, text="").place(x=1000, y=350)
    pedir_cabeleireiros = tk.CTkEntry(janela_deducoes, placeholder_text=("Valor"), font=("Segoe UI", 20))
    pedir_cabeleireiros.place(x=980, y=450)

    veterinario = tk.CTkImage(dark_image =Image.open("Veterinario.png"), size = (100,100))
    imagem_veterinario = tk.CTkLabel(janela_deducoes, image = veterinario, text = "") .place(x=80, y=500)
    pedir_veterinario = tk.CTkEntry(janela_deducoes, placeholder_text = ("Valor"), font = ("Segoe UI", 20 ))
    pedir_veterinario.place(x=60, y=600)
    transportes = tk.CTkImage(dark_image=Image.open("Passes Mensais.png"), size=(100, 100))
    imagem_transportes = tk.CTkLabel(janela_deducoes, image=transportes, text="").place(x=460, y=500)
    pedir_transportes = tk.CTkEntry(janela_deducoes, placeholder_text=("Valor"), font=("Segoe UI", 20))
    pedir_transportes.place(x=440, y=600)
    ginasios = tk.CTkImage(dark_image=Image.open("Ginasios.png"), size=(100, 100))
    imagem_ginasios = tk.CTkLabel(janela_deducoes, image=ginasios, text="").place(x=840, y=500)
    pedir_ginasios = tk.CTkEntry(janela_deducoes, placeholder_text=("Valor"), font=("Segoe UI", 20))
    pedir_ginasios.place(x=820, y=600)
    jornais = tk.CTkImage(dark_image=Image.open("Jornais.png"), size=(100, 100))
    imagem_jornais = tk.CTkLabel(janela_deducoes, image=jornais, text="").place(x=1180, y=500)
    pedir_jornais = tk.CTkEntry(janela_deducoes, placeholder_text=("Valor"), font=("Segoe UI", 20))
    pedir_jornais.place(x=1160, y=600)
    botao_confirmar = tk.CTkButton(janela_deducoes, text = "Confirmar", font =("Segoe UI", 20), command=lambda: irs_casados_resultado(janela_deducoes, pedir_automovel,pedir_gerais_familiares, pedir_saude,  pedir_educacao, pedir_habitacao,pedir_lares,pedir_moto, pedir_restaurantes, pedir_cabeleireiros, pedir_veterinario, pedir_transportes, pedir_ginasios, pedir_jornais)) .place(x=630, y= 650)
def rendimento_b_casado(janela_rendimento_a, pedir_rendimento_a, pedir_ss_a, pedir_rentencao_a):
    renumeracao_log.append(float(pedir_rendimento_a.get()))
    retencao_log.append(float(pedir_rentencao_a.get()))
    ss_log.append(float(pedir_ss_a.get()))
    janela_rendimento_a.withdraw()
    janela_rendimento_b = tk.CTkToplevel()
    janela_rendimento_b.title("Simulação do Imposto sobre o Rendimento de Pessoas Singulares - Casado")
    janela_rendimento_b.geometry("1400x700")
    texto_topo = tk.CTkLabel(janela_rendimento_b, text="Simulação do Imposto sobre o Rendimento de Pessoas Singulares\nCasado", font=("Segoe UI", 20)).place(x=445, y=0)
    texto_sujeito_b = tk.CTkLabel(janela_rendimento_b, text="SUJEITO PASSIVO B", font=("Segoe UI", 20)).place(x=615, y=150)
    texto_rendimento_b = tk.CTkLabel(janela_rendimento_b, text="Insira o valor total de todos os rendimentos deste ano:", font=("Segoe UI", 20)).place(x=493, y=200)
    pedir_rendimento_b = tk.CTkEntry(janela_rendimento_b, placeholder_text = "Valor", font=("Segoe UI", 20))
    pedir_rendimento_b.place(x=634, y=250)
    texto_retencao = tk.CTkLabel(janela_rendimento_b, text="Insira o valor total da retenção da fonte deste ano:", font=("Segoe UI", 20)).place(x=550, y=300)
    pedir_rentencao_b = tk.CTkEntry(janela_rendimento_b, placeholder_text="Valor", font=("Segoe UI", 20))
    pedir_rentencao_b.place(x=634, y=350)
    texto_ss = tk.CTkLabel(janela_rendimento_b, text="Insira o valor total da taxa social única deste ano:", font=("Segoe UI", 20)).place(x=511, y=400)
    pedir_ss_b = tk.CTkEntry(janela_rendimento_b, placeholder_text="Valor", font=("Segoe UI", 20))
    pedir_ss_b.place(x=634, y=450)
    botao_confirmar = tk.CTkButton(janela_rendimento_b, text = "Confirmar", font =("Segoe UI", 20), command=lambda: deducoes_casados(janela_rendimento_b, pedir_rendimento_b, pedir_ss_b, pedir_rentencao_b)) .place(x=634, y= 600)

def rendimento_a_casado(janela_dados,pedir_dependentes):
    dependentes_log.append(int(pedir_dependentes.get()))
    janela_dados.withdraw()
    janela_rendimento_a = tk.CTkToplevel()
    janela_rendimento_a.title("Simulação do Imposto sobre o Rendimento de Pessoas Singulares - Casado")
    janela_rendimento_a.geometry("1400x700")
    texto_topo = tk.CTkLabel(janela_rendimento_a, text="Simulação do Imposto sobre o Rendimento de Pessoas Singulares\nCasado", font=("Segoe UI", 20)).place(x=445, y=0)
    texto_sujeito_a = tk.CTkLabel(janela_rendimento_a, text="SUJEITO PASSIVO A", font=("Segoe UI", 20)).place(x=615, y=150)
    texto_rendimento_a = tk.CTkLabel(janela_rendimento_a, text="Insira o valor total de todos os rendimentos deste ano:", font=("Segoe UI", 20)).place(x=493, y=200)
    pedir_rendimento_a = tk.CTkEntry(janela_rendimento_a, placeholder_text = "Valor", font=("Segoe UI", 20))
    pedir_rendimento_a.place(x=634, y=250)
    texto_retencao = tk.CTkLabel(janela_rendimento_a, text="Insira o valor total da retenção da fonte deste ano:", font=("Segoe UI", 20)).place(x=511, y=300)
    pedir_rentencao_a = tk.CTkEntry(janela_rendimento_a, placeholder_text="Valor", font=("Segoe UI", 20))
    pedir_rentencao_a.place(x=634, y=350)
    texto_ss = tk.CTkLabel(janela_rendimento_a, text="Insira o valor total da taxa social única deste ano:", font=("Segoe UI", 20)).place(x=511, y=400)
    pedir_ss_a = tk.CTkEntry(janela_rendimento_a, placeholder_text="Valor", font=("Segoe UI", 20))
    pedir_ss_a.place(x=634, y=450)
    botao_confirmar = tk.CTkButton(janela_rendimento_a, text="Confirmar", font=("Segoe UI", 20),  command=lambda: rendimento_b_casado(janela_rendimento_a, pedir_rendimento_a, pedir_ss_a, pedir_rentencao_a)).place(x=634, y=600)

def rendimento_a_solteiro(janela_dados,pedir_dependentes):
    dependentes_log.append(int(pedir_dependentes.get()))
    janela_dados.withdraw()
    janela_rendimento_a = tk.CTkToplevel()
    janela_rendimento_a.title("Simulação do Imposto sobre o Rendimento de Pessoas Singulares - Solteiro")
    janela_rendimento_a.geometry("1400x700")
    texto_topo = tk.CTkLabel(janela_rendimento_a, text="Simulação do Imposto sobre o Rendimento de Pessoas Singulares\nSolteiro", font=("Segoe UI", 20)).place(x=445, y=0)
    texto_sujeito_a = tk.CTkLabel(janela_rendimento_a, text="SUJEITO PASSIVO A", font=("Segoe UI", 20)).place(x=615, y=150)
    texto_rendimento_a = tk.CTkLabel(janela_rendimento_a, text="Insira o valor total de todos os rendimentos deste ano:", font=("Segoe UI", 20)).place(x=493, y=200)
    pedir_rendimento_a = tk.CTkEntry(janela_rendimento_a, placeholder_text = "Valor", font=("Segoe UI", 20))
    pedir_rendimento_a.place(x=634, y=250)
    texto_retencao = tk.CTkLabel(janela_rendimento_a, text="Insira o valor total da retenção da fonte deste ano:", font=("Segoe UI", 20)).place(x=511, y=300)
    pedir_rentencao_a = tk.CTkEntry(janela_rendimento_a, placeholder_text="Valor", font=("Segoe UI", 20))
    pedir_rentencao_a.place(x=634, y=350)
    texto_ss = tk.CTkLabel(janela_rendimento_a, text="Insira o valor total da taxa social única deste ano:", font=("Segoe UI", 20)).place(x=511, y=400)
    pedir_ss_a = tk.CTkEntry(janela_rendimento_a, placeholder_text="Valor", font=("Segoe UI", 20))
    pedir_ss_a.place(x=634, y=450)
    botao_confirmar = tk.CTkButton(janela_rendimento_a, text="Confirmar", font=("Segoe UI", 20),  command=lambda: deducoes_solteiro(janela_rendimento_a, pedir_rendimento_a, pedir_ss_a, pedir_rentencao_a)).place(x=634, y=600)


def irs1(inicio):
    inicio.withdraw()
    janela_dados = tk.CTkToplevel()
    janela_dados.title("Simulação do Imposto sobre o Rendimento de Pessoas Singulares")
    janela_dados.geometry("1400x700")
    texto_topo = tk.CTkLabel(janela_dados, text="Simulação do Imposto sobre o Rendimento de Pessoas Singulares", font=("Segoe UI", 20)).place(x=445, y=0)

    texto_dependentes = tk.CTkLabel(janela_dados, text="Insira a quantidade de dependentes: ", font=("Segoe UI", 20)).place(x=568, y=150)
    pedir_dependentes = tk.CTkEntry(janela_dados, placeholder_text="Dependentes", font = ("Segoe UI", 20))
    pedir_dependentes.place(x=634, y = 200)
    texto_regime = tk.CTkLabel(janela_dados, text="Selecione a situação fiscal: ", font=("Segoe UI", 20)).place(x=606, y=350)

    escolher_solteiro = tk.CTkButton(janela_dados, text="Solteiro", font=("Segoe UI", 20), command=lambda: rendimento_a_solteiro(janela_dados,pedir_dependentes)).place(x=643, y=400)
    escolher_casado = tk.CTkButton(janela_dados, text="Casado", command=lambda: rendimento_a_casado(janela_dados,pedir_dependentes),  font=("Segoe UI", 20)).place(x=643, y=450)


########################## PAGINA INICIAL ###################################################
def inicio1():
    inicio = tk.CTk()


    inicio.title("Simulador de Impostos")
    inicio.geometry("1400x700")
    customtkinter.set_default_color_theme("dark-blue")  # Themes: "blue" (standard), "green", "dark-blue"
    customtkinter.set_appearance_mode("system")
    texto_inicial = tk.CTkLabel(inicio, text="Bem-vindo ao simulador de impostos!\nSelecione o imposto que deseja calcular para continuar.", font = ("Segoe UI", 20)) .place(x=450,y=0)


    carro1 = tk.CTkImage(dark_image =Image.open("carro2.png"), size = (300,300))
    imagem_iuc = tk.CTkLabel(inicio, image = carro1, text = "") .place(x=587, y=150)
    botao1 = tk.CTkButton(inicio, text="IUC", command=lambda:botao_menu1(inicio), font = ("Segoe UI", 20)) .place(x=660, y= 400)
    ordenado1 = tk.CTkImage(dark_image = Image.open("ordenado_liquido.png"), size = (200,200))
    imagem_ordenado = tk.CTkLabel(inicio, image = ordenado1, text = ""). place(x=273,y= 200)
    botao20 = tk.CTkButton(inicio, text ="Taxas sobre os rendimentos", font = ("Segoe UI", 20),command=lambda: ordenado(inicio))
    botao20.place(x = 236, y =400)
    botao21 = tk.CTkButton(inicio, text ="IRS", font = ("Segoe UI", 20),command=lambda: irs1(inicio))
    botao21.place(x = 990, y =400)
    botao_historico = tk.CTkButton(inicio, text = "Histórico", font = ("Segoe UI", 20), command=lambda: abrir_historico()) .place(x=20, y=650)
    irs2 = tk.CTkImage(dark_image = Image.open("irs.png"), size = (200,200))
    imagem_ordenado = tk.CTkLabel(inicio, image = irs2, text = ""). place(x=965,y= 200)


    inicio.mainloop()

inicio1()

print("Parece que tas com dificuldade em raciocionar, reconsidera reconstruir a tua base de dados")
