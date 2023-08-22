# Identifica se há ou não o nome 'santo' dentre os nomes colocados

nc = str (input ('Digite o nome de sua cidade:'))
print ('Santo' in nc)

# outra forma:

n = str (input ('Digite o nome de sua cidade:')).strip()
print (n[:5].upper() == 'SANTO')