'''definir a distancia, diametro 1 e diametro2
dividir a distancia pela soma do diametro 1 com o diametro 2
o resultado deve ter apenas 2 casas decimais'''

distancia, diametro_sauron, diametro_saruman = (input().split())

distancia = int(distancia)
diametro_sauron = int(diametro_sauron)
diametro_saruman = int(diametro_saruman)

resultado =(distancia / (diametro_sauron + diametro_saruman))

format_float = "{:.2f}".format(resultado)
print ( 
    format_float
     )

