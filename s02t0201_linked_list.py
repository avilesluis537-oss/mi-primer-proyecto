class Node:
    #constructor 
    def __init__(self, date=None):
        self.date = date 
        self.next = None

# testear nuestra clase nodo
node_01 = Node("eggs")
node_02 = Node("ham")
node_03 = Node("bacon")

print(" nodes sin enlazar   ")
print(f"node 01: D:{node_01.date} - N:{node_01.next}")
print(f"node 02: D:{node_02.date} - N:{node_02.next}")
print(f"node 03: D:{node_03.date} - N:{node_03.next}")

#enlazando los nodos 
node_01.next = node_02
node_02.next = node_03        

print(" nodes enlazados")
print(f"Node 01: D:{node_01.date} - N:{node_01.next}")
print(f"Node 02: D:{node_02.date} - N:{node_02.next}")
print(f"Node 03: D:{node_03.date} - N:{node_03.next}")

#list Traversal (Recorrido)
current = node_01

while current:
    print(current.date, end= "->" )
    current = current.next
    print("")













