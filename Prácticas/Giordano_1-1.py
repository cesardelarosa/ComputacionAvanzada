
'''
Práctica inicial

Problema:
    Calcular la velocidad de un cuerpo por acción de la gravedad comparando la solución analítica con el método de Euler

Alumno:
    César de la Rosa (cesar.rosa@estudiante.uam.es)

Repositorio web:
    https://github.com/cesardelarosa/ComputacionAvanzada
    
Computación Avanzada, Física UAM.
'''

g = 9.8
t_max = 10
h = float(input("Defina el intervalo de tiempo 'h' en segundos"))
t = 0
v = 0

print("Tiempo (s) \t Velocidad Euler (m/s) \t Velocidad Analítica (m/s)")
while t < t_max:
    v_analitica = -g * t
    print(f"{t:.3f} \t\t {v:.3f} \t\t {v_analitica:.3f}")
    v -= g * h
    t += h