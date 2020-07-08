# inheritance
# problem statement - Employee class with full name and apply raise methods, raise amt 4% and init method
# Developer class - its own raise amount 10% and mention prog language in dev object.
# Manager class - its own employees list in init , methods to add remove and print employees.

class Employee:
    raise_amount = 1.04
    count = 0
    def __init__(self, first, last, salary):
        self.first = first
        self.last = last
        self.salary = salary
        self.email = first+'.'+last+"@gmail.com"

        Employee.count += 1

    def full_name(self):
        return '{} {}'.format(self.first,self.last)
    def apply_raise(self):
        self.salary=int(self.raise_amount*self.salary)

#emp1 = Employee("tanmay","vaidya",10000)
#emp1.apply_raise()
#print(emp1.full_name())
#print(emp1.__dict__)
#print(Employee.count)

class Developer(Employee):
    raise_amount = 1.10
    def __init__(self,first,last,salary,prog_lang):
        super().__init__(first,last,salary)
        self.prog_lang = prog_lang

#dev1 = Developer("manasi","vaidya",40000,"java")
#dev2 = Developer("tanmay","vaidya",50000,"python")
#dev2.apply_raise()
#print(help(Developer))
#print(dev1.__dict__)
#print(dev2.__dict__)

class Manager(Employee):
    def __init__(self,first,last,salary,employees=None):
        super().__init__(first,last,salary)
        if employees is None:
            self.employees = []
        else:
            self.employees = employees

    def add_employee(self, emp):
        if emp not in self.employees:
           self.employees.append(emp)
    def remove_employee(self,emp):
        if emp in self.employees:
            self.employees.remove(emp)
    def print_emp(self):
        for emp in self.employees:
            print("emp name -->", emp.full_name())

dev1 = Developer("manasi","vaidya",40000,"java")
dev2 = Developer("tanmay","vaidya",50000,"python")
mgr1 = Manager("taniya","mitzoki",200000,[dev1])
#print(mgr1.__dict__)
#mgr1.add_employee(dev1)
#print(mgr1.email)
mgr1.print_emp()








