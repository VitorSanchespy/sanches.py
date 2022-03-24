"""
Loop While

Forma geral

while expressão_booleana:
    //execução do Loop

o bloco do while será repetido enquanto a expressão booleana for verdadeira.

Expressão Booleana é toda expressão onde o resultado é verdadeiro ou falso.

Exemplos:

num = 5

num < 10

# Exemplo 1

numero = 1

while numero < 10:
    print(numero)
    numero = numero + 1 # Linha de incremento do numero.

# OBS: Em um loop while, é importante que cuidemos do critério de parada para não causar um loop infinito.

---------------- C ou Java ---------------------
While(expressão){
    //execução
}

------ do while (C ou Java) ------------
do {
    //execução
}while(expressão);
"""
# Exemplo 2
resposta = ''
while resposta  != 'sim':
    resposta = input('Já acabou Jessica? ')

