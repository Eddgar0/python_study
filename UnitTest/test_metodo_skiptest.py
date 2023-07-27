# TestCase tambien provee un metodo skipTest(reason)
# este puede ser llamado en un metodo de test o en el metodo setUp()
import unittest
import urllib, urllib.request, urllib.error, urllib.response
class TestSkips(unittest.TestCase):
    def setUp(self):
        url = 'http://www.example.com'
        try:
            f = urllib.request.urlopen(url)
        except urllib.error.URLError as err:
            # skip test si no podemos contactar el site
            self.skipTest(err.reason)
        else:
            self.page = f.read()
    def test_page(self):
        self.assertTrue(self.page.startswith(b'<!doctype'))

if __name__ == '__main__':
    unittest.main()
