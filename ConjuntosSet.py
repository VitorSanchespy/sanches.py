"""
Conjuntos

- Conjuntos em qualquer linguagem de programação estamos fazendo referência à Teoria dos Conjuntos da Matemática.

- Aqui no Python, os conjuntos são chamados de Sets.

Dito isso, da mesma forma que na matemática:

- Sets (conjuntos) não possuem valores duplicdos;
- Sets (conjuntos) não possuem valores ordenados;
- Elementos não são acessados via índices, ou seja, conjuntos não são índexados;

COnjuntos são bons para se utilizar quando precisamos armazenar elementos
mas não nos importamos com a ordenação deles, Quando não precisamos se preucupar
com chaves, valores e ítens duplicados.

Os conjuntos (sets) são referênciados em Python com chaves {}

Diferença entre Conjuntos (sets) e Mapas (Dicionários) em Python:
    - Um dicionário tem  chave/valor
    - Um conjunto tem apenas valor;

-------------------------------------------------------------------
# Definindo um conjunto:

# Forma - 1

s = set({1, 2, 3, 4, 5, 5, 6, 7, 2, 3,}) # Repare que temos valores repetidos.
print(s)
print(type(s))

# OBS: AO criar um conjunto, caso seja adicionado um valor já existente,
# o mesmo será ignorado sem gerar erros enão fara parte do conjunto

# Forma - 2 =  Mais comum

s = set({1, 2, 3, 4, 5, 5})
print(s)
print(type(s))

# Podemos verificar se determinado elemento está contido no conjunto

if 3 in s:
    print('Tem o 3')
else:
    print('Não tem o 3')

---------------------------------------------------------------------------
#Importante lembrar que, além de não termos valores duplicados, não temos ordem

# Listas aceitam valores duplicados, então temos 10 elementos
lista = [99, 2, 34, 23, 2, 12, 1, 44, 5, 34]
print(f'lista: {lista} com {len(lista)} elementos')

# Tuplas aceitam valores duplicados, então temos 10 elementos
tupla = (99, 2, 34, 23, 2, 12, 1, 44, 5, 34)
print(f'Tupla: {tupla} com {len(tupla)} elementos')

# Dicionários não aceitam chaves duplicados, então temos 8 elementos
dicionario = {}.fromkeys([99, 2, 34, 23, 2, 12, 1, 44, 5, 34], 'dict') # Não repete chaves
print(f'Dicionário: {dicionario} com {len(dicionario)} elementos')

# Conjuntos não aceitam valores duplicados, então temos 8 elementos
conjunto = {99, 2, 34, 23, 2, 12, 1, 44, 5, 34}  # Não repete valores
print(f'Conjunto: {conjunto} com {len(conjunto)} elementos')

----------------------------------------------------------------------------------------
# Assim como todos outros conjuntos Python podemos colocar tipos de dados misturados em Sets

s = {1, 'b', True, 34.22, 44}
print(s)
print(type(s))

# Podemos Iterar em um set normalmente
for valor in s:
    print(valor)

--------------------------------------------------------------------------------------
# Usos interessantes com sets

# Imagine que fizemos um formulário de castro de vizitantes em uma feira ou museu, e os visitantes
# informam manualmente a cidade de onde vieram.

# Nós adicionamos cada cidade em um lista python, já que em uma lista podemos adicionar novos elementos
# e ter repetição.

cidades = ['Bela Horizonte', 'São Paulo', 'Campo Grande', 'Cuíaba', 'Campo Grande', 'São Paulo', 'Cuíaba']
print(cidades)
print(len(cidades))

# Agora precisamos saber quantas cidades distintas, ou seja, unícas, temos.

# O que você faria? Faria um Loop na lista ...?

# Podemos utilizar o set para isso:

print(len(set(cidades)))

--------------------------------------------------------------------------------------
#Adicionando elementos em um conjunto
s = {1, 2, 3}
s.add(4)
s.add(4)  # Duplicidade não gera erro. Simplismente é ignorado e não é adicionado.
print(s)
print(type(s))

-----------------------------------------------------------------------------------------
# Remover elementos em um conjunto
s = {1, 2, 3}
print(s)

# Forma - 1

s.remove(3)  # Não é índice! Informamos o valor a ser removido.
print(s)
# OBS: Caso o valor não seja encontrado será gerado o erro KeyError. Nenhum valor é retornado.

# Forma - 2

s.discard(22)
print(s)

# OBS: Se o valor não for encontrado, nenhum erro é gerado.

------------------------------------------------------------------------------------------------
# Copiando um conjunto para outro ...

s = {1, 2, 3}
print(s)

# Forma 1 - Deep Copy
nova = s.copy()
print(nova)

nova.add(4)
print(nova)
print(s)

--------------------------------------------------------------------------------------------------
# Forma 2 - Shalow Copy
s = {1, 2, 3}
print(s)

novo = s
novo.add(4)
print(novo)
print(s)

---------------------------------------------------------------------------------------------
s = {1, 2, 3}
print(s)

# Podemos remover todos os ítems de um conjunto
s.clear()
print(s)

------------------------------------------------------------------------------------------------
# Precisamos gerar um conjunto com nomes de estudantes únicos

estudantes_python = {'Marcos', 'Patricia', 'Helen', 'Pedro', 'Julia', 'Guilherme'}
estudantes_java = {'Fernando', 'Gustavo', 'Julia', 'Ana', 'Patricia'}

# Forma 1 - Utilizando union
unicos1 = estudantes_python.union(estudantes_java)
print(unicos1)

# Forma 2 - Utilizando o caractere  pipe ( | )
unicos2 = estudantes_python | estudantes_java
print(unicos2)

----------------------------------------------------------------------------------------------------
# Veja que alguns alunos que estudam Python também estudam Java.

# Gerar um conjunto de estudantes que estão em ambos os cursos

# Forma 1 - Utilizando intersection
ambos1 = estudantes_python.intersection(estudantes_java)
print(ambos1)

# Forma 2 - Utilizando o &
ambos2 = estudantes_python & estudantes_java
print(ambos2)

------------------------------------------------------------------------------------------------------
# Métodos Matemáticos de Conjuntos

# Imagine que temos dois conjuntos: um contendo estudantes do curso Python e um
# contendo estudantes do curso de java

# Gerar um conjunto de estudandtes que  não estão no outro
so_python = estudantes_python.difference(estudantes_java)
print(so_python)

so_java = estudantes_java.difference(estudantes_python)
print(so_java)

-------------------------------------------------------------------------------------------------------------

"""
# Soma*, Valor Máximo*, Valor Minímo*, Tamanho

# * Se os valores forem todos inteiros ou reais

s = {1, 2, 3, 4, 5, 6,}

print(sum(s))
print(max(s))
print(min(s))
print(len(s))

