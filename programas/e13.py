from datetime import date


class Pessoa:
    def __init__(self: object, nome: str, idade: int) -> None:
        self.nome: str = nome
        self.idade: int = idade

    @classmethod
    def apartirAnoNascimento(cls, nome: str, ano: int):
        return cls(nome, date.today().year - ano)

    @staticmethod
    def eMaiorDeIdade(idade: int) -> bool:
        return idade >= 18


pessoa1 = Pessoa('João', 30)
pessoa2 = Pessoa.apartirAnoNascimento('Maria', 1990)
print(pessoa1.nome, pessoa1.idade)
print(pessoa2.nome, pessoa2.idade)
print(Pessoa.eMaiorDeIdade(30))
