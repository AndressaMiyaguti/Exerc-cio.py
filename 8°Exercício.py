#08 - Crie um programa que leia nome, ano de nascimento e carteira de trabalho e cadastre-os 
# (com idade) em um dicionário. Se por acaso a CTPS for diferente de 0, o dicionário 
# receberá também o ano de contratação e o salário. Calcule e acrescente , além da idade, 
# com quantos anos a pessoa vai se aposentar. Considere que o trabalhador deve contribuir 
#  35 anos para se aposentar.

import datetime
hoje = datetime.date.today()
dados = dict()
lista = list()
while True:
    dados['Nome'] = str(input('Digite o nome do colaborador: ')).title()
    dados['Nasc'] = int(input('informe o ano de nascimento: '))
    if  datetime.date.today().year - dados['Nasc'] >  100 or datetime.date.today().year - dados['Nasc'] < 14:
#if para restringir cadastro de pessoas com mais de 100 anos e menor que 14 anos.       
        print('Ano de nascimento não permitido, para as finalidades desse cadastro.')
        break
    dados['CTPS'] = int(input('Informe o número da carteira de trabalho: '))
    if dados['CTPS'] != 0 :
       dados['Ano_Contratação'] = int(input('Informe o ano de contratação: '))
       dados['Salario'] = float(input('informe o salario: ').replace(',','.'))
       cal = datetime.date.today().year - dados['Nasc']   
       apo = dados['Ano_Contratação'] + 35
       if apo < datetime.date.today().year :#if para que já seja identificado que a pessoa cadastrada esta aposentada.Caso contrario no campo previsão de aposentadoria, vai ser atribuido uma idade menor do que a pessoa tem agora
           dados['Prev.Apos'] = 'Aposentado'
       else:
           dados['Prev.Apos.'] = apo - dados['Nasc']
       dados['Idade'] = cal
       
    else:
        dados['CTPS'] = 'Não possue registro'  
    cont = input('Deseja continuar?').strip().upper()[0]
    lista.append(dados.copy())
    
    if cont == 'N':
        break
for c in lista:
    print(c)
