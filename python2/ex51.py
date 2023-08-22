# Calcula uma progressão aritmética

p = int (input ('Primeiro termo:'))
r = int (input ('Razão:'))
n = 1
c = 0
for x in range (0, 10):
    u = p + ((n - 1) * r)
    n += 1
    c += 1
    print (f'O {c}o termo é {u}.')