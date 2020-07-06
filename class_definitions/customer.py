"""
Program: customer.py
Author: Ryan Elliott
Last date modified: 07/2/2020
Customer Class with Driver
"""


class Customer:
    """Customer Class """

    def __init__(self, custid, lname, fname, pnum, address):
        """Customer constructor"""
        # exception should be raised in the constructor, because the object should not be made if it has an incorrect data type

        if not isinstance(custid, int):
            raise AttributeError
        self._customer_id = custid
        self._last_name = lname
        self._first_name = fname
        self._phone_number = pnum
        self._address = address

    def display(self):
        """Display customer information """
        return str(self._customer_id) + "\n" + str(self._first_name) + "\n" + str(self._last_name) + "\n" + str(
            self._phone_number) + "\n" + str(self._address)

    def __str__(self):
        """str override"""
        return "customer id " + str(self._customer_id) + " last name " + str(self._last_name) + " first name " + \
               str(self._first_name) + " phone number " + str(self._phone_number) + " address " + str(self._address)

    def __repr__(self):
        """repr override"""
        return "customer id " + str(self._customer_id) + " last name " + str(self._last_name) + " first name " + \
            str(self._first_name) + " phone number " + str(self._phone_number) + " address " + str(self._address)


# Driver
if __name__ == '__main__':
    customer1 = Customer(9567, 'Johnson', "Bill", "515-123-4567", "123 Sunny Street")
    print(customer1.display())
    try:
        customer2 = Customer("9567", 'Johnson', "Bob", "515-123-8910", "123 Sunny Street")
    except AttributeError as err:
        print("'Customer' object has no attribute 'cid'")
    print(customer1.display())
