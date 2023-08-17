from math import sin, cos, tan, radians
an = int (input ('Digite um ângulo:'))
print ('O valor do Seno é {:.2f}, do Cosseno é {:.2f}, e da Tangente é {:.2f}.'.format (sin (radians(an)), cos (radians(an)), tan (radians(an))))