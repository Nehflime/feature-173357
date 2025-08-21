import unittest
from unittest.mock import patch
import io


class TestCodigoEstudiantes(unittest.TestCase):

    def test_nombre(self):
        # Prueba para la variable nombre
        try:
            from exercises_01 import nombre
        except ImportError:
            print("Valida que declaraste la variable nombre")
        if not isinstance(nombre, str):
            print("Verifica que la varibale nombre tenga asignada una cadena de caracteres")

    def test_matricula(self):
        # Prueba para la variable matricula
        try:
            from exercises_01 import matricula
        except ImportError:
            print("Valida que declaraste la variable matricula")
        if not isinstance(matricula, int):
            print("Verifica que la varibale nombre tenga asignada un entero")

    def test_sumar(self):
        # Pruebas para la función sumar
        try:
            from exercises_01 import sumar
        except ImportError:
            print("Valida que tienes definida la función sumar")
        self.assertEqual(sumar(2, 3), 5)
        self.assertEqual(sumar(-1, 1), 0)
        self.assertEqual(sumar(0, 0), 0)

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_bucle_for(self, mock_stdout):
        # Prueba para el bucle for
        from exercises_01 import bucle_for
        bucle_for()
        salida = mock_stdout.getvalue()
        esperado = "\n".join(str(i) for i in range(1, 11)) + "\n"
        self.assertEqual(salida, esperado)

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_print_numbers(self, mock_stdout):
        # Prueba para la lista de números
        from exercises_01 import print_numbers
        print_numbers()
        salida = mock_stdout.getvalue()
        esperado = "\n".join(str(i) for i in range(1, 6)) + "\n"
        self.assertEqual(salida, esperado)


if __name__ == '__main__':
    unittest.main()
