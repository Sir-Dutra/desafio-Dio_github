salario = int(input()) 


if salario <= 600:
    reajuste = salario + salario/100 * 17
    ganho = reajuste - salario
    print(f'Novo salario: {{:.2f}}'.format(reajuste))
    print(f'Reajuste ganho: {{:.2f}}'.format(ganho))
    print('\nEm percentual: 17%')

elif salario > 600 and salario <= 900:
    reajuste = salario + salario/100 * 13
    ganho = reajuste - salario
    print(f'Novo salario: {{:.2f}}'.format(reajuste))
    print(f'Reajuste ganho: {{:.2f}}'.format(ganho))
    print('\n Em percentual: 13%')

elif salario > 900 and salario <= 1500:
    reajuste = salario + salario/100 * 12
    ganho = reajuste - salario
    print(f'Novo salario: {{:.2f}}'.format(reajuste))
    print(f'Reajuste ganho: {{:.2f}}'.format(ganho))
    print('\n Em percentual: 12%')

elif salario > 1500 and salario <= 2000:
    reajuste = salario + salario/100 * 10
    ganho = reajuste - salario
    print(f'Novo salario: {{:.2f}}'.format(reajuste))
    print(f'Reajuste ganho: {{:.2f}}'.format(ganho))
    print('\n Em percentual: 10%')

elif salario > 2000:
    reajuste = salario + salario/100 * 5
    ganho = reajuste - salario
    print(f'Novo salario: {{:.2f}}'.format(reajuste))
    print(f'Reajuste ganho: {{:.2f}}'.format(ganho))
    print('\n Em percentual: 5%')
