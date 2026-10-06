# Creamos una lista de estudiantes 
student_list_01 = ['Jordan','Pipen','Curry','Shack'] # O(1) - Asignación de lista constante

def random_function(students): 
    first = students[0] # O(1) -  elemento por índice
    total = 0 # O(1) -  variable
    new_list = [] # O(1) - Creación de lista 

    for student in students: # O(n) - El bucle se repite n veces 
        total += 1 # O(1) - Operación aritmética simple por cada iteración
        new_list.append(student) # O(1) - Inserción al final de la lista por cada iteración

    print(new_list) # O(n) - Recorre la lista completa 
    return total # O(1) - Retorno de valor

print(random_function(student_list_01)) 

# Calcular O(?)
# Complejidad Temporal Total: O(1) + O(1) + O(1) + O(n) + O(n) + O(1) = O(n)
# Resultado final: O(n) - Complejidad Lineal