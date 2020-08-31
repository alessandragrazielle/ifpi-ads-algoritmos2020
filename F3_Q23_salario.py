n = int(input('Número de casos: '))

for a in range(n):
    cod = int(input('Código do funcionário: '))
    h_t = int(input('Quantidade de horas trabalhadas: '))
    n_d = int(input('Quantidade de dependentes: '))

    s_b = (h_t*12) + (n_d*40)
    inss = s_b * (8.5/100)
    ir = s_b * (5/100)
    s_l = s_b - inss - ir

    print(f'*Código {cod}* \nDesconto INSS: R${inss:.2f} \nDesconto IR: R${ir:.2f} \nSalário líquido: R${s_l:.2f}')