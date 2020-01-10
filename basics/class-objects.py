#--- CLASS AND OBJECTS ---#
class Student():
    def __init__(self, name, marks):  # constructor i.e called on object creation
        self.name = name
        self.marks = marks

    def report(self):  # self refers to the current object
        print("Name:", self.name, "  Marks:", self.marks)


student1 = Student("Bobby", 72)
student1.report()

#--- INHERITANCE ---#


class Person():
    # Parent class
    def __init__(self, name):
        self.name = name

    def show(self):
        print(self.name)


class Employee(Person):
    # Child class
    def __init__(self, name, salary):
        super().__init__(name)
        self.salary = salary

    def show(self):
        print(self.name, self.salary)


per1 = Person("Mona")
emp1 = Employee("Sonu", 120000)

per1.show()
emp1.show()
