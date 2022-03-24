"""
--------------- Loop for -----------------------
Loop -> Estrutura de repetição.
For -> Uma dessas estruturas

-------C ou Java-------

for(int i = 0; i < 10; i ++){
    //execução do loop
}

------------Python---------

for item in interavel:
    //execução do loop

Utilizamos loops para iterar sobre sequências ou sobre valores iteráveis

Exemplos de iteraveis
1  String
    nome = 'Geek University'
2  Lista
    lista = [1, 3, 5, 7, 9]
3  Range
    numeros = range (1, 10)

--------------------------------------------------------
print(hasattr(lista, '__iter__'))
for v in lista:
    print(v)
"""

"""
#Exemplos de for 1 (Iterando sobre uma String)
for letra in nome:
    print(letra)

#Exemplos de for 2 (Iterando sobre uma lista)
for numero in lista:
    print(numero)

# Exemplo de for 3 (Iterando sobre um range)

range(valor_inicial, valor_final)
OBS: o valor final não é inclusive.
1
2
3
4
5
6
7
8
9
10 - Não 

----------------------- Range -------------
for numero in range(1,10):
    print(numero)
"""

#--------------Iteráveis---------------
nome = 'Geek University'  #String
lista = [1, 3, 5, 7, 9] # lista
numero = range (1, 10) #Temos que transformar em uma lista



"""
Enumerate:
((0, 'G'), (1, 'e'), (2, 'e'), (3, 'k'), (4, ' '), (5, 'U')......)

for indice, letra in enumerate(nome):
    print(nome[indice])

for _, letra in enumerate(nome):
    print(letra)
    
OBS: Quando precisamos de um valor, podemos descartá-lo utilizando um underline (_) 

for valor in enumerate(nome):
    print(valor)
    
--------------------------------------------------------------
quantidade =  int(input('Quantas vezes esse loop deve rodar? '))
soma = 0

for n in range(1, quantidade+1):
    num = int(input(f'Informe  o {n}/{quantidade} valor: '))
    soma = soma + num
print(f'A soma é {soma}')
--------------- Java ------------
Sytem.out.println (letra)
System.out.print (letra)

--------------- C ----------------
printf("%s/n", letra)

-----------------------------------------
for letra in nome:
    print(letra, end='')

"""
nome = "Andreia"
for _ in range (3):
    for num in range(1, 11):
        print(f'{nome * num}')