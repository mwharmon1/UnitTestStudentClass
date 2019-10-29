"""
Author: Michael Harmon
Last Date Modified: 10/28/2019
Description: These unit tests will test the Student class constructors and functionality
"""


import unittest
from class_definitions import student as s


class MyTestCase(unittest.TestCase):
    def setUp(self):
        self.student = s.Student('Harmon', 'Michael', 'BIS')

    def tearDown(self):
        del self.student

    def test_object_created_required_attributes(self):
        student = s.Student('Harmon', 'Michael', 'BIS')
        assert student.last_name == 'Harmon'
        assert student.first_name == 'Michael'
        assert student.major == 'BIS'

    def test_object_created_all_attributes(self):
        student = s.Student('Harmon', 'Michael', 'BIS', 4.0)
        assert student.last_name == 'Harmon'
        assert student.first_name == 'Michael'
        assert student.major == 'BIS'
        assert student.gpa == 4.0

    def test_student_str(self):
        self.assertEqual(str(self.student), "Harmon, Michael has major BIS with gpa: 0.0")

    def test_object_not_created_error_last_name(self):
        with self.assertRaises(ValueError):
            student = s.Student('100', 'Michael', 'BIS')

    def test_object_not_created_error_first_name(self):
        with self.assertRaises(ValueError):
            student = s.Student('Harmon', '200', 'BIS')

    def test_object_not_created_error_major(self):
        with self.assertRaises(ValueError):
            student = s.Student('Harmon', 'Michael', '12345')

    def test_object_not_created_error_gpa(self):
        with self.assertRaises(ValueError):
            student = s.Student('Harmon', 'Michael', 'BIS', 'Bad GPA')


if __name__ == '__main__':
    unittest.main()
