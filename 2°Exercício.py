#02 - Utilizando estruturas de repetição com variável de controle, faça um programa que receba
# tring com uma frase informada pelo usuário e conte quantas vezes aparece as 
# vogais a,e,i,o,u e mostre na tela, depois mostre na tela essa mesma frase 
# sem nenhuma vogal.

vogais = 'AEIOU'
frase = input('Digite uma frase para verificação de vogais: ').upper()
contA = 0
contE = 0
contI = 0
contO = 0
contU = 0

for i in frase:
    if i in 'A':
        contA += 1
    if i in 'E':
        contE +=1
    if i in 'I':
       contI +=1
    if i in 'O':
       contO +=1
    if i in 'U':
       contU +=1
   
print(f' A frase:\n{frase}\n\nPossui em seus caracteres a quantidade a seguir de vogais:\n{contA} letras A\n{contE} letras E\n{contI} letras I\n{contO} letras O \n{contU} letras U.\nE será representada abaixo, com suas vogais subtraídas\n')     

for c in vogais:
      frase = frase.replace(c, '')
print(frase)
print()
print()















