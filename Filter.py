"""
Filter

filter() ->  Serve para filtrar dados de uma determinada coleção.

valores = 1, 2, 3, 4, 5, 6
media = sum(valores) / len(valores)
print(media)

--------------------------------------------------------------------------------
# Biblioteca para trabalhar com dados estatístico
import statistics

# Dados coletados de algum sensor
dados = [1.3, 0.5, 5.19, 8, 15, 1.5, 5.8, 9.5, -0.1,]

# Calculando a média dos dados utilzando a função mean()
media = statistics.mean(dados)

print(f'Média: {media}')
# OBS: Assim como a função map(), a filter() recebe dois parâmetros, sendo
# Uma função e um iterável.

res = filter(lambda valor: valor > media, dados)
print(list(res))

# OBS: Assim como na função map(), após ser utlizados os dado de filter ele são excluidos da memória.

----------------------------------------------------------------------------------------------------------------
paises  = ['','Brasil', 'Chile', '','Colombia', '', 'Equador', '', '', 'Venezuela']
print(paises)
res = filter(None, paises)
print(list(res))

---------------------------------------------------------------------------------------------------------------
paises  = ['','Brasil', 'Chile', '','Colombia', '', 'Equador', '', '', 'Venezuela']

# res = filter(lambda x: x != '' , paises)
#res = filter(lambda pais: len(pais)> 0, paises)
res = filter(None, paises)
print(list(res))

--------------------------------------------------------------------------------------------------------------------------------------------
# filter() or True or False
# mapa() retorna valores

# A diferença entre map() e filter() é
# map() --> Recebe dois parâmetros, uma função e um iterável e retorna um objeto mapeando a função para cada elemento do iterável.

# filter() --> Recebe dois parâmetros, uma função e um iterável e retorna um objeto filtrando apenas os elementos de acordo com a função.

---------------------------------------------------------------------------------------------------------------------------------------------
# Exemplo mais complexo

usuarios = [
    {'username': 'samuel', 'tweets':['Eu adoro bolos', 'Eu adoro pizzas']},
    {'username': 'carla', 'tweets':['Eu amo meu gato']},
    {'username': 'jheff', 'tweets':[]},
    {'username': 'bobmonograma', 'tweets':[]},
    {'username': 'doggo', 'tweets': ['Eu gosto de cachorro', 'Eu vou sair hoje']},
    {'username': 'gau', 'tweets': []},
]
print(usuarios)
# Filtrar os usúarios que estão inativos no Twitter
# Forma 1
# inativos = list(filter(lambda u: len(u['tweets']) == 0, usuarios))
# print(inativos)

# Forma 2
inativos = list(filter(lambda u: not  (u['tweets']), usuarios))
print(inativos)

-------------------------------------------------------------------------------------------------------------------------------

"""
# Combinar filter() e map()
nomes = ['Vanessa','Ana', 'Maria']
# Devemos criar uma lista contendo 'Sua instrutora é' +nome, desde que cada nome tenha menos de 5 caracteres

lista = list(map(lambda nome:  f'Sua instrutora é {nome}', filter(lambda nome: len(nome)<5,nomes)))
print(lista)















