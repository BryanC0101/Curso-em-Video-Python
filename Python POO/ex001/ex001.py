# Declaração de Classes
class Testando:
    def __init__(self): # Método Construtor
        # Atributos de instância
        self.nome = ''
        self.idade = 0

    # Métodos de instância
    def aniversario(self):
        self.idade += 1

    def mensagem(self):
        return f'{self.nome} é uma pessoa e tem {self.idade} anos de idade '

# Declaração de Objetos
p1 = Testando()
p1.nome = 'Maria'
p1.idade = 17
print(p1.mensagem())