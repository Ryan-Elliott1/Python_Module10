"""
Program: invoice.py
Author: Ryan Elliott
Last date modified: 07/5/2020
Invoice Class with Driver
"""


class Invoice:
    """Invoice Class """

    def __init__(self, invoid, custid, lname, fname, pnum, address, iwp=dict()):
        """Invoice constructor"""
        # exception should be raised in the constructor, because the object should not be made if it has an incorrect data type
        try:
            if not isinstance(custid, int):
                raise AttributeError
        except AttributeError:
            raise AttributeError
            print("'Customer' object has no attribute 'cid'")
        self._invoice_id = invoid
        self._customer_id = custid
        self._last_name = lname
        self._first_name = fname
        self._phone_number = pnum
        self._address = address
        self._items_with_price = iwp

    def add_item(self, dictadd):
        """Add item to dictionary
        :param dictadd, dictionary item to add
        """
        self._items_with_price.update(dictadd)

    def create_invoice(self):
        """Creates invoice with prices, tax and total
        """
        total = 0
        for x in self._items_with_price:
            print(str(x))
        for x in self._items_with_price.values():
            print("$"+str(x))
            total += x
        tax = total * 0.06
        print("Tax "+"$"+str(round(tax,2)))
        total += tax
        print("Total "+"$"+str(round(total,2)))

    def __str__(self):
        """str override"""
        return "invoice id" + str(self._invoice_id) + "customer id " + str(self._customer_id) + " last name " + str(
            self._last_name) + " first name " + \
               str(self._first_name) + " phone number " + str(self._phone_number) + " address " + str(self._address)

    def __repr__(self):
        """repr override"""
        return "invoice id" + str(self._invoice_id) + "customer id " + str(self._customer_id) + " last name " + str(
            self._last_name) + " first name " + \
               str(self._first_name) + " phone number " + str(self._phone_number) + " address " + str(self._address)


# Driver
if __name__ == '__main__':
    invoice = Invoice(1, 123, '1313 Disneyland Dr, Anaheim, CA 92802', 'Mouse', 'Minnie', '555-867-5309')
    invoice.add_item({'iPad': 799.99})
    invoice.add_item({'Surface': 999.99})
    invoice.create_invoice()
