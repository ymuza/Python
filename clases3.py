class Computer:
    
    def __init__(self):
        self.name = "pepo"
        self.age = 29

    def update(self):
        self.age = 30
    
    def compare(self, c2):
        if self.age == c2.age:
            return True
        else:
            return False


c1 = Computer()
c2 = Computer()

c1.name = "pachi"
c2.age = 34

c1.update()

if c1.compare(c2):
    print("they are the same")
