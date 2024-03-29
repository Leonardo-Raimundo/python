# Mostrar saída no console
print('Olá, mundo!')

# Inicializando variáveis, pedindo entrada e transformando a variável em saída
nome = input('Digite seu nome: ')
print('É um prazer te conhecer, {}!'.format(nome))

# Tipos primitivos de dados
numero_natural = int(input('Insira um número interio: '))
num_virgula = float(input('Insira um número com ponto flutuante: '))
nome = str(input('Insira um nome: '))
# Não existe variável char, toda variável com um caracter é do tipo string

# Tipos primitivos e utilização de funções na saída.
primeiro_numero = int(input('Digite um número: '))
segundo_numero = int(input('Digite um número: '))
soma = primeiro_numero + segundo_numero
# As chaves substituem as variáveis que estiverem dentro da função format(), na ordem em que estiverem lá
# Precisa separar por vírgula cada variável
print('A soma de {} e {} é igual a: {}'.format(primeiro_numero, segundo_numero, soma))

# Buscando informações em uma variável, com funções que retornam True ou False
variavel = input('Digite algo: ')
#Verifica se a variável tem algo armazenado, e se são apenas letras, se esse for o caso, retorna True. Caso contrário, False
print('É alfabética? {}'.format(variavel.isalpha())) 

# Verifica se a variável tem algo armazenado, e se são apenas número, se esse for o caso, retorna True. Caso contrário, False
print('É numérica? {}'.format(variavel.isnumeric()))

# Possui números e letras ao mesmo tempo? (Não parece estar funcionando 100%)
print('É alfanumérica? {}'.format(variavel.isalnum()))

# O conteúdo da variável é composto por letras minúsculas?
print('É caixa-baixa? {}'.format(variavel.islower()))

# O conteúdo da variável é composto por letras maiúsculas?
print('É caixa-alta {}'.format(variavel.isupper()))

primeiro_numero = int(input('Digite um número: '))
segundo_numero = int(input('Digite um número: '))
media = (primeiro_numero + segundo_numero) /2

print('A média de {} e {} é igual a: {}'.format(primeiro_numero, segundo_numero, media))

# ou

primeiro_numero = int(input('Digite um número: '))
segundo_numero = int(input('Digite um número: '))

# Pode-se fazer operações diretamente na saída, a operação fica separada das demais variáveis por vírgula também.
print('A soma de {} e {} é igual a: {}'.format(primeiro_numero, segundo_numero, (primeiro_numero + segundo_numero) / 2))
# o python entende que o que será impresso no terceiro par de {} vai ser o resultado da operação (n1+n2)/2
'''
--------------------------
OBSERVAÇÕES
--------------------------
1. É uma boa prática as chaves {} não ficarem grudadas nas demais letras/palavras da string de saída,
pois o conteúdo das variáveis que vai substituir as {} vai aparecer grudado nessas letras. Tudo bem as 
chaves estarem grudadas nas aspas simples da string, as aspas não vão ser imprimidas na tela.

1.2. É uma boa prática o # do comentário de uma linha não estar grudado no conteúdo à direita.

2. Comandos nesse formato: .format() ou .isnumeric() ou input() são funções. Precisam portanto estarem
sempre acompanhadas dos parênteses (), grudados. O mesmo vale para funções que possuam ponto "."
Essas funções estam agindo sobre alguma variável ou outra função, portanto não pode haver espaço nem
antes e nem depois do ponto:
'''

# Exemplo
# print('É uma variável numérica? {}' .format('var.isnumeric()'))
               # espaço vai dar erro ^
               
# ----------------------------------------------------------------

# print('É uma variável numérica? {}'. format('var.isnumeric()'))
                # espaço vai dar erro ^
            
# ----------------------------------------------------------------
                       
# print('É uma variável numérica? {}'.format ('var.isnumeric()'))
                       #espaço vai dar erro ^
                       
# ----------------------------------------------------------------
                    
# print('É uma variável numérica? {}'.format('var.isnumeric()'))
                       # agora vai dar boa :D


