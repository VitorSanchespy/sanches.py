"""
Generator Expression

Em aulas anteriores nós estudamos:
- List Comprehension;
- Dictionary Comprehension;
- Set Comprehension;

Não vimos:
- Tuple Comprehension ... porque elas se chamam Generators

nome = ['Carlos', 'Camilia', 'Carla', 'Cristina', 'Vanessa']

print(any(nome[0] == 'C' for nome in nomes)

---------------------------------------------------------------------------------------------------------------------------
# Poderiamos ter feito utilizando  Generators
nomes = ['Carlos', 'Camilia', 'Carla', 'Cristina', 'Vanessa']
print(any((nome[0] == 'C' for nome in nomes)))

# List Comprehension
res = [nome[0] == 'C' for nome in nomes]
print(type(res))
print(res)

# Generator
res = (nome[0] == 'C' for nome in nomes) # Parênteses
print(type(res))
print(res)

------------------------------------------------------------------------------------------------------------------------
# Qual é a utilidade de getsizeof()? --> Retorna a quantidade de bytes em memória do elemento passado como parâmetro
from sys import getsizeof

# Mostra quantos bytes a string 'Geek' está ocupando em memória. Quanto maior a string, mais espaço ocupa.
print(getsizeof('Geek'))
print(getsizeof('University'))
print(getsizeof(9))
print(getsizeof(91))
print(getsizeof(921839218491251))
print(getsizeof(True))

-------------------------------------------------------------------------------------------------------------------------
from sys import getsizeof

# Gerando uma lista de números com list com List Comprehension
list_comp = getsizeof([x * 10 for x in range(1000)])

# Gerando uma lista de números com list com Set Comprehension
set_comp = getsizeof({x * 10 for x in range(1000)})

# Gerando uma lista de números com list com Dictinary Comprehension
dic_comp = getsizeof({x: x * 10 for x in range(1000)})

# Gerando uma lista de números com Generator
gen_comp = getsizeof((x * 10 for x in range(1000)))

print('Para fazer a mesma tarefa gastamos em memória: ')
print(f'List Comprehension: {list_comp} bytes')
print(f'Set Comprehension: {set_comp} bytes')
print(f'Dict Comprehension: {dic_comp} bytes')
print(f'List Comprehension: {gen_comp} bytes')

-------------------------------------------------------------------------------------------------------------------------


"""
# Eu posso iterár no Generator Expression? SIM!

gen_comp = (x * 10 for x in range(1000))
print(gen_comp)
print(type(gen_comp))
for num in gen_comp:
    print(num)









