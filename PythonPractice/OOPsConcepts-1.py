# instance variable and class variable
class Employee:
    payment_raise = 1.04
    emp_count = 0
    def __init__(self,first,last,salary):
        self.first = first
        self.last = last
        self.salary = salary

        Employee.emp_count += 1

    def fullName(self):
        return '{} {}'.format(self.first,self.last)
    def empSalary(self):
        return '{}'.format(self.salary)
    def raise_salary(self):
        self.salary = (self.salary * self.payment_raise)

emp1 = Employee("Tanmay","Vaidya",5000)
emp2 = Employee("Manasi","Vaidya",6000)

print(emp1.__dict__)
#print(Employee.emp_count)
emp1.raise_salary()
print(emp1.__dict__)
print(emp1.payment_raise)
print(emp2.payment_raise)
print(Employee.payment_raise)