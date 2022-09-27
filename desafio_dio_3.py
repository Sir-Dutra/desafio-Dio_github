'''
Calcular o consumo em litros de um carro usando a distancia e a velocidade media
o carro faz 12km/litro
resultado em 3 casas decimais
'''

horas, velocidade_media= (input().split())

horas = int(horas)
velocidade_media = int(velocidade_media)


distancia =(horas * velocidade_media)

consumo = (distancia/12)

format_float = "{:.3f}".format(consumo)
print ( 
    format_float
     )



