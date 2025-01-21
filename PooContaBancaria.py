# Pessoa
#   -titular
#   -saldo

# Comportamentos dentro da Conta (Metodos)
#   -sacar
#   -depositar
#   -verificar saldo
    

from dataclasses import dataclass

@dataclass
class Conta_Bancaria:
    titular: str
    saldo: float
    
    #metodo
    def sacar(self, valor):
        if valor > self.saldo:
            print(f'Valor solicitado maior do que o saldo atual.\nSaldo atual: R${self.saldo}')
        else:
            self.saldo -= valor
            print(f'R${valor} sacado com sucesso!')
    
    def depositar(self, valor):
        self.saldo += valor
        print(f'R${valor} depositado com sucesso! Saldo atual: R${self.saldo}')
        
    def saldo_total(self):
        print(f'Seu saldo atual eh de: R${self.saldo}')
        
    
conta = Conta_Bancaria(titular='Milena', saldo=0)

conta.saldo_total()
print('*************')
conta.sacar(20)
print('*************')
conta.depositar(100)
print('*************')
conta.sacar(10)
print('*************')
conta.saldo_total()