class Pessoa:
    def __init__(self):
        pass

    def setNome(self, nome):
        self.nome = nome

    def setIdade(self, idade):
        self.idade = idade

    def getNome(self):
        return self.nome

    def getIdade(self):
        return self.idade

def meu_metodo(pessoa):
    print(pessoa.getNome())
    print(pessoa.getIdade())

def meu_outro_metodo():
    pessoa = Pessoa()
    pessoa.setNome("Leonardo")
    pessoa.setIdade(23)
    meu_metodo(pessoa)


meu_outro_metodo()