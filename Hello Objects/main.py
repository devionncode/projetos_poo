# Importando a classe que será utilizada 
# para criar os objetos
from pessoa import Pessoa
from veiculo import Veiculo

def main():
    print('Meu primeiro programa orientado a objetos!')

    # Instânciando um novo objeto a partir
    # da classe Pessoa e armazenando a 
    # instância na variável pessoa1
    pessoa1 = Pessoa()
    print(type(pessoa1))

    pessoa1.nome = 'Diego'
    pessoa1.idade = 29
    pessoa1.sexo = 'M'
    print('Nome: {}'.format(pessoa1.nome))
    print('Idade: {}'.format(pessoa1.idade))
    print('Sexo: {}'.format(pessoa1.sexo))

    print(pessoa1.imprimir())

    # Instânciando um objeto a partir da
    # classe Veículo, cujo construtor foi
    # sobrescrito
    veiculo = Veiculo('Gol', 'VW', 'Branca', '1997')
    print('Nome do veículo:', veiculo.nome)
    print(veiculo)

main()
