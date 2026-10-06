# creando una lista de estudiante 
student_list_01 = ['Jorda','pipen','curry','lebron'] 
student_list_02 = ['jorge','luis','kevin','fran'] 
#verificando la precencia de un estudiante 
def check_student(input_student,student_list):
    for student in student_list:
        if input_student == student:
            print("Estudiante encontrado")
            return student
# si no ecuentra al aestudiante
        print("Estudiante no encontrado ")
        return None            
#probando algoritmo 
check_student("walter",student_list_01)
