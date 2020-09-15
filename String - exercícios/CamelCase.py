s = input()
letra = 0
qtd = 1

alfabeto_mai = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

while letra < len(s):
    if s[letra] in alfabeto_mai:
        qtd += 1
    letra += 1 
    
print(qtd)
