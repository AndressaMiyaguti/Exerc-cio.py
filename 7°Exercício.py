#07 - Crie um programa onde o usuário possa digitar sete valores numéricos e 
# cadastre-os em uma lista única que mantenha separados os valores pares e 
# ímpares. No final, mostre os valores pares e ímpares em ordem crescente.

lista = [[],[]]

for c in range(1,8):

    perg = int(input('Digite um número para verficação de par ou ímpar: '))
    if perg % 2 == 0:
        lista[0].append(perg) 
    else:
        lista[1].append(perg)
lista[0].sort()
lista[1].sort()
print()
print(f'Os números adicionados pares são :\n{lista[0]}\n')
print(f'Os números ímpares,seguem abaixo:\n{lista[1]}\n')