class Human:
    def __init__(self):
        print("calling init from human")
        self.num_eyes = 2
        self.num_nose = 1
    def eat(self):
        print("I can eat")
    def work(self):
        print("I can work")

class Male:
    def __init__(self, name):        
        print("calling init from male")
        self.name = name
    def flirt(self):
        print("I can flirt")
    def work(self):
        print("I can code")

class Boy(Human,Male):
    def __init__(self, name, language):
        Human.__init__(self)
        Male.__init__(self, name)
        self.language = language
    def sleep():
        print("I can sleep")
    def work(self):
        print("I can test")

boy1 = Boy("Naman", "Python")
""" boy1.eat()
boy1.flirt()
boy1.work() """
#Male.work(boy1)
print(boy1.num_nose)
print(f"{boy1.name} teaches {boy1.language}")
