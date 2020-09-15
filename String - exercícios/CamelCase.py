s = input()
letra = 0
qtd = 1

alfabeto_mai = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

while letra < len(s):
    if s[letra] in alfabeto_mai:
        qtd += 1
    letra += 1 
    
print(qtd)