class pillinfo:
    def __init__(self, id) -> None:
        self.id = id
        self.name = None
        self.quantity = 0
        self.dosage = 0
    
    def setname(self, name):
        self.name = name
    
    def setquantity(self, quantity):
        self.quantity = quantity
    
    def setdosage(self, dosage):
        self.dosage = dosage

    def getname(self):
        return self.name
    
    def getquantity(self):
        return self.quantity
    
    def getdosage(self):
        return self.dosage
    
    def getid(self):
        return self.id
    
    def __str__(self) -> str:
        return "Pill: " + str(self.id) + \
                " Name: " + str(self.name) + \
                " Quantity: " + str(self.quantity) + \
                " Dosage: " + str(self.dosage)