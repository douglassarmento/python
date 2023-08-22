# Sorteia um aluno dentre três possíveis

from random import choice
a = str (input ('Digite um nome:'))
b = str (input ('Digite um nome:'))
c = str (input ('Digite um nome:'))
list = (a, b, c)
print ('O aluno sorteado foi {}.'.format (choice (list)))