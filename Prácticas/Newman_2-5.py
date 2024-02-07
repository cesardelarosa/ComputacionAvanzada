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

m = 9.11e-31        # kg
E = 10              # eV
V = 9               # eV


k1 = sqrt(2 * m * E)
k2 = sqrt(2 * m * (E - V))

# No ha hecho falta introducir h-barra ya que en las ecuaciones de T y K
# se cancela su valor al dividirse por si mismo

T = 4 * k1 * k2 / (k1 + k2)**2
K = ((k1 - k2) / (k1 + k2))**2

print(f"La probablidad de transmisión es de {T:.3f} y la de reflexión de {K:.3f}.")