# EP 2019-1: Escape Insper
#
# Alunos: 
# - aluno A:Gabriel Formario, gabrielf3@insper.edu.br
# - aluno B: Pedro Villela Ball, pedrovb@insper.edu.br
# - aluno C: Edivaldo Rangel, edivaldojcrj@al.insper.edu.br

import time 
import random 
import json
### SISTEMA DE INVENTÁRIO

inventário = {
        "cura":{'suquinho de laranja':'recure 40 pontos de vida'},
        'arma':{'.38':'uma arma da pesada','faca de combate ak 47':'a faca perfeita para o combate','lápis':'é o que tem'},
        'itens chave':{'chave do veterano dorminhoco':'permite o acesso ao segundo andar','chave do Poloni':'permite acesso à sala do professor'}
        }   
mochila_do_player = {}

### APARARIÇÃO DE MONSTROS ###
def aparece_monstro(cenario_atual):
    if cenario_atual == cenario_atual:
        chance = random.randint(1,10)
        if chance <= 4:
            print('Meu Deus! Um monstro apareceu!')
            combate(vida_do_player)
 
### FUNÇÃO COMBATE ###
vida_do_player = 100
def combate(vida_do_player):
    vida_do_monstro = 70
    ataque_do_player = 30
    ataque_critico = 50
    opções_de_combate = {
            'fugir':'Arregar da luta para poupar tempo',
            'atacar':'Dê uma porrada nesse monstro ordinário!',
            'inventário': 'Recupere sua vida'
            }
    if 'lápis' in mochila_do_player:
        ataque_do_player += 10
        ataque_critico += 10
    elif ' faca de combate ak 47' in mochila_do_player:
        ataque_do_player += 20
        ataque_critico += 20
    elif '.38' in mochila_do_player:
        ataque_do_player += 30
        ataque_critico += 30
    while vida_do_player > 0 or vida_do_monstro > 0:
        print('Você tem {0} pontos de vida '.format(vida_do_player))
        print('O monstro tem {0} pontos de vida '.format(vida_do_monstro))
        print(opções_de_combate)
        decisão = input('Seu turno, o que deseja fazer? ')
        print(decisão)
        if decisão == 'atacar':
            ataque = random.randint(0,100)
            if ataque >= 90: 
                vida_do_monstro -= ataque_critico
                print('Ataque crítico! O monstrou perdeu 50 de vida')
            elif ataque <= 5:
                print('Você errou o ataque! Mais sorte da próxima vez!')
            else:
                vida_do_monstro -= ataque_do_player
                print('O monstro perdeu 30 de vida!')
        elif decisão == 'fugir':
            fuga = random.randint(0,10)
            if fuga > 2:
                print('Fuga bem sucedida, seu arregaõ!')
                break
            else:
                print('Que pena, você não conseguiu fugir!')
        else:
            if 'suquinho_de_laranja' in mochila_do_player:
                perguntar = input('Deseja se curar? ')
                if perguntar == 'Sim' or ' sim':
                    vida_do_player += 40
                    mochila_do_player['suquinho_de_laranja'] -= 1
                    print("Você recuperou 40 de hp")
                elif perguntar == 'Não' or 'não' or 'nao':
                    print('Perdeu o turno por ser indeciso!')
        print('Turno do mostro!')
        ataque_do_monstro = random.randint(0,100)
        if ataque_do_monstro >= 90:
            vida_do_player -= 30
            print('Ataque crítico! Você perdeu 30 de vida')
        elif ataque_do_monstro <= 5:
            print('Você desviou do ataque!')
        else:
            vida_do_player -= 10
            print('Você perdeu 10 de vida!')
        if vida_do_monstro <= 0:
            print('Você derrotou o monstro! Parabéns!')
            print('Você tem {0} pontos de vida restantes!'.format(vida_do_player))  
            break
        elif vida_do_player <= 0:
            print('Acabou seus pontos de vida, você perdeu! Você é muito ruim!')
            break
    return vida_do_player
        
### IMPRIME TUDO DO CENÁRIO ATUAL ###       

