class Girl:

    gender = "female"  # class variable. Every object from Girl class will have that same attribute

    def __init__(self, name, age):
        self.name = name  # instance variable. Every object from Girl class will have its own attribute (name, in this case)
        self.age = age

    @classmethod
    def lega_status(cls):
        cls.status = "adult"


r = Girl('carla', 27)
s = Girl('Valery', 34)

print(r.name, r.age)
print(s.name, r.age)
print(r.gender)
print(s.gender)
