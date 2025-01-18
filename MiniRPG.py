from random import randint

lista_npc = []

def criar_npc():
    level = randint(0,50)
    novo_npc = {
        'nome': f'Monstro #{level}',
        'level': level,
        'dano': 5 * level,
        'hp': 100 * level,
    }
    return novo_npc

 
def gerar_npcs(n_npcs):
    for x in range(n_npcs):
        novo_npc = criar_npc()
        lista_npc.append(novo_npc)
        
        
        
def exibir_npcs():
    for npc in lista_npc:
        print(f'Nome: {npc['nome']} // Level: {npc['level']} // Dano: {npc['dano']} // HP: {npc['hp']}')    
        
        

        
gerar_npcs(5)
exibir_npcs()


    
    