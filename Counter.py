"""
Módulo Collections - Counter ( Contador )

Collections -> High-performance - Container Datetypes

Counter -> Recebe um interável como parâmetro e cria um objeto do tipo Collections Counter que é parecido com um dicionário
contendo como chave o elemento da lista passada como parâmetro e como valor a quantidade de ocorrências desse elemento.

-------------------------------------------------------------------------------------------------------------------------------------
# Realizando o import
from collections import Counter

# Exemplo - 1

# Podemos utilizar qualquer iterável, aqui utilizamos uma lista
lista = [1, 1, 1, 1, 1, 2, 2, 2, 2, 3, 3, 3, 4, 4, 5,  45, 66, 53, ]

# Utilizando o Counter
res = Counter(lista)
print(res)
print(type(res))

# Counter({1: 5, 2: 4, 3: 3, 4: 2, 5: 1, 45: 1, 66: 1, 53: 1})
# Cada elemento declarado. o Counter cria uma chave e colocou como valor a quantidade de ocorrências.

# Exempos - 2
print(Counter('Geek University'))
# Counter({'e': 3, 'i': 2, 'G': 1, 'k': 1, ' ': 1, 'U': 1, 'n': 1, 'v': 1, 'r': 1, 's': 1, 't': 1, 'y': 1})

--------------------------------------------------------------------------------------------------------------

"""
from collections import Counter

# Exemplo - 3

texto = """Django (/ˈdʒæŋɡoʊ/ JANG-goh; sometimes stylized as django)[6] 
is a Python-based free and open-source web framework that follows the model–template–views 
(MTV) architectural pattern.[7][8] It is maintained by the Django Software Foundation (DSF),
an independent organization established in the US as a 501(c)(3) non-profit.
Django's primary goal is to ease the creation of complex,
database-driven websites. The framework emphasizes reusability and "pluggability" of components,
less code, low coupling, rapid development, and the principle of don't repeat yourself.[9] Python is used throughout, 
even for settings, files, and data models. Django also provides an optional administrative create, read, update and delete interface
that is generated dynamically through introspection and configured via admin models."""

palavra = texto.split()
#print(palavra)
res = Counter(palavra)
print(res)

# Encontrando as 5 palavras com mais ocrrências no texto
print(res.most_common(10))










