

class Grandfather:
    def property(self):
        print("Owns land")

class Father(Grandfather):
    def car(self):
        print("Owns car")

class Son(Father):
    def bike(self):
        print("Owns bike")

obj = Son()
obj.property()
obj.car()
obj.bike()
