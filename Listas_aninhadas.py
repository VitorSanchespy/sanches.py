"""
Listas aninhadas (Nested Lists)

- Algumas linguagem de programação (C / Java) possuem uma estrutura de dados chamadas de Arrays:
    - Unidimensionais (Array / Vetores);
    - Multidimensionais (Matrizes);

Em Python nós temos as Listas

numeros = [1, 'b', 2.23, 'True', 3, 4, 5]

---------------------------------------------------------------------------------------------------------

print(listas)

print(type(listas))

# Como fazemos para acessar os dados?
print(listas[0] [0]) # Linha [], Coluna [] ---- # 2
print(listas[2] [1]) # 8

----------------------------------------------------------------------------------------------------------
# Iterando com Loops em uma lista aninhada
for lista in listas:
    for num in lista:
       print(num)

-------------------------------------------------------------------------------------------------------------
# Exemplos
listas = [[1, 2, 3], [4, 5, 6], [7, 8, 9]] # Matriz 3 x 3

# List Comprehension
[[print(valor) for valor in lista] for lista in listas]

------------------------------------------------------------------------------------------------------------------


"""
# Outros exemplos

# Gerando um tabuleiro / matriz  3x3
                # Linhas                                Colunas
tabuleiro = [[numero for numero in range (1, 4)] for valor in range(1, 4)]
print(tabuleiro)

# Gerando jogadas para o jogo da velha
velha = [['X' if numero % 2 == 0 else 'O' for numero in range(1, 4)]for valor in range (1, 4)]
print(velha)

# Gerando valores iniciais
print([['*' for i in range(1, 4)]for j in range(1, 4)])
