# Hierarchical
class GreatGrandFather:
    def __init__(self, value1, value2):
        self.value1 = value1
        self.value2 = value2
    def sub(self):
        print("Substraction :", self.value1 - self.value2)

class GrandFather(GreatGrandFather):
    def __init__(self, value1, value2):
        self.value1 = value1
        self.value2 = value2
    def add(self):
        print("Addition :", self.value1 + self.value2)

class Father(GrandFather):
    pass

class child(Father):
    pass


obj = child(2,2)
obj.sub()
obj.add()