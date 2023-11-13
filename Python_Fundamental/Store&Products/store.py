import product

class Store:
    def __init__(self, name):
        self.name = name
        self.list_of_products = []
        #self.product = Product(name='phone', price=1000, category='technology')


    def add_product(self, new_product):
        self.list_of_products.append(new_product) 
        return self

    def sell_product(self, id):
        for i in range(len(self.list_of_products)):
            #print(self.list_of_products[i].id)
            if(self.list_of_products[i].id == id):
                self.list_of_products.remove(self.list_of_products[i])
                break    
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
    

store = Store('SuperMark')
store.add_product(product.tomato).add_product(product.pen).inflation(20).set_clearance('food', 5)
product.tomato.print_info() 
product.pen.print_info() 
store.sell_product(2)
print(store.list_of_products[0].name)

