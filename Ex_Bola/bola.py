class Bola:
    cor = ''
    circunferencia = 0
    material = ''

    def __init__(self, cor, circunferencia, material):
        self.cor = cor
        self.circunferencia = circunferencia
        self.material = material

    def trocarCor(self, nova_cor):
        self.cor = nova_cor

    def mostrarCor(self):
        print('Cor: ', self.cor)