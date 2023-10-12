import random
numeros = ['A','2','3','5','4','6','7','8','9','10','J','Q','K']
figura = ['♥','♦','♣','♠']
mano = []
for i in figura:
    for j in numeros:
        mano.append(j+i)
random.shuffle(mano)
print(mano)

jugadores = 7
cartas = 4
for i in range(1,jugadores+1):
    print(f'jugador {i} tiene la mano: {mano[:cartas]}')
    for _ in range(cartas):
        mano.pop(0)