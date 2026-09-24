"""
Escribir un que calcule la suma 
de los "N" numeros naturales
# ciclo for
por ejemplo si n=100,el programa 
calculara la suma del 1 al 100
"""
import time 
#funcion que suma los n numeros naturale 
#maraca de tiempo 
def sum_of_n(n):
    total_sum = 0
    #sumando los "n" numeros
    #cicolo for 
    for number in range (1,n+1):
      total_sum =  total_sum + number
    return total_sum
#variable para guardar
#El data set
dataset=[]
#generando el contenido del datset
for repeticio in range(1,11):
   #toma de timpo 1 (inicial) 
    timestamp_01 = time.time()
    #sumo los "n" numeros
    n = repeticio*500 
    # guardo el resultado en result
    result=sum_of_n(n)
    # tommando el tiempo final
    timestamp_02 =  time.time()
    #calculo de tiempo 
    elapsed_time=round((timestamp_02-timestamp_01) * 1e6,2)



    """

total_sum = 0
    #1: linea de codigo <- 0+1
    #suma = 1
    #2: sum<- 1 + 2
    #suma = 3
print(f"La suma de 1 hasta {n} es : {total_sum}")

#Tomando el tiempo final
timestamp_02 =  time.time()

#Tomando el timepo del tiempo de ejecuicion
#print(f"Timepo de ejecicion: {timestamp_02 - timestamp_01} segundos")
#Tomando el tiempo final
timestamp_02 =  time.time()

#Tomando el timepo del tiempo de ejecuicion
print(f"Timepo de ejecicion: {(timestamp_02 - timestamp_01) * 1e6:.2f}  µs")
"""