import random
from time import sleep

RESET = "\033[0m"
RED = "\033[91m"
GREEN = "\033[92m"
YELLOW = "\033[93m"

resposta = 'sim'

while resposta == 'sim':
    
    print("-" * 29)
    print("PEDRA PAPEL TESOURA EM PYTHON")
    print("-" * 29)
    print("\n")
    
    player = str(input("Qual sua escolha? \npedra \npapel \ntesoura \n: ")).lower()
    print('-' * 30)
    
    while player != 'pedra' and player != 'papel' and player != 'tesoura':
        if player != 'pedra' and player != 'papel' and player != 'tesoura':
            print("Entrada errada. Digite pedra, papel ou tesoura")
            
        player = str(input("Qual sua escolha? \npedra \npapel \ntesoura \n: ")).lower()
        print('-' * 30)
        
    computador = random.choice(['pedra', 'papel', 'tesoura'])
    
    print('Computador está escolhendo...')
    sleep(2)
    
    resultado = ''
    if player == computador:
        resultado = '{}Deu empate!{}'.format(YELLOW, RESET)
    elif (player == 'pedra' and computador == 'tesoura') or (player == 'tesoura' and computador == 'papel') or (player == 'papel' and computador == 'pedra'):
        resultado = '{}Você venceu!{}'.format(GREEN, RESET)
    else:
        resultado = '{}Você perdeu!{}'.format(RED, RESET)

    print(resultado)
    print("Jogador = {} \nComputador = {}".format(player, computador))
    print('-' * 30)
        
    resposta = str(input('Jogar novamente (sim/não)? '))
    print('-' * 30)