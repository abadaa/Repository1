import unittest
from add_fractions import Fractions

class testadd(unittest.TestCase):
    def setup(self):
        pass
    
    def test_add_zero(self):
        result = Fractions(0).add(Fractions(0))
        self.assertEqual(result, 0)
        
if __name__ == '__main__':
     unittest.main()