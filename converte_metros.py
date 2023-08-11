''' algoritmo para converter metros em centímetros e milímetros:
 1. pedir a quantidade de metros por entrada Input(), do tipo Int
 2. converter para centímetro
 3. converter para milímetro
 4. exibir na saída a quantidade de metros, e os valores convertidos, formatados
 para 0 números após a vírgula. '''

metros = float(input('Insira o valor em metros: '))

print('{} metros em centímetros é igual a: {:.2f} \nem milímetros é igual a: {:.2f}'.format(metros, metros * 100, metros * 1000))

