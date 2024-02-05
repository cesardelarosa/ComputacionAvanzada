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

i = 0
n = 1
while (n < 1e9):
    print(n)
    n=(4*i+2)/(i+2)*n
    i = i + 1
