import unittest
from unittest import TestCase
from unittest.mock import Mock
from myclass import Person, get_data
# from main import addition, is_even


# class MainTest(unittest.TestCase):
#
#     def setUp(self):
#         print("setUp")
#         self.x = 5
#         self.string = "q"
#
#     def tearDown(self):
#         pass
#
#     def test_addition(self):
#         assert addition(self.x, self.x) == 10
#         self.assertEqual(addition(5, 5), 10)
#
#
#     def test_numbers(self):
#         self.assertGreater(self.x, 3)
#
#     def test_is_even_with_even(self):
#         self.assertEqual(is_even(4), True)
#         self.assertEqual(is_even(10), True)


class TestPerson(TestCase):

    def setUp(self):
        self.obj_person = Person("Jon", 18)


    def tearDown(self):
        pass

    # def test_process_data(self):
    #     mock_get_data = Mock(return_value=[9, 3, 6])
    #     get_data = mock_get_data
    #     result = self.obj_person.process_data()
    #     mock_det_data.assert_called_ance()
    #     print(result)
    #     assert result == 7

    def test_create_obj_person(self):
        self.assertEqual(self.obj_person, "Jon")
        self.assertEqual(self.obj_person.age, 18)

    def test_get_year(self):
        self.assertEqual(self.obj_person.get_year(), "Jon", 2005)

    def test_can_check(self):
        self.assertFalse(self.obj_person.check_name())


if __name__ == "__main__":
    unittest.maipip
