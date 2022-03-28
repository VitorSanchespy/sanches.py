def funcao1():
    print('Geek University - primeiro.py')

if __name__ =="__main__":
    funcao1()
    print('Primeiro.py está sendo executado diretamente.')
else:
    print(f'Primeiro.py foi importado.{__name__}')