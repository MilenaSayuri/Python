from random import randint

lista_npc = []

player = {
    'nome': 'Milena',
    'level': 1,
    'exp': 0,
    'exp_max': 50,
    'hp': 100,
    'hp_max': 100,
    'dano': 25,
    
}

def criar_npc(level):
    novo_npc = {
        'nome': f'Monstro #{level}',
        'level': level,
        'dano': 5 * level,
        'hp': 100 * level,
        'hp_max': 100 * level,
        'exp': 7 * level,
    }
    return novo_npc

 
def gerar_npcs(n_npcs):
    for x in range(n_npcs):
        novo_npc = criar_npc(x + 1)
        lista_npc.append(novo_npc)
        
        
        
def exibir_npcs():
    for npc in lista_npc:
        exibir_npc(npc)
        
                
def exibir_npc(npc):
        print(f'Nome: {npc['nome']} // Level: {npc['level']} // Dano: {npc['dano']} // HP: {npc['hp']} // EXP: {npc['exp']}')    
        
def exibir_player():
        print(f'Nome: {player['nome']} // Level: {player['level']} // Dano: {player['dano']} // HP: {player['hp']}/{player['hp_max']} // EXP: {player['exp']}/{player['exp_max']}')    

   
def reset_player():
    player['hp'] = player['hp_max']
    
def reset_npc(npc):
    npc['hp'] = npc['hp_max']
      
        
def iniciar_batalha(npc):
    while player['hp'] > 0 and npc['hp'] > 0:
        atacar_npc(npc)
        atacar_player(npc)
        exibir_info_batalha(npc)
        
    if player['hp'] > 0:
        print(f'A {player['nome']} venceu e ganhou {npc['exp']} de EXP')
        player['exp'] += npc['exp']
        exibir_player()
    else:
        print(f'O {npc['name']} venceu...')
        exibir_npc(npc)
    reset_player()
    reset_npc(npc)



def atacar_npc(npc):
    npc['hp'] -= player['dano']

def atacar_player(npc): 
    player['hp'] -= npc['dano']

def exibir_info_batalha(npc):
    print(f'Player: {player['hp']}/{player['hp_max']}')
    print(f'NPC: {npc['nome']}: {npc['hp']}/{player['hp_max']}')
    print('---------------------\n')


gerar_npcs(5)
#exibir_npcs()

npc_selecionado = lista_npc[0]
iniciar_batalha(npc_selecionado)





    
    