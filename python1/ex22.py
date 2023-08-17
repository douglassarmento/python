n = str (input ("Digite seu nome completo:"))
print (f"{n.upper()}, {n.lower()}, {len (n) - n.count(' ')}, {n.find (' ')}")

# outra forma de fazer o primeiro nome e a quantidade de letras do primeiro nome.

ns = n.split()
print (f"O primeiro nome é {ns[0]} e possui {len(ns)} letras.")