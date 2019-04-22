# EP 2019-1: Escape Insper
#
# Alunos: 
# - aluno A:Gabriel Formario, gabrielf3@insper.edu.br
# - aluno B: Pedro Villela Ball, pedrovb@insper.edu.br
# - aluno C: Edivaldo Rangel, edivaldojcrj@al.insper.edu.br

import time 
import random 

inventário = {
        "cura":{'revive':'reviva depois de esgotar seus pontos de vida','suquinho de laranja':'recure 40 pontos de vida'},
        'arma':{'.38':'uma arma da pesada','faca de combate ak 47':'a faca perfeita para o combate','lápis':'é o que tem'},
        'itens chave':{'chave de combate':'permite acesso a sala de armas leves','cartão falso':'permite acesso à sala dos professores','chave do morro':'permite acesso à sala dos menó'}
        }    

def combate():
    vida_do_player = 100
    vida_do_monstro = 70
    opções_de_combate = {
            'fugir':'Arregar da luta para poupar tempo',
            'atacar':'Dê uma porrada nesse monstro ordinário!'
            }
    while vida_do_player > 0 or vida_do_monstro > 0:
        print('Você tem {0} pontos de vida '.format(vida_do_player))
        print('O monstro tem {0} pontos de vida '.format(vida_do_monstro))
        print(opções_de_combate)
        decisão = input('Seu turno, o que deseja fazer? ')
        print(decisão)
        if decisão == 'atacar':
            ataque = random.randint(0,100)
            if ataque >= 90: 
                vida_do_monstro -= 50
                print('Ataque crítico! O monstrou perdeu 50 de vida')
            elif ataque <= 5:
                print('Você errou o ataque! Mais sorte da próxima vez!')
            else:
                vida_do_monstro -= 30
                print('O monstro perdeu 30 de vida!')
        elif decisão == 'fugir':
            fuga = random.randint(0,10)
            if fuga > 2:
                print('Fuga bem sucedida, seu arregaõ!')
                break
            else:
                print('Que pena, você não conseguiu fugir!')
        print('Turno do mostro!')
        ataque_do_monstro = random.randint(0,100)
        if ataque_do_monstro >= 90:
            vida_do_player -= 30
            print('Ataque crítico! Você perdeu 30 de vida')
        elif ataque <= 5:
            print('Você desviou do ataque!')
        else:
            vida_do_player -= 10
            print('Você perdeu 10 de vida!')
    if vida_do_monstro == 0:
        print('Você derrotou o monstro! Parabéns!')
        print('Você tem {0} pontos de vida restantes!'.format(vida_do_player))
    else:
        print('Acabou seus pontos de vida, você perdeu! Você é muito ruim!')
        
        
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


def carregar_cenarios():
    cenarios = {
        "inicio": {
            "titulo": "Saguao do perigo",
            "descricao": "Voce esta no saguao de entrada do insper",
            "opcoes": {
                "andar professor": "Tomar o elevador para o andar do professor",
                "biblioteca": "Ir para a biblioteca"
            }
        },
        "andar professor": {
            "titulo": "Andar do desespero",
            "descricao": "Voce chegou ao andar da sala do seu professor",
            "opcoes": {
                "inicio": "Tomar o elevador para o saguao de entrada",
                "professor": "Falar com o professor"
            }
        },
        "professor": {
            "titulo": "O monstro do Python",
            "descricao": "Voce foi pedir para o professor adiar o EP. "
                         "O professor revelou que é um monstro disfarçado "
                         "e devorou sua alma.",
            "opcoes": {}
        },
        "biblioteca": {
            "titulo": "Caverna da tranquilidade",
            "descricao": "Voce esta na biblioteca",
            "opcoes": {
                "inicio": "Voltar para o saguao de entrada"
            }
        }
    }
    nome_cenario_atual = "inicio"
    return cenarios, nome_cenario_atual


def main():
    print("Na hora do sufoco!")
    print("------------------")
    print()
    print("Parecia uma boa idéia: vou só jogar um pouquinho/assistir Netflix/"
        "embaçar em geral. Amanhã eu começo o EP. Mas isso não deu certo...")
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

        # Aluno A: substitua este comentário pelo código para imprimir 
        # o cenário atual.

        opcoes = cenario_atual['opcoes']
        if len(opcoes) == 0:
            print("Acabaram-se suas opções! Mwo mwo mwooooo...")
            game_over = True
        else:

            # Aluno B: substitua este comentário e a linha abaixo pelo código
            # para pedir a escolha do usuário.
            escolha = ""
            escolha = input("O que deseja fazer ? ")

            if escolha in opcoes:
                nome_cenario_atual = escolha
            else:
                print("Sua indecisão foi sua ruína!")
                game_over = True
    time.sleep(1)            
    print("")
    print("Você morreu!")


# Programa principal.
if __name__ == "__main__":
    main()
        