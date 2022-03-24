'''
Faça um programa que solicite o preço de uma mercadoria e o percentual de desconto. Exiba o valor do desconto e o preço a pagar.
'''

preço_mercadoria = int(input('Digite o Preço da MERCADORIA: '))
desconto = int(input('Digite o quantos você vai quere de DESCONTO: '))

percentual = (preço_mercadoria * desconto) / 100
valor_final = preço_mercadoria - percentual

print('A sua mercadoria teve desconto de {}%, o valor a paga R$ {} reais'.format(percentual, valor_final))
