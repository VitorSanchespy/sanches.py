""""
**Tipo booleano **

True

False

"""

ativo = False

print(ativo)

""""
#negação (not); **negação**

Fazendo a negação, se o valor booleano  for verdadeiro o resultado será falso se for falso,
se for falso  o resultado será verdadeiro, ou seja sempre o contrário"
"""

print(not ativo )

logado = True
print(logado)
# Ou (or)
"""
E uma operação binaria, ou seja, depende de dois valores. Ou um ou outro deve ser verdadeiro.

True or True  -> True
True or False ->True
False or True -> True 
False or False -> False 
"""

print(ativo or logado)

#E (and):
""" 
Também é uma operação binária, ou seja, depende de dois valores. Ambos os valores devem ser verdadeiros.

True and True --> True 
True and False --> False
False and True --> False
False and False --> False
"""

print(ativo and logado)