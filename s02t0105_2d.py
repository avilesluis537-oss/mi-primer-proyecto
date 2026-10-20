from array import array as arr

#Impresion de una tabla 
def print_table(inpunt_table):
#Imprimiendo cada elemento 
 for row in inpunt_table:
    for column in row:
        print(column, end=",")
    print("\b ")

table = [
    arr("i",[1,2,3]),
    arr("i",[4,5,6]),
    arr("i",[7,8,9]),
]

print_table(table)
#incercion
row = 1
column = 2
value = 99

# insertar en la fila 
table[row].insert(column,value)

#imprimiendo mensaje 
print("--- despues de la insercion elemento ---")
print_table(table) #DRY

# insertando una fila completa
new_row = arr('i',[100,200,300])
pos = 1
table.insert(pos,new_row)

#imprimiendo mensaje 
print("--- despues de la insercion de la fila ---")
print_table(table) #DRY

del table[2]

#imprimiendo de la tabla despues de la insercion 
print("--- despues de la eliminacion de la fila 2  ---")
print_table(table) #DRY
