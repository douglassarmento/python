# Identifica o tipo e se a palavra é ou não um termo númerico, alfabético e alfanumérico

a = input ('Digite algo:')
print ('O tipo primiitivo de', a, 'é', type (a))
print ('O termo digitado é númerico?', a.isnumeric ())
print ('O termo digitado é alfabético?', a.isalpha ())
print ('O termo digitado é alfanumérico?', a.isalnum ())