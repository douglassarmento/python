v = int (input ('Digite um valor:'))
print ('[1] BINÁRIO - [2] OCTAL - [3] HEXADECIMAL')
bn = int (input ('Digite a base numérica:'))
if bn == 1:
    print (f'O binário de {v} é {bin(v)[2:]}.')
elif bn == 2:
    print (f'O octal de {v} é {oct(v)[2:]}.')
elif bn == 3:
    print (f'O hexadecimal de {v} é {hex(v)[2:]}.')
else:
    print ('Opção inválida.')