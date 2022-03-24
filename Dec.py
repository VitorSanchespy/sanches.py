"""
Módulo collections - Deque

Podemos dizer que o deque é uma lista de alta performance. (Lista)


"""
# Importa
from collections import deque

# Criando Deques
deq = deque('Geek')
print(deq)

# Adicionando elementos no deque
deq.append('y')  # Adiciona no final
print(deq)

deq.appendleft('k') # Adiciona no começo
print(deq)

# Remover elementos
print(deq.pop()) # Remove  o ultimo elemento
print(deq)

print(deq.popleft()) # Remove e retorna o primeiro elemento
print(deq)
