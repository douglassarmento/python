# Mostra os números divisíveis por 11, cujo resto é 5, entre o número 1000 e o número 2000

for x in range (1000, 2001):
    x%11
    if x%11 == 5:
        print (x)