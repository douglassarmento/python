s = 0
for n in range (0, 6):
    n = int (input ())
    if n%2 == 0:
        s += n
        print ('Este número é par.')
    else:
        print ('Este número é ímpar.')
print (f'A soma dos números pares é {s}.')