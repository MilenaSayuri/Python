banco_questoes = []

print('-----------------')
print('@ Questoes')
print('-----------------')
print('Escolha alguma questao para resolver:')
print('-----------------')
print('1 - Pergunta: Qual é a soma de 5 + 3?')
print('2 - Pergunta: Qual é o resultado de 10 dividido por 2?')
print('3 - Pergunta: Qual é a capital do Brasil?')
print('4 - Pergunta: Quantos segundos tem 1 minuto?')
print('\n# Digite outro numero para encerrar #\n')

    
def verificar_resposta(correta, tipo=int):
    resposta = tipo(input('Digite a resposta: '))
    if resposta == correta:
        print('Resposta Correta!')
    else:
        print('Resposta Errada X')
        
def resolver_questao(opcao):
    if opcao == 1:
        print('1 - Pergunta: Qual é a soma de 5 + 3?')
        verificar_resposta(8, int)
        
    elif opcao == 2:
        print('2 - Pergunta: Qual é o resultado de 10 dividido por 2?')
        verificar_resposta(5, int)
        
    elif opcao == 3:
        print('3 - Pergunta: Qual é a capital do Brasil?')
        verificar_resposta('Brasilia' or 'Brasília', str)
    
    elif opcao == 4:
        print('4 - Pergunta: Quantos segundos tem 1 minuto?')
        verificar_resposta(60, int)
        
    else:
        print(('-----------------'))
        print('Encerrando o programa')
        return False
    return True

while True:
    
    opcao = int(input('Digite a opcao da questao: '))
    if not resolver_questao(opcao):
        break
    
    