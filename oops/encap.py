from inheritance import Item

class Phone(Item):
    def __init__(self, model, osType, price, quantity):

        #calling the parent class
        super().__init__(model, price=0, quantity=0)
        self.osType = str(osType)


        

p1 = Phone('Apple','IOS',1000,3)
print(p1)
