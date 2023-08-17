v = float (input ('Digite o valor do produto: R$'))
f = int (input ('[1] À VISTA/DINHEIRO/CHEQUE - [2] À VISTA/CARTÃO - [3] PARCELADO 2X - [4] PARCELADO 3X OU MAIS:'))
if f == 1:
    print (f'O valor do produto pago à vista no dinheiro/cheque é R$ {v - (v*0.1)}.')
elif f == 2:
    print (f'O valor do produto pago à vista no cartão é R$ {v - (v*0.5)}.')
elif f == 3:
    print (f'O valor do produto parcelado em 2x é R$ {v}.')
else:
    print (f'O valor do produto parcelado em 3x ou mais é R$ {v + (v*0.3)}.')