# Identifica a quantidade de pessoas com mais de 18 anos e menos de 18 anos

maior = 0
menor = 0
from datetime import date
for ano in range (0,7):
    ano = int (input ())
    if date.today().year - ano >= 18:
        maior += 1
        print ('Esta pessoa é maior da idade.')
    else:
        menor += 1
        print ('Esta pessoa é menor da idade.')
print (f'{maior} pessoa(s) tem 18 anos ou mais. {menor} pessoa(s) tem menos de 18 anos.')