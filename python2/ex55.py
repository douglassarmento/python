maior = 0
menor = 0
for p in range (0, 5):
    p = float (input ())
    if p > maior:
        maior = p
        if menor == 0:
            menor = p
        else:
            menor = menor
    elif p > menor:
        if menor == 0:
            menor = p
        else:
            menor = menor
    else:
        menor = p       
print (f'O maior peso é de {maior} quilos. O menor peso é de {menor} quilos.')