# Calcula o valor do saldo final com base no valor do crédito, do saldo inicial e do débito informados

c = float (input ('Crédito:'))
s = float (input ('Saldo:'))
d = float (input ('Débito:'))
sa = s - d + c
if sa >= 0:
    print (f'Saldo = {sa}. SALDO POSITIVO.')
else:
    print (f'Saldo = {sa}. SALDO NEGATIVO.')