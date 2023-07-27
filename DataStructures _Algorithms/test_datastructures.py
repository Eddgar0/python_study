import unittest
from queue import QueueLst

class TestCola(unittest.TestCase):
    cola = None
    def setUp(self):
        self.cola = QueueLst()
    def test_cola_is_empty(self):
        self.assertEqual(self.cola.is_empty(), True)
        self.cola.enqueue(5)
        self.assertEqual(self.cola.is_empty(), False)
    def test_cola_enqueue(self):
        self.cola.enqueue(5)
        self.assertEqual(self.cola.front(), 5)
        self.cola.enqueue(6)
        self.assertEqual(self.cola.front(), 5)
        self.assertEqual(self.cola.rear(), 6)
        for x in range(7, 10):
            self.cola.enqueue(x)
        self.assertEqual(self.cola.rear(), 9)
        self.assertEqual(self.cola.front(), 5)
    def test_cola_dequeue(self):
        self.assertRaises(ValueError,self.cola.front)
        self.cola.enqueue(5)
        self.cola.enqueue(6)
        for x in range(7, 10):
            self.cola.enqueue(x)
        self.cola.dequeue()
        self.assertEqual(self.cola.front(), 6)
        self.assertEqual(self.cola.rear(), 9)
    def test_front_rear(self):
        self.assertRaises(ValueError,self.cola.front)
        self.assertRaises(ValueError,self.cola.rear)

if __name__ == 'main':
    unittest.main()