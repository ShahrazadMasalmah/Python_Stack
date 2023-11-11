class Animal:
    def __init__(self, name, age, health_level, happiness_level):
        self.name = name
        self.age = age
        self.health_level = health_level
        self.happiness_level = happiness_level

    def display_info(self):
        print(f"The name of the animal is {self.name} and his health_level is {self.health_level}, also his happiness_level is {self.happiness_level}")
        return self

    def feed_method(self):
        self.health_level += 10
        self.happiness_level += 10
        return self    

class Lion(Animal):
    def __init__(self, name, age, health_level, happiness_level, shape):
        super().__init__(name, age, health_level, happiness_level)
        self.family = 'Panthera leo'
        self.shape = shape

class Tiger(Animal):
   def __init__(self, name, age, health_level, happiness_level,shape):
       super().__init__(name, age, health_level, happiness_level)
       self.family = 'Panthera pardus pardus'
       self.shape = shape

class Bear(Animal):
    def __init__(self, name, age, health_level, happiness_level):
        super().__init__(name, age, health_level, happiness_level)


class Zoo:
    def __init__(self, zoo_name, name):
        self.animals = []
        self.name = zoo_name    
    def add_lion(self, name, age, health_level, happiness_level, shape):
        self.animals.append( Lion(name,age, health_level, happiness_level, shape))
        return self
    def add_tiger(self, name, age, health_level, happiness_level, shape):
        self.animals.append( Tiger(name,age, health_level, happiness_level, shape))
        return self
    def add_bear(self, name, age, health_level, happiness_level):
        self.animals.append( Bear(name,age, health_level, happiness_level))
        return self
    def print_all_info(self):
        print("-"*30, self.name, "-"*30)
        for animal in self.animals:
            animal.display_info()
        return self    



#lion = Lion('Lovey',20, 10, 10, 'huge') 
#lion.feed_method().display_info()
#print(lion.family)
#tiger = Tiger('Alden', 30, 40, 35, 'huge')
#tiger.feed_method().display_info() 
#print(tiger.family) 
 
zoo1 = Zoo("John's Zoo")
zoo1.add_lion("Nala", 21, 20, 15, 'huge').add_lion("Simba", 10, 30, 40, 'small').add_tiger("Rajah", 30, 50, 60, 'big').add_tiger("Shere Khan", 35, 45, 35, 'huge').print_all_info()     
zoo1.add_bear("Hello_bear", 15, 60, 65).print_all_info()