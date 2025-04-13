import unittest
from class1 import Calculator

class test_my_calculator(unittest.TestCase):
    
    def setUp(self):
        
        self.calc = Calculator(10,5)
        
    def test_addition(self):
        
        self.assertEqual(self.calc.addition(),15)
        
    def test_subtraction(self):
        
        self.assertEqual(self.calc.subtraction(),5)
        
    def test_multiplication(self):
        
        self.assertEqual(self.calc.multiplication(),50)
        
    def test_division(self):
        
        self.assertEqual(self.calc.division(),2)
        
if __name__ == '__main__':
    
    unittest.main()
        