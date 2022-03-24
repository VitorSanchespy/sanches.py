"""
Expressões Lambdas

Conhecidas por Expressões Lambdas, ou simplesmente Lambdas são funções sem nome, ou seja,
funções  anônimas.

---------------------------------------------------------------------------------------------
# Função em python
def funcao (x):
    return 3 * x +1
print(funcao(4))
print(funcao(7))

# Expressão Lambda
lambda x: 3 * x +1
# E como utilizar a expressão lambda?
calc = lambda x: 3 * x +1
print(calc(4))
print(calc(7))

----------------------------------------------------------------------------------------
# Podemos ter expreções lambdas com múltiplas entradas

nome_completo = lambda nome, sobrenome: nome.strip().title() + ' ' + sobrenome.strip().title()
print(nome_completo(' angelina', 'JOLIE'))
print(nome_completo(' Jones', 'FeLICITY'))

--------------------------------------------------------------------------------------------------
# Em funções Python podemos ter nenhuma ou variás entradas. Em lambdas também
amar = lambda :'Como não amar Python? '
uma = lambda x: 3 * x + 1
duas = lambda x,y:(x * y) **0.5
tres = lambda x, y, z: 3 / (1/x + 1/ y + 1/ z)
#   n = lambda x1, x1, ..., xn: < expressão >
print(amar())
print(uma(6))
print(duas(3, 7))
print(tres(3, 6, 9))

# OBS: Se passarmos  mais argumentos do que parâmetros esperados teremos TypeError

----------------------------------------------------------------------------------------------------------
# Outro Exemplo
autores = ['Issac Asimov','Times Gret','Peter Aqui', 'Robert JR. Peper', 'Arthur R. Durval', 'Orlean Jayce', 'Douglas Solas', 'Vitor Braga Sanches']
print(autores)
autores.sort(key=lambda sobrenome: sobrenome.split('  ')[-1].lower())
print(autores)

------------------------------------------------------------------------------------------------------------


"""
# Função quadrática
# f(x) = a * x ** 2 + b * x + c
# Definindo a função
def geradora_funcoa_quadratica(a, b, c):
    """ Retorna a função c(x) =  a*x**2 + b*x + c"""
    return lambda x: a*x**2 + b*x + c
teste = geradora_funcoa_quadratica(2, 3, -5) # Valores para O ( A, B, C )
print(teste(0)) # Valores para o ( X )
print(teste(1))
print(teste(2))

print(geradora_funcoa_quadratica(1, 2, 3)(2))


# Função em python
def funcao (x):
    return 3 * x +1
print(funcao(4))
print(funcao(7))

# Expressão Lambda
lambda x: 3 * x +1
# E como utilizar a expressão lambda?
calc = lambda x: 3 * x +1
print(calc(4))
print(calc(7))