class Animal:
    def status(self):
        print("An animal runs on the street.")
class Vehicle:
    def status(self):
        print("A vehicle drives on the street.")
def in_the_street(obj):
    obj.status()

dog=Animal()
car=Vehicle()
in_the_street(dog)
in_the_street(car)
