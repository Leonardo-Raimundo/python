# Lista 1 - Exercícios Python

"""
EXERCÍCIO 002: Respondendo ao Usuário
Faça um programa que leia o nome de uma pessoa e mostre uma mensagem de boas-vindas.
"""
# nome = str(input('Insira seu nome: '))
# print('Bem vindo(a) {} ao encontro de Python'.format(nome))

"""
EXERCÍCIO 003: Somando Dois Números
Crie um programa que leia dois números e mostre a soma entre eles.
"""
# primeiro_numero = int(input('Insira o primeiro número: '))
# segundo_numero = int(input('Insira o segundo número: '))
# soma = primeiro_numero + segundo_numero

# print('A soma de {} e {} é igual a {}'.format(primeiro_numero, segundo_numero, soma))

"""
EXERCÍCIO 004: Dissecando uma Variável

Faça um programa que leia algo pelo teclado e mostre na tela o seu tipo primitivo
e todas as informações possíveis sobre ele.
"""
# variável = input('Insira um valor qualquer: ')
# print('É alfabética? {}'.format(variável.isalpha()))
# print('É numérica? {}'.format(variável.isnumeric()))
# print('É alfanumérica? {}'.format(variável.isalnum()))
# print('É caixa-baixa? {}'.format(variável.islower()))
# print('É caixa-alta {}'.format(variável.isupper()))

"""
EXERCÍCIO 005: Antecessor e Sucessor
Faça um programa que leia um número inteiro e mostre na tela o seu sucessor e seu antecessor.
"""
# numero = int(input('Insira um número inteiro: '))
# print('Seu número foi {}, seu antecessor é {} e seu sucessor é {}'.format(numero, numero - 1, numero + 1))

"""
EXERCÍCIO 006: Dobro, Triplo, Raiz Quadrada
Crie um algoritmo que leia um número e mostre o seu dobro, triplo e raiz quadrada.
"""
# numero = int(input('Insira um número: '))
# dobro = numero * 2
# triplo = numero * 3
# raiz_quadrada = numero ** (1/2)

# print('O número inserido foi: {} \nSeu dobro é: {} \nSeu triplo é: {} \nSua raíz quadrada é: {:.2f}'.format(numero, dobro, triplo, raiz_quadrada))

"""
EXERCÍCIO 007: Média Aritmética
Desenvolva um programa que leia as duas notas de um aluno, calcule e mostre a sua média.
"""
#primeira_nota = float(input('Insira a primera nota: '))
#segunda_nota = float(input('Insira a segunda nota: '))
#media = (primeira_nota + segunda_nota) / 2

#print('O aluno teve as notas {} e {}, alcançando média igual a: {:.2f}'.format(primeira_nota, segunda_nota, media))
"""
EXERCÍCIO 008: Conversor de Medidas
Escreva um programa que leia um valor em metros e o exiba convertido em centímetros e milímetros.
"""
# metros = float(input('Insira um valor em metros: '))
# centimetros = metros * 100
# milimetros = metros * 1000
# print('Metros: {} \nCentímetros: {} \nMilímetros: {}'.format(metros, centimetros, milimetros))
"""
EXERCÍCIO 009: Tabuada
Faça um programa que leia um número inteiro qualquer e mostre na tela a sua tabuada.
"""
# umero = int(input('Insira um número inteiro para calcular sua tabuada: '))
# print('{} x 1 = {}'.format(numero, numero * 1))
# print('{} x 2 = {}'.format(numero, numero * 2))
# print('{} x 3 = {}'.format(numero, numero * 3))
# print('{} x 4 = {}'.format(numero, numero * 4))
# print('{} x 5 = {}'.format(numero, numero * 5))
# print('{} x 6 = {}'.format(numero, numero * 6))
# print('{} x 7 = {}'.format(numero, numero * 7))
# print('{} x 8 = {}'.format(numero, numero * 8))
# print('{} x 9 = {}'.format(numero, numero * 9))
# print('{} x 10 = {}'.format(numero, numero * 10))
"""
EXERCÍCIO 010: Conversor de Moedas
Crie um programa que leia quanto dinheiro uma pessoa tem na carteira
e mostre quantos Dólares ela pode comprar.
"""
# reais = float(input('Insira a quantia em reais R$: '))
# dolares = reais / 4.97
# print('Você tem R${:.2f} reais e pode comprar com isso ${:.2f} dólares.'.format(reais, dolares))

"""
EXERCÍCIO 011: Pintando Parede
Faça um programa que leia a largura e a altura de uma parede em metros,
calcule a sua área e a quantidade de tinta necessária para pintá-la,
sabendo que cada litro de tinta, pinta uma área de 2 m².
"""

# largura = float(input('Insira a largura da parede: '))
# altura = float(input('Insira a altura da parede: '))
# area = largura * altura
# tinta = area / 2
# print('Área da parede: {}m² \nLitros de tinta a serem utilziados: {}'.format(area, tinta))

"""
EXERCÍCIO 012: Calculando Descontos
Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto.
"""
# preço_produto = float(input('Insira o valor do produto R$: '))
# preço_desconto = preço_produto - (preço_produto * 5/100)
# print('Preço original R${} \nPreço com desconto R${}'.format(preço_produto, preço_desconto))

"""
EXERCÍCIO 013: Reajuste Salarial
Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento.
"""
# salario_original = float(input('Insira o valor do sa'))

"""
EXERCÍCIO 014: Conversor de Temperaturas
Escreva um programa que converta uma temperatura digitada em ºC e converta para ºF.
"""
# celsius = float(input('Insira uma temperatura em Celsius: '))
# fahrenheit = celsius * 1.8 + 32
# print('Temperatura em Celsius: {}º \nEquivalente em Fahrenheit: {}º'.format(celsius, fahrenheit))

"""
EXERCÍCIO 015: Aluguel de Carros
Escreva um programa que pergunte a quantidade de km percorridos por um carro alugado
e a quantidade de dias pelos quais ele foi alugado. Calcule o preço a pagar,
sabendo que o carro custa R$ 60 por dia e R$ 0,15 por km rodado.
"""
# km_percorridos = float(input('Km percorridos: '))
# dias_alugado = int(input('Quantidade de dias alugado: '))
# total_pagar = (km_percorridos * 0.15) + (dias_alugado * 60)
# print('Km percorridos: {} \nDias alugado: {} \nTotal a pagar R${:.2f}'.format(km_percorridos, dias_alugado, total_pagar))

"""
EXERCÍCIO 020: Sorteando uma Ordem aleatória na Lista
O mesmo professor do exercício anterior quer sortear a ordem de apresentação de trabalhos dos alunos.
Faça um programa que leia o nome dos quatro alunos e mostre a ordem sorteada.
"""
# from random import shuffle

# nome1 = str(input('Insira um nome: '))
# nome2 = str(input('Insira um nome: '))
# nome3 = str(input('Insira um nome: '))
# nome4 = str(input('Insira um nome: '))

# lista = [nome1, nome2, nome3, nome4]
# shuffle(lista)
# print(lista)
# print(lista[0])
# print(lista[2:])

