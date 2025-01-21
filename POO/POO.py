# class Cliente:
#     def __init__(self):
#         pass
        
#     def exibir(self):
#         print('Eu sou um cliente')
        
#     def chamar_exibir(self):
#         self.exibir()
        
# milena = Cliente()
# milena.chamar_exibir()

from dataclasses import dataclass

@dataclass
class Cliente:
    nome: str
    email: str
    idade: int
    
    def exibir(self):
        print(f'Meu nome eh {self.nome} tenho {self.idade} anos e meu email eh: {self.email}')

mi = Cliente(nome = 'Milena', email = 'milena@gmail', idade = 21)

mi.exibir()