"""
Len, Abs, Sum, Round

# Len

len() --> Retorna  o tamanho (ou seja, o número de ítens ) de um iterável



-------------------------------------------------------------------------------------------------------------------------
------------------------    Len    -------------------------------------------------------------------------------------
# Só para revisar
print(len('Geek University'))
print(len([1, 2, 3, 4, 5, 6,]))
print(len((1, 2, 3, 4, 5)))
print(len({1, 2, 3, 4, 5, 6, 7,}))
print(len({'a': 1, 'b': 2, 'c':3, 'd': 4, 'e': 5}))
print(len(range(0, 10)))

# Por debaixo dos panos, quando utilizamos a função len() o python faz o seguinte:

# Dunder len
print('Geek University'.__len__())

-------------------------------------------------------------------------------------------------------------------------
------------------------    ABS    -------------------------------------------------------------------------------------
abs() --> Ela retorna o valor absoluto de um numero inteiro ou real. De forma básica, seria o seu valor real sem o sinal.

print(abs(-5))
print(abs(5))
print(abs(3.14))
print(abs(-3.14))

-------------------------------------------------------------------------------------------------------------------------
------------------------    Sum    -------------------------------------------------------------------------------------
sum() --> Recebe como parâmetro um iterável, podendo receber um valor inicial e retorna a soma total dos elementos, incluindo
o valor inicial

OBS: O valor inicial default = 0

# Exemplos SUm

print(sum([1, 2, 3, 4, 5,]))
print(sum([1, 2, 3, 4, 5,], 5))
print(sum([1.32, 3.412, 5.123]))
print(sum((1, 3, 1, 5, 7, 8,)))
print(sum({1, 3, 1, 5, 7, 8,}))
print(sum({'a': 1, 'b': 3, 'c':1, 'd': 5, 'e': 7, 'f':8}.values()))

-------------------------------------------------------------------------------------------------------------------------
------------------------    Round    -------------------------------------------------------------------------------------
# Round

round --> Retorna um número arredondado para n digito de precisão após a casa decimal. Se a precisão não
for informada retorna o inteiro mais próximo da entrada.



"""
# Exemplos de Round
print(round(10.2))
print(round(10.5))
print(round(10.6))
print(round(1.212123213123, 2))
print(round(1.219999999, 2))
print(round(1.212123213123))













