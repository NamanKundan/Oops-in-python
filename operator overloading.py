class Complex_number:
    def __init__(self,r,i):
        self.real = r
        self.imaginary = i
    def __add__(self,other):
        return f"{self.real+other.real} + {self.imaginary+other.imaginary}i"
    
c1 = Complex_number(1,2)
c2 = Complex_number(4,5)
print(c1+c2)


class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age
p1 = Person("Naman",21)
p2 = Person("Rohit",24)
if p1.age > p2.age:
    print(f"{p1.name} will pay the bill")
else:
    print(f"{p2.name} will pay the bill")