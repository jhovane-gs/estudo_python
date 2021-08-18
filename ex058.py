sexo = str(input('Qual é o seu sexo? [M/F]')).upper().strip()[0]
while not sexo in 'MmFf':
    sexo = str(input('Dados invalidos. por favor informe seu sexo: ')).strip().upper()[0]
print('Sexo {} Registrado com sucesso'.format(sexo))

