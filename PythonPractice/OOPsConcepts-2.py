# class method static method
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
    @classmethod
    def from_string(cls,emp_str):
        first, last, salary = emp_str.split("-")
        return cls(first, last, salary)
    @staticmethod
    def is_workday():
        # some implemantation
        return True


emp_str_1 = 'Tanmay-Vaidya-50000'
emp_str_2 = 'Manasi-Vaidya-10000'

new_emp_1 = Employee.from_string(emp_str_1)
print(new_emp_1.__dict__)
print(Employee.is_workday())