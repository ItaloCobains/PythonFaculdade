class IMC:
    def __init__(self, peso, altura):
        self.peso = peso
        self.altura = altura

    def calcular(self):
        return self.peso / (self.altura ** 2)

    def __str__(self):
        return f'IMC: {self.calcular():.2f}'


if __name__ == '__main__':
    peso = float(input('Peso: '))
    altura = float(input('Altura: '))
    imc = IMC(peso, altura)
    print(imc)
