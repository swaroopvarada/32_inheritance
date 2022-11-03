# Hybrid inhertance

class neighbour:
    def __init__(self, value1, value2):
        self.value1 = value1
        self.value2 = value2
    def multiply(self):
        print("Multiplication :", self.value1 * self.value2)

class GrandFather:
    def __init__(self, value1, value2):
        self.value1 = value1
        self.value2 = value2
    def add(self):
        print("Addition :", self.value1 + self.value2)

class Father(GrandFather):
    pass

class child(Father, neighbour):
    pass

obj = child(22, 10)
obj.add()
obj.multiply()