"""
Author: Dula Temesgen
program: invoice.py

invoice class

"""

class Invoice:
    """Invoice class constructor"""

    def __init__(self, invoice_id, customer_id, last_name, first_name, phone_number, address,  items_with_price=''):
        self.invoice_id = invoice_id
        self.customer_id = customer_id
        self.last_name = last_name
        self.first_name = first_name
        self.phone_number = phone_number
        self.address = address
        self.items_with_price = items_with_price



    def __str__(self):
        return str(self.customer_id) + ", " + str(self.invoice_id) + ", " + str(self.address) + ", " + str(self.last_name) + ", " +str(self.first_name) + ", " + str(self.phone_number)

    def __repr__(self):
        return str(self.customer_id) + ", " + repr(self.invoice_id) + ", " + repr(self.address) + ", " + repr(
            self.last_name) + ", " + repr(self.first_name) + ", " + repr(self.phone_number)

    def add_item():
        entry = input"Enter a dictionary"
        items_with_price = {}
        return items_with_price.append(entry)

    def create_invoice():
        for key, value in items_with_price.items():
            print(key, ".....", value)
        print("Tax....." + (0.06 * (items_with_price.values())))
        print("Total....."+ (sum(items_with_price.values)))







"""
# Driver code
invoice = Invoice(1, 123, '1313 Disneyland Dr, Anaheim, CA 92802' ,'Mouse', 'Minnie', '555-867-5309')
invoice.add_item({'iPad': 799.99})
invoice.add_item({'Surface': 999.99})
invoice.create_invoice()
"""