import unittest

from tp1_2 import main as invictos
from tp1_1 import main as lavarropas

def _normalizar(invictas):
    # el orden interno no debe importar para comparar (se conservan duplicados)
    return sorted(invictas)

class TestInvictos(unittest.TestCase):

    def test_conjunto_vacio(self):
        invictas, cantidad = invictos([])
        self.assertEqual(invictas, [])
        self.assertEqual(cantidad, 0)

    def test_un_solo_punto(self):
        invictas, cantidad = invictos([(3, 7)])
        self.assertEqual(_normalizar(invictas), [(3, 7)])
        self.assertEqual(cantidad, 1)

    def test_ejemplo_del_enunciado(self):
        entrada = [(3, 4), (1, 5), (4, 2), (2, 2), (5, 1), (4, 5)]
        invictas, cantidad = invictos(entrada)

        self.assertEqual(_normalizar(invictas), [(4, 2), (4, 5), (5, 1)])
        self.assertEqual(cantidad, 3)

    def test_ejemplos_del_ejercicio(self):
        A = (3, 2)
        B = (4, 2)
        C = (2, 2)
        D = (1, 1)
        E = (1, 3)
        F = (2, 3)

        casos = [
            ([A, C, B, D, E], [B, E]),
            ([D, D, D, D], [D, D, D, D]),
            ([A, B, B, E], [B, B, E]),
            ([A, D, B, D, E, D, F], [B, F]),
            ([D, B, E, D, F], [B, F]),
            ([E, D, A, C, F], [A, F]),
        ]

        for entrada, esperadas in casos:
            with self.subTest(entrada=entrada):
                resultado, cantidad = invictos(entrada)

                self.assertEqual(_normalizar(resultado), _normalizar(esperadas))
                self.assertEqual(cantidad, len(esperadas))

    def test_registro_del_torneo(self):
        entrada = [
            (9, 47),
            (14, 23),
            (14, 40),
            (28, 31),
            (37, 11),
            (37, 35),
            (45, 18),
            (52, 9),
            (52, 22),
        ]

        resultado, cantidad = invictos(entrada)

        esperadas = [
            (9, 47),
            (14, 40),
            (37, 35),
            (52, 9),
            (52, 22),
        ]

        self.assertEqual(_normalizar(resultado), _normalizar(esperadas))
        self.assertEqual(cantidad, 5)

    def test_dos_criaturas_identicas(self):
        entrada = [
            (40, 40),
            (40, 40),
        ]

        resultado, cantidad = invictos(entrada)

        self.assertEqual(
            _normalizar(resultado),
            [(40, 40), (40, 40)]
        )
        self.assertEqual(cantidad, 2)

    def test_una_criatura_domina_a_todas(self):
        entrada = [
            (10, 10),
            (5, 5),
            (2, 2),
        ]

        resultado, cantidad = invictos(entrada)

        self.assertEqual(_normalizar(resultado), [(10, 10)])
        self.assertEqual(cantidad, 1)

class TestLavarropas(unittest.TestCase):

    def test_no_ropas(self):
        output = lavarropas("./tp1_files/vacio")

        self.assertEqual(output, [])

    def test_no_incompatibilidades(self):
        output = lavarropas("./tp1_files/no_incompatibilidades")

        etiquetas = [x[1] for x in output]
        self.assertEqual(len(set(etiquetas)), 1)


    def test_caso_basico(self):
        output = lavarropas("./tp1_files/enunciado")
        etiquetas = [x[1] for x in output]

        self.assertEqual(len(set(etiquetas)), 2)

    def test_asignacion_del_ejemplo(self):
        output = lavarropas("./tp1_files/enunciado")

        esperado = [
            (1, "A"),
            (2, "B"),
            (3, "B"),
            (4, "B"),
            (5, "A"),
        ]

        self.assertEqual(output, esperado)

    def test_incompatibilidades_no_comparten_lavarropas(self):
        output = lavarropas("./tp1_files/enunciado")

        asignacion = dict(output)
        incompatibilidades = [
            (1, 3),
            (1, 2),
            (1, 4),
        ]

        for prenda_a, prenda_b in incompatibilidades:
            self.assertNotEqual(
                asignacion[prenda_a],
                asignacion[prenda_b]
            )

        self.assertEqual(len(set(asignacion.values())), 2)

if __name__ == "__main__":
    unittest.main()
