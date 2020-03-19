var1 = int(input('Variável 1: '))
var2 = int(input('Variável 2: '))

def condicoes():
    if var1%var2 == 1:
        print((var1 + var2) + (var1 % var2))
   
    elif var1%var2 == 2:
        if var1 % 2 == 0 and var2 % 2 == 0:
            print(f'O números {var1} e {var2} são pares')
        else:
            print(f'O números {var1} e {var2} são ímpares')

    elif var1%var2 == 3:
        print((var1 + var2) * var1)

    elif var1%var2 == 4:
        if var2 != 0:
            print((var1 + var2) / var2)

    else:
        print(var1**2, 'e', var2**2)

    
        

condicoes()