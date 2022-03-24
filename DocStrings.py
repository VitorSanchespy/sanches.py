"""
Documentando funções com DocStrings

OBS: Podemos ter acesso a documentação de uma função em Python
utilizando a propriedade especial __doc__

Podemos ainda fazer acesso á documentação com a função help()
--------------------------------------------------------------------------------

"""
# Exemplos
def diz_oi():
    """ Uma função simples que retorna a string 'oi!' """
    return 'oi!'

def exporencial(numero,potencia=2):
    """
    Função quer retorna por padrão o quadrado de ' número ' ou ' número ' á ' potência ' informada.
    :param numero: Número que desejamos gerar o exporencial.
    :param potencia: Potência que queremos gerar o exporêncial. Por padrão é 2.
    :return: Retorna o exporência de ' número ' por ' potência '.
    """
    return numero ** potencia

