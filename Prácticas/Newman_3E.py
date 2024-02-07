'''
Práctica inicial

Problema:
    Diagrama de dispersión

Alumno:
    César de la Rosa (cesar.rosa@estudiante.uam.es)

Repositorio web:
    https://github.com/cesardelarosa/ComputacionAvanzada

Computación Avanzada, Física UAM.
'''

from pylab import imshow, show, jet, colorbar
from numpy import loadtxt

datos = loadtxt("circular.txt", float)
imshow(datos), jet(), colorbar()
show()