# Identifica o primeiro e o último nome

n = str (input ('Digite seu nome completo:')).strip().split()
print ('O seu primeiro nome é:', f'{(n[0])}')
print ('O seu último nome é:', f'{n[len(n)-1]}')