comprimento = int(input())
senha = input()

numeros  =  "0123456789" 
lower_case  =  "abcdefghijklmnopqrstuvwxyz" 
upper_case  =  "ABCDEFGHIJKLMNOPQRSTUVWXYZ" 
special_characters  =  "! @ # $% ^ & * () - +"

letra = 0

qtd_numeros = 0
qtd_lower_case = 0
qtd_upper_case = 0
qtd_special_characters = 0

for a in range(comprimento):
    if senha[letra] in numeros:
        qtd_numeros += 1
    elif senha[letra] in lower_case:
        qtd_lower_case += 1
    elif senha[letra] in upper_case:
        qtd_upper_case += 1
    elif senha[letra] in special_characters:
        qtd_special_characters += 1

    letra += 1


error = 0

if qtd_numeros == 0:
    error += 1
if qtd_lower_case == 0:
    error += 1
if qtd_upper_case == 0:
    error += 1
if qtd_special_characters == 0:
    error += 1


if comprimento >= 6:
    print(error)
else:
    if error > (6 - comprimento):
        print(error)
    else:
        print(6 - comprimento)

