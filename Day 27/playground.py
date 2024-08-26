def add(*args):
    for i in args:
        i+= i
    return i
        
print(add(1,2,3,4,5))

def calculate(**kwargs):
    print(kwargs)
    for key, value in kwargs.items():
        print(key)
        print(value)

calculate(name="alwa", number=80)

class Car:
    
    def __init__(self, **kw):
        self.model = kw.get("model")
        self.name = kw.get("name")
        
my_car = Car(model="Nissan")

print(my_car.name)