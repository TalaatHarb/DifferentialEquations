import math
import numpy
import matplotlib.pyplot

total_time = 24.0 * 3600

earth_mass = 5.97e24
gravitational_constant = 6.67e-11

radius = gravitational_constant * earth_mass * total_time **2. /4 / math.pi ** 2.0
speed = 2.0 * math.pi * radius / total_time

def acceleration(spaceship_position):
    global earth_mass, gravitational_constant
    
    distance_to_earth = numpy.linalg.norm(spaceship_position)
    
    result = gravitational_constant * (earth_mass/distance_to_earth**3*spaceship_position)    
    
    return result
    
def calculate_error(num_steps):
    global total_time, g
    
    h = total_time / num_steps
    
    x = numpy.zeros([num_steps + 1, 2])
    v = numpy.zeros([num_steps + 1, 2])
    
    x[0, 0] = radius
    v[0, 1] = speed
    
    for step in range(num_steps):
        x[step + 1] = x[step] + h * v[step]
        v[step + 1] = v[step] + h * acceleration(x[step])
        
    error = numpy.linalg.norm(x[-1] - x[0])
    matplotlib.pyplot.scatter(h,error)
    
    return error
        
for num_steps in [200, 500, 1000, 2000, 5000, 10000]:
    error = calculate_error(num_steps)

matplotlib.pyplot.xlim(xmin = 0.0)

axes = matplotlib.pyplot.gca()
axes.set_xlabel('Step size in s')
axes.set_ylabel('Error in m')
matplotlib.pyplot.show()
