


performance_jogador = dict()
gols_partidas = list()
i = 0

performance_jogador['name'] = str(input('Digite o nome do jogador: '))
performance_jogador['tot_partidas'] = int(input(f'Digite o total de partidas que no {performance_jogador["name"]} jogou nesse campionato: '))


for i in range(0, performance_jogador['tot_partidas']):
    gols_partidas.append(int(input(f'Digite o total de gols na {i+1}° partida: ')))

performance_jogador['cont_gols'] = gols_partidas
performance_jogador['tot_gols'] = sum(gols_partidas)


#print(performance_jogador)
print(f'O jogador {performance_jogador['name']} fez um total de {performance_jogador["tot_gols"]} gols.')
print(f'O jogador {performance_jogador['name']} jogou {len(performance_jogador['cont_gols'])} partidas.')

for j in range(0, len(performance_jogador['cont_gols'])):
    print(f'Na partida {j+1}, fez {performance_jogador['cont_gols'][j]} gols.')



'''
#Metodo Guana

jog = dict()
partidas = list()

jog['nome'] = str(input('Digite o nome do jogador: '))
tot =  int(input(f'Quantas partidas {jog["nome"]} jogou? '))

for c in range(0, tot):
    partidas.append(int(input(f'Quantos gols na partida {c+1}? ')))
jog['gols'] = partidas[:]
jog['total'] = sum(partidas)

#print(jog)
#print(partidas)

print('-='*30)
print(jog)
print('-='*30)
for k, v in jog.items():
    print(f'O campo {k} tem o valor {v}')
print('-='*30)
print(f'O jogador {jog['nome']} jogou {jog["tot_jogadas"]} partidas.')

for i, v in enumerate(jog['gols']):
    print(f'   =>Na partidas {i}, fez {v} gols.')
print(f'Foi um total de {jog["total"]} gols.')
'''






