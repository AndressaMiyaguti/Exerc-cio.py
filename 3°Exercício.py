#03 - Utilizando estruturas de repetição com teste lógico, faça um programa
#  que peça uma senha para iniciar seu processamento, só deixe o usuário 
# continuar se a senha estiver correta, após entrar dê boas vindas a seu 
# usuário e apresente a ele o jogo da advinhação, onde o computador vai “pensar”
#  em um número entre 0 e 10. O jogador vai tentar adivinhar qual número foi 
# escolhido até acertar, a cada palpite do usuário diga a ele se o número 
# escolhido pelo computador é maior ou menor ao que ele palpitou, no final 
# mostre quantos palpites foram necessários para vencer.
import random 
print()
senha = int(input('\nOlá, para iniciarmos o jogo, é necessário que responda corretamente a charada:\n\nCaminhando ao fim da tarde, uma senhora contou 20 casas em uma rua à sua direita.\nNo regresso, ela contou 20 casas à sua esquerda.\nQuantas casas ela viu no total?   '))  
if senha != 20:
    print('Resposta incorreta\nTente novamente')
else:
    print('''
    Boas vindas ao jogo do sexto sentido!
    Vamos começar a jogar.
    Você terá que adivinhar o número de 0 a 10,
    com benefício de dicas, ao longo do caminho.
    Boa sorte!
    ''')
    cont = 0
    n1 = random.randint(0,10)
    #print(n1)
    while True:
        per = int(input('Te desafio a adivinhar o número que pensei, qual é o seu palpite?  '))
        if per == n1:
            print()
            print(f'Fui derrotado.\nMeus parabéns') 
            cont += 1
            if cont == 1:
                print()
                print('Você acertou de primeira')
            if cont != 1:
                print()
                print(f'Você acertou, porém teve que receber "{cont}" dicas.\n Será que da proxima vez\nconsegue acertar de primeira? ')
                print()
                desafio = (input('Vamos jogar novamente?\nDigite não caso desista de tentar\nOu insira qualquer informação\npara continuar.\n ')).strip().upper()[0]
                if desafio == 'N':
                    print('Fim do jogo!')
                    print()
                    break

        elif per > n1:
            print('Você errou, vou dar uma dica\nO número que pensei tem o valor menor...')
            cont +=1
        elif per < n1:
            print('Você errou, vou dar uma dica\nO número que pensei tem o valor maior...')
            cont += 1

        