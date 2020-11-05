"""
Author: Dula Temesgen
program: students.py

testing student class
"""
import unittest
from class_definitions import students as s


class MyTestCase(unittest.TestCase):
    def setUp(self):
        self.student = s.Student('Temesgen', 'Dula', 'Maths', 4.0)

    def tearDown(self):
        del self.student

    def test_object_created_required_attributes(self):
        self.assertEqual(self.student.first_name, "Dula")
        self.assertEqual(self.student.last_name, "Temesgen")
        self.assertEqual(self.student.major, "Maths")
        self.assertEqual(self.student.gpa, 4.0)

    def test_object_created_all_attributes(self):
        student = s.Student('Temesgen', 'Dula', 'Maths', 4.0)
        assert student.last_name == 'Temesgen'
        assert student.first_name == "Dula"
        assert student.major =="Maths"
        assert student.gpa == 4.0

    def test_student_str(self):
        self.assertEqual(str(self.student), "Temesgen, Dula has major Maths with gpa: 4.0")

    def test_object_not_created_error_last_name(self):
        with self.assertRaises(ValueError):
            stu = s.Student("234fre", "Dula", "Maths", 4.0)


    def test_object_not_created_error_first_name(self):
        with self.assertRaises(ValueError):
            stu = s.Student("Temesgen", "3D43ula", "Maths", 4.0)

    def test_object_not_created_error_major(self):
        with self.assertRaises(ValueError):
            stu = s.Student("Temesgen", "Dula", "Spells", 4.0)

    def test_object_not_created_error_gpa(self):
        with self.assertRaises(ValueError):
            stu = s.Student("Temesgen", "Dula", "Maths", 4.1)

if __name__ == '__main__':
    unittest.main()
