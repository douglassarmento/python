# Calcula a média de um aluno e expõe a sua aprovação ou a sua reprovação

m = (float (input ('Digite a 1a nota:')) + float (input ('Digite a 2a nota:')))/2
if m >= 6:
    print (f'APROVADO. Média {m}.')
else:
    print (f'REPROVADO. Média {m}.')