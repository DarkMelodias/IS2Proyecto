from negocio import *
import unittest
import HtmlTestRunner
import random


class TestServer(unittest.TestCase):

    def test_lab_register(self):
        self.assertEqual(rlab(4,"Fisica 3",20),True,"No registro")
    
    def test_lab_actua(self):
        self.assertEqual(alab(4,"Fisica 3",15),True,"No actualizo")

    def test_lab_delete(self):
        self.assertEqual(elab(4),True,"No elimino")


if __name__ == "__main__":
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='reports',report_name='Prueba_Laboratorios', add_timestamp=False))