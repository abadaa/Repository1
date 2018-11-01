import unittest
from addfractions import add_frac

class testadd(unittest.TestCase):
    def setup(self):
        pass
    
    def test_add_integers(self):
        result = add_frac(1/2, 3)
        print(result)
        self.assertEqual(result, 3.5)
        
if __name__ == '__main__':
     unittest.main()