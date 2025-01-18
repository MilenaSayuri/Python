#input, conversões/cast
nome = input('Digite seu nome:')
peso = float(input('Digite seu peso:'))
idade = int(input('Digite seu idade:'))

print(nome)
print(type(peso))
print(type(idade))

#operadores
soma = 1+1
multiplicacao = 4 * 4
divisao = 30 / 3
potencia = 7 ** 2

print('soma', soma)
print('multiplicacao', multiplicacao)
print('divisao', divisao)
print('potencia', potencia)

idade = int(input('Informe sua idade: '))

#condicionais
if idade >= 18:
    print('Permitido') 
else: 
    print('Bloqueado')

salario = float(input('Informe seu salario: '))

if salario <= 3000:
    print('programador junior')
elif salario > 3000 and salario <= 6000:
    print('programador pleno')
elif salario > 6000 and salario <= 15000:
    print('programador senior')
else:
    print('gerente de projetos')

#listas
numero = [1, 2, 3]
string = ['Joao', 'Maria', 'Gabriel']
decimais = [10.8, 5.2, 33.3]

lista_vazia = []

lista_vazia.append('Amo')
lista_vazia.append('Comer')

print(lista_vazia)

numero = [10, 5, 3, 6, 2, 1]

print('total: ', len(numero))
print('menor valor: ', min(numero))
print('maior valor: ', max(numero))


#loop
notas = []

for x in range(5):
    codigo_aluno = input('RM: ')
    nota = float(input('Nota: '))
    resultado = [codigo_aluno, nota]
    notas.append(resultado)
    
print('quantidade de notas', len(nota))

for n in notas:
    codigo_aluno = n[0]
    nota = n[1]
    print('O RM', codigo_aluno, 'tirou nota: ', nota)

player = {
    'nome': 'Milena',
    'level': 1,
    'hp': 100,
    'exp': 0,
    'dano': 6,
}

npcs = [
    {'nome': 'Slime', 'dano': 1, 'hp': 10, 'exp': 5 },
    {'nome': 'King Slime', 'dano': 15, 'hp': 220, 'exp': 100 }
]
    
    
#função
def funcao_soma(valor1, valor2):
    return valor1 + valor2

while True:
    valor1 = int(input('Digite um numero: '))
    valor2 = int(input('Digite outro numero: '))
    
    resposta = funcao_soma(valor1, valor2)

    
    print(valor1, '+', valor2, '=', resposta)
    