a = input('Telefonou para a vítima? ')
e = input('Esteve no local do crime? ')
i = input('Mora perto da vítima? ')
o = input('Devia para a vítima? ')
u = input('Já trabalhou com a vítima? ')


def main():
    print(f'A pessoa é: {classificacao()}')



def classificacao():
    if f'{a}' and f'{e}' and f'{i}' and f'{o}' and f'{u}'=='sim':
        return 'Culpada'

    
    elif f'{a}' and f'{e}' and f'{i}' and f'{o}'=='sim' f'{a}' and f'{e}' and f'{i}' and f'{u}'=='sim':
        return 'Cúmplice'
    elif f'{a}' and f'{e}' and f'{o}' and f'{u}'=='sim' f'{a}' and f'{i}' and f'{o}' and f'{u}'=='sim':
        return 'Cúmplice'
    elif f'{e}' and f'{i}' and f'{o}' and f'{u}'=='sim':
        return 'Cúmplice'


    elif f'{a}' and f'{e}' and f'{i}'=='sim'  or f'{a}' and f'{e}' and f'{o}'=='sim' or f'{a}' and f'{e}' and f'{u}'=='sim':
        return 'Cúmplice'
    elif f'{a}' and f'{i}' and f'{o}'=='sim'  or f'{a}' and f'{i}' and f'{u}'=='sim' or f'{a}' and f'{o}' and f'{u}'=='sim':
        return 'Cúmplice'
    elif f'{e}' and f'{i}' and f'{o}'=='sim'  or f'{e}' and f'{i}' and f'{u}'=='sim' or f'{e}' and f'{o}' and f'{u}'=='sim': 
        return 'Cúmplice'
    elif f'{i}' and f'{o}' and f'{u}'=='sim':
        return 'Cúmplice'

    
    elif f'{a}' and f'{e}'=='sim' or f'{a}' and f'{i}'=='sim' or f'{a}' and f'{o}'=='sim' or f'{a}' and f'{u}'=='sim':
        return 'Suspeita'
    elif f'{e}' and f'{i}'=='sim' or f'{e}' and f'{o}'=='sim' or f'{e}' and f'{u}'=='sim':
        return 'Suspeita'
    elif f'{i}' and f'{o}'=='sim' or f'{i}' and f'{u}'=='sim' or f'{o}' and f'{u}'=='sim':
        return 'Suspeita'


    else:
        return 'Inocente'



main()
