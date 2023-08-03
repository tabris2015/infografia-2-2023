estudiantes = [
    {
        'nombre': 'juan',
        'apellido': 'perez',
        'notas': {
            'MAT': 30,
            'QMC': 30,
            'FIS': 30,
            'LAB': 30
        },
        'extras': [2, 3, 1, 1, 1],
        'asistencia': 90
    },
    {
        'nombre': 'ana',
        'apellido': 'rivera',
        'notas': {
            'MAT': 98,
            'QMC': 98,
            'FIS': 98,
            'LAB': 98
        },
        'extras': [1],
        'asistencia': 100
    }
]


class Evaluador:
    """Esta clase implementa diversas funciones para calcular promedios
    de una lista de estudiantes y obtener otros datos adicionales, ademas,
    tambien implementa una funcion para escribir un reporte de notas"""
    def __init__(self, lista_estudiantes, min_asistencia, max_extras):
        self.lista_estudiantes = lista_estudiantes
        self.min_asistencia = min_asistencia
        self.max_extras = max_extras

    def calcular_promedios(self):
        # IMPLEMENTAR METODO
        lista_notas = []
        return lista_notas

    def obtener_mejor_estudiante(self):
        # IMPLEMENTAR METODO
        return {'nombre completo': 'juan perez', 'promedio': 50}

    def salvar_datos(self, nombre_archivo):
        # IMPLEMENTAR METODO
        print('salvando datos')


# -----------------------------------------#
# ----> NO MODIFICAR DESDE AQUI! <---------#
# -----------------------------------------#
def comparar_archivo_notas(archivo):
    with open('ejemplo_notas.csv', 'r') as archivo_correcto:
        correcto_str = archivo_correcto.read()

    with open(archivo, 'r') as archivo:
        archivo_str = archivo.read()

    return correcto_str == archivo_str


if __name__ == '__main__':
    # datos iniciales
    nombre_archivo = 'notas.csv'
    notas_correcto = [{'nombre completo': 'Juan Perez', 'promedio': 35.0}, {'nombre completo': 'Ana Rivera', 'promedio': 99.0}]
    mejor_correcto = {'nombre completo': 'Ana Rivera', 'promedio': 99.0}

    # Instanciar evaluador
    evaluador = Evaluador(lista_estudiantes=estudiantes, min_asistencia=80, max_extras=5)
    # calcular promedios
    notas = evaluador.calcular_promedios()
    print(f'calcular_promedios: {notas}')
    if notas == notas_correcto:
        print('Calculo de promedios correcto!')
    else:
        print(f'ERROR, lista de promedios esperada: {notas_correcto}')
    # obtener mejor estudiante
    mejor = evaluador.obtener_mejor_estudiante()
    print(f'obtener_mejor_estudiante: {mejor}')
    if mejor == mejor_correcto:
        print('Mejor estudiante correcto!')
    else:
        print(f'ERROR, mejor estudiante esperado: {mejor_correcto}')
    # salvar datos en archivo
    evaluador.salvar_datos(nombre_archivo)
    if comparar_archivo_notas(nombre_archivo):
        print('Generacion de archivo correcta')
    else:
        print('Generacion de archivos incorrecta, ver archivo "ejemplo_notas.csv"')
