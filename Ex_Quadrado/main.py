from quadrado import Quadrado

def main():
    novo_1 = Quadrado(5)
    print(novo_1.retornar_valor())
    print(novo_1.area)
    novo_1.calcular_area()
    print(novo_1.area)

    lado = int(input('Informe o valor do lado: '))
    novo_1.mudar_valor(lado)
    novo_1.calcular_area()
    print(novo_1.area)

    novo_2 = Quadrado(8)
    print('Objeto 1', novo_1.retornar_valor())
    print('Objeto 2', novo_2.retornar_valor())

main()