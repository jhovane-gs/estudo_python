num = int(input('Digite um número inteiro:'))
print('''Escolha uma das bases para conversão:
[1] converter para BINÁRIO
[2] converter para OCTAL
[3] converter para HEXADECIMAL''')
opção = int(input('Sua opção:'))
if opção == 1:
   print('{} Convertido pra BINÁRIO é igual a {}'.format(num, bin(num)[2:]))
elif opção == 2:
    print ('{} convertido pra OCTAL é igual a {}'.format(num, oct(num)[2:]))
elif opção == 3:
    print('Convertido para HEXADECIMAL {}'.format(num, hex(num)[2:]))
else:
    print('Opção inválida. Tente novamente mais tarde')