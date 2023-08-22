# Calcula o metro quadrado (m²) de uma parede e a quantidade de tinta (l) a ser usada

a = float (input ('Digite o valor (m) da altura de sua parede:'))
b = float (input ('Digite o valor (m) do comprimento de sua parede:'))
print ('O metro quadrado é de {}, sendo {}l a quantidade de tinta a ser utilizada.'.format (a*b, (a*b)/2))