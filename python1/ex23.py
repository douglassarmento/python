n = int (input ('Digite um número de 0 até 9999:'))
print ('Analisando o número', n)
num = str (n)
print ('Unidade:', f'{(num[3])}')
print ('Dezena:', f'{(num[2])}')
print ('Centena:', f'{(num[1])}')
print ('Milhar:', f'{(num[0])}')

# também pode ser feito matematicamente, como da maneira a seguir:

print ('Unidade:', f'{n//1%10}')
print ('Dezena:', f'{n//10%10}')
print ('Centena', f'{n//100%10}')
print ('Milhar', f'{n//1000%10}')