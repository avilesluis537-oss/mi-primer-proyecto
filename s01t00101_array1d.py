#arrray 
import array as arr

#creacion de un areglo 
#i: entero con signo 
#i: entero sin signo 
#f: numero decimal 
#d: numero decimal doble 
#u: caracteres unicode
my_array = arr.array('i',[10,22,300,22,44,55,88,999,453,22,45421])
#inteacion automatica 
# for num in my_array: 
#     print (num)
# #    
# print(my_array[0])
# print(my_array[1])
# print(my_array[2])

#TAMAÑO DE UN ARREGLO 
#length
print(len(my_array))
#interacion por indices
for i in range(len(my_array)):
    if my_array[i]%2 == 0:
        print(f"Elemento:¨{i+1}:{my_array[i]}")
        