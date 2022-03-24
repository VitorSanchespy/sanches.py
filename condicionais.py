"""
---------------Estruturas condicionais--------------
if, else, elif (else if)

----------Estrutura condicional if, e else em C------------
if (idade < 18){
    printf('Menor de idade');
} else if (idade == 18 ) {
    printf('Tem 18 anos');
} else {
    printf('Maior de idade');
}

----------Estrutura condicional if, e else em Java------------
if (idade < 18){
    System.out.println('Menor de idade');
} else if (idade == 18 ) {
    System.out.println('Tem 18 anos');
} else {
    System.out.println('Maior de idade');
}

"""

idade = int(input('Digite sua idade '))
if idade < 18:
    print(f'Você tem {idade} anos e é menor de idade')
elif idade == 18:
    print(f'Você tem {idade} anos ')
elif idade >= 40:
    print(f'Você tem {idade} anos ta veio em ')
else:
    print(f'Você tem {idade} anos e é maior de idade')
