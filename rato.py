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
rato = randint(0,79)
print(saida, '<<<<<<')
if saida <= 19:
    #cima
    if saida == 0:
        matrix [0][saida] = 54
        matrix [0][saida+1] = 0
        matrix [1][saida] = 0
    elif saida == 19:
        matrix [0][saida] = 54
        matrix [0][saida-1] = 0
        matrix [1][saida] = 0

    else:
        matrix [0][saida] = 54
    


elif saida > 19 and saida < 40:
    #direta
    
    if saida == 20:
        matrix [saida-COLUNAS][COLUNAS-1] = 54
        matrix [saida-COLUNAS][COLUNAS-2] = 0
        matrix [saida-COLUNAS+1][COLUNAS-1] = 0
        
    elif saida == 39:
        matrix [saida-COLUNAS][COLUNAS-1] = 54
        matrix [saida-COLUNAS][COLUNAS-2] = 0
        matrix [saida-COLUNAS-1][COLUNAS-1] = 0

    else:
        matrix [saida-COLUNAS][COLUNAS-1] = 54



elif saida > 39 and saida < 60:
    #baixo
    if saida  == 40:
        matrix [LINHAS-1][saida - (COLUNAS*2)] = 54
        matrix [LINHAS-2][saida - (COLUNAS*2)] = 0
        matrix [LINHAS-1][saida - (COLUNAS*2 -1)] = 0
    elif saida == 59:
        matrix [LINHAS-1][saida - (COLUNAS*2)] = 54
        matrix [LINHAS-2][saida - (COLUNAS*2)] = 0
        matrix [LINHAS-1][saida - (COLUNAS*2 +1)] = 0
    else:
        matrix [LINHAS-1][saida - (COLUNAS*2)] = 54
elif saida > 59 and saida < 80:
    #esquerda
    if saida == 60:
        matrix [saida-(LINHAS*3)][COLUNAS-COLUNAS] = 54
        matrix [saida-(LINHAS*3-1)][COLUNAS-COLUNAS] = 0
        matrix [saida-(LINHAS*3)][COLUNAS-COLUNAS+1] = 0
    elif saida == 79:
        matrix [saida-(LINHAS*3)][COLUNAS-COLUNAS] = 54
        matrix [saida-(LINHAS*3+1)][COLUNAS-COLUNAS] = 0
        matrix [saida-(LINHAS*3)][COLUNAS-COLUNAS+1] = 0
    else:
        matrix [saida-(LINHAS*3)][COLUNAS-COLUNAS] = 54
    

#criar as barreiras

NUMERO_DE_BARREIRAS = int(COLUNAS / 1.5)
count_barreira = 0
print(NUMERO_DE_BARREIRAS, 'total esperado de barreiras')
holder = 0

while count_barreira < NUMERO_DE_BARREIRAS:

    b_linhas = randint(1,18)
    b_colunas = randint(1,18)


    direcao  = randint(0, 1)
    if direcao == 0:
        #direita

        while b_colunas != 19:
            dot = randint(0, 1)
            if dot == 1:
                matrix[b_linhas][b_colunas] = 7
                b_colunas +=1
            else:
                b_colunas +=1

    elif direcao == 1:
        #baixo
        while b_linhas != 19:
            dot = randint(0, 1)
            if dot == 1:
                matrix[b_linhas][b_colunas] = 7
                b_linhas +=1
            else:
                b_linhas +=1
        
    elif direcao == 2:
        #esquerda
        while b_linhas != 19:
            dot = randint(0, 1)
            if dot == 1:
                matrix[b_linhas][b_colunas] = 7
                b_linhas -=1
            else:
                b_linhas -=1
    
    elif direcao == 3:
        #cima
        while b_linhas != 19:
            dot = randint(0, 1)
            if dot == 1:
                matrix[b_linhas][b_colunas] = 7
                b_colunas -=1
            else:
                b_colunas -=1 
    count_barreira += 1


#gera o rato
if rato <= 19:
        matrix [0][rato] = 69   
if rato > 19 and rato < 40:
        matrix [rato-COLUNAS][COLUNAS-1] = 69
if rato > 39 and rato < 60:
        matrix [LINHAS-1][rato - (COLUNAS*2)] = 69
if rato > 59 and rato < 80:
        matrix [rato-(LINHAS*3)][COLUNAS-COLUNAS] = 69


print(matrix)
print(matrix[0][0])

