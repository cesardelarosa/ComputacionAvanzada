'''
Práctica inicial

Problema:
    Diagrama Hertzsprung-Russell

Alumno:
    César de la Rosa (cesar.rosa@estudiante.uam.es)

Repositorio web:
    https://github.com/cesardelarosa/ComputacionAvanzada

Computación Avanzada, Física UAM.
'''

from pylab import scatter, xlabel, ylabel, xlim, ylim, title, show, text
from numpy import loadtxt

datos = loadtxt("stars.txt", float)
x, y = datos[: , 0], datos[: , 1]
scatter(x, y, c = x, cmap = "hsv", s = 75)
xlabel("Temperatura")
ylabel("Magnitud")
xlim(13000, 0)
ylim(20, -5)
text(4500, 4.5, "Secuencia Principal", fontsize = 14, style = "italic")
text(11000, 15, "Enanas Blancas", fontsize = 14, style = "italic")
title("Diagrama Hertzprung-Russell")
show()