# Multiple inheritence
class father:
    def __init__(self, a1, a2):
        self.a1 = a1
        self.a2 = a2
    def details(self):
        print('Name :', self.a1, '\nAge :', self.a2)

class mother:
    def add(self):
        print("Addition :", self.a1 + self.a2)

class child(father, mother):
    pass


obj = child('vijay', ' Babu')
obj.details()
obj.add()


