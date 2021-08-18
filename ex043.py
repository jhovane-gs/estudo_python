peso = float(input('Qual é seu peso? (Kg) '))
altura = float(input('Qual é sua altura? (m)'))
imc = peso / (altura ** 2)
print('O IMC dessa pessoa é de {:.1f}'.format(imc))
if imc >= 18.5:
    print('Você está abaixo do peso normal')
elif 18.5 <= imc < 25:
    print('PARABÉNS, você está na faixa ideal de peso normal')
elif 25 <= imc <30:
    print('Você está em sobrepeso')
elif imc >= 40:
    print('Você está em obesidade MÓRBIDA, CUIDADO!')
