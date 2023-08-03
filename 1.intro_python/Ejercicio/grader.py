import random
import string
import unittest
from estudiantes import Evaluador
from solution import Evaluador as Baseline


def get_estudiante(min_nota=50, max_nota=100, asistencia=90, total_extras=4):
    letras = string.ascii_lowercase
    return {
        'nombre': ''.join(random.choice(letras) for i in range(10)),
        'apellido': ''.join(random.choice(letras) for i in range(10)),
        'asistencia': asistencia,
        'extras': [1 for i in range(total_extras)],
        'notas': {
            'MAT': random.randint(min_nota, max_nota),
            'QMC': random.randint(min_nota, max_nota),
            'FIS': random.randint(min_nota, max_nota),
            'LAB': random.randint(min_nota, max_nota)
        }
    }


class TestEvaluador(unittest.TestCase):
    def test_calcular_promedios_vacio(self):
        baseline = Baseline([], 90, 4)
        evaluador = Evaluador([], 90, 4)
        self.assertEqual(baseline.calcular_promedios(), evaluador.calcular_promedios())

    def test_calcular_promedios_valido(self):
        lista_estudiantes = [get_estudiante() for i in range(1000)]
        baseline = Baseline(lista_estudiantes, 90, 4)
        evaluador = Evaluador(lista_estudiantes, 90, 4)
        self.assertEqual(baseline.calcular_promedios(), evaluador.calcular_promedios())

    def test_calcular_promedios_extra_extras(self):
        lista_estudiantes = [get_estudiante(total_extras=8) for i in range(10)]
        baseline = Baseline(lista_estudiantes, 90, 4)
        evaluador = Evaluador(lista_estudiantes, 90, 4)
        self.assertEqual(baseline.calcular_promedios(), evaluador.calcular_promedios())

    def test_calcular_promedios_baja_asistencia(self):
        lista_estudiantes = [get_estudiante(asistencia=40) for i in range(10)]
        baseline = Baseline(lista_estudiantes, 90, 4)
        evaluador = Evaluador(lista_estudiantes, 90, 4)
        self.assertEqual(baseline.calcular_promedios(), evaluador.calcular_promedios())


if __name__ == '__main__':
    unittest.main()
    # test_list = [get_estudiante() for i in range(10)]
    # evaluador = Evaluador(lista_estudiantes=test_list, min_asistencia=80, max_extras=5)
    # baseline = Baseline(lista_estudiantes=test_list, min_asistencia=80, max_extras=5)
    #
    # print(evaluador.calcular_promedios() == baseline.calcular_promedios())
    # print(evaluador.obtener_mejor_estudiante() == baseline.obtener_mejor_estudiante())


