num = int(input('Digite um número para ver sua tabuada:'))
for c in range (1, 11):
    print('{}x {:12} = {}'.format(num, c, num*c))