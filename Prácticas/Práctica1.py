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
import sys

g = 9.81

h = float(input("¿Cúal es la altura de la torre (en metros)? "))
t = float(input("¿Para qué tiempo quieres saber la altura de la bola (en segundos)? "))
if h < 0 or t < 0:
	print("No se aceptan valores negativos.")
	sys.exit()

y = h - g * t**2 /2
if y > 0:
	print(f"La altura de la bola tras {t} segundos es de {y:.3f} metros.")
else:
	tf = math.sqrt(2 * h / g)
	print(f"La bola ya llegó al suelo en el segundo {tf:.3f}")
