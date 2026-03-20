with open("arquivo_rad04.txt","r") as arquivo:
    print("Representação original da minha linha")
    for linha in arquivo:
        dado_da_linha = linha.strip()
        print(repr(linha))
        print(repr(dado_da_linha))

lista_de_comida = ["pizza", "feijão", "carne", "banana"]
lista_ = ','.join(lista_de_comida)

with open("lista_de_comida.txt", "w") as arquivo:
    arquivo.write(lista_)