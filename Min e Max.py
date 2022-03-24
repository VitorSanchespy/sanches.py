"""
Mim e Max

max() --> Retorna o maior valor em um iterável ou o maior de dois ou mais elemnetos

min90

------------------------------------------------------------------------------------------------------------------------
# Exemplos
lista = [1, 2, 4, 61, 71, 90, 91, 12, 51, 31, 111, 512,]
print(max(lista))

tupla = (1, 2, 4, 61, 71, 90, 91, 12, 51, 31, 111, 512,)
print(max(tupla))

set = {1, 2, 4, 61, 71, 90, 91, 12, 51, 31, 111, 512,}
print(max(set))

dicionario = {"a": 1, 'b':2, 'c':4, 'd':61, 'e':71, 'f':90, 'g':91, 'h':12, 'i':51, 'j':31, 'k':111, 'l':512,}
print(max(dicionario))

dicionario = {"a": 1, 'b':2, 'c':4, 'd':61, 'e':71, 'f':90, 'g':91, 'h':12, 'i':51, 'j':31, 'k':111, 'l':512,}
print(max(dicionario.values()))

------------------------------------------------------------------------------------------------------------------------
# Faça um programa que receba dois valores do usuário e mostre o maior

va1 = int(input('Informe o primeiro valor: '))
va2 = int(input('Informe o segundo valor: '))

print(max(va1, va2))

------------------------------------------------------------------------------------------------------------------------
print(max(4, 67, 54))
print(max('a', 'ab', 'abc'))
print(max('a', 'b', 'g', 't'))
print(max(3.14, 5.31, 5.12))
print(max('Geek University'))

------------------------------------------------------------------------------------------------------------------------
min() --> Retorna o menor valor em um iterável ou o menor de dois  ou mais elementos

# Exemplos
lista = [1, 2, 4, 61, 71, 90, 91, 12, 51, 31, 111, 512,]
print(min(lista))

tupla = (1, 2, 4, 61, 71, 90, 91, 12, 51, 31, 111, 512,)
print(min(tupla))

set = {1, 2, 4, 61, 71, 90, 91, 12, 51, 31, 111, 512,}
print(min(set))

dicionario = {"a": 1, 'b':2, 'c':4, 'd':61, 'e':71, 'f':90, 'g':91, 'h':12, 'i':51, 'j':31, 'k':111, 'l':512,}
print(min(dicionario))

dicionario = {"a": 1, 'b':2, 'c':4, 'd':61, 'e':71, 'f':90, 'g':91, 'h':12, 'i':51, 'j':31, 'k':111, 'l':512,}
print(min(dicionario.values()))

va1 = int(input('Informe o primeiro valor: '))
va2 = int(input('Informe o segundo valor: '))

print(min(va1, va2))

------------------------------------------------------------------------------------------------------------------------
# Outros exemplos
nomes = ['Andreia', 'Vanessa', 'Joelma', 'Judit', 'Giovana', 'Ana']
print(max(nomes))   # Vanessa
print(min(nomes))   # Ana

print(max(nomes, key=lambda nome: len(nome)))  # Andreia

print(min(nomes, key=lambda nome: len(nome))) # Ana

------------------------------------------------------------------------------------------------------------------------


"""
musicas = [
    {'titulo':'Prepara', 'tocou':3},
    {'titulo':'Vai passar mal', 'tocou':2},
    {'titulo':'Olha o tuim', 'tocou':4},
    {'titulo':'Bolsonaro estourado', 'tocou':31},
]
print(max(musicas, key=lambda musica: musica['tocou']))
print(min(musicas, key=lambda musica: musica['tocou']))

# Desafio! Imprima somente o titulo da musica mais e menos tocada

print(max(musicas, key=lambda musica: musica ['tocou'])['titulo'])
print(min(musicas, key=lambda musica: musica['tocou'])['titulo'])

# Desafio! Como encontrar a musica mais tocada e a menos tocada sem usar max min e lambda

max = 0
for musica in musicas:
    if musica['tocou'] > max:
        max = musica['tocou']

for musica in musicas:
    if musica ['tocou'] == max:
        print(musica['titulo'])


min = 9999
for musica in musicas:
    if musica['tocou'] < min:
        min = musica['tocou']
for musica in musicas:
    if musica ['tocou'] == min:
        print(musica['titulo'])


















