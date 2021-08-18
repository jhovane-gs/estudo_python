from datetime import date
atual = date.today().year
nome = str(input('Qual é o seu nome?'))
nasc = int(input('Ano de nascimento: '))
idade = atual - nasc
print('óla {} você nasceu em {} e tem {} anos em {}.'.format(nome, nasc, idade, atual))
if idade == 18:
    print('Você tem que se alistar IMEDIATAMENTE!!')
elif idade < 18:
    saldo = idade - 18
    print('Ainda faltam {} anos para o alistamento'.format(saldo))
elif idade > 18:
    saldo = idade - 18
    print('Você já deveria ter se alistado há {} anos VAGABUNDO!'.format(saldo))