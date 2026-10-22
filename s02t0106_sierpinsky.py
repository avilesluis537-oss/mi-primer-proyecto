from array import array as arr

# parametros de mi circuito 
#fila
rows = 8
colums = 2* rows - 1

# crando el grid  2D 
matrix = []

#construyendo la rejilla o grid 
for _ in range(rows):
    new_row = arr('i',[0] * colums)
    matrix.append(new_row)
# validando fila la construcion del grid 
print (f"cantidad de filas: {len (matrix)}") 
print(f"cantidad de columnas : {len(matrix[0])}")  

for row in matrix:
    print(list(row))