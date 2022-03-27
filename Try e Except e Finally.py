"""
# Exemplo complexo ERRADO
def dividir(a, b):
    return a / b

#valor1=1
#valor2=1
try:
    valor1 = int(input('Digite o primerio valor: '))
    valor2 = int(input('Digite o segundo valor: '))
except ValueError:
    print('Valor precisa ser numérico')
try:
    print(dividir(valor1, valor2))
except NameError:
    print('Valor  incorreto')

---------------------------------------------------------------------------------------------------------------------------
# Exemplo complexo CORRETO
# OBS: Você é responsável pelo entrada das suas funções. Então, trate-as!
def dividir(a, b):
    try:
        return int(a) / int(b)
    except ValueError:
        return 'Valor Incorreto'
    except ZeroDivisionError:
        return 'Não é possivel realizar uma divisão por zero'

valor1 = input('Digite o primerio número ')
valor2 = input('Digite o segundo número ')
print(dividir(valor1, valor2))

---------------------------------------------------------------------------------------------------------------------------
# Exemplo complexo Genérico
# OBS: Você é responsável pelo entrada das suas funções. Então, trate-as!
def dividir(a, b):
    try:
        return int(a) / int(b)
    except :
        return 'Ocorreu um problema '


valor1 = input('Digite o primerio número ')
valor2 = input('Digite o segundo número ')
print(dividir(valor1, valor2))

---------------------------------------------------------------------------------------------------------------------------

"""
