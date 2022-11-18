from negocio import *
import unittest
import HtmlTestRunner
import random


class TestServer(unittest.TestCase):

    def test_mat_register(self):
        self.assertEqual(rmat(5,"Silicio",20.80),True,"No registro")
    
    def test_mat_actua(self):
        self.assertEqual(amat(5,"Silicio",19.30),True,"No actualizo")

    def test_mat_delete(self):
        self.assertEqual(emat(5),True,"No elimino")


if __name__ == "__main__":
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='reports',report_name='Prueba_Materiales', add_timestamp=False))