"""
Any e All

All() --> Retorna True se todos os elementos do iterável são verdadeiros ou ainda se o iterável está vazio.

any() --> Retorna True se qualquer elemento do iterável for verdadeiro. Se o iterável estiver vazio, retorna False

# Exemplo  all()
print(all([0, 1, 2, 3, 4])) # Todos os numeros são verdadeiros? False [0]
print(all([ 1, 2, 3, 4])) # Todos os numeros são verdadeiros? True
print(all([])) # Todos os numeros são verdadeiros? True
print(all(( 1, 2, 3, 4))) # Todos os numeros são verdadeiros? True
print(all({ 1, 2, 3, 4})) # Todos os numeros são verdadeiros? True
print(all('Geek')) # Todos os numeros são verdadeiros? Trues

nomes = ['Carlos', 'Camilia', 'Carla', 'Cristina']
print(all([nome[0] == 'C' for nome in nomes]))

------------------------------------------------------------------------------------------------------------
# OBS: Um iterável vazio convertido em boolean é False. mas o all() entende como True
print(all([letra for letra in 'eio' if letra in 'aeuiou']))

---------------------------------------------------------------------------------------------------------------
print(all([num for num in [4, 2, 10, 6, 8] if num %2 ==0]))

--------------------------------------------------------------------------------------------------------------------
Any -->

"""
print(any([0, 1, 2, 3, 4])) # True
print(any([0, False, [], {}, ()])) # False
print(any([0, False, [], {}, (), 1])) # True

nomes = ['Carlos', 'Camilia', 'Carla', 'Cristina', 'Vanessa'] # varios
print(any(nome[0] == 'C' for nome in nomes))

print(any([num for num in [4, 2, 10, 6, 8, 9] if num % 2 == 0]))















