#desafio de codido, verificar o estado das pernas levantadas do papagaio e informar que lingua ele fala

while True: 
    try: 
        estado = input()

        if estado == 'esquerda':
            print ('ingles')

        elif estado == 'direita':
            print ('frances')

        elif estado == 'nenhuma':
            print('portugues')
        
        elif estado == 'ambas':
            print('caiu')
    except EOFError: 
        break