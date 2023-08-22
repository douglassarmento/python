# Calcula a metade de um número e sua porção inteira

import math
n = float (input ('Digite um número:'))
print ('A metade desse número é {}, e sua porção inteira é {}.'.format ((n/2), math.trunc(n/2)))

# outra forma:

v = float (input ('Digite um valor:'))
print ('A metade desse número é {}, e sua porção inteira é {}.'.format (v/2, int (v/2)))