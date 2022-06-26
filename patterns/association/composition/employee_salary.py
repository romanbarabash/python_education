# Has-A Relation

class Salary:
    # component class constructor
    def __init__(self, pay):
        self.pay = pay

    # component class instance method
    def get_total(self):
        return (self.pay * 12)


class Employee:
    # composite class constructor
    def __init__(self, pay, bonus):
        self.pay = pay
        self.bonus = bonus
        # creating object of component class
        self.obj_salary = Salary(self.pay)

    def annual_salary(self):
        # calling get_total() method of component class
        return "Total: " + str(self.obj_salary.get_total() + self.bonus)


# creating object of composite class and calling method of composite class
obj_emp = Employee(600, 500)
print(obj_emp.annual_salary())

# if you delete the composite object then all of its component objects are also deleted.
