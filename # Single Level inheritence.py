# Single Level inheritence
class parent:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def details(self):
        print('Name :', self.name, '\nAge :', self.age)

class child(parent):
    pass
  
obj = parent('Abhi', 22)
obj.details()
obj = child('Dhoni', 77)
obj.details()