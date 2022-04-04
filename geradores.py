"""
Geradores

 - Geradores(Geradores) são Iterators(Iteradores);

Obs: O contrarionão é verdadeiro. Ou seja, nem todo iterator é um generador.

Outras informações:
 - Generators podem ser criados com função geradoras;
 - Funções geradoras utilizam a palavra reservada yield;
 - Generators podem ser criados com Expressões Geradoras;

Diferenças entre funções e Generator Function (Funções Geradoras )

------------------------------------------------------------------------------------------
/ Funções                                        / Generator Functions                  /
------------------------------------------------------------------------------------------
/ Utilizam return                                / Utilizam  Yield                      /
-----------------------------------------------------------------------------------------
/ Retorna uma vez                                / Pode Utilizar Yield  Multiplas vezes /
-----------------------------------------------------------------------------------------
/ Quando Execultada, retorna um valor            /Quando Execultada Retorna um Generator/
-----------------------------------------------------------------------------------------
gen = conta_ate(5)

# print(type(gen))

print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))

------------------------------------------------------------------------------------------------------------------------
for num in gen:
    print(num)

------------------------------------------------------------------------------------------------------------------------
print(next(gen)) # 1

print('Geek University')

for num in gen:
    print(num)

------------------------------------------------------------------------------------------------------------------------
"""
# Exemplo Função Geradora (Generator Function)
def conta_ate(valor_maximo):
    contador = 1
    while contador <= valor_maximo:
        yield contador
        contador = contador+1
# OBS: Uma Generator Function não é um Generator. Ela gera um generador. ok?

gen = list(conta_ate(10))
print(gen)










