
from time import sleep
performance_jogador_temp = dict()
performance_jogador = list()
gols_partidas = list()
i = 0
total_jogadores =0

while True:
    performance_jogador_temp['name'] = str(input('Digite o nome do jogador: '))
    performance_jogador_temp['tot_partidas'] = int(input(f'Digite o total de partidas que no {performance_jogador_temp["name"]} jogou nesse campionato: '))

    for i in range(0, performance_jogador_temp['tot_partidas']):
        gols_partidas.append(int(input(f'Digite o total de gols na {i + 1}° partida: ')))
    performance_jogador_temp['cont_gols'] = gols_partidas.copy()
    performance_jogador_temp['tot_gols'] = sum(gols_partidas)
    list_temp = performance_jogador_temp.copy()
    performance_jogador.append(list_temp)
    performance_jogador_temp.clear()
    gols_partidas.clear()

    status = input('Deseja continuar - [S/N]?').upper().strip()[0]
    if status == 'N':
        break

#print(performance_jogador)

#Rank
print('=-'*30)
print('Cod','Nome'.center(20),'Gols', 'Total de Gols'.rjust(30))
print('-'*60)
for k in range(0, len(performance_jogador)):
    gols_str = str(performance_jogador[k]['cont_gols'])
    total_gols = str(performance_jogador[k]['tot_gols'])
    print(f'{k} {performance_jogador[k]['name'].center(23)} {gols_str} {total_gols.rjust(24-len(gols_str)-1)}')
    sleep(1)

#Abertura de dados por jogador
total_jogadores = len(performance_jogador) #O len ira funcionar, pois dentro da lista existe a inserção dos dicionarios, logo faze sentido usar o len
while True:
    select_jogador = int(input('Mostar dados de qual jogador? '))

    if select_jogador == 999:
        print('<<VOLTE SEMPRE>>')
        break
    elif select_jogador > (total_jogadores-1):
        print(f'ERRO! Não existe jogador com código {select_jogador}! Tente novamente.')
    elif select_jogador < (total_jogadores):
        print(f'LEVANTAMENTO DO JOGADOR: {performance_jogador[select_jogador]["name"]}')
        x =len(performance_jogador[select_jogador]['cont_gols'])
        for j in range(0, x):
            print(f'No jogo {j} fez {performance_jogador[select_jogador]['cont_gols'][j]} gols.')

#Falta implementar o elif de abertura de cada jogador e expor os dados do mesmo.






