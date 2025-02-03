class AvtoClass:
    def __init__(self, model, color):
        self.model = model
        self.color = color
    def bark(self):
        if self.color == "black":
            return True
        else:
            return False
avto = AvtoClass('malubu', 'white')
print(avto.__dict__)

print(AvtoClass.__dict__['bark'](avto))

a = 'hello'
b = 'world'
print(vars()['a'])
print(vars()['b'])

s = "This {car_model} model is {car_color}."
print(s.format(car_model = "colbalt", car_color = "white"))

s = "This is {dog_name} and he has {eye_color} eyes"
print(s.format(dog_name = "rudra",eye_color = "black"))

dog_name, eye_color  = "rudra",'blue'
print(s.format(**vars()))

dog_name, eye_color = "rudra",'white'
print(s.format_map(vars()))





class MissingClass(dict):
    def __missing__(self,key):
        return "{" + key + "}"

print(s.format(**MissingClass(vars())))
del dog_name
print(s.format_map(MissingClass(vars())))
del eye_color
print(s.format_map(MissingClass(vars())))