precos = [200,300,400,1000,100]

with open("precos_roupas.txt", "a") as arquivo:
    for preco in precos:
        arquivo.write(str(preco) + '\n')
        print(preco)
    arquivo.write('60000' + "\n")

precos = [200,100]

with open("precos_roupas.txt", "w") as arquivo:
    for preco in precos:
        arquivo.write(str(preco) + '\n')
        print(preco)
    
