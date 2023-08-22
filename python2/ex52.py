# Identifica se um número qualquer é ou não primo

n = int (input ())
for x in range (1, 10):
    if x == 1 or x == n:
        continue
    n/x
    if n%x == 0:
        break
if n%x != 0:
    print ('Este número é primo.')
else:
    print ('Este número não é primo.')