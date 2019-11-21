from animal import Animal

def main():
    nome = input('Informe o nome: ')
    raca = input('Informe a raça: ')
    idade = int(input('Informe a idade: '))
    animal = Animal(nome, raca, idade)
    print(animal)

main()