from datetime import date
ano = date.today().year
a = int (input ('Digite o ano em que nasceu:'))
if ano - a < 18:
    print (f'Você poderá se alistar daqui a {18-(ano-a)} ano(s).')
elif ano - a == 18:
    print ('Está na hora de se alistar.')
else:
    print (f'Já passou o prazo de {a-18} para se alistar.')