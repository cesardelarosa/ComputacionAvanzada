'''
Práctica inicial

Problema:
    Imprimir números de Catalan hasta 1e9

Alumno:
    César de la Rosa (cesar.rosa@estudiante.uam.es)

Repositorio web:
    https://github.com/cesardelarosa/ComputacionAvanzada

Computación Avanzada, Física UAM.
'''

i, n = 0, 1
while (n <= 1e9):
    print(int(n))
    n *= (4 * i + 2) / (i + 2)
    i += 1