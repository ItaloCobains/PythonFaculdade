class Pessoa:
    def __init__(self: object, nome: str, ender: str) -> None:
        self.set_nome(nome)
        self.set_ender(ender)

    def set_nome(self: object, nome: str) -> None:
        self.nome = nome

    def set_ender(self: object, ender: str) -> None:
        self.ender = ender

    def get_nome(self: object) -> str:
        return self.nome

    def get_ender(self: object) -> str:
        return self.ender


class Profissional(Pessoa):
    def __init__(self: object, nome: str, ender: str, profissao: str) -> None:
        super().__init__(nome, ender)
        self.set_profissao(profissao)

    def set_profissao(self: object, profissao: str) -> None:
        self.profissao = profissao

    def get_profissao(self: object) -> str:
        return self.profissao


pessoa1 = Pessoa('João', 'Rua 1')
pessoa2 = Pessoa('Maria', 'Rua 2')

profissional = Profissional('José', 'Rua 3', 'Programador')

print(profissional.get_nome())
print(profissional.get_ender())
print(profissional.get_profissao())

print(pessoa1.get_nome())
print(pessoa1.get_ender())
print(pessoa2.get_nome())
print(pessoa2.get_ender())
