# Identifica a relação entre os números (de maior e de menor)

n1 = int (input ('Digite um número:'))
n2 = int (input ('Digite outro número:'))
n3 = int (input ('Digite um último número:'))
maior = n1
if n2>n1 and n2>n3:
    maior = n2
if n3>n1 and n3>n2:
    maior = n3
menor = n1
if n2<n1 and n2<n3:
    menor = n2
if n3<n1 and n3<n2:
    menor = n3
print ('O maior valor é',maior,'e o menor é',menor,'.')