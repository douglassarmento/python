r1 = int (input ('Digite o valor da primeira reta:'))
r2 = int (input ('Digite o valor da segunda reta:'))
r3 = int (input ('Digite o valor da terceira reta:'))
if r2+r3>r1 and r1+r3>r2 and r1+r2>r3:
    print ('Os valores da reta constituem um triângulo.')
else:
    print ('Os valores da reta não constituem um triângulo.')