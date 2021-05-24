#04 - Utilizando funções e listas faça um programa que receba uma data no formato DD/MM/AAAA 
# e devolva uma string no formato DD de mesPorExtenso de AAAA. 
# Opcional: valide a data e retorne 'data inválida' caso a data seja inválida.

from datetime import date
dia = date.today().day #retorna o dia atual
mes = date.today().month #retorna o mês atual
ano = date.today().year #retorna o ano atual


dados = list()
data = list()
meses = ['Janeiro','Fevereiro','Março','Abril', 'Maio','Junho','Julho','Agosto','Setembro','Outubro','Novembro','Dezembro']
print()
print('Para finalizar seu cadastro, preencha os campos com a data de HOJE: ')
print()
dados.append(int(input('Dia:  ')))
dados.append(int(input('Mês:  ')))
dados.append(int(input('Ano:  ')))
data.append(dados[:])
for c in data:
    if c[0] != dia or c[1] != mes or c[2] != ano: #Validação se o dia, mes e ano, são diferentes da data de hoje
        print()
        print('Data inválida\n')
    elif c[1] == 1: # Contador na posição 1(mes), para comparação e substituição de numeral por extenso
        print()
        print(f'Dia {dados[0]} de {meses[0]} de {dados[2]}\n\nCadastro finalizado com sucesso.\n')
    elif c[1] == 2:
        print()
        (f'Dia {dados[0]} de {meses[1]} de {dados[2]}\n\nCadastro finalizado com sucesso.\n')
    elif c[1] == 3:
        print()
        (f'Dia {dados[0]} de {meses[2]} de {dados[2]}\n\nCadastro finalizado com sucesso.\n')
    elif c [1] == 4:
        print()
        (f'Dia {dados[0]} de {meses[3]} de {dados[2]}\n\nCadastro finalizado com sucesso.\n')
    elif c[1] == 5 :
        print()
        print(f' Dia {dados[0]} de {meses[4]} de {dados[2]}\n\nCadastro finalizado com sucesso.\n')
    elif c[1] == 6:
        print()
        (f'Dia {dados[0]} de {meses[5]} de {dados[2]}\n\nCadastro finalizado com sucesso.\n')
    elif c[1] == 7:
        print()
        (f'Dia {dados[0]} de {meses[6]} de {dados[2]}\n\nCadastro finalizado com sucesso.\n')
    elif c[1] == 8:
        print()
        (f'Dia {dados[0]} de {meses[7]} de {dados[2]}\n\nCadastro finalizado com sucesso.\n')
    elif c[1] == 9:
        print()
        (f'Dia {dados[0]} de {meses[8]} de {dados[2]}\n\nCadastro finalizado com sucesso.\n')
    elif c[1] == 10:
        print()
        (f'Dia {dados[0]} de {meses[9]} de {dados[2]}\n\nCadastro finalizado com sucesso.\n')
    elif c[1] == 11:
        print()
        (f'Dia {dados[0]} de {meses[10]} de {dados[2]}\n\nCadastro finalizado com sucesso.\n')
    elif c[1] == 12:
        print()
        (f'Dia {dados[0]} de {meses[11]} de {dados[2]}\n\nCadastro finalizado com sucesso.\n')




        




