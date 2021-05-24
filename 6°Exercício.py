#06 - Utilizando listas faça um programa que faça 5 perguntas para uma pessoa sobre um crime.
#  As perguntas são:
   # "Telefonou para a vítima?"
   # "Esteve no local do crime?"
   # "Mora perto da vítima?"
   # "Devia para a vítima?"
   # "Já trabalhou com a vítima?" 
# O programa deve no final emitir uma classificação sobre a participação da pessoa no crime. 
   # Se a pessoa responder positivamente a 2 questões ela deve ser classificada como "Suspeita",
   # Entre 3 e 4 como "Cúmplice" e 5 como "Assassino". 
   # Caso contrário, ele será classificado como "Inocente".

dados = list()
perg = list()
cont = 0
print('Responda [1] para sim ou [2] não no questionário abaixo: ')

dados.append(int(input('Telefonou para a vítima?  ')))
dados.append(int(input('Esteve no local do crime?  ')))
dados.append(int(input('Mora perto da vítima?  ')))
dados.append(int(input('Devia para a vítima?  ')))
dados.append(int(input('Já trabalhou com a vítima?  ')))
perg.append(dados[:])
for c in perg[0]:
    if c == 1:
        cont += 1
if cont <= 2:
    print(f'\nO senhor (a) respondeu positivamente a {cont} questões portnato é considerada "Suspeita"\n') 
elif cont <= 4:
    print(f'\nO senhor (a) repondeu positivamente a {cont}, sendo assim, é considerada "Cúmplice"de assassinato.\n')
elif cont == 5:
    print(f'\nO senhor(a) respondeu positivamente a todas as questões e será indiciado como  "Assassino"\n')
else:
    print('\nCom base em nosso interrogatório, o senhor(a) é considerado inocente\n ')
        