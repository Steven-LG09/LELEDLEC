class Node:  
    def __init__(self, value):  
        self.value = value  
        self.next = None  
        self.prev = None  


class DoublyLinkedList:  
    def __init__(self):  
        self.head = None  
        self.tail = None  

    def insert(self, value):  
        new_node = Node(value)  
        if not self.head:  
            self.head = new_node  
            self.tail = new_node  
            return

        self.tail.next = new_node  
        new_node.prev = self.tail  
        self.tail = new_node  

    def delete(self, value):  
        current = self.head  

        while current and current.value != value:  
            current = current.next  

        if not current:  
            print("Value not found in the list.")
            return

        if current == self.head:  
            self.head = current.next  
            if self.head:  
                self.head.prev = None  
        elif current == self.tail:  
            self.tail = current.prev  
            if self.tail:  
                self.tail.next = None  
        else:  
            current.prev.next = current.next  
            current.next.prev = current.prev  

    def display_forward(self):  
        current = self.head  
        while current:  
            print(current.value, end=" ⇄ ")  
            current = current.next  
        print("None")  

    def display_backward(self): 
        current = self.tail 
        while current:  
            print(current.value, end=" ⇄ ")  
            current = current.prev  
        print("None") 



dll = DoublyLinkedList()  

dll.insert(10)  
dll.insert(20)  
dll.insert(30)  

dll.display_forward()  
dll.display_backward()  

dll.delete(20)  

dll.display_forward()  
dll.display_backward()  
