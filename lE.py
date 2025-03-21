class Node:  
    def __init__(self, value):  
        self.value = value  
        self.next = None  


class LinkedList:  
    def __init__(self): 
        self.head = None  

    def insert(self, value):  
        new_node = Node(value)  
        if not self.head:  
            self.head = new_node  
            return 

        current = self.head  
        while current.next:  
            current = current.next  
        current.next = new_node  

    def delete(self, value): 
        current = self.head  
        previous = None  

        while current and current.value != value:  
            previous = current  
            current = current.next  

        if not current:  
            print("Value not found in the list.")
            return 

        if previous is None:
            self.head = current.next 
        else:
            previous.next = current.next 

    def display(self):  
        current = self.head  
        while current:  
            print(current.value, end=" -> ")  
            current = current.next  
        print("None")



linked_list = LinkedList()  

linked_list.insert(10)  
linked_list.insert(20)  
linked_list.insert(30)  

linked_list.display()  

linked_list.delete(20) 

linked_list.display()  
