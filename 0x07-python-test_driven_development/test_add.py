import unittest
import 0-add_integer


class Test_add(unittest.Testcase):

    def test_add(self):
        result = 0-add_integer.add_integer(10, 5)
        self.assertEqual(result, 15)
