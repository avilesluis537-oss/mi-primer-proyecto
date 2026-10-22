from array import array as arr

# parametros de mi circuito 
#fila
rows = 8
colums = 2* rows - 1

# crando el grid  2D 
matrix = []

#construyendo la rejilla o grid 
for _ in range(rows):
    new_row = arr('i'[0] * colums)