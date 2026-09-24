
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
dataset=[] #[(n,times,s),((a,b,c))]
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
    #agregar la tripleta de los datos al dataset
    dataset.append((n,elapsed_time,result))

# imprimir el dataset
for tup in dataset:
  print(tup)

