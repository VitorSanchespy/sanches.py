import primeiro
def funcao2():
    primeiro.funcao1()

if __name__ == '__main__':
    funcao2()
    print('Segundo.py  está sendo execultado diretamente.')
else:
    print(f'Segundo.py foi importado.{__name__}')
