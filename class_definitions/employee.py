"""
Program: employee.py
Author: Ryan Elliott
Last date modified: 07/2/2020
Employee Class with Driver
"""
import datetime


class Employee:
    """Employee Class """

    def __init__(self, lname, fname, address, pnum, salaried, startd, salary):
        """Employee constructor"""
        self._last_name = lname
        self._first_name = fname
        self._address = address
        self._phone_number = pnum
        self._salaried = salaried
        self._start_date = startd
        self._salary = salary

    def set_last_name(self, lname):
        """Set employee's last name
        :param lname, new last name
        """
        self._last_name = lname

    def set_first_name(self, fname):
        """Set employee's first name
        :param fname, new first name
        """
        self._first_name = fname

    def display(self):
        """Display employee information """
        if self._salaried:
            return str(self._first_name) + ", " + str(self._last_name) + "\n" + str(self._address) + "\n" + str(self._phone_number) + "\n" \
                   + "Salaried employee: $" + str(self._salary) + "/year" + "\n" + str(self._start_date)
        else:
            return str(self._first_name) + ", " + str(self._last_name) + "\n" + str(self._address) + "\n" + str(self._phone_number) + "\n" \
                   + "Hourly employee: $" + str(self._salary) + "/hour" + "\n" + str(self._start_date)

    def __str__(self):
        return "first name " + str(self._first_name) + " last name " + str(self._last_name) + " address " + str(self._address) + " phone number " \
                + str(self._phone_number) + " salaried employee " + str(self._salaried) + " salary " + str(self._salary) + " start date " + str(self._start_date)

    def __repr__(self):
        return "first name " + str(self._first_name) + " last name " + str(self._last_name) + " address " + str(self._address) + " phone number " \
                + str(self._phone_number) + " salaried employee " + str(self._salaried) + " salary " + str(self._salary) + " start date " + str(self._start_date)


# Driver
if __name__ == '__main__':
    emp = Employee('Ruiz', 'Matthew', "123 Happy St", "515-123-4567", True, datetime.date.today(), 40000)
    emp.set_first_name('Matt')
    emp2 = Employee('Elliott', 'Ryan', "123 Happy St", "515-123-4567", False, datetime.date.today(), 8.25)
    print(emp.display())
    print(emp2.display())
    print(str(emp))
    del emp
    del emp2
