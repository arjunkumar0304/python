class Bird:
    def sound(self):
        print("Some generic bird sound")

class Sparrow(Bird):
    def sound(self):
        print("Chirp Chirp")

class Crow(Bird):
    def sound(self):
        print("Caw Caw")

# Same method name 'sound()', different behaviors
for bird in [Sparrow(), Crow()]:
    bird.sound()
