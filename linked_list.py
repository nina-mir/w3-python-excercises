# 1. Write a Python program to create a singly linked 
# list, append some items and iterate through the list.
class Node:

    def __init__(self, data=None):
        self.data = data
        self.next = None

class singly_linked_list:

    def __init__(self):
        self.head= None
        self.tail = None
        self.count = 0
    
    def append(self, data):
        node = Node(data)

        if self.head:
            self.head.next = node
            self.head = node
        else:
            self.head = node
            self.tail = node
        self.count += 1

    def iter_items(self):
        curr = self.tail
        while curr:
            val = curr.data
            curr = curr.next
            yield val


nina = singly_linked_list()
nina.append("38 jahre alt")
nina.append("frau")
nina.append("der Kaffee")





for val in nina.iter_items():
    print(val)