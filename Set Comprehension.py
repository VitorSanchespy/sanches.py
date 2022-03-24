"""
Set Comprehension

Lista = [1, 2, 3, 4, 5]

Set = {1, 2, 3, 4}
"""
#  Exemplos
numeros = {num for num in range (1, 7)}
print(numeros)

# Outro Exemplo
numeros ={x ** 2 for x in range(10)}
print(numeros)
print(type(numeros))

# OBS: Faça uma alteração na estrura acima para gerar um dicionário ao invés de set
key = 'abcdefgrt'
numeros = {key[0:x]: x ** 2 for x in range(10)}
print(numeros)
print(type(numeros))
# Para finalizar
letra = {letra for letra in 'Geek University'} # Sem repetição e sem ordenação
print(letra)
print(type(letra))