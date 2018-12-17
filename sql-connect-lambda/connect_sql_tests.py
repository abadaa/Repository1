import unittest
import connect_sql

class testSQL(unittest.TestCase):
    def setup(self):
        pass
    
    def test_SQL_Connection(self):
        result = connectDB("aiubnm7", "Fus10n!!", "appraise-qa-copy")
        assertEqual(True, result)
        
if __name__ == '__main__':
     unittest.main()