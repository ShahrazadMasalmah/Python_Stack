class SLNode:
    def __init__(self, val):
        self.value = val
        self.next = None


class SList:
    def __init__(self):
        self.head = None

    def add_to_front(self, val):	# added this line, takes a value
        new_node = SLNode(val)
        current_head = self.head
        new_node.next = current_head
        self.head = new_node
        return self

    def print_values(self):
        runner = self.head
        while (runner != None):
           print(runner.value)
           runner = runner.next 	# set the runner to its neighbor
        return self         # once the loop is done, return self to allow for chaining
    
    def add_to_back(self, val):
        if self.head == None:	# if the list is empty
           self.add_to_front(val)	# run the add_to_front method
           return self	# let's make sure the rest of this function doesn't happen if we add to the front
        new_node = SLNode(val)
        runner = self.head
        while (runner.next != None):
           runner = runner.next
        runner.next = new_node	# increment the runner to the next node in the list
        return self       # return self to allow for chaining
    
    def remove_from_front(self):
        if self.head == None:
            print("The linked list is empty!")
            return self
        value = self.head.value
        current_head = self.head.next
        del(self.head)
        #print(current_head.value)
        self.head = current_head
        return value
    
    def remove_from_back(self):
        if self.head == None:
            print("The linked list is empty!")
            return self
        elif self.head.next == None:
            self.remove_from_front()
            return self
        
        runner = self.head
        while (runner.next.next != None):
           runner = runner.next
        value = runner.next.value
        runner.next = None
        del(runner)
        return value
    
    def remove_val(self, val):
        if self.head == None:
            print("The linked list is empty!")
            return self
        
        if self.head.value == val:
            self.remove_from_front()
            return self
        runner = self.head
        while (runner.next != None):
            if runner.next.value == val:
                temp = runner.next
                runner.next = runner.next.next
                del(temp)
                break
            runner = runner.next
        return self 

    def insert_at(self, val, n):
        if n == 0:
           self.add_to_front(val)
           return self
        
        new_node = SLNode(val)
        count = 1
        runner = self.head
        while(runner.next != None):
           if count == n:
             new_node.next = runner.next
             runner.next = new_node
             break
           count +=1
           runner = runner.next
        if runner.next == None:   
           self.add_to_back(val)   
        return self   
  

my_list = SList()	# create a new instance of a list
my_list.add_to_front("are").add_to_front("Linked lists").add_to_back("fun!").print_values()  # chaining, yeah!
my_list.add_to_front("is here!!").add_to_front("Shahrazad").add_to_back("Masalmah").print_values()  # chaining, yeah!
print("The node that is deleted:", my_list.remove_from_front())
print("The node that is deleted:", my_list.remove_from_back())
my_list.remove_val('are').print_values()
my_list.remove_val('is here!!').print_values()
my_list.insert_at('Hellooo', 2).print_values()



        