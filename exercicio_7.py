# Entrada
prestacao_inicial = float(input(f'\n\tInsira os valores:\n\tValor da prestação, antes do atraso: '))
taxa = 2
tempo = int(input(f'\n\tDias de atraso: '))

# Processamento
prestacao_final = prestacao_inicial + (prestacao_inicial * (taxa/100)* tempo)

# Saída
print(f'\n\tValor final da prestação: {prestacao_final} reais')
