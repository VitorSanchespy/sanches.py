"""
**Kwargs

Poderiamos chamar esse parâmetro **xis, mas por conveção chamamos de **kwargs

Este é só mais um parâmetro, mas diferente do *args que coloca os valores extras
em uma tupla, o **kwargs exige que utilizemos parâmetros nomeados, e transforma esses
parâmetros extras em um dicionário.

------------------------------------------------------------------------------------------------------
# Exemplos
def cores_favoritas(**kwargs): # Dicionário
    for pessoa, cor in kwargs.items():
        print(f'A cor favorida de {pessoa.upper()} é {cor} ')

cores_favoritas(Marcos='verde', Julia='amarelo', Fernanda='Azul', Vanessa='Branco')

# OBS: Os parâmetros *args e **kwargs não são obrigatórios.
cores_favoritas()
cores_favoritas(gekk='navy')

----------------------------------------------------------------------------------------------------------
# Exemplos mais complexos
def cumprimento_especial(**kwargs):
    if 'geek' in kwargs and kwargs['geek'] == 'Python':
        return 'Você recebeu um cumprimento Pythônico Geek!'
    elif 'geek' in kwargs:
        return f'{kwargs["geek"]} Geek!'
    return 'Não tenho certeza de quem você é...'
print(cumprimento_especial())
print(cumprimento_especial(geek='Python'))
print(cumprimento_especial(geek='oi'))
print(cumprimento_especial(geek='especial'))

----------------------------------------------------------------------------------------------------------------
# Nas nossas funções, podemos ter (NESTA ORDEM)
# - Parâmetros obrigatórios;
# - *args ;
# - Parâmetros default (não obrigatórios);
# - **kwargs


------------------------------------------------------------------------------------------------------------
def minha_funcao(idade, nome, *args, solteiro=False, **kwargs):
    print(f'{nome} tem {idade} anos ')
    print(*args)
    if solteiro:
        print(solteiro)
    else:
        print('Casado')
    print(kwargs)

minha_funcao(8, 'Julia')
minha_funcao(18, 'Felicity', 4, 5, 3, solteiro=True)
minha_funcao(34, 'Felipe', eu='Não', voce='Vai')
minha_funcao(19, 'Carla', 9, 4, 3, java =False, python=True)

----------------------------------------------------------------------------------------------------------------
# Entenda o por quê é importante manter a ordem dos parâmetros na declaração

# Função com ordem correta de parâmetros

#def mostra_info(a, b,  *args, instrutor='Geek', **kwargs):
#   return [a, b, args, instrutor, kwargs]

# Função com a ordem incorreta de parâmetros
def mostra_info(a, b, instrutor='Geek',  *args, **kwargs):
   return [a, b, args, instrutor, kwargs]
(
a = 1
b = 2
args = (3,)
instruto = 'Geek'
kwargs = {sobrenome: 'University' cargo: 'Instrutor'}
)
print(mostra_info(1, 2, 3, sobrenome='Universtity', cargo='Instrutor'))

--------------------------------------------------------------------------------------------------------------
# Desenpacotar com **kwargs
def motra_nome(**kwargs):
    return f'{kwargs["nome"]}{kwargs["sobrenome"]}'

nomes ={'nome':'Felicity ', 'sobrenome': 'Jones'}
print(motra_nome(nome='Felicity ', sobrenome='Jones'))
print(motra_nome(**nomes))


-----------------------------------------------------------------------------------------------------------


"""
def soma_multiplos_numeros(a, b, c, **kwargs):
    print(a + b + c)

lista = [1, 2, 3]
tupla = (1, 2, 3)
conjunto = {1, 2, 3,}
soma_multiplos_numeros(*lista)
soma_multiplos_numeros(*tupla)
soma_multiplos_numeros(*conjunto)

dicionario = dict (a=1, b=2, c=3)
soma_multiplos_numeros(**dicionario)

# OBS: Os nomes da chave em um dincionário devem ser os mesmos dos parâmetros da função
# dicionario = dict (d=1, e=2, f=3)
# soma_multiplos_numeros(**dicionario)

dicionario = dict (a=1, b=2, c=3, nome='Geek')

soma_multiplos_numeros(**dicionario, lang='Python')
