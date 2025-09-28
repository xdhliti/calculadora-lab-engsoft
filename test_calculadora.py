import unittest
from calculadora import calculadora

class TestCalculadora(unittest.TestCase):

    def test_soma_positivos(self):
        self.assertEqual(calculadora(5, 3, '+'), 8)

    def test_soma_negativos(self):
        self.assertEqual(calculadora(-5, -3, '+'), -8)

    def test_soma_com_zero(self):
        self.assertEqual(calculadora(10, 0, '+'), 10)

    def test_soma_decimais(self):
        self.assertAlmostEqual(calculadora(2.5, 3.5, '+'), 6.0)

    def test_subtracao_positivos(self):
        self.assertEqual(calculadora(10, 4, '-'), 6)

    def test_subtracao_com_negativo(self):
        self.assertEqual(calculadora(5, -2, '-'), 7)

    def test_subtracao_resulta_negativo(self):
        self.assertEqual(calculadora(3, 10, '-'), -7)

    def test_subtracao_decimais(self):
        self.assertAlmostEqual(calculadora(5.5, 2.2, '-'), 3.3)

    def test_multiplicacao_positivos(self):
        self.assertEqual(calculadora(3, 7, '*'), 21)

    def test_multiplicacao_por_zero(self):
        self.assertEqual(calculadora(100, 0, '*'), 0)

    def test_multiplicacao_com_negativo(self):
        self.assertEqual(calculadora(5, -4, '*'), -20)

    def test_multiplicacao_decimais(self):
        self.assertAlmostEqual(calculadora(1.5, 2.0, '*'), 3.0)

    def test_divisao_simples(self):
        self.assertEqual(calculadora(10, 2, '/'), 5)

    def test_divisao_resulta_decimal(self):
        self.assertAlmostEqual(calculadora(5, 2, '/'), 2.5)

    def test_divisao_com_negativo(self):
        self.assertAlmostEqual(calculadora(-10, 2, '/'), -5.0)

    def test_divisao_por_zero_retorna_none(self):
        self.assertIsNone(calculadora(10, 0, '/'))

    def test_potencia_simples(self):
        self.assertEqual(calculadora(2, 3, '^'), 8)

    def test_potencia_expoente_zero(self):
        self.assertEqual(calculadora(10, 0, '^'), 1)

    def test_potencia_base_negativa_expoente_par(self):
        self.assertEqual(calculadora(-2, 2, '^'), 4)
        
    def test_potencia_base_negativa_expoente_impar(self):
        self.assertEqual(calculadora(-2, 3, '^'), -8)

    def test_potencia_com_decimal(self):
        self.assertAlmostEqual(calculadora(2.5, 2, '^'), 6.25)
        
    def test_operacao_invalida_retorna_none(self):
        self.assertIsNone(calculadora(10, 5, '%'))

    def test_valor1_nao_numerico_retorna_none(self):
        self.assertIsNone(calculadora('a', 5, '+'))

    def test_valor2_nao_numerico_retorna_none(self):
        self.assertIsNone(calculadora(5, 'b', '-'))

    def test_ambos_valores_nao_numericos_retorna_none(self):
        self.assertIsNone(calculadora('a', 'b', '*'))

if __name__ == '__main__':
    unittest.main(verbosity=2)