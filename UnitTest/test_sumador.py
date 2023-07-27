# los archivos del unittest deben empezar con test_
import unittest # 1- importa unittest
from sumador import suma # 2- importa el modulo a probar

class TestSumador(unittest.TestCase): # 3- Define test Case, deben empezar con Test 
    def test_suma(self): # 4- Define el metodo, debe empezar con test_, ya que unittest correra solo los metodos que empiezen con test. 
        self.assertEqual(suma(3,5), 8)    # 5- Usa las assertions  para probar el comportamiento.
        self.assertEqual(suma(8, -2), 6)
        self.assertEqual(suma(-4, -5), -9)
        self.assertEqual(suma(-2, 8), 6)

    def test_base_invalida(self):
        with self.assertRaises(ValueError): #metodos como assertRaises(exception, fun, *args, *kargs) pueden usarse dentro de context manager
            int('1', base=1)
    def test_base_invalida_multiple(self):
            for base_invalida in [-1, 0, 1, 2, 37]: # para assertRaises con multiples entradas, se debe crear un argumento o usar un loop en este caso
                 msg = 'Base invalida: {}'.format(base_invalida) # de esta forma en el loop podemos saber cual entrada causo el error  y mostrarlo
                 with self.assertRaises(ValueError, msg=msg):     # Notese tambien que esta forma para en el primer fallo
                      int('1', base=base_invalida)
    def test_base_invalida_subclass(self): 
        for base_invalida in [-1, 0, 1, 2, 37]:
             with self.subTest(base=base_invalida): # de la anterior usando subtest es la mejor opcion ya que te da mas detalles enlos resultados
                  with self.assertRaises(ValueError): # y no para en el primer fallo
                       int('1', base=base_invalida) 

if __name__ == '__main__':
    unittest.main()

