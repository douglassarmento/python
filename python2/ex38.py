# Identifica a relação entre dois números (de maior, de menor ou de igualdade)

n1 = float (input ('Digite um valor:'))
n2 = float (input ('Digite outro valor:'))
if n1 > n2:
    print ('O primeiro número é maior.')
elif n1 < n2:
    print ('O segundo é maior.')
else:
    print ('Os números são iguais.')