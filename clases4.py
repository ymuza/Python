class Cars:

    def __init__(self, make, year, engine, km):
        self.make = make
        self.year = year
        self.engine = engine
        self.km = km
        self.serv = False

    def service(self):
        op = input("does the car have the latest service done (y/n)? ")
        if op == "y":
            self.serv = True
        else:
            self.serv = False
        return self.serv

    def usage(self):
        if self.km < 80000 and self.serv is True:
            print("The car does not need maintenance.")
        else:
            print("you need to perform maintenance.")




c = Cars(input("type the make: "), input("type the year: "), input("type the engine model: "), int(input("type the amount of kms: ")))

c.service()

c.usage()





