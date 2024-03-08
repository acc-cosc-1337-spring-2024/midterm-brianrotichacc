#write function tests here, don't add input('') statements here!
import unittest

#follow this example to add questions b, c, and d for testing including their functions
from src.question_c.question_c import get_person_category
from src.question_d.question_d import get_bonus_pay

class Test_Config(unittest.TestCase):

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


