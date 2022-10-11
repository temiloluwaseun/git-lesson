class Fan:
    def __init__(self, number, color):
        self.wing = number
        self.color = color


    def __str__(self):
        return f'this is a fan with {self.wing} and {self.color} color'

fan = Fan(4, 'black')

print(fan)
print(fan.color)


class Car:
    def __init__(self, colour, tyres):
        self.colour = colour
        self.tyres= tyres

x = Car("blue",8)


print(f"{x.colour}  {x.tyres}")