# Identifica se uma palavra é ou não um palíndromo

f = str (input ()).replace(' ', '')
if f == f [::-1]:
    print ('Esta frase é um palíndromo.')
else:
    print ('Esta frase não é um palíndromo.')