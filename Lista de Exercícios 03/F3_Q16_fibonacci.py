qtd = int(input('Quantidade de termos: '))

qtd_atual = 2
atual = 1
anterior = 0

print(anterior, atual, end =' ')

while qtd_atual < qtd:
    novo_atual = atual + anterior
    anterior = atual
    atual = novo_atual

    print(atual, end=' ')

    qtd_atual += 1
