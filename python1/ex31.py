# Identifica o valor da viagem com base nos quilometros percorridos

km = int (input ('Digite o número de quilometros (km) percorridos:'))
if km <= 200:
    print ('Sua viagem foi de',km,'km e o valor foi de R$', f'{km*0.5}.')
if km > 200:
    print ('Sua viagem foi de',km,'km e o valor foi de R$', f'{km*0.45}.')

# outra forma:

km = int (input ('Digite o número de quilometros (km) percorridos:'))
p = km*0.5 if km <=200 else km*0.45
print ('Sua viagem foi de',km,'km e o valor foi de R$',p)