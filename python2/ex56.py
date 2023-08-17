idade = 0
idadevelho = 0
nomevelho = ()
menosvinte = 0
for x in range (0, 4):
    n = str (input ('Nome:'))
    i = int (input ('Idade:'))
    s = int (input ('Sexo: [1] MASCULINO - [2] FEMININO:'))
    idade += i
    if s == 1:
        if i > idadevelho:
            idadevelho = i
            nomevelho = n
    elif s == 2:
        if i < 20:
            menosvinte += 1
    else:
        print ('Opção inválida.')    
print (f'A média de idade é de {idade/4} anos.')
print (f'O nome do homem mais velho é {nomevelho}.')
print (f'O número de mulheres com menos de 20 anos de idade é {menosvinte}.')