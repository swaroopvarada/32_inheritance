#Hierarchical Inheritance
class Parent:
      def fun1(self):
          print("this is function 1")
class Child(Parent):
      def fun2(self):
          print("this is function 2")
class Child2(Parent):
      def fun3(self):
          print("this is function 3")
 
ob = Child()
ob1 = Child2()
ob.fun1()
ob.fun2()