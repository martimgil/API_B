#criar um ficheiro e guardar informação
encoding = 'utf8'
f = open('Exemplo1.txt','w+')
f.write("Bom dia Turma!\n")
f.write("Bom fim de semana!!\n")
f.seek(0) #define a posição do cursor no inicio
print(f.read())
f.write("Hoje a Escola faz 37 anos!!!\n")
f.write("Parabéns Cristina Torres!!!\n")

f.seek(0)
print(f.read())

f.close()
