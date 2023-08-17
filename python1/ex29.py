km = int (input ('Digite a velocidade percorrida (km:)'))
if km>80.0:
    print ('Você foi multado. Multa = R$', f'{(km-80)*7}')
else:
    print ('Velocidade dentro do padrão.')