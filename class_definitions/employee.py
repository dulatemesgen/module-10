"""
Author: Dula Temesgen
program: employee.py

class assignment 1
"""
from datetime import date

class Employee:
    """Employee class"""

    # Constructor
    def __init__(self, lname, fname, address, pnumber, salaried, sdate, salary):
        self.last_name = lname
        self.first_name = fname
        self.address = address
        self.phone_number = pnumber
        self.salaried = salaried
        self.start_date = sdate
        self.salary = salary

    def display(self):
        if self.salaried:
            return self.first_name + " " + self.last_name + "\n" \
                + self.address + "\n" + self.phone_number + "\n" \
                + "Salaried employee: $" +str(self.salary) + "/year" "\n" + str(self.start_date)
        else:
            return self.first_name + " " + self.last_name + "\n" \
                   + self.address + "\n" + self.phone_number + "\n" \
                   + "Hourly employee: $" + str(self.salary) + "/hour" + "\n" + str(self.start_date)
    def __str__(self):
        return 'Employee: First Name =' + str(self.first_name) + ', Last Name=' \
        + str(self.last_name) + ', Address=' + str(self.address) + ', Phone=' \
        + str(self.phone_number) + ', Salary=$' + str(self.salary) \
        + ', Start Date=' + str(self.start_date) + ', Salaried=' + str(self.salaried)

    def __repr__(self):
        return 'Employee: First Name =' + repr(self.first_name) + ', Last Name=' \
               + repr(self.last_name) + ', Address=' + str(self.address) + ', Phone=' \
               + repr(self.phone_number) + ', Salary=$' + repr(self.salary) \
               + ', Start Date=' + repr(self.start_date) + ', Salaried=' + repr(self.salaried)

tdate = date.today()
empl = Employee("Temesgen", "Dula", "5912 park ave., Des Moines IA 50213", "515-555-4000", True, tdate, 35000)
print(empl.display())
print(empl)

empl2 = Employee("Temesgen", "Dula", "5912 park ave., Des Moines IA 50213", "515-555-4000", False, tdate, 7.25)
print(empl2.display())
print(repr(empl2))

