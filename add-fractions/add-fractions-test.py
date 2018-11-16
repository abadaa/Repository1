import unittest
from addfractions import add_frac

class testadd(unittest.TestCase):
    def setup(self):
        pass
    
    def test_add_integers(self):
        result = add_frac(0, 0)
        print(result)
        self.assertEqual(result, 0)
        
if __name__ == '__main__':
     unittest.main()