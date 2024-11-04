encoding = 'utf8'

f=open('Exemplo1.txt','a+')

print('Posição do cursor no ficheiro', f.tell())

f.seek(0)
f.write("Olá!!\n")

print(f.read())
print('Posição do cursor no ficheiro', f.tell())

print("-------")
f.seek(20)
print(f.read())
