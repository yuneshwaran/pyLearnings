import csv

class Item:
    def __init__(self,model,price,quantity):
        #Assertion and Validation
        assert price >= 0 , "Invalid Price"
        assert quantity >=0 , "Invalid Quantity" 

        #Initializations to Objects
        self.model = str(model)
        self.price = float(price)
        self.quantity = quantity
         
    #repr to print the object on print call
    def __repr__(self):
        return f"model:'{self.model}',price:{self.price},quantity:{self.quantity}"
    
    @property
    def read_only (self):
        print("Hello")

class Laptop(Item):

    AllLaptops = []
    def __init__(self, model, price=0, quantity=0):
        
        super().__init__(model,price,quantity)

        #TO Execute
        Laptop.AllLaptops.append(self)
    
    def calculate_price(self):
        return self.price * self.quantity

    @classmethod
    def load_from_csv(cls):
        with open('files_assets/Laptops.csv', 'r') as f:
            reader = csv.DictReader(f)
            laptops = list(reader)
        
        for laptop in laptops:
            Laptop(
                model= laptop.get('model'),
                price= int(laptop.get('price')),
                quantity= int(laptop.get('quantity'))
            )

#print(Laptop.AllLaptops)
# Laptop.load_from_csv()
# l1 = Laptop('Lenovo',100,100)
#print(l1)