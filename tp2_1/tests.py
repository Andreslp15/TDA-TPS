import unittest
from tp2_1 import main as edificios

class TestEdificios(unittest.TestCase):
    def test_un_edificio_visible(self):
        self.assertEqual(edificios(1, 1), 1)

    def test_tres_edificios_dos_visibles(self):
        # [1, 3, 2], [2, 1, 3], [2, 3, 1]
        self.assertEqual(edificios(3, 2), 3)

    def test_todos_visibles_solo_orden_creciente(self):
        self.assertEqual(edificios(5, 5), 1)
        self.assertEqual(edificios(10, 10), 1)

    def test_cuatro_y_cinco_edificios_dos_y_tres_visibles(self):
            self.assertEqual(edificios(4, 2), 11)
            self.assertEqual(edificios(4, 3), 6)
            self.assertEqual(edificios(5, 2), 50)
            self.assertEqual(edificios(5, 3), 35)
            
    def test_para_seis_y_siete_edificios(self):
            self.assertEqual(edificios(6, 2), 274)
            self.assertEqual(edificios(6, 3), 225)
            self.assertEqual(edificios(6, 4), 85)
            self.assertEqual(edificios(6, 5), 15)
            self.assertEqual(edificios(6, 6), 1)
            self.assertEqual(edificios(7, 2), 1764)
            self.assertEqual(edificios(7, 3), 1624)
            self.assertEqual(edificios(7, 4), 735)
            self.assertEqual(edificios(7, 5), 175)
            self.assertEqual(edificios(7, 6), 21)
            self.assertEqual(edificios(7, 7), 1)

if __name__ == "__main__":
    unittest.main()  