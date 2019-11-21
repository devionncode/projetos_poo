class Quadrado:
    tamanho_lado = 0
    area = 0

    # Construtor
    def __init__(self, tamanho_lado):
        self.tamanho_lado = tamanho_lado

    def mudar_valor(self, novo_tamanho):
        self.tamanho_lado = novo_tamanho

    def retornar_valor(self):
        return self.tamanho_lado

    def calcular_area(self):
        self.area = self.tamanho_lado * self.tamanho_lado
    



    