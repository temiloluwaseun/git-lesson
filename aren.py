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
    def __init__(self, colour, tyres, model, convertible):
        self.colour = colour
        self.tyres= tyres
        self.model = model
        self.convertible = convertible

    def __str__(self):
        return f"This is a {self.colour} {self.model} car with {self.tyres} tyres and it is {self.convertible}"

x = Car("blue",4,"Toyota Hilux","convertible")

print(x)
print(f"{x.colour}  {x.tyres}  {x.model}  {x.convertible} ")