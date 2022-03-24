"""
Dictionary Comprehension ()

Pense no seguinte:

Se quisermos criar uma lista fazemos:
lista = [1, 2, 3, 4,]

Se quisermos criar uma tupla:
tupla = (1, 2, 3, 4,) # 1, 2, 3, 4,

Se quisermos criar um set (conjunto):
conjunto = {1, 2, 3, 4,}

Se quizermos criar um dicionário:
dicionario = {'a':1, 'b':2, 'c':3}

# Sintaxy
{ chave:valor for valor in iterável }
[ valor for valor in iterável ]

-----------------------------------------------------------------------------------------
# Exemplos
numeros = {'a':1, 'b':2, 'c':3, 'd':14, 'e':20}
quadrado ={chave:valor **2  for chave, valor in numeros.items()}
print(quadrado)

--------------------------------------------------------------------------------------
numero =[ 1, 2, 3, 4, 15, 1, 2 ]
quandrados = {valor: valor **2 for valor in numero}
print(quandrados)

--------------------------------------------------------------------------------------
chaves ='abcde'
valor = [1, 2, 3, 4, 5]
mistura = {chaves[i]: valor[i]  for i in range (0, len(chaves))}
print(mistura)

---------------------------------------------------------------------------------------


"""
# Exemplo com lógica condicional
numeros = [1, 2, 3, 4, 5]
res = {num:('par' if num % 2 == 0 else 'impar')for num in numeros}
print(res)
