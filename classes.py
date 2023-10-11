# class student:
#     def check_fail_pass(self):
#         if self.marks>=40:
#             return True
#         else:
#             return False
#     pass
# student1 = student()
# student1.name = "Talha"
# student1.salary = 19
# student1.marks = 88

# print(student1.name)
# print(student1.salary)
# print(student1.marks)

# print(student1.check_fail_pass())


# student2 = student()
# student2.name = "Ali"
# student2.marks = 39

# Pass_or_fail = student2.check_fail_pass()
# print(Pass_or_fail)



# class animal():
#     name = ""
#     salary = 0
# animal1 = animal()
# animal1.name = "Monkey"  
# animal1.salary = 17



# animal2 = animal()
# animal2.name = "Dog"
# animal2.salary = 20


# print(f"{animal1.name} is {animal1.salary} years old")
# print(f"{animal2.name} is {animal2.salary} years old")


# =>Classes and objects

# class student:
#     name = ""
#     salary = 0
#     def function(self):
#         print(self.name, " has" , self.salary)
# student1 = student()
# student1.name ="Talha"
# student1.salary = 19
# print(student1.function())  
 

# =>Create Class
# class person:
#     def __init__(self,fname,lname):
#         self.firstname = fname
#         self.lastname = lname
#     def printname(self):
#         print(self.firstname, self.lastname)    
# class Ali(person):
#     def __init__(self,fname,lname,year):
#         # super().__init__(self,fname,lname,year)
#         person.__init__(self,fname,lname)
#         self.graduationyear = year
#     def welcome(self):
#         print("welcome",self.firstname,self.lastname ,"To the class of",self.graduationyear)    
# x = Ali("Talha ", "Talib",2019)
# x.printname()

# Single Inheritence

# class Parent:
#     def func1(self):
#         print("This function is in parent class.")
# class Child(Parent):
#     def func2(self):
#         print("This function is in child class.")
# object = Child()
# object.func1()
# object.func2()

# Single Inheritence

# class Dog:
#     def sleep(self):
#         print("Sleeping")
# class dog1(Dog):
#     def bark(self):
#         print("Barking")
# dog = dog1()
# dog.sleep()
# dog.bark()

# Multilevel Inheritence
# class class1:
#     pass
# class class2(class1):
#     pass
# class class3(class2):
#     print("python")


# class Animal:  
#     def speak(self):  
#         print("Animal Speaking")  
# class Dog(Animal):  
#     def bark(self):  
#         print("dog barking")  
# class DogChild(Dog):  
#     def eat(self):  
#         print("Eating bread...")  
# d = DogChild()  
# d.bark()  
# d.speak()  
# d.eat()  


# multilevel inheritance

# class Grandfather:
 
#     def __init__(self, grandfathername):
#         self.grandfathername = grandfathername
# class Father(Grandfather):
#     def __init__(self, fathername, grandfathername):
#         self.fathername = fathername
#         Grandfather.__init__(self, grandfathername)
# class Son(Father):
#     def __init__(self, sonname, fathername, grandfathername):
#         self.sonname = sonname
#         Father.__init__(self, fathername, grandfathername)

#     def print_name(self):
#         print('Grandfather name :', self.grandfathername)
#         print("Father name :", self.fathername)
#         print("Son name :", self.sonname)
# s1 = Son('Arslan', 'Samsaam', 'Ahmed')
# print(s1.grandfathername)
# s1.print_name()

# Multiple inheritance

# class Calculation1:  
#     def Sum(self,a,b):  
#         return a+b;  
# class Calculation2:  
#     def Multiplication(self,a,b):  
#         return a*b;  
# class Derived(Calculation1,Calculation2):  
#     def Divide(self,a,b):  
#         return a/b;  
# d = Derived()  
# # print(d.Sum(10,20))  
# # print(d.Multiplication(10,20))  
# # print(d.Divide(10,20)) 
# print(issubclass(Derived,Calculation2))  
# print(issubclass(Calculation1,Calculation2)) 


# 
# class Mother:
# 	mothername = ""

# 	def mother(self):
# 		print(self.mothername)
# class Father:
# 	fathername = ""
# 	def father(self):
# 		print(self.fathername)
# class Son(Mother, Father):
# 	def parents(self):
# 		print("Mother :", self.mothername)
# 		print("Father :", self.fathername)
		
# s1 = Son()
# s1.mothername = "Sara"
# s1.fathername = "Rashid"
# s1.parents()

# Hierarchical Inheritence

# class Parent:
#     def func1(self):
#         print("This function is in parent class.")
# class Child1(Parent):
#     def func2(self):
#         print("This function is in child 1.")
# class Child2(Parent):
#     def func3(self):
#         print("This function is in child 2.")
# object1 = Child1()
# object2 = Child2()
# object1.func1()
# object1.func2()
# object2.func1()
# object2.func3()

