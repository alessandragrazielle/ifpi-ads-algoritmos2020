n = int(input('Número de votos: '))
c1 = 0
c2 = 0
c3 = 0
nulo = 0
branco = 0

for a in range(n):
    cod = int(input('Código: '))

    if cod == 1:
        c1 += 1
    elif cod == 2:
        c2 += 1
    elif cod == 3:
        c3 += 1
    elif cod == 9:
        nulo += 1
    elif cod == 0:
        branco += 1

if c1>c2 and c1>c3:
    vencedor = 'Candidato 1'
elif c2>c1 and c2>c3:
    vencedor = 'Candidato 2'
elif c3>c1 and c3>c2:
    vencedor = 'Candidato 3'

print(f'Votos no candidato 1: {c1} \nVotos no candidato 2: {c2} \nVotos no candidato 3: {c3} \nVotos nulos: {nulo} \nVotos em branco: {branco}')
print(f'O vencedor é: {vencedor}')