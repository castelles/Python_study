#Aula 1
print("hello world")

instrumentos = ['Baixo','Bateria','Guitarra']
for instrumento in instrumentos:
    print (instrumento)

import math
10 % 3

i = [0,1,2,3,4,5,6,7,8,9,10]
for n in i:
    print (13*n)

crieiumavariavelgigantepoisestoucompreguicadeescrevertudo = 10

# Atribuicao multipla
a = 1
b = 200
print(a,b)
a,b=b,a
print(a,b)

#Strings

nome = 'Caio'
canto1 = 'vem ai, '
canto2 = 'la '

print(nome + ' ' + canto1 + canto2*6 + '!!')

print(len(nome))

nome = input('Digite seu nome: ')
frase = 'Ola, {}'.format(nome)
print(frase)

#LISTAS

frutas = ['banana','maca','abacaxi']

'banana' in frutas
frutas[:2]

lista_estranha = ['duas palavras', 42, True, ['batman', 'robin'], -0.84, 'hipófise']
'batman'in lista_estranha
'batman'in lista_estranha[3]

len(lista_estranha)
len(lista_estranha[3])

del lista_estranha[2]

a = [1,2,3]
b = [4,5,6]
c = a+b
a*2

lista = ['a','b','c']
lista2 = ['d','e']
lista.append('e')
lista.insert(3,'d')

a = 7
b = 8

if a < b:
    print('a é menor!')
elif a > b:
    print('b é menor!')
else:
    print('sao iguais')


try:
    idade = int(input('Informe sua idade: '))
    peso = int(input('Informe seu peso: '))
    horas = int(input('Informe quantas horas você dormiu nas últimas 24h: '))
except ValueError:
    print('Só é permitida a entrada de numeros inteiros sem qualquer letra ou caractere')

if idade > 18 and peso > 50 and horas > 6: print('Você está apto a doar sangue')
else: print('Você NÃO está apto a doar sangue')

novaLista = [1,2,3,4,5]

for numero in novaLista: 
    print(numero ** 2)



