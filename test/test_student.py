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


if __name__ == '__main__':
    unittest.main()
