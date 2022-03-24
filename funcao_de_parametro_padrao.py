"""
Função com Parâmetro Padrão ( Default Paramters )
- Funções onde a passagem de parâmetro seja opicional;

# Exemplo de função onde a passagem de parâmetro seja opcional
print('Geek University')
print()

----------------------------------------------------------------------
# Exempo de função onde a passagem de parâmetro seja obrigatória
def quadrado(numero):
    return numero **2
print(quadrado(3))
print(quadrado()) # TypeError

----------------------------------------------------------------------------
def exporencia(numero=4, potencia=2):
    return numero ** potencia
print(exporencia(2, 3))
print(exporencia(3, 2))
print(exporencia(3)) # Por padrão eleve ao quadrado
print(exporencia(3, 5)) # Eleva ao potência informada pelo usuário

# OBS:
# Se o usuário passar somente 1 argumento, este será atribuído ao parâmetro numero, e será calculado o quadrado deste número:
# Se o usuário passar 2 argumentos, o primeiro será atribuído ao parãmetro numero e o segundo ao parâmetro potência. Então
# será calculada está potência.

print(exporencia())

-----------------------------------------------------------------------------------------------------
# OBS: Em função Python, os parâmetros com valores default ( Padrão ) DEVEM SEMPRE estar  ao final da declaração.

# ERRO!!
def teste(num=2, potencia):
    return num ** potencia
print(teste(6))

-----------------------------------------------------------------------------------------------------------
# Outros Exemplos:
def soma(num1=5, num2=3):
    return num1+num2
print(soma(4,3))
print(soma(4))
print(soma())

---------------------------------------------------------------------------------------------------------------
# Exemplo mis complexo:
def mostra_informacao(nome='Geek', instrutor=False):
    if nome == 'Geek' and instrutor: # 2 - Nome Geek, Instrutor TRUE
        return 'Bem-vindo instrutor Geek!'
    elif nome == 'Geek': # - 1
        return 'Eu pensei que você fosse o instrutor '
    return f'Olá {nome} ' # 3 -
print(mostra_informacao()) # 1 - Nome = Geek, Instrutor = False
print(mostra_informacao(instrutor=True))  #True Apenas no instrutor
print(mostra_informacao(True))
print(mostra_informacao('Ozzy')) # Nome não é Geek
print(mostra_informacao(nome='Tifanny'))

-------------------------------------------------------------------------------------------------
# Por quê utilizar parâmetros com valor default?
# - Nós permite ser mais flexiveis nas funções;
# - Evita erros com parâmetros incorretos;
# - Nós permite trabalhar com exemplos mais legíveis de códigos;

# Quais tipos de dados podemos utilizar como valores default para parâmetros?
# - Qualquer tipo de dados:
    # Números - Strings - Floats - Booleano - Listas - Tuplas - Dicionários - Funções e etc...;
-----------------------------------------------------------------------------------------------------
# Exemplos
def soma(num1, num2):
    return num1 + num2
def mat (num1, num2, fun=soma):
    return fun(num1, num2)
def subtracao (num1,num2):
    return num1 - num2
print(mat(2,3))
print(mat(2,2, subtracao))

---------------------------------------------------------------------------------------------------------
# Escopo - Evitar problemas e confusões...

# Variáveis globais
# Variáveis locais

instrutor = 'Geek' # Variável Global
def diz_oi():
    instrutor = 'Python' # Variável Local
    return f'Oi {instrutor}'
print(diz_oi())

# OBS: Se tivermos uma variável local com o mesmo nome de uma variável global, a local terá preferência.

def diz_oi():
    prof ='Geek' # Variável Local
    return f'Olá {prof}'
print(diz_oi())
print(prof) # NameError

------------------------------------------------------------------------------------------------------------
# ATENÇÂO com variáveis Globais (Se puder evitar, Evite)

total = 0

def incremento():
    total = total + 1 # UnboundLocalError (A variável local está sendo utilizada para processamento sem ter sido inicializada)
    return total
print(incremento())

-----------------------------------------------------------------------------------------------------------------
# ATENÇÂO com variáveis Globais (Se puder evitar, Evite)

total = 0

def incremento():
    global total # AVISANDO que queremos utilizar a variável global
    total = total + 1
    return total
print(incremento())
print(incremento())
print(incremento())

-----------------------------------------------------------------------------------------------------------------
# Podemos ter funções que são declaradas dentro de funções, e também tem um forma especial de escopo de variável
def fora():
    contador = 0
    def dentro():
        nonlocal contador
        contador = contador + 1
        return contador
    return dentro()

print(fora())
print(fora())
print(fora())
print(dentro) # NameError
"""






