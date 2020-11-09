"""
Author: Dula Temesgen
program: students.py
creating class for customer
"""
class Customer:
    """Customer class"""

    # Constructor
    def __init__(self, customer_id, last_name, first_name, phone_number, address):

        # raises a valeError with numeric customer id
        if isinstance(customer_id, int):
            raise ValueError


        self.customer_id = customer_id
        self.last_name = last_name
        self.first_name = first_name
        self.phone_number = phone_number
        self.address = address



    def display(self):
        return "Customer ID: " + self.customer_id + \
               "\n"+ "Name: " + self.last_name + ", " + self.first_name \
        + "\n" + self.phone_number + \
               "\n" + self.address

    def __str__(self):
        return "Customer ID: " + str(self.customer_id) +\
               "\n" "Name: " + str(self.first_name) + ", " + str(self.last_name) +\
               "\n" "Phone Number: " + str(self.phone_number) +\
               "\n" "Address: " + str(self.address)

    def __repr__(self):
        return "Customer ID: " + repr(self.customer_id) +\
               "\n" "Name: " + repr(self.first_name) + ", " + repr(self.last_name) +\
               "\n" "Phone Number: " + repr(self.phone_number) +\
               "\n" "Address: " + repr(self.address)

customer_1 = Customer("4520", "Temesgen", "Dula", "515-100-2003", "909 Robert D. Ray Dr, Des Moines, IA 50309")

print(customer_1.display())

"""
customer_2 = (cid, "Temesgen", "Dula", "515-100-2003", "909 Robert D. Ray Dr, Des Moines, IA 50309")

print(customer_1.display())
"""