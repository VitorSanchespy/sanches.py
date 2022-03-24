"""
Módulo Colletions - Default Dict

Default Dict -> Ao Criar um dicionário utilizando - o, nós informamos um valor default,
podendo utilizar um lambda para isso. Esse valor será utilizado sempre que não houver
um valor definido. Caso tentemos acessar um chave que não existe, essa chave será
criada e o valor default será atribuído.

OBS: Lambdas são funções sem nome que podem ou não receber parâmetros de entrada e
e retornar valores.

dicionario = {'curso': 'Programação em Python: Essêncial'}
print(dicionario)
print(dicionario['curso']) #Value

print(dicionario['valor']) # ??? KeyError

--------------------------------------------------------------------


"""
# Fazendo import
from collections import defaultdict

dicionario = defaultdict(lambda: 0)

dicionario['curso'] = 'Prgramação em Python: Essêncial'
print(dicionario)

print(dicionario['outro']) # KeyError no dicionário comum, mas aqui não.
print(dicionario)



