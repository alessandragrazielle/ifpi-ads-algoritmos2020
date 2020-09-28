qtd_elementos = int(input('Quantos elementos deseja? '))
A = [''] * qtd_elementos

for i in range(qtd_elementos):
    A[i] = input('Digite o elemento: ')
print(f'Vetor A: {A}')


def inverte_vetor(A):
    inverso = [''] * len(A)
    x = len(A) - 1
    
    for elemento in A:
        inverso[x] = elemento
        x -= 1

    return inverso

B = inverte_vetor(A)

print(f'Vetor B: {B}')
