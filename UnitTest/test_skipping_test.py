# unittest tiene 4 decoradores para saltarse un test
# @skip(reason)
# @skipIf(condition, reason)  se salta si la condicion es verdadera
# @skipUnless(condition, reason) se salta si la condicion es falsa
# @expectedFailure

# @expectedFailure se utiliza para saltarse tests con fallos esperados, por ejemplo un modulo no terminado. 
# Si el test falla, expected failure es reportado, si el test es logrado, unexpected success es reportado y el test
# se reporta como fallado. 

import unittest
import sys
import os
from sumador import suma

class TestSkips(unittest.TestCase):
    @unittest.skip('Not implementado todavia')
    def test_x(self):
        pass # Recordar escribir el test
    @unittest.skipIf(sys.platform == 'win32', 'Not a POSIX system')
    def test_posix(self):
        self.assertEqual(os.sep, '/')
    @unittest.skipUnless(sys.platform == 'win32', 'Not a Windows system')
    def test_windows(self):
        self.assertEqual(os.sep, '\\')
    @unittest.expectedFailure
    def test_suma(self):
        # La funcio suma esta rota todavia
        self.assertEqual(suma(3,5), 7)
            


if __name__ == '__main__':
    unittest.main()
