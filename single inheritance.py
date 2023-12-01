class Human:
    def __init__(self, num_heart):
        self.num_eyes = 2
        self.num_nose = 1
        self.num_heart = num_heart
    def eat(self):
        print("I can eat")
    def work(self):
        print("I can work")

class Male(Human):
    def flirt(self):
        print("I can flirt")
    def work(self):
        super().work()
        print("I can code")

Male_1 = Male(1)
Male_1.eat()
Male_1.work()
print(Male_1.num_heart)