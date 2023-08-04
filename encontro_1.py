#Tipos primitivos de dados
num = int(input('Insira um número interio: '))
num = float(input('Insira um número com ponto flutuante: '))
num = str(input('Insira um nome: '))

#Mostrar saída no console
print('Olá, mundo!')

#Inicializando variáveis, pedindo entrada e transformando a variável em saída
nome = input('Digite seu nome: ')
print('É um prazer te conhecer, {}!'.format(nome))

#Tipos primitivos e utilização de funções na saída.
n1 = int(input('Digite um número: '))
n2 = int(input('Digite um número: '))
soma = n1 + n2
print('A soma de {} e {} é igual a: {}'.format(n1, n2, soma))

#Buscando informações em uma variável
var = input('Digite algo: ')
print('É alfabética? {}'.format(var.isalpha()))
print('É numérica? {}'.format(var.isnumeric()))
print('É alfanumérica? {}'.format(var.isalnum()))
print('É caixa-baixa? {}'.format(var.islower()))
print('É caixa-alta {}'.format(var.isupper()))

#Operações diretamente no .format()
num = int(input('Insira um número inteiro: '))
print('Antecessor é {} e o sucessor é {}'.format((num-1), (num+1)))

#Operações matemáticas
num = int(input('Digite um número: '))
dobro = num * 2
triplo = num * 3
raiz_quadrada = num ** (1/2)
print('O dobro é {} \nO triplo é {}, \nA raiz quadrada é {:.2f}'.format(dobro, triplo, raiz_quadrada))

#Formatando a saída
n1 = int(input('Nota 1: '))
n2 = int(input('Nota 2: '))
media = (n1 + n2) /2
print('A média é {:.2f}'.format(media))

#Conversão de metros em centímetro e milímetros
metros = float(input('Insira um valor em metros: '))
centimentros = metros * 100
milimetros = metros * 1000

print('Centímetros ={:.0f} milímetros ={;.0f}'.format(centimentros, milimetros))

#while em python
num = int(input('Número: '))
i = 1
while(i < 11):
    print('{} x {} = {}'.format(num, i, num*i))
    i+=1  

#Tabuada sem loop
# print('{} x {} = {}'.format(num, 1, num*1))
# print('{} x {} = {}'.format(num, 2, num*2))
# print('{} x {} = {}'.format(num, 3, num*3))
# print('{} x {} = {}'.format(num, 4, num*4))
# print('{} x {} = {}'.format(num, 5, num*5))
# print('{} x {} = {}'.format(num, 6, num*6))
# print('{} x {} = {}'.format(num, 7, num*7))
# print('{} x {} = {}'.format(num, 8, num*8))
# print('{} x {} = {}'.format(num, 9, num*9))
# print('{} x {} = {}'.format(num, 10, num*10))

#calcular o preço de um produto depois de 5% de desconto
preco_produto = float(input('Preço do produto: '))

preco_produto = preco_produto - (preco_produto * 5 / 100)

print('O novo preço do produto é R${}'.format(preco_produto))

# Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento.
salario = float(input('Salário: '))

salario += salario * 0.15

print('Novo salário R${:.2f}'.format(salario))

#Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado e a quantidade de dias pelos quais ele foi alugado. Calcule o preço a pagar, 
# sabendo que o carro custa R$60 por dia e R$0,15 por Km rodado.
km_percorridos = int(input('Km percorridos: '))
dias_alugado = int(input('Dias pelos quais foi alugado: '))

total_pagar = (km_percorridos * 0.15) + (dias_alugado * 60)

print('Total a pagar pelo aluguel do carro R${:.2f}'.format(total_pagar))

