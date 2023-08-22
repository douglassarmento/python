# Identifica se há ou não o nome 'silva' dentre os nomes colocados

n = str (input ('Digite seu nome:')).strip()
print ('Silva' in n)

# outra forma:

nome = str (input ('Digite seu nome:')).strip()
print ('silva' in nome.lower())