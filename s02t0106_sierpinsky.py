from array import array as arr

# parametros de mi circuito 
#fila
rows = 3
colums = 2* rows - 1 # CALCULO DE COLUMNAS 

# funcion parra imprimir matrix
def print_matrix (input_matrix):
    for row in input_matrix:
        print(list(row))

# crando el grid  2D 
matrix = []

#construyendo la rejilla o grid 
for _ in range(rows):
    new_row = arr('i',[0] * colums)
    matrix.append(new_row)
# validando fila la construcion del grid 
print (f"cantidad de filas: {len (matrix)}") 
print(f"cantidad de columnas : {len(matrix[0])}")  

#for row in matrix:
    #print(list(row))

# Calculando el centro de la primera fila 
center = colums //2 # se hace dvision entera 

#estableciendo el centro en 1
matrix[0][center]=1

#print_matrix(matrix)

#se calcula el resto de la matrix
#siguiendo la logica del siperpinsky
for row in range(1,rows): 
 for col in range(0,coumns):
   lef_upper_cell = 0
   right_upper_cell = 0


   if col > 0:
      lef_upper_cell = matrix[row-1][col-1]

      if col < colums -1:
         right_upper_cell = matrix[row-1][col+1]

         if left_upper_cell ¡ = right_upper_cell:
            matrix[row] [col] = 1
        else:
         matrix[row][col] = 0
             

