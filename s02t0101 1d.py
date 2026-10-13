

from array import array as arr

def print_array(input):
    print("[",end="")
    for element in input :
        print(element,end=',')
    print("\b]")    
my_array = arr('i',[2,10,15,20])  
print_array(my_array)  
# buscar el elemento 15
numeber_to_search = 100 
counter = 0 

for integer in my_array:
    if integer == numeber_to_search:
        print("numero encontardo")
        #sirve para terminar el ciclo 
        break
    counter+=1
    if counter == len(my_array):
        print("numero no encontardo ")
