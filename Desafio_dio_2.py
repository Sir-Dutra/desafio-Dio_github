'''calcular a média de cachorros quentes comidos 
resultado em 2 casas decimais'''

participantes, numero_de_cachorros= (input().split())

participantes = int(participantes)
numero_de_cachorros = int(numero_de_cachorros)


resultado =(participantes/numero_de_cachorros)

format_float = "{:.2f}".format(resultado)
print ( 
    format_float
     )

