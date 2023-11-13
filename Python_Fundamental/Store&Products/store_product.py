class Store:
    def __init__(self, name):
        self.name = name
        self.list_of_products = []
        self.product = Product(name='phone', price=1000, category='technology')

    def add_product(self, new_product):
        self.list_of_products.append(new_product) 
        return self

    def sell_product(self, id):
        for i in range(len(self.list_of_products)):
            if(i == id):
                self.list_of_products[i].split(1)
        return self  

    def inflation(self, percent_increase):
        for i in range(len(self.list_of_products)):
            self.list_of_products[i].update_price(percent_increase, True) 
        return self   

    def set_clearance(self, category, percent_discount):
        for i in range(len(self.list_of_products)):
            if self.list_of_products[i].category == category:
                self.list_of_products[i].update_price(percent_discount, False)
        return self
    def print_products(self):
        for i in self.list_of_products:
            print("the product is ", i) 
        return self          

class Product:
    def __init__(self, name, price, category):
        self.name = name
        self.price = price
        self.category = category

    def update_price(self, percent_change, is_increased):
        if is_increased:
            self.price = self.price +  percent_change

        else:
            self.price = self.price -  percent_change 
        return self
    
    def print_info(self):
        print(f"The Product name is {self.name} and the price is {self.price}, also the category is {self.category}")
        return self
    

tomato = Product('tomato', 50, 'food')
pen = Product('pen', 10, 'educate')
store = Store('SuperMark')
print(store.product.name)
store.add_product(tomato).add_product(pen).inflation(20).set_clearance('food', 5).sell_product(1)
tomato.print_info()
#pen.print_info()   