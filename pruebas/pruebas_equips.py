from negocio import *
import unittest
import HtmlTestRunner
import random


class TestServer(unittest.TestCase):

    def test_equip_register(self):
        self.assertEqual(requip(3,"Microscopiop",20,"19 en Perfecto y 1 dañado"),True,"Ingreso valido")
    
    def test_equip_actua(self):
        self.assertEqual(aequip(3,"Microscopio",19,"19 en Perfecto"),True,"Ingreso valido")

    def test_equip_delete(self):
        self.assertEqual(eequip(3),True,"Ingreso valido")


if __name__ == "__main__":
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='reports',report_name='Prueba_Equipos', add_timestamp=False))