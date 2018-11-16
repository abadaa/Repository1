import unittest
from add_fractions import add_frac

class testadd(unittest.TestCase):
    def setup(self):
        pass
    
    def test_add_zero(self):
        result = add_frac(0, 0)
        self.assertEqual(result, 0)
        
    def test_add_zero_and_one(self):
        result = add_frac(0, 1)
        self.assertEqual(result, 1)
    def test_add_one_and_one(self):
        result = add_frac(1, 1)
        self.assertEqual(result, 2)
        
if __name__ == '__main__':
     unittest.main()