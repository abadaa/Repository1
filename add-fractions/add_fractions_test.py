import unittest
from add_fractions import Fractions

class testadd(unittest.TestCase):
    def setup(self):
        pass
    
    def test_add_zero(self):
        result = Fractions(0).add(Fractions(0))
        self.assertEqual(result, 0)
    def test_add_zero_plus_five(self):
        result = Fractions(0).add(Fractions(5))
        self.assertEqual(result, 5)
    def test_add_three_plus_four(self):
        result = Fractions(3).add(Fractions(4))
        self.assertEqual(result, 7)
    def test_add_negative_two_plus_fourteen(self):
        result = Fractions(-2).add(Fractions(14))
        self.assertEqual(result, 12)
    def test_add_nine_plus_negative_seventeen(self):
        result = Fractions(9).add(Fractions(-17))
        self.assertEqual(result, -8)
    def test_add_one_fourth_and_two_fourths(self):
        result = Fractions(1, 4).add(Fractions(2, 4))
        self.assertEqual(result, Fractions(3, 4))
    def test_add_negative_one_fifth_and_three_fifths(self):
        result = Fractions(-1, 5).add(Fractions(3, 5))
        self.assertEqual(result, Fractions(2, 5))
    def test_add_two_sevenths_and_negative_three_sevenths(self):
        result = Fractions(2, 7).add(Fractions(-3, 7))
        self.assertEqual(result, Fractions(-1, 7))
    def test_add_seven_eighths_and_two_eigths(self):
        result = Fractions(7, 8).add(Fractions(2, 8))
        self.assertEqual(result, Fractions(9, 8))
        
if __name__ == '__main__':
     unittest.main()