# file for testing an error in the lists
'''
from Single_Linked_List import linked_list

ll = linked_list()

ll.insert(1)
ll.insert(2)
ll.insert(3)
ll.insert(4)

ll.delete(ll.length() - 1)

for i in range(ll.length()):
    print(ll.read(i))
    '''

from Double_Linked_List import double_linked_list

dll = double_linked_list()

def deq():
    if dll.first_node is not None:
        print("called")
        d =  dll.read(0)
        dll.delete(0)
        return d




dll.insert(1)
dll.insert(2)
dll.insert(3)
dll.insert(4)

dll.delete(0)
dll.delete(0)
dll.delete(0)
dll.delete(0)

#print(deq())
#print(deq())
#print(deq())
#print(deq())

print("start")
for i in range(dll.length()):
    print(dll.read(i))
