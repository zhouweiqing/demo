import unittest
import func

class MyTestCase(unittest.TestCase):
    def test_something(self):
        #func.cal()
        self.assertEqual(True, True)
    def test_someelse(self):
        self.assertEqual(True, True, "2nd test fail!")

if __name__ == '__main__':
    unittest.main()
