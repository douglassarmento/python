a = float (input ('Digite sua altura:'))
p = float (input ('Digite seu peso:'))
imc = p/(a)**2
if imc < 18.5:
    print (f'IMC = {imc:.1f}. Vocẽ está abaixo do peso.')
elif imc >= 18.5 and imc <= 25:
    print (f'IMC = {imc:.1f}. Você está no peso ideal.')
elif imc > 25 and imc <= 30:
    print (f'IMC = {imc:.1f}. Você está com sobrepreso.')
elif imc > 30 and imc <= 40:
    print (f'IMC = {imc:.1f}. Você está com obesidade.')
else:
    print (f'IMC = {imc:.1f}. Você está com obesidade mórbida.')