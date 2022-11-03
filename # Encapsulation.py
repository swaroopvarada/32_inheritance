# Encapsulation
class circket:
    name = 'dhoni'
    age = 40
    team = 'India'
    def details(self):
        print("Name :", self.name)

obj = circket()
print(obj.name)
obj.details()