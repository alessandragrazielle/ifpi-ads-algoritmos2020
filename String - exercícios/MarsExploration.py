s = input()

letra1 = 0
letra2 = 1
letra3 = 2

erro1 = 0
erro2 = 0
erro3 = 0

contador = len(s)//3

for a in range(contador):
    if s[letra1] != 'S':
        erro1 += 1
    if s[letra2] != 'O':
        erro2 += 1
    if s[letra3] != 'S':
        erro3 += 1

    letra1 += 3
    letra2 += 3
    letra3 += 3

total_erros = erro1 + erro2 + erro3

print(total_erros)