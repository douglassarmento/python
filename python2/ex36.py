v = float (input ('Valor da casa: R$'))
s = float (input ('Salário do comprador: R$'))
q = float (input ('Quantidade de anos a pagar:'))
pm = v/(q*12)
if pm > s*0.3:
    print ('Empréstimo negado.')
else:
    print ('Empréstimo aceito.')