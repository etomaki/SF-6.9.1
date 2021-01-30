class Cat:
    def __init__(self, name, sex, age):
        self.name = name
        self.sex = sex
        self.age = age

    def getName(self):
        return self.name
    
    def getAge(self):
        return self.age

    def getSex(self):
        return self.sex

class Circle:
    def __init__(self, radius):
        self.radius = radius
    
    def get_circle_area(self):

        pi_number = 3.14

        return pi_number * self.radius ** 2