# Práctica de laboratorio #1: Introducción a Python
En esta práctica de laboratorio se explorarán los aspectos más básicos de la programación en python. Usted deberá 
implementar una clase que cumpla con tareas de cálculo de promedios y notas finales.

Esta práctica cuenta con dos archivos principales:
  1. **estudiantes.py**: Archivo de código principal, toda la lógica de la práctica deberá estar contenida en la clase `Evaluador`.
  2. **grader.py**: Archivo con casos de prueba para calificar el ejercicio.

## Instrucciones
Usted deberá implementar una clase `Evaluador` en el archivo `estudiantes.py` que cumpla con las siguientes características:
  - En la inicialización, deberá recibir una **lista de diccionarios** correspondiente con el registro de notas de cada estudiante,
    la lista tiene la siguiente estructura:
    ```python
    estudiantes = [
    {
        'nombre': 'juan',
        'apellido': 'perez',
        'notas': {
            'MAT': 87,
            'QMC': 76,
            'FIS': 56,
            'LAB': 78
        },
        'extras': [2, 3, 1, 1, 1],
        'asistencia': 90
    },
    {...}
    ]
    ```
    Cada elemento de la lista es un diccionario con los siguientes keys:
      - nombre: nombre del estudiante
      - apellido: apellido del estudiante
      - notas: es un diccionario con elementos correspondientes a {materia: nota}
      - extras: puntos extra obtenidos por el estudiante
      - asistencia: porcentaje de asistencia a las clases del estudiante
    
    Junto con los datos del estudiante, el objeto de tipo Evaluador, también deberá recibir dos parámetros adicionales:
      - min_asistencia: porcentaje mínimo de asistencia para aprobar el semestre
      - max_extras: máximo puntaje extra posible a agregar
    
  - Se contará con un método llamado **calcular_promedios** que realizará un cálculo de promedios y notas finales
    para los estudiantes, este cálculo debe seguir las siguientes reglas:
    - Se debe tomar en cuenta todas las materias incluidas en el key `notas` del diccionario del estudiante. 
    - En caso de que el diccionario `notas` se encuentre vacìo o simplemente no exista, asigne un promedio final de `0`.
    - En caso de que el estudiante cuente con un porcentaje de asistencia **menor** al valor de `min_asistencia`, asigne un promedio final de `0`.
    - Acumule los puntos extras en el key `extras` y sume el acumulado al promedio final tomando en cuenta que el promedio no debe superar el valor `100`
    - El acumulado de puntos extra no puede superar el valor de `max_extras`.
    - El método **calcular_promedios** deberá retornar una lista de diccionarios, en la cual cada elemento debe tener los siguientes keys: **nombre completo** con el 
      nombre completo del estudiante con el nombre y apellido capitalizados, ej: "Jorge Canqui" y **promedio** con la nota final del estudiante
    - 
  - Se contará con un método llamado **obtener_mejor_estudiante** que devolverá un diccionario con los keys: **nombre completo** con el 
      nombre completo del estudiante con el nombre y apellido capitalizados, ej: "Jorge Canqui" y **promedio** con la nota final del mejor estudiante
  - Se contará finalmente con un método llamado **salvar_datos** que realizará el cálculo de las notas y escribirá un archivo con formato 
    `.csv` con el nombre asignado como parámetro con las siguientes columnas: | Nombre Completo | Asistencia | MAT | FIS | QMC | LAB | Total Extras | Promedio Final | Observación |
    - Cada fila será el registro de un estudiante y el campo *Observación* tendrá 2 valores posibles: APROBADO si el promedio final es mayor a 50 puntos y REPROBADO en otro caso.
    - Un archivo de ejemplo se puede encontrar en la carpeta del ejercicio con el nombre de `ejemplo_notas.csv`. 
    
### Pruebas
Para realizar pruebas, usted podrá modificar solamente el archivo `estudiantes.py`, considere todos los casos pertinentes
en la implementación del ejercicio. Para la evaluación se realizarán diversas pruebas y se evaluará la nota del laboratorio según
la cantidad de pruebas superadas con éxito.