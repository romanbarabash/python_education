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

    def annual_salary(self):
        # calling get_total() method of component class
        return "Total: " + str(self.pay.get_total() + self.bonus)


# creating object of component class
obj_sal = Salary(100)
# creating object of composite class with component object as param
obj_emp = Employee(obj_sal, 10)
# calling method of composite class
print(obj_emp.annual_salary())

# If you delete the composite object then component objects can live without composite object.
