#05 - Refatore o exercício 2, para que uma função receba a frase, faça todo o tratamento 
# necessário e retorne o resultado. Depois mostre na tela o resultado e a quantidade de 
# letras foram retiradas da frase original.

def funcao(frase):
    vogais = 'AEIOU'
    a = 'ÃÂÁÀ'
    e = 'ÈÉÊ'
    i = 'ÌÍ'
    o = 'ÒÓÔÕ'
    u = 'ÚÙ'
    cont = 0
    #frase = input('Digite uma frase para verificação de vogais: ').upper()
    for c in a:
        frase = frase.replace(c, 'A')
        for c in e:
            frase = frase.replace(c, 'E')
        for c in i :
            frase = frase.replace(c,'I')
        for c in o:
            frase = frase.replace(c, 'O')
        for c in u:
            frase = frase.replace(c,'U')
            print()
    print(f'A frase digitada, após receber tratamente de caracteres, apresenta - se da seguinte forma\n\n{frase}')
   #Print da frase digitada, sem acentos, caso a mesma possua
    for i in frase:
        if i in vogais: #A cada volta que o for dará na frase, vai representar uma letra da variavel vogais
            cont += 1 #Adição ao contador das vogais existentes na frase
    for i in frase:
        if i in vogais:
            frase = frase.replace(i, '') # o contador i em cada volta, vai subtrair uma vogal, já que optei por não deixar espaço vazio, ou outro caracter
    print(f'''

    Com a retirada de {cont} vogais, a frase ficou com esse formato:

    {frase}    
    ''')
frases = input('Digite uma frase para verificação de vogais: ').upper()
funcao(frases)



'''
cont = 0

for i in voagais:
    if i in frase:
        cont += 1

for c in vogais:
      frase = frase.replace(c, '')
print(frase)
print()
print()
'''