"""
Entendo o *ARGS

- O * args é um parâmetro como outro qualquer isso significa que você poderá
chamar de qualquer coisa, desde começa com asterísco.

Exemplo:

*xis

Mas por conveção, utilizamos *args para definí-lo

Mas oque  é o *args?

O parâmetro *args utilizado em uma função, coloca os valores extras informado como
entrada em um tupla. Então desde já lembre-se que tuplas são imútaveis.

--------------------------------------------------------------------------------------------------------
# Exemplos
def soma_todos_numeros(num1=1, num2=2, num3=3):
    return num1 + num2 + num3
print(soma_todos_numeros(4, 6, 9))

print(soma_todos_numeros(4, 6))
# print(soma_todos_numeros(4, 6, 9, 5)) # TypeError

----------------------------------------------------------------------------------------------------------
# Entendendo o *ARGS

def soma_todos_numeros(nome,email, *args):
    return sum (args)
print(soma_todos_numeros('Angelina','Jolie'))
print(soma_todos_numeros('Angelina','Jolie', 1, 2))
print(soma_todos_numeros('Angelina','Jolie', 4, 6, 10))
print(soma_todos_numeros('Angelina','Jolie', 10, 20, 3, 2, 3))

print(soma_todos_numeros('Angelina','Jolie', 23.5, 12.5))

----------------------------------------------------------------------------------------------------------------
# Outro exemplo de utilização do *args
def verifica_info(*args): # ARGS é uma TUPLA
    if 'Geek' in  args and 'University' in args:
        return 'Bem-vindo Geek'
    return 'Eu não tenho certeza qume você é ....'
print(verifica_info())
print(verifica_info(1, True, 'University', 'Geek'))
print(verifica_info(1, 'University', 3.145))

--------------------------------------------------------------------------------------------------------------------


"""


# Entendendo o *ARGS

def soma_todos_numeros(*args):
    print(args)
    return sum (args)
# print(soma_todos_numeros())
# print(soma_todos_numeros(4, 6, 10))

numeros = {1, 2, 3, 4, 5, 6,}

# Desempacotador

print(soma_todos_numeros(*numeros))

# OBS: O asteríscos serve para que informemos ao python que estamos passando como argumentos uma coleção de dados.
# Desta forma ele saberá que precisará antes desempacotar estes dados.

