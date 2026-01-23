
def ficha(name=0, gols=0):
    if len(name) == 0:
        print(f'O jogador <desconhecido> fez ', end='')
    else:
        print(f'O jogador {name} fez ', end='')
    if len(gols) == 0:
        print('0 gol(s) no campeonato.')
    else:
        print(f'{gols} gol(s) no campeonato.')

    

name = str(input('Digite o nome do jogador: '))
gols= input(f'Digite a quantidade de gols que o {name} fez: ')

ficha(name, gols)






