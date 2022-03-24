"""
Definindo Funções

- Funções são pequenas partes de código que realizam tarefas específicas;
- Pode ou não receber entradas de dados e retornar uma saida de dados:
- Muitos uteis para execultar procedimentos similares por repetidas vezes;

OBS: Se você escrever uma função que realiza várias tarefas dentro dela;
é bom fazer uma verificação para que a função seja simplificada.

Já utilizamos varias funções desde que íniciamos este curso:
- print()
- len()
- max()
- min()
- count()
- e muitas outras;

"""
# Exemplo de utilização de funções:
#cores = ['verde','amarelo','azul','branco','preto']

# Utilizando a função integrada (Buil-in) do Python print()

# print(cores)

#curso = 'Programação em Python: Essencial'
# print(curso)

#cores.append('roxo') # adicionar na lista
# print(cores)

# curso.append('Mais daods') # AttributeError

#cores.clear() # Lista
# print(cores)

# print(help(print))

# DRY - Don't Repeat Yourself - Não repita você mesmo / Não repita seu código.

# Mas então, como defeinir funções?
"""
Em Python a forma geral de definir uma função é:

def nome_da_funcao( parametros_de_entrada ):
    bloco_da_função
        
Onde: 

nome_da_funcao -> SEMPRE, com letras minúsculas, e se for nome composto, separado por undeline ( Snake Case ) ;
parametros_de_entrada -> Opcionais, onde tendo mais de um, cada um separado por vírgula, podendo ser opcionais ou não;
bloco_da_funcao -> Também chamado de corpo da função ou implementação. É onde o processamento da função acontece.
Neste bloco, pode ter ou não retorno da função.

OBS: Veja que para definir uma função, utilizamos a palavra reservada 'def' informando ao Python que 
estamos definindo uma função. Também abrimos o bloco de códigos com o já conhecidos dois pontos : que é
utilizado em Python para definir blocos. 

"""
# Definindo a primeira função
# - Definição
def diz_oi():
    print('Oi!')


"""
OBS:
1 - Veja que, dentro das nossas funções podemos utilizar outras funções:
2 - Veja que nossa função só executa 1 tarefa, ou seja a única coisa que ela faz é dizer oi;
3 - Veja que esta função não recebe nenhum parâmetro de entrada;
4 - Vej que esta função não retorna nada;
"""
# Utilizando funções

# Chamada de execução
# diz_oi()

"""
ATENÇÃO:

Nunca esqueça de utilizar o parênteses ao execultar uma função.

Exemplo:

#ERRADO!!
diz_oi

# CERTO
diz_oi()

# ERRADO!!
diz_oi ()
"""
# Exemplo - 2
def cantar_parabens():
    print('Parabens pra você ')
    print('Nesta data querida ')
    print('Muitas felicidades ')
    print('Muitos anos de vida ')
    print('Viva o aniversariante! ')

# 0, 1, 2, 3, 4
#for n in range(5):
#    cantar_parabens()

# Em python, podemos inclusive criar variáveis do tipo de uma função e execultar está função atravez da variável

canta = cantar_parabens
canta()
