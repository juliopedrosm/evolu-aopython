titulo = 'Calculadora Python'
print('#'*30)
print(f'{titulo:#^30}')
print('#'*30)
while True:
    print()
    num_1 = input('Digite um número: ')
    num_2 = input('Digite outro número: ')
    operador = input('Digite um operador (+ , - , / ou *): ')

    if not num_1.isnumeric() or not num_2.isnumeric():
        print('Você precisa digitar um número nas duas entradas!')
        continue

    num_1 = int(num_1)
    num_2 = int(num_2)

    if operador == '+':
       print('Resultado: ', num_1 + num_2)
    elif operador == '-':
       print ('Resultado: ', num_1 - num_2)
    elif operador == '/':
       print('Resultado: ', num_1 / num_2)
    elif operador == '*':
        print('Resultado: ', num_1 * num_2)
    else:
        print('Operador inválido, escolha um entre as possibilidades(+ , - , / ou *).')