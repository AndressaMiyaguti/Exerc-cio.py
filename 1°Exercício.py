#01 - Utilizando estruturas condicionais faça um programa que pergunte ao usuário dois números e mostre:
   # A soma deles; ok
   # A multiplicação entre eles; ok
   # A divisão inteira deles; ok
   # Mostre na tela qual é o maior; ok
   # Verifique se o resultado da soma é par ou impar e mostre na tela; ok
   # Se a multiplicação entre eles for maior que 40, divida pelo resultado da divisão inteira e mostre o 
   # resultado na tela. Se não, mostre que a multiplicação não foi maior que 40.

n1 = int(input('Informe o primeiro número para futuros calculos: '))
n2 = int(input('Informe o segundo número para futuros calculos: '))
    
if n1 >= n2:
    maior = n1
    menor = n2
else:
    maior = n2
    menor = n1
div_int = maior // menor
soma = n1 + n2
if soma % 2 == 0:
    par_imp = 'par'
else:
    par_imp = 'ímpar'
mult = n1 * n2
if mult > 40:
        div_quar = ( mult / div_int )
        print()
        print(f'O resultado da multiplicação dividido pelo resultado\nda divisão inteira é: {div_quar:.2f}')  
        print()
else:
    div_quar = print(' A multiplicação não foi maior que 40! ')
    print()


print(f'''
O resultado da  soma entre os números é: {soma}
O resulatdo da multiplicação entre eles é: {mult}
O resultado da divisão inteira deles é: {div_int}
O maior número entre eles é: {maior}
A soma dos produtos traz um número: {par_imp}
''')