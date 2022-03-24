"""
Estruturas Logicas: and (e), or (ou), not (não), is (é)

Operadores Unários:
    - not;
Operadores binários:
    - and, or, is;

------------Regras para funcionamento-------------------
Para o 'and', ambos os valores precisam ser True (+ +)
Para o 'or', um ou outro valor precisa ser True  + - nega(- -)
Para o 'not', o valor do booleano é invertido, ou seja se for True, vira False, se for False ele vira True
Para o 'is', o valor é comparado com um segundo.
--------------------- and----------------
ativo = True
logado = True

if ativo and logado:
    print('Bem-vindo(a) usuário!')
else:
    print('Você precisa ativar sua conta. Por favor cheque seu e-mail')

------------------- or ---------------
ativo = True
logado = False

if ativo or logado:
    print('Bem-vindo(a) usuário!')
else:
    print('Você precisa ativar sua conta. Por favor cheque seu e-mail')

-------------------- not -------------------
ativo = True
logado = False
# Se não estiver ativo
if not ativo: # Se não for ativo (-,-)
    print('Você precisa ativar sua conta. Por favor, cheque seu e-mail')
else: # Senão
    print('Bem-vindo(a) usuário')

print(not True)
---------------------------- is --------------------
ativo = True
logado = False

if ativo is False :
    print('Você precisa ativar sua conta. Por favor, cheque seu e-mail')
else: # Senão
    print('Bem-vindo(a) usuário')
"""

ativo = True
logado = False

if ativo :
    print('Bem-vindo(a) usuário')
else: # Senão
    print('Você precisa ativar sua conta. Por favor, cheque seu e-mail')

# Ativo é verdadeiro?
print(ativo is True)


