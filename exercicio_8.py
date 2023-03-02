# Entrada
dep = float(input(f'\n\tInsira os valores\n\tValor do Depósito: '))
taxa = float(input(f'\n\tTaxa de Juros: '))
tempo = int(input(f'\n\tTempo de Rendimento:'))

# Processamento
valor_final = dep * (1 + (taxa/100))**tempo

# Saída
print(f'\n\tValor depois do rendimento: {valor_final}')
