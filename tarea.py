from array import array as arr
from enum import Enum

# Borra pantalla con caracteres ANSI
def clear_screen():
    print("\033[2J\033[H", end="")

# Encapsulado de los valores ANSI para colores en un enumerado
class AnsiColor(Enum):
    RED = "\033[91m"
    YELLOW = "\033[93m"
    CYAN = "\033[96m"
    RESET = "\033[0m"

# Función para imprimir matriz en formato de lista (depuración)
def print_matrix(input_matrix):
    for row in input_matrix:
        print(list(row))

# Función para generar el triángulo
def generate_triangle(rows=5):
    columns = 2 * rows - 1
    matrix = []
    
    # Construyendo el grid
    for _ in range(rows):
        new_row = arr('i', [0] * columns)
        matrix.append(new_row)
        
    # Calculando el centro de la primera fila
    center = columns // 2  # División entera
    matrix[0][center] = 1
    
    # Se calcula el resto de la matriz siguiendo la lógica del Sierpinski Gasket
    for row in range(1, rows):
        for col in range(0, columns):
            left_upper_cell = 0
            right_upper_cell = 0
            
            if col > 0:
                left_upper_cell = matrix[row-1][col-1]
            if col < columns - 1:
                right_upper_cell = matrix[row-1][col+1]
                
            if left_upper_cell != right_upper_cell:
                matrix[row][col] = 1
            else:
                matrix[row][col] = 0
                
    return matrix

# Dibuja la matriz con símbolos y colores ANSI
def draw_matrix(input_matrix, symbol="*"):
    for row in input_matrix:
        for cell in row:
            if cell == 1:
                print(AnsiColor.CYAN.value + symbol + AnsiColor.RESET.value, end="")
            else:
                print(AnsiColor.RED.value + " " + AnsiColor.RESET.value, end="")
        print()

# Método principal
def main():
    # Genera el triángulo de Sierpinsky con 15 filas para mejor resolución
    matrix = generate_triangle(15)
    
    # Limpia la pantalla antes de dibujar la matriz
    clear_screen()
    
    # Dibuja la matriz en pantalla usando un bloque como símbolo
    draw_matrix(matrix, symbol="■")

if __name__ == "__main__":
    main()