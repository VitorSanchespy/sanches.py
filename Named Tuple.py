"""
Módulo Collections - Named_Tuple

# Recap Tupla
tupla = (1, 2, 3,)
print(tupla[1])

Named Tuple -> São tuplas diferencidas, onde, especificamos um nome para a mesma e tabém parâmetros




"""
# Primeiro  IMPORT
from collections import namedtuple
# Precisamos definir o nome e parâmetros.

# Forma - 1  Declaração Named Tuple

cachorro = namedtuple('cachorro', 'idade raça nome')

# Forma - 2  Declaração Named Tuple

cachorro = namedtuple('cachorro', 'idade, raça, nome')

# Forma - 3  Declaração Named Tuple

cachorro = namedtuple('cachorro', ['idade', 'raça', 'nome'])

# Usando

ray = cachorro(idade=2, raça='Pug', nome='Ray')

print(ray)

# Acessando os dados

# Forma 1

print(ray[0])  # idade
print(ray[1])  # Nome
print(ray[2])  # raça

# Forma 2
print(ray.idade)  # idade
print(ray.nome)  # Nome
print(ray.raça)  # raça

print(ray.index('Pug'))
print(ray.count('Pug'))


