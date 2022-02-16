# class Employee:
#     pass

# emp1 = Employee()
# emp2 = Employee()

# emp1.name = "abc"
# emp2.name = "xyz"

# emp1.pay = 50000
# emp2.pay = 60000

# emp1.mail = "abc@gmail.com"
# emp2.mail = "xyz@gmail.com"

# print(emp1.mail)
# print(emp2.mail)


# each method takes the instance which we mention as self as first argument and 
# and when we create the instance, self(instance name is passed automatically and we need to mention other variables.)
class Employee:

    abc = 10

    def __init__(self, first, last,pay):
        self.first = first
        self.last = last
        self.pay = pay

    def fullname(self):
        return '{} {}'.format(self.first,self.last)

    def apply_raise(self):
        self.pay = int(self.pay * self.abc)

emp4 = Employee("cvb","sdf", 30000)
emp4.fullname()

print(emp4.pay)

emp4.apply_raise()
print(emp4.pay)

emp4.abc = 15
emp4.apply_raise()
print(emp4.pay)



#when we create the instance, init method is run automaticaly and emp4
# is passed as self and it will be passed like emp4.first = cvb

#print(emp4.first)


#instance.method()
#is converted to below in background
#Class.method(instance)

#class variables are variables that are shared among all instances of class
#first, pay
