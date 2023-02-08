class Salario:
    def __init__(self: object, base: float, bonus: float) -> None:
        self.base = base
        self.bonus = bonus

    def salario_anual(self: object) -> float:
        return self.base * 12 + self.bonus


class Empregado:
    def __init__(self: object, nome: str, idade: int, salario: Salario) -> None:
        self.nome: str = nome
        self.idade: int = idade
        self.salario_agregado: salario = salario

    def salario_total(self: object) -> float:
        return self.salario_agregado.salario_anual()


salario = Salario(1000, 1000)
empregado = Empregado('João', 30, salario)
print(empregado.salario_total())
