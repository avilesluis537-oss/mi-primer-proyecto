from array import array as arr
from s02t0101_1d import print_array

my_array = arr('i', [2, 10, 15, 20]) 

print("--- ANTES DE LA ELIMINACIÓN ---")
print_array(my_array)

# Eliminación con manejo de excepciones
try:
    my_array.remove(100)
except :
    print("Ese número no fue encontrado")

print("--- DESPUES DE LA ELIMINACIÓN ---")
print_array(my_array)