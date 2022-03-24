"""
Dicionários

OBS: Em algumas linguagem de programção, os dicionários python são conhecidos por mapas.

Dicionários são coleções do tipo chave/valor.

Dicionário são represntados por chaves {}.

[0, 1, 2, 3, 4, 5,] - indice ( Chave )
[1, 2, 3, 4, 5, 6,] - valor

print(type({}))

OBS: Sobre dicionários
    - Chave e valor são separados por 'Chave:valor';
    - Tanto chave quanto valor podem ser de qualquer tipo de dado;
    - Podemos misturar tipo de dados;


------------------------------------------------------------------------------------
# Criação de dicionários

# Forma - 1 (Mais comum)

paises = {'br': 'Brasil', 'eua': 'Estados Unidos ', 'py': 'Paraguai ' }
print(paises)
print(type(paises))

# Forma - 2 (Menos comum)

paises = dict(br= 'Brasil', eua= 'Estados Unidos ', py= 'Paraguai ' )
print(paises)
print(type(paises))

"""
paises = {'br': 'Brasil', 'eua': 'Estados Unidos ', 'py': 'Paraguai ' }

# Acessando elementos

# Forma - 1 ( Acessando via chave, da mesma forma que lista/tupla )  ( Chave )

print(paises['br'])
print(paises['eua'])
print(paises['py'])
print(paises['ru']) # Errror
# OBS: Caso tentamos fazer um acesso utilizando uma chave que não existe, teremos o erro KeyError

# Forma - 2 ( Acessando via get - Recomendado )

print(paises.get('br'))
print(paises.get('eua'))
print(paises.get('py'))
print(paises.get('ru')) # None 


