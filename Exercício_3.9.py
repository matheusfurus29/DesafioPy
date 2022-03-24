'''
Escreva um programa que leia a quantidade de dias, horas, minutos e segundo do
usúario. Calcule total em segundos.
'''

dias = int(input('Dias: '))
horas = int(input('Horas: '))
minutos = int(input('Minutos: '))
segundo = int(input('Segundos: '))

total_segundos = (dias * 24 * 3600) + (horas * 3600) + (minutos * 60) + segundo
print("A quantidade da {} segundos".format(total_segundos))
