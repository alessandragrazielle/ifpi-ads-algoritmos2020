qtd_numeros = int(input('Quantos números pretende digitar? '))
vetor = ['-1'] * qtd_numeros

for i in range(len(vetor)):
    vetor[i] = float(input('Digite o número que deseja: '))
print(vetor)   


# separação
print('-'* 25)


def pos_ou_neg(vetor):
    npos = 0
    nneg = 0
    for i in range(len(vetor)):
        if vetor[i] >= 0:
            npos += 1
        else:
            nneg += 1   

    return npos, nneg   

def imp_ou_par(vetor):
    nimp = 0
    npar = 0    
    for i in range(len(vetor)): 
        if vetor[i]%2 == 0: 
            npar += 1
        else:
            nimp += 1

    return nimp, npar 

pos, neg = pos_ou_neg(vetor)     
impar, par = imp_ou_par(vetor)

print(f'Positivo(s): {pos} \nNegativo(s): {neg} \nImpar(s): {impar} \nPar(s): {par}')

# separação
print('-'* 25)


for i in range(len(vetor)):
    if i%2 == 0:
        vetor[i] = vetor[i] * 2
    else:
        vetor[i] = vetor[i] / 2
print(vetor)


pos2, neg2 = pos_ou_neg(vetor)     
impar2, par2 = imp_ou_par(vetor)

print(f'Positivo(s): {pos2} \nNegativo(s): {neg2} \nImpar(s): {impar2} \nPar(s): {par2}')


# separação
print('-'* 25)


def media_lista(vetor):
    soma = 0
    for i in range(len(vetor)):
        soma += vetor[i]
    media = soma/len(vetor)

    return media

print(f'O valor da média é de: {media_lista(vetor)}')