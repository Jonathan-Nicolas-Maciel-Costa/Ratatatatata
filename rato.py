from random import randint
import numpy

import os

LINHAS = 20
COLUNAS = 20

matrix = numpy.zeros(shape=(LINHAS, COLUNAS)).astype(int)
print(matrix)


#criar tabuleiro fechado
count = 0
while count < 20:

    matrix[count][0] = 1
    count +=1

count = 0
while count < 20:

    matrix[19][count] = 1
    count +=1
count = 0
while count < 20:

    matrix[count][19] = 1
    count +=1
count = 0
while count < 20:

    matrix[0][count] = 1
    count +=1
count = 0

#criar uma saida aleatoria.
os.system('cls')

saida = randint(0,79)
print(saida, '<<<<<<')
if saida <= 19:
    #cima
    matrix [0][saida] = 54

elif saida > 19 and saida < 40:
    #direta
    matrix [saida-COLUNAS][COLUNAS-1] = 54

elif saida > 39 and saida < 60:
    #baixo
    matrix [LINHAS-1][saida - (COLUNAS*2)] = 54

elif saida > 59 and saida < 80:
    #esquerda
    matrix [saida-(LINHAS*3)][COLUNAS-COLUNAS] = 54

#criar as barreiras

NUMERO_DE_BARREIRAS = int(COLUNAS / 1.5)
count_barreira = 0
print(NUMERO_DE_BARREIRAS, 'total esperado de barreiras')

while count_barreira < NUMERO_DE_BARREIRAS:

    b_linhas = randint(0,19)
    b_colunas = randint(0,19)

    direcao  = randint(0, 4)

    count_barreira += 1

print(matrix)
print(matrix[0][0])

