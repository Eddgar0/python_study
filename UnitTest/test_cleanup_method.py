# El metodo TestCase.addCleanup(func, *args, **kwargs)
# Este metodo puede ser usado para definir limpiezas adicionales
# Estas limpiezas son llamadas despues del meotodo tearDown() y son llamados en orden reverso.
import os
import unittest

class TestOpen(unittest.TestCase):
    def test_open(self):
        fname = 'testfile.txt'
        f = open(fname, 'w')
        # La limpieza siempre son ejectuadas
        self.addClassCleanup(os.remove, fname)
        self.addClassCleanup(f.close)
        # Valida si el archivo esta abierto
        self.assertFalse(f.closed)
        # Si el assert previo falla 
        # La siguiente linea no sera ejectuada
        f.close() # cierra el archivo
        # Valida si el archivo esta cerrado
        self.assertTrue(f.closed)

if __name__ == '__main__':
    unittest.main()