with open("teste1.txt", "w+") as arquivo:
    arquivo.write("Iai galerinha blz? \n")
    arquivo.write("Bem vindo turma a minha quinta-feira ")
    
    arquivo.seek(0)
    conteudo = arquivo.read()
    print(conteudo)

precos = [200, 100, 300, 500, 400, 600]
with open ("teste1.txt", "a") as arquivo:
    for preco in precos:
        arquivo.write(str(preco) + '\n')