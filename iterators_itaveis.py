"""
Entendendo Iterators e Iterables

Iterator  -->
    - Um objeto da programção que pode ser iterado;
    - Um objeto que retorna um dado, sendo um elemento por vez quando uma função next() é chamada;

Iterable -->
    - Um objeto que irá retorna um iterator quando a função iter() for chamada.

-------------------------------------------------------------------------------------------------------------------------
nome = 'Geek'  # É um iterable  mas não é um iterator.
numeros = [1, 2, 3, 4, 5, ] # É um iterable  mas não é um iterator.

it1 = iter(nome)
it2 = iter(numeros)

print(next(iter1))
print(next(iter1))
print(next(iter1))
print(next(iter1))

print(next(iter2))
print(next(iter2))
print(next(iter2))
print(next(iter2))
-------------------------------------------------------------------------------------------------------------------------
"""

nome = 'Geek'

for letra in nome:
    print(f'{letra}')