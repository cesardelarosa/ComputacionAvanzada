'''
Práctica inicial

Problema:
    Una bola se deja caer desde una torre.
    Calcular la altura de la bola en un tiempo t (input)

Alumno:
    César de la Rosa (cesar.rosa@estudiante.uam.es)

Repositorio web:
    https://github.com/cesardelarosa/ComputacionAvanzada
    
Computación Avanzada, Física UAM.
'''
<<<<<<< HEAD:Prácticas/tests/test1.py

import math
=======
from math import sqrt
from sys import exit
>>>>>>> 8e60b59cab2d5a1b968b816da30c3bca9195f1ef:Prácticas/Newman_2-1.py

g = 9.81

h = float(input("¿Cúal es la altura de la torre (en metros)? "))
t = float(input("¿Para qué tiempo quieres saber la altura de la bola (en segundos)? "))
if h < 0 or t < 0:
	print("No se aceptan valores negativos.")
	exit()

y = h - g * t**2 /2
if y > 0:
	print(f"La altura de la bola tras {t} segundos es de {y:.3f} metros.")
else:
<<<<<<< HEAD:Prácticas/tests/test1.py
    tf = math.sqrt(h/g)
    print("La bola ya llegó al suelo en el segundo", tf)
=======
	tf = sqrt(2 * h / g)
	print(f"La bola ya llegó al suelo en el segundo {tf:.3f}")
>>>>>>> 8e60b59cab2d5a1b968b816da30c3bca9195f1ef:Prácticas/Newman_2-1.py
