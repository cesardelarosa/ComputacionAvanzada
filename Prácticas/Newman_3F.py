'''
Práctica inicial

Problema:
    Simular estructura NaCl

Alumno:
    César de la Rosa (cesar.rosa@estudiante.uam.es)

Repositorio web:
    https://github.com/cesardelarosa/ComputacionAvanzada

Computación Avanzada, Física UAM.
'''

from vpython import sphere, color, vector

L, M , N = 5, 4, 3
RNa, RCl = 0.5, 0.4
colNa, colCl = color.green, color.magenta

for k in range(-N, N+1, 2):
    for j in range(-M, M+1, 2):
        for i in range(-L, L+1, 2):
            sphere(pos = vector(i,j,k), radius = RNa, color = colNa)
        for i in range(-L+1, L+1, 2):
            sphere(pos = vector(i,j,k), radius = RCl, color = colCl)
    for j in range(-M+1, M+1, 2):
        for i in range(-L, L+1, 2):
            sphere(pos = vector(i,j,k), radius = RNa, color = colNa)
        for i in range(-L+1, L+1, 2):
            sphere(pos = vector(i,j,k), radius = RCl, color = colCl)
for k in range(-N, N+1, 2):
    for j in range(-M, M+1, 2):
        for i in range(-L, L+1, 2):
            sphere(pos = vector(i,j,k), radius = RNa, color = colNa)
        for i in range(-L+1, L+1, 2):
            sphere(pos = vector(i,j,k), radius = RCl, color = colCl)
    for j in range(-M+1, M+1, 2):
        for i in range(-L, L+1, 2):
            sphere(pos = vector(i,j,k), radius = RNa, color = colNa)
        for i in range(-L+1, L+1, 2):
            sphere(pos = vector(i,j,k), radius = RCl, color = colCl)