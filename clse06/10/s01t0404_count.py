# Creamos una lista de estudiantes 
student_list_01 = ['Jordan','Pipen','Curry','Shack'] # O(1) - Asignación de lista constante

def random_function(students): 
    first = students[0] # O(1) - Acceso a un elemento por índice
    total = 0 # O(1) - Asignación de variable
    new_list = [] # O(1) - Creación de lista vacía

    for student in students: # O(n) - El bucle se repite n veces (donde n es la cantidad de elementos)
        print("se le suma 1 a total")
        total += 1 # O(1) - Operación aritmética simple por cada iteración
        new_list.append(student) # O(1) - Inserción al final de la lista por cada iteración

    print(new_list) # O(n) - Recorre la lista completa de n elementos para imprimirla
    return total # O(1) - Retorno de valor

print(f"tamaño de lista: {len(student_list_01)}")
print(random_function(student_list_01)) 
print("")
# Calcular O(?)
# Complejidad Temporal Total: O(1) + O(1) + O(1) + O(n) + O(n) + O(1) = O(n)
# Resultado final: O(n) - Complejidad Lineal