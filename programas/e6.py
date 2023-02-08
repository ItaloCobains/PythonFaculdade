import numpy as np


class Raizes:
    def __init__(self: object) -> None:
        pass

    def calcular_delta(self: object, a: float, b: float, c: float) -> float:
        delta = b*b-4*a*c
        return delta

    def calcular_raizes(self: object, a: float, b: float, c: float, delta: float) -> (float | list[float] | None):
        if (delta < 0):
            return None
        elif (delta == 0):
            x = -b/(2*a)
            return x
        else:
            x1 = (-b+np.sqrt(delta))/(2*a)
            x2 = (-b-np.sqrt(delta))/(2*a)
            resultado: list[float] = [x1, x2]
            return resultado


if __name__ == '__main__':
    raizes = Raizes()
    a = float(input('a: '))
    b = float(input('b: '))
    c = float(input('c: '))
    delta = raizes.calcular_delta(a, b, c)
    print(f'Delta: {delta}')
    raiz = raizes.calcular_raizes(a, b, c, delta)
    if raiz is None:
        print('Não há raízes reais')
    elif type(raiz) == float:
        print(f'Raiz: {raiz}')
    else:
        print(f'Raízes: {raiz[0]} e {raiz[1]}')
