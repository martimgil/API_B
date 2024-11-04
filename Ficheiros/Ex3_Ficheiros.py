f = open('Exemplo2.txt','w+')
f.write("Olá Turma!! Estamos a trabalhar em ficheiros Python!\n")
f.write("Esquero que gostem da aula!\n")
f.write("Obrigado!\n")

f.seek(0)
print(f.read())