# Hybrid inheritence

# class School:
#     def func1(self):
#         print("This function is in school.") 
# class Student1(School):
#     def func2(self):
#         print("This function is in student 1. ")
# class Student2(School):
#     def func3(self):
#         print("This function is in student 2.") 
# class Student3(Student1, School):
#     def func4(self):
#         print("This function is in student 3.")
# object = Student3()
# object.func1()
# object.func2()


# Polymorphism

# class Banana(): 
#      def type(self): 
#        print("Vegetable") 
#      def color(self):
#        print("yellow") 
# class Apple(): 
#      def type(self): 
#        print("Fruit") 
#      def color(self): 
#        print("Red") 
      
# def func(obj): 
#        obj.type() 
#        obj.color()
        
# obj_Banana = Banana() 
# obj_apple = Apple() 
# func(obj_Banana) 
# func(obj_apple)



# Overloadings
# class A:
#     # def show(self):
#     #     print("running")
#     # def show(self,name=""):
#     #     print("Starting",name)
#     def show(self,name="",salary=""):
#          print("Wehshi",name,salary)
# A1 = A()
# A1.show()               
# A1.show('Talha')  
# A1.show("Gondal",29)  


# overriding 
# class A:
#     def show(self):
#         print("This is parent class")
# class B(A):
#     def show(self):
#         super().show()
#         print("child class")
# B1 =B()
# B1.show()

# Encapsulation

# class Employee:
#     def __init__(self,name,salary,project):
#         self.salary = salary
#         self.name = name
#         self._project = project
#     def show(self):
#         print("Name",self.name, "Salary" , self.salary)
#     def work(self):
#         print("Project",self._project)

# emp = Employee("Talha",9000,"NLP")
# emp.show()
# emp.work()

# Public method to access private memberss
# class Employee:
#     def __init__(self, name, salary):
#         self.name = name
#         self.__salary = salary
#     def show(self):
#         print("Name: ", self.name, 'Salary:', self.__salary)
# emp = Employee('Talha', 10000)
# emp.show()


# Name Mangling to access private members

# class Employee:
#     def __init__(self, name, salary):
#         self.name = name
#         self.__salary = salary
#     def show(self):
#         print("Name: ", self.name, 'Salary:', self.__salary)
# emp = Employee('Usman', 1500000)
# print("Salary :",emp._Employee__salary)

# Protected Member

# class Company:
#     def __init__(self):
#         self._project = "Python Developer"
# class Employee(Company):
#     def __init__(self, name,salary):
#         self.name = name
#         self.salary = salary
#         Company.__init__(self)
#     def show(self):
#         print("Employee name :", self.name)
#         print("Employee Salary :" , self.salary)
#         print("Working on project :", self._project)
# c = Employee("Usman",200000)
# c.show()
# print('Project:', c._project)

# Setter and getter method
# class Employee:
#     def __init__(self, name, salary):
#         self.name = name
#         self.__salary = salary
#     def get_salary(self):
#         return self.__salary
#     def set_salary(self,salary):
#         self.__salary = salary
#     # def show(self):
#     #     print("Name: ", self.name, 'Salary:', self.__salary)
# emp = Employee('Usman', 1500000)
# # print("Salary :",emp._Employee__salary)
# print("Name", emp.name, emp.get_salary())
# emp.set_salary(200000)
# print("salary",emp.name,emp.get_salary())


# Information Hiding and conditional logic for setting an object attributes

# class Student:
#     def __init__(self, name , age, roll_no):
#         self.name = name
#         self.age = age
#         self.__roll_no = roll_no
#     def show(self):
#         print('Student Details:', self.name, self.__roll_no)
#     def get_roll_no(self):
#         return self.__roll_no
#     def set_roll_no(self, number):
#         if number>=50:
#             print("Invalid roll no. please enter again right Roll No.")
#         else:
#             self.__roll_no = number
# obj = Student("Talha", 19, 60)
# obj.show()
# obj.set_roll_no(78)
# obj.set_roll_no(49)
# obj.show()


# Abstraction
# from abc import ABC,abstractmethod
# class Computer(ABC):
#     @abstractmethod
#     def process(self):
#         print("Running")
# class Laptop:
#     pass
# # a = Computer()
# # a.process()        
# b= Laptop()


# import array
# module_whitespace = dir(array)
# print(module_whitespace)

# for i in array.__dict__:
#     print(i)
    
# class Ahmed:
#   print('Show the whitespace of This class')
# for i in Ahmed.__dict__:
#   print(i)
  
# class Talha:
#     def __init__(self,name,age):
#        self.name = name
#        self.age = age
       
#        print(self.name,self.age)
# obj =   Talha("talha" , "17")
# print(obj.__dict__)

# import builtins
# help(builtins.abs)
# print(builtins.abs(-155))
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
