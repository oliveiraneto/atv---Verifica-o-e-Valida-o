import unittest

# Função que calcula a média de três notas
def calcular_media(nota1, nota2, nota3):
    notas = [nota1, nota2, nota3]
    if any(nota < 0 or nota > 10 for nota in notas):
        raise ValueError("Notas devem estar entre 0 e 10")
    return sum(notas) / len(notas)

# Classe de testes
class TestCalculoMedia(unittest.TestCase):

    def test_media_notas_validas(self):
        self.assertAlmostEqual(calcular_media(5, 6, 7), 6.0)

    def test_media_todas_as_notas_zero(self):
        self.assertEqual(calcular_media(0, 0, 0), 0)

    def test_media_notas_maximas(self):
        self.assertAlmostEqual(calcular_media(10, 10, 10), 10.0)

    def test_media_notas_decimais(self):
        self.assertAlmostEqual(calcular_media(5.5, 6.5, 7.5), 6.5)

    def test_media_notas_invalidas(self):
        with self.assertRaises(ValueError):
            calcular_media(-1, 5, 6)
        with self.assertRaises(ValueError):
            calcular_media(11, 5, 6)

if __name__ == '__main__':
    unittest.main()
