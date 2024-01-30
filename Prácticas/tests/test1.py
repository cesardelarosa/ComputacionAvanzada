
from vpython import sphere, vector, rate

my_sphere = sphere(pos=vector(0, 0, 0), radius=0.5)

while True:
	rate(60)
	my_sphere.pos.x += 0.01
