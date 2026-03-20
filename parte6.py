with open("musica.txt", "r") as arquivo:
    tipos = arquivo.readlines()

tipos.append("\n Eurodance")

with open("musica.txt", "w") as arquivo:
    arquivo.writelines(tipos)
