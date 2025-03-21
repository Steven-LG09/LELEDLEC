class Node:  
    def __init__(self, value):  
        self.value = value  
        self.next = None  


class CircularLinkedList: 
    def __init__(self):  
        self.head = None  

    def insert(self, value):  
        new_node = Node(value)  
        if not self.head:  
            self.head = new_node  
            new_node.next = self.head  
            return

        current = self.head  
        while current.next != self.head: 
            current = current.next  

        current.next = new_node  
        new_node.next = self.head  

    def delete(self, value):  
        if not self.head:  
            print("List is empty.")
            return

        current = self.head
        previous = None

        while True:  
            if current.value == value:  
                if previous: 
                    previous.next = current.next  
                else:  
                    if current.next == self.head: 
                        self.head = None  
                        return
                    else:
                        self.head = current.next  
                        temp = self.head
                        while temp.next != current:  
                            temp = temp.next
                        temp.next = self.head  

                return  

            previous = current  
            current = current.next  

            if current == self.head:  
                print("Value not found in the list.")
                return

    def display(self):  
        if not self.head:  
            print("List is empty.")
            return

        current = self.head 
        while True: 
            print(current.value, end=" -> ") 
            current = current.next  
            if current == self.head:  
                break
        print("(Back to head)")  


cll = CircularLinkedList()  

cll.insert(10)  
cll.insert(20) 
cll.insert(30)  

cll.display()  

cll.delete(20)  

cll.display()  
