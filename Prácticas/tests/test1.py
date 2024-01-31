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

import math

g = 9.81

h = float(input("¿Cúal es la altura de la torre (en metros)? "))
t = float(input("¿Para qué tiempo quieres saber la altura de la bola (en segundos)? "))

y = h - g * t * t
if y > 0:
    print("La altura de la bola tras", t," segundos es de ", y," metros.")
else:
    tf = math.sqrt(h/g)
    print("La bola ya llegó al suelo en el segundo", tf)
