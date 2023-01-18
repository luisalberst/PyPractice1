from pickle import *

class Auto:

    def __init__(self, colour, doors):
        self.colour = colour
        self.doors = doors

    def __str__(self):
        return self.colour + " " + self.doors


Chevrolet = Auto("Gray", "2")
print(Chevrolet)

file = open('Obj_Auto', 'w+b')

dump(Chevrolet, file)

file.seek(0)
new_Chevrolet = load(file)

print(new_Chevrolet)
file.close()