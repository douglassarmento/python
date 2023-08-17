a = int (input ('Digite um ano:'))
if a%4 == 0:
    print ('Este ano é bissexto.')
else:
    print ('Este ano não é bissexto.')

#Outra forma de fazer (mais completa):

a = int (input ('Digite um ano:'))
if a%4 == 0 and a%100 != 0 or a%400 == 0:
    print ('Este ano é bissexto.')
else:
    print ('Este ano não é bissexto.')