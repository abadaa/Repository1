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
    
        
if __name__ == '__main__':
     unittest.main()