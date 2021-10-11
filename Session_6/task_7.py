exchange_rate = {
        "EUR" : 0.93,
        "BYN" : 2.1,
        "JPY" : 113.64
        }
def sum(args):
    s = Money(0, (args[0]).name)
    for i in args:
        if isinstance(i, Money):
            s = s + i
            print(s.count)
        else:
            print("Cannot be added")
    return s
            
def func(self, other, symb):
        if symb == "/":
            self.count /= other
            return self
        if other.name != self.name:
            for i in exchange_rate.keys():
                if i == other.name:
                    other.count /= exchange_rate[i]
            for i in exchange_rate.keys():
                if i == self.name:
                    other.count *= exchange_rate[i]
            if symb == "+":
                self.count += other.count
            if symb == "-":
                self.count -= other.count
        else:
            if symb == "+":
                self.count += other.count
            if symb == "-":
                self.count -= other.count
        return self

class Money:

    def __init__(self, count, name = "USD"):
        self.count = count
        self.name = name 

    def __add__(self, other):
        return func(self, other, "+") 
   
    def __sub__(self, other):
        return func(self, other, "-")

    def __mul__(self, other):
        self.count *= other
        return self

    def __rmul__(self, other):
        self.count *= other
        return self
    
    def __truediv__(self, other):
        return func(self, other, "/")
        

x = Money(10, "BYN") 
y = Money(11) 
z = Money(12.34, "EUR")
print((z + 3.11 * x + y * 0.8).count)

lst = [Money(10,"BYN"), Money(11), Money(12.01, "JPY")]
s = sum(lst)
