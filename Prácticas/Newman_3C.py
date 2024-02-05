'''
Práctica inicial

Problema:
    Representación del movimiento armónico simple

Alumno:
    César de la Rosa (cesar.rosa@estudiante.uam.es)

Repositorio web:
    https://github.com/cesardelarosa/ComputacionAvanzada

Computación Avanzada, Física UAM.
'''

from pylab import plot, show, ylim, xlabel, ylabel, legend, title
from numpy import linspace, sin, exp, pi

x1, x2 = linspace(0.0, 2.0, 20), linspace(0.0, 2.0, 200)
y1, y2, y3 = exp(-x1), exp(-x2), sin(2 * pi * x2)
y4 = y2 * y3
l1, l3, l4 = plot(x1, y1, "bD-"), plot(x2, y3, "go-"), plot(x2, y4, "rs-")
xlabel("Segundos")
ylabel("Voltios")
legend( (l3[0], l4[0]), ("Oscilatorio", "Amortiguado"), shadow = True)
title("Movimiento Oscilatorio Amortiguado")
show()