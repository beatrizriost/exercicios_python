# Entrada
num1 = float(input(f'\n\tInsira os números:\n\tNúmero 1: '))
num2 = float(input(f'\n\tNúmero 2: '))

# Saída 1
print(f'\n\tAntes de inverter')
print(f'\n\tNúmero 1: {num1}')
print(f'\n\tNúmero 2: {num2}')


#Processamento
X = num2
num2 = num1
num1 = X

# Saída 2
print(f'\n\tDepois de inverter')
print(f'\n\tNúmero 1: {num1}')
