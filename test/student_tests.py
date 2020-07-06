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

    def test_student_str(self):
        self.assertEqual(str(self.student), 'Johnson, Bill has major Business with gpa: 3.5')

    def test_object_not_created_error_last_name(self):
        with self.assertRaises(ValueError):
            s = a.Student('123', 'Bill', 'Business')

    def test_object_not_created_error_first_name(self):
        with self.assertRaises(ValueError):
            s = a.Student('Johnson', '123', 'Business')

    def test_object_not_created_error_major(self):
        with self.assertRaises(ValueError):
            s = a.Student('Johnson', 'Bill', '123')
