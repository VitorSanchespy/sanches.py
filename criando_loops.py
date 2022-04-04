"""
Criando sua própria versão de loop

for num in [1, 2, 3, 4, 5]:
    print(num)

for letra in 'Geek University':
    print(letra)

iter([1, 2, 3, 4, 5])
iter('Geek University')

------------------------------------------------------------------------------------------------------------------------
"""
def melhor_loop(iteravel):
    it = iter(iteravel)
    while True:
        try:
            print(next(it))
        except StopIteration:
            break
melhor_loop('Geek university')

numeros = [1, 2, 3, 4, 5,]
melhor_loop(numeros)