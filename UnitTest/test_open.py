# Unitest puede definir metodos setUp() y tearDown() 
# setUp() es llamado automaticamente antes de la ejecucion de cada test metodo de prueba
# tearDown() es llamado automaticamente despues de la ejecucion de cada metodo de prueba
import os
import shutil
import unittest

class TestOpen(unittest.TestCase):
    dirname = 'testdir'
    filename = 'testfile.txt'    
    def setUp(self):
        os.mkdir(self.dirname)  # Crea el directorio temporal
        self.oldcwd = os.getcwd()  # Guarda el directorio actual
        os.chdir(self.dirname) # cambia al directorio temporal
    def tearDown(self):
        os.chdir(self.oldcwd) # Restaura el previo cwd
        shutil.rmtree(self.dirname) # remueve el directorio temporal
    def test_open_creates_new_file(self):
        self.assertNotIn(self.filename, os.listdir())
        open(self.filename, 'w').close()
        self.assertIn(self.filename, os.listdir())


if __name__ == '__main__':
    unittest.main()
