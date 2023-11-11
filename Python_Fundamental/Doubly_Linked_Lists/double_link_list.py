class Node:
    def __init__(self, value):
        self.value = value
        self.prev = None
        self.next = None

class DList:
    def __init__(self):
        self.head = None
    
    def add_on_the_front(self, value):
        new_node = Node(value)
        if self.head == None:
            self.head = new_node
            return self
        current = self.head
        new_node.next = current
        current.prev = new_node
        self.head = new_node
        return self
    
    def add_on_the_back(self, value):
        new_node = Node(value)
        if self.head == None:
            new_node.prev = None
            self.head = new_node
            return self
        runner = self.head
        while(runner.next != None):
            runner = runner.next
        runner.next = new_node
        new_node.prev = runner
        return self 

    def remove_node(self, value):
        if self.head == None:
            print("The double linked list is empty!")
            return self
        
        runner = self.head
        if runner.value == value:
            self.head = self.head.next
            del(runner)
            self.head.prev = None
            return self
        
        while(runner.value != value):
            runner = runner.next    

        if runner.next != None:
            runner.next.prev = runner.prev
        
        else: 
            runner.prev.next = None    

        if runner.prev != None:  
            runner.prev.next = runner.next
        else:
            runner.next.prev = None    
        
        del(runner)         
        return self  

    def insert_at(self, value, index):
        new_node = Node(value)
        if self.head == None:
            self.head = new_node
            return self
        if index == 1:
            self.add_on_the_front(value)
            return self
        
        runner = self.head
        for i in range(1, index-1):
            if(runner != None):
                runner = runner.next 
        
        if runner != None:
            new_node.next = runner.next
            new_node.prev = runner
            runner.next = new_node
            if new_node.next != None:
                new_node.next.prev = new_node
                    
        return self  

    def  middle_element(self):
        slow = self.head
        fast = self.head 
        while (fast != None and fast.next != None):
            slow = slow.next
            fast = fast.next.next
        print("The middle node of the double linked list: ",slow.value)
        return self

    def remove_diblicate_values(self):
        if self.head == None:
            print("The double linked list is empty!")
            return self
        
        runner = self.head 
        #index = None
        while(runner != None):
            index = runner.next
            while(index != None):
                if runner.value == index.value:
                    #self.remove_node(runner.value)
                    temp = index
                    index.prev.next = index.next
                    if index.next != None:
                        index.next.prev = index.prev
                    del(temp) 
                index = index.next
            runner = runner.next
        return self

    def reverse(self): 
        temp = None
        runner = self.head 
        # Swap next and prev for all nodes  
        # of doubly linked list 
        while runner is not None: 
            temp = runner.prev 
            runner.prev = runner.next
            runner.next = temp 
            runner = runner.prev 
        if temp is not None: 
            self.head = temp.prev 
        return self                          

    def print_values(self):
        runner = self.head 
        while(runner.next != None):
            print(runner.value,end=" ---> ")
            runner = runner.next
        print(runner.value,"--->")    
        return self      


double_list = DList()
double_list.add_on_the_back(5).add_on_the_back(6).add_on_the_back(8).add_on_the_back(7).add_on_the_back(10).print_values()
double_list.add_on_the_front(4).add_on_the_front(5).add_on_the_front(11).add_on_the_front(6).add_on_the_front(7).print_values()
double_list.add_on_the_front(3).add_on_the_front(3).add_on_the_back(20).add_on_the_back(3).add_on_the_front(5).add_on_the_front(25).add_on_the_front(5).print_values()
double_list.remove_node(5).print_values()
double_list.insert_at(15, 1).print_values()
double_list.middle_element()
double_list.remove_diblicate_values().print_values()
double_list.reverse().print_values()

#What is Circular linked list?
#The circular linked list is a linked list where all nodes are connected to form a circle.
#In a circular linked list, the first node and the last node are connected to each other which forms a circle.
#There is no NULL at the end.

