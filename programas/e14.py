class NomeCompleto:
    def __init__(self: object, nome: str, sobrenome: str) -> None:
        self.nome: str = nome
        self.sobrenome: str = sobrenome

    @classmethod
    def fromString(cls, texto: str) -> object:
        nome, sobrenome = map(str, texto.split(' '))
        objecto = cls(nome, sobrenome)
        return object

    @staticmethod
    def isValid(texto: str) -> bool:
        nomes = texto.split(' ')
        return len(nomes) > 1


print(NomeCompleto('João', 'Silva'))
print(NomeCompleto.fromString('Maria Silva'))
