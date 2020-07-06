import unittest
from class_definitions import student as a


class MyTestCase(unittest.TestCase):
    def setUp(self):
        self.student = a.Student('Johnson', 'Bill', 'Business', 3.5)

    def tearDown(self):
        del self.student

    def test_object_created_required_attributes(self):
        self.assertEqual(self.student.last_name, 'Johnson')
        self.assertEqual(self.student.first_name, 'Bill')
        self.assertEqual(self.student.major, 'Business')

    def test_object_created_all_attributes(self):
        self.assertEqual(self.student.last_name, 'Johnson')
        self.assertEqual(self.student.first_name, 'Bill')
        self.assertEqual(self.student.major, 'Business')
        self.assertEqual(self.student.gpa, 3.5)
