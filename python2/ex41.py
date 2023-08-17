from datetime import date
anoatual = date.today().year
anonasc = int (input ('Digite o ano em que nasceu:'))
idade = anoatual - anonasc
if idade > 20:
    print (f'Idade: {idade}. Categoria: MASTER.')
elif idade == 20:
    print (f'Idade: {idade}. Categoria: SÊNIOR.')
elif idade > 15 and idade <= 19:
    print (f'Idade: {idade}. Categoria: JUNIOR.')
elif idade > 9 and idade <= 14:
    print (f'Idade: {idade}. Categoria: INFANTIL.')
else:
    print (f'Idade: {idade}. Categoria: MIRIM.')