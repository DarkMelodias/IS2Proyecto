from negocio import *
import unittest
import HtmlTestRunner
import random


class TestServer(unittest.TestCase):

    def test_res_register(self):
        self.assertEqual(rreser("ninguno","ninguno","2022-10-23",140000,2),True,"No registro")
    
    def test_res_busqueda(self):
        self.assertNotEqual(bereserva("2022/10/05","2022/10/23"),None,"No actualizo")

    def test_res_delete(self):
        self.assertEqual(ereser(25),True,"No elimino")


if __name__ == "__main__":
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='reports',report_name='Prueba_Reservas', add_timestamp=False))