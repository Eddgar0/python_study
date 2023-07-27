# tambien podemos usar setUpClass() y tearDownClas(), estos se ejecutan antes y despues de ejecutada la clase, y debe ser decorado con
# @classmethod

# tambien estan setUpModule() y tearDownModule(), estos evaluan a nivel de modulo, ejecutan accionnes antes y despues ejecutar
# lo que hay dentro del modulo
import unittest

def setUpModule():
    print('Setteando el modulo')
def tearDownModule():
    print('Limpiando el modulo')

class TestFixtures(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        print('Seteando la Clase')
    @classmethod
    def tearDownClass(cls):
        print('Limpiando la Clase')
    def setUp(self):
       print('Seteando el metodo..')
    def tearDown(self):
        print('Limpiando el metodo')
    def test_fixtures(self):
        self.assertEqual(1+1, 2)

if __name__ == '__main__':
    unittest.main()