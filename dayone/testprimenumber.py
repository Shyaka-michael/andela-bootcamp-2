import unittest
from primenumbers import primenumber

class Testprimenumber(unittest.TestCase):

    def testint(self):
        result = primenumber('str')
        self.assertEqual(result,'value incorect',  msg = 'value incorect')

    def test_no_two(self):
        result = primenumber(2)
        self.assertEqual(result,[1,2],  msg = 'two is prime')

    def test_prime(self):
        result = primenumber(11)
        self.assertEqual(result,[1,2,3,5,7,11],msg='invalid output')

    def all_numbers_in_are_Intergers(self):
        result =primenumber(34)
        self.assertTrue(all(isinstance(number, int) for number in result), msg="Not all the numberes are integers")


if __name__ == '__main__':
    unittest.main()

