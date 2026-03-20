disciplinas = ["rad", "poo", "disp moveis"]

with open ("disciplinas.txt", "w") as arquivo:
    arquivo.write("minhas disciplinas + top \n")
    for i, z in enumerate(disciplinas,1):
        arquivo.write(f'{i}. {z}\n')

with open("disciplinas.txt", 'r') as arquivo:
    print(arquivo.read())