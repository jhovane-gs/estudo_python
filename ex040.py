nota1 = float(input('Primeira nota:'))
nota2 = float(input('Segunda nota:'))
média = (nota1 + nota2)  /2
print('Tirando {:.1f} e {:.1f} a média do aluno é {}'.format(nota1, nota2, média))
if média > 5:
    print('(Aprovado)')

elif média == 5:
    print('(Aprovado)')

elif média < 5:
     print('(Reprovado)')