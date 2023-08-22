# Aplica certo desconto com base no salário

s = float (input ('Digite o valor de seu salário (R$):'))
if s>1250:
    print ('Salário com 10% de aumento: R$', f'{s+(s*0.10)}')
if s<=1250:
    print ('Salário com 15% de aumento: R$', f'{s+(s*0.15)}')