# Mostra a soma dos valores ímpares múltiplos de três entre o número 1 e o número 500

s = 0
for x in range (1, 501):
    if x%2 == 1 and x%3 == 0:
        s += x
print (f'A soma dos valores ímpares múltiplos de três é {s}.')