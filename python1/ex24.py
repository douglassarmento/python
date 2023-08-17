nc = str (input ('Digite o nome de sua cidade:'))
print ('Santo' in nc)

# Outra forma de fazer:

n = str (input ('Digite o nome de sua cidade:')).strip()
print (n[:5].upper() == 'SANTO')