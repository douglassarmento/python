# Calcula a quantidade média de um estoque e expõe se deve ou não efetuar uma compra

qa = float (input ('Quantidade atual:'))
qmax = float (input ('Quantidade máxima:'))
qmin = float (input ('Quantidade mínima:'))
qmed = (qmax + qmin)/2
if qa >= qmed:
    print ('Não efetuar compra.')
else:
    print ('Efetuar compra.')