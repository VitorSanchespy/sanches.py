"""
Funções com parâmetro (entrada)
- Funções que recebem dados para serem procesados dentro da mesma:

Se a gente pensar em um programa qualquer, geralmente temos:
entrada -> processamento -> saida
Se agente pensar em uma função, já sabemos que temos funções que:
- Não possuem entrada;
- Não possuem saída;
- Posuem entrada mas não possuem saída;
- Não possuem entrada mas possuem saída;
- Possuem entrada e saida;
----------------------------------------------------------------------------
# Refatorando uma função
            # Parâmetro
def quadrado(numero):  # ( Entrada )
    return numero**2         # ( Processamento )
print(quadrado(8))        # ( Saida )
print(quadrado(6))      # ( Saida )
print(quadrado(4))    # ( Saida )

print(quadrado()) # TypeError

-----------------------------------------------------------------------------------
# Refatrando a função:
def cantar_parabens(aniversariante):
    print('Paranbés pra você')
    print('Nesta data querida')
    print('Muitas felicidades')
    print('Muitos anos de vida')
    print(f'Viva o(a){aniversariante}!')
cantar_parabens('Patricia')

----------------------------------------------------------------------------------------
# Funções podem ter n parâmetros de entrada. Ou seja podemos receber como entrada
# em uma função quantos parâmetros forem necessários. Eles são separados por vírgula.
        #( Parâmetro )
def soma(a, b):
    return a + b

def multiplicacao(num1,num2):
    return num1 * num2

def outra(num1, b, msg):
    return (num1 + b) * msg
        # ( Argumento )
print(soma(2, 5))
print(soma(10, 20))

print(multiplicacao(4, 5))
print(multiplicacao(2, 8))

print(outra(3, 2, 'Geek '))
print(outra(5, 4, 'Python '))

# OBS: Se a gente informar um número errado de parâmetro ou argumentos, teremos TypeError

# print(soma(3, 2, 5)) # TypeError - Passando argumentos a mais
# print(soma(4)) # TypeError - Passando argumentos a menos

-------------------------------------------------------------------------------------------------
# Nomeando Parâmetros
def nome_completo(nome, sobrenome):
    return f'seu nome completo é {nome} {sobrenome}'
                    # Argumentos
print(nome_completo('Angelina','Jolie'))

# A diferença entre Parâmetros e Argumentos

# Parâmetros são variáveis declaradas na definição de uma função;
# Argumentos são dados passados durante a execução de uma função;

# A ordem dos Parâmetros importa !
nome = 'Felicity'
sobrenome = 'Jonnes'
print(nome_completo(sobrenome, nome))

# Argumentos nomeados ( Keyword Arguments )

# Caso utilizemos nomes dos parâmetros nos argumentos para informá-los, podemos
# utilizar qualquer ordem.

print(nome_completo(nome='Angelina', sobrenome='Jolie'))
print(nome_completo(nome=nome, sobrenome=sobrenome))
print(nome_completo(sobrenome='Marques', nome='Marcia'))

-------------------------------------------------------------------------------------------

"""
# Erro Comum na utilização do return

def soma_impares(numeros):
    total = 0
    for num in numeros:
        if num % 2 != 0:
            total = total + num
    return total # Finalisa a função


lista = [1, 2, 3, 4, 5, 6, 7]
print(soma_impares(lista))

tupla = (1, 2, 3, 4, 5, 6, 7)
print(soma_impares(tupla))

