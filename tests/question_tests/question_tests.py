#write function tests here, don't add input('') statements here!
import unittest

#follow this example to add questions b, c, and d for testing including their functions
from src.question_a.question_a import use_global,x # importing variable x from question a document 
from src.question_b.question_b import get_fahrenheit
from src.question_c.question_c import get_person_category
from src.question_d.question_d import get_bonus_pay


class Test_Config(unittest.TestCase):
    
    def test_global_variable(self):
        #altering the value of x which was initially set to 10. This should match what the function will return.
        global x
        x = 50
        self.assertEqual(use_global(),50)

    
    def test_get_fahrenheit(self):
        self.assertEqual(get_fahrenheit(0),32)
        self.assertEqual(get_fahrenheit(5),41)
        self.assertEqual(get_fahrenheit(10),50)

    def test_get_person_category(self):
        self.assertEqual(get_person_category(1),"infant")
        self.assertEqual(get_person_category(2),"child")
        self.assertEqual(get_person_category(14),"teenager")
        self.assertEqual(get_person_category(20),"adult")
    
    def test_get_bonus_pay(self):
        self.assertEqual(get_bonus_pay(-1),"Invalid arguments")
        self.assertEqual(get_bonus_pay(200),10)
        self.assertEqual(get_bonus_pay(600),36)
        self.assertEqual(get_bonus_pay(1000),70)
        self.assertEqual(get_bonus_pay(1500),120)
        self.assertEqual(get_bonus_pay(2000),"Invalid arguments")


