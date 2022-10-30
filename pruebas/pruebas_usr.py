from negocio import *
import unittest
import HtmlTestRunner
import random


class TestServer(unittest.TestCase):

    def test_user_valid(self):
        self.assertEqual(ingreso("samu","1234"),True,"Ingreso valido")
    
    def test_user_dont_valid(self):
        self.assertEqual(ingreso("samue","1234"),True,"Ingreso no valido")
    
    def test_register_valid(self):
        cont = random.randint(0,10000)
        self.assertEqual(registrar(f"samu{cont}","1234"),True,"Si registro")
    
    def test_register_dont_valid(self):
        self.assertEqual(registrar("samu","1234"),True,"No registro")


if __name__ == "__main__":
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='reports',report_name='example', add_timestamp=False))