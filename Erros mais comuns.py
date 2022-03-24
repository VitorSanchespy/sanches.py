"""
Erros mais comuns em Python

ATENÇÃO! É importatne prestar atenção  e aprender a ler as saídas de erros geradas pela execução
do nosso código.

Os erros mais comuns:

SytanxError --> Ocorre quando o Python encontra um erro de sintaxe. Ou seja, você  escreveu algo que o Python
não reconhece como parte da linguagem.

-------------------------------------------------------------------------------------------------------------------------
# Exemplos SyntaxError
a)def funcao:
    print("Geek University")

b)
None = 1

c)
return

-------------------------------------------------------------------------------------------------------------------------
2 - NameError --> Ocorre quando uma variável ou função não foi definida,

# Exemplos NameError

a)
print(geek)

b)
geek()

c)
a = 18
if a < 10:
    msg ='É maior que 10'
print(msg)

-------------------------------------------------------------------------------------------------------------------------
3 - TypeError --> Ocorre quando uma função/operação/ação é aplicada a um tipo errado.

Exemplos TypeError

a)
print(len(5))

b)
print('Geek'+[])

-------------------------------------------------------------------------------------------------------------------------
4 - IndexError --> Ocorre quando tentamos acessar um elemento em uma lista ou outro tipo de dado indexado utilizanodo
um índice inválido.

# Exemplos IndexError

a)lista = ['Geek']
print(lista[1])

b) lista = ['Geek']
print(lista[0][10])

c) tupla = ('Geek',)
print(lista[0][10])

-------------------------------------------------------------------------------------------------------------------------
5 - ValueError --> Ocorre quando uma função/operação built-in (integrada)  recebe um argumento com tipo correto mas
valor inapropriado.

a)
print(int('Geek'))

b)
print(float('Geek'))

-------------------------------------------------------------------------------------------------------------------------
6 - KeyError --> Ocorre quando tentamos acessar um dicionário com uma chave  que não existe.

# Exemplos KeyError

a)
dic = {'python':'University'}
print(dic['geek'])

-------------------------------------------------------------------------------------------------------------------------
6 - AttibuteError --> Ocorre quando uma carável não tem um atributo/função.

# Exemplos AttibuteError

a)
tupla = (1, 2, 23, 44, 15)
tupla.sort()
print(tupla)

-------------------------------------------------------------------------------------------------------------------------
6 - IndentationError --> Ocorre quando não respeitamos a identação do Python (4 espaços).

# Exemplos IndentationError

a)
def nova():
print('Geek')

b)
for i in range(10):
i + 1
print(i)

OBS: Exceptions e Erros são sinônimos na programação.

OBS: Importante ler e prestar atenção na saida de erro.
"""
# Exemplos IndentationError