def imprime_cenario(cenario_atual):
    print(cenario_atual["titulo"])
    print("-"*len(cenario_atual["titulo"]))
    time.sleep(1)
    print(cenario_atual["descricao"])
    print("")
    time.sleep(1)
    print("Opcoes:")
    time.sleep(1)
    for i in cenario_atual["opcoes"]:
        print(i,":",cenario_atual["opcoes"][i])
    print("")



### ATUALIZA O CENÁRIO ATUAL ###


with open('cenarios.json', 'r',encoding="utf-8-sig")as cenarios_arq:
    cenarios_str = cenarios_arq.read()
    cenario_dict = json.loads(cenarios_str)
    

def carregar_cenarios():
    
    nome_cenario_atual = "inicio"
    return cenario_dict, nome_cenario_atual

### PROGRAMA QUE RODA TUDO###
    
def main():
    print("Na hora do sufoco!")
    print("------------------")
    print()
    print("Parecia uma boa idéia: vou só jogar um pouquinho/assistir Netflix/"
        "embaçar em geral. Amanhã eu começo o EP. Mas isso não deu certo...")
    jogador = input("Digite seu nome: ")
    time.sleep(2)
    print()
    print("'{0}!'".format(jogador))
    time.sleep(2)
    print("Seu amigo se aproxima de voce e te entrega uma Mochila!")
    time.sleep(1)
    print("'Voce esqueceu isso ontem!'")
    time.sleep(2)
    print()
    print("Mochila foi equipado. Use ele com sabedoria...")
    time.sleep(1)
    print()
    print("É o dia de entregar o EP e você está muuuuito atrasado! Você está "
        "na entrada do Insper, e quer procurar o professor para pedir um "
        "adiamento do EP (boa sorte...)")
    print()

    cenarios, nome_cenario_atual = carregar_cenarios()

    game_over = False
    while not game_over:
        cenario_atual = cenarios[nome_cenario_atual]
        imprime_cenario(cenario_atual)
        aparece_monstro(cenario_atual)
       
        

       
        opcoes = cenario_atual['opcoes']
        if len(opcoes) == 0:
            print("Acabaram-se suas opções! Mwo mwo mwooooo...")
            game_over = True
        else:
            escolha = ""
            escolha = input("O que deseja fazer ? ")

            if escolha == "Sala 6":
                teleporte = input('Para onde deseja ir? ')
                nome_cenario_atual = teleporte
            elif escolha == 'aquario 2':
                resposta = input('Você achou um lápis! Deseja pegá-lo? ')
                if resposta == 'Sim' or 'sim':
                    mochila_do_player['lápis']=1
                else:
                    print('Demorou então desumilde!')
                nome_cenario_atual = escolha
            elif escolha == "Sala 2":
                resposta = input('Você achou a faca de combate AK 47! Deseja pegá-lo? ')
                if resposta == 'Sim' or 'sim':
                    mochila_do_player['faca de combate ak 47']=1
                    if 'lápis' in mochila_do_player:
                        del mochila_do_player['lápis']    
                else :
                    print('Demorou então desumilde!')
                nome_cenario_atual = escolha    
            elif escolha == "Sala 5":
                resposta = input('Você achou uma .38! Deseja pegá-la? ')
                if resposta == 'Sim' or 'sim':
                    mochila_do_player['.38']=1
                    if 'lápis' in mochila_do_player:
                        del mochila_do_player['lápis']
                    elif 'faca de combate ak 47' in mochila_do_player:
                        del mochila_do_player['faca de combate ak 47'] 
                else :
                    print('Demorou então desumilde!')
                nome_cenario_atual = escolha    
            elif escolha == 'casa do pão de queijo':
                print('Você achou um suquinho de laranja')
                if 'suquinho_de_laranja' in mochila_do_player:
                    mochila_do_player['suquinho_de_laranja'] += 1
                else:
                    mochila_do_player['suquinho_de_laranja'] = 1
                nome_cenario_atual = escolha    
            elif escolha in opcoes:
                nome_cenario_atual = escolha
            else:
                print("Sua indecisão foi sua ruína!")
                game_over = True    
        if vida_do_player <= 0:
            game_over = True
    time.sleep(1)            
    print("")
    print("Você morreu!")

# Programa principal.
if __name__ == "__main__":
    main()