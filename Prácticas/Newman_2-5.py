'''
Práctica inicial

Problema:
    Calcular coeficientes de transmisión y reflexión dados unos datos

Alumno:
    César de la Rosa (cesar.rosa@estudiante.uam.es)

Repositorio web:
    https://github.com/cesardelarosa/ComputacionAvanzada

Computación Avanzada, Física UAM.
'''

from math import sqrt

m = 9.11e-31    # kg
E = 10          # eV
V = 9           # eV
hbarra = 1.054  # J*s

k1 = sqrt(2 * m * E) / hbarra
k2 = sqrt(2 * m * (E - V)) / hbarra

T = 4 * k1 * k2 / (k1 + k2)**2
K = ((k1 - k2) / (k1 + k2))**2

print(f"La probablidad de transmisión es de {T:.3f} y la de reflexión de {K:.3f}.")
