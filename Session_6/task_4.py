def str(obj):
    ls = []
    for elem in dir(obj):
        if '__' not in elem and elem != "eat" and elem != "name" and elem != "ration":
            ls.append(elem)
    st = " can "
    i = 0
    while i < len(ls)-2:
        st += ls[i] + ', '
        i += 1
    st += ls[i] + ' and ' + ls[i+1] 
    print(obj.name + st)

class Bird:

    def __init__(self, name):
        self.name = name

    def fly(self):
        print(f'{self.name} bird can fly')

    def walk(self):
        print(f'{self.name} bird can walk')

class FlyingBird(Bird):
    
    def __init__(self, name, ration = "grains"):
        self.ration = ration
        super().__init__(name)

    def eat(self):
        print(f'It eats mostly {self.ration}')

class NonFlyingBird(Bird):

    def __init__(self, name, ration = "fish"):
        self.ration = ration
        super().__init__(name)
    
    def fly(self):
        raise AttributeError(f'{self.name} object has no attribute fly')

    def swim(self):
        print(f'{self.name} bird can swim')
    
    def eat(self):
        print(f'It eats mostly {self.ration}')

class SuperBird(NonFlyingBird, FlyingBird):
    
    def __init__(self, name, ration = "fish"):
        super(NonFlyingBird, self).__init__(name, ration)

    def fly(self):
        super(FlyingBird, self).fly()




b = Bird("Any")
b.walk()

p = NonFlyingBird("Penguin", "fish")
p.swim()
#p.fly()
p.eat()

c = FlyingBird("Canary")
str(c)
c.eat()

s = SuperBird("Gull")
str(s)
s.eat()
print(dir(SuperBird))
