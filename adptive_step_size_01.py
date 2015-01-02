import math
import numpy
import matplotlib.pyplot

total_time = 24.0 * 60 * 60

earth_mass = 5.97e24
gravitational_constant = 6.67e-11

radius = (gravitational_constant * earth_mass * total_time **2. / 4. / math.pi ** 2.0) **(1.0/3.0)
speed = 2.0 * math.pi * radius / total_time

def acceleration(spaceship_position):
    global earth_mass, gravitational_constant
    
    vector_to_earth = -spaceship_position
    return gravitational_constant * earth_mass / numpy.linalg.norm(vector_to_earth)**3 * vector_to_earth

def orbit():
    x = numpy.zeros(2)
    v = numpy.zeros(2)
    
    x[0] = 15e6
    x[1] = 1e6
    v[0] = 2e3
    v[1] = 4e3
    
    matplotlib.pyplot.scatter(x[0], x[1], s = 4)
    current_time = 0.0
    
    h = 100
    h_new = h
    
    tolerance = 5e5
    
    while current_time < total_time :
        acceleration0 = acceleration(x)
        xe = x + h * v
        ve = v + h * acceleration0
        xh = x + 0.5 * h * (v + ve)
        vh = v + 0.5 * h * (acceleration0 + acceleration(xe))
        
        x = xh
        v = vh 
        
        error = numpy.linalg.norm(xe-xh) + total_time * numpy.linalg.norm(ve - vh)
        h_new = h * math.sqrt(tolerance / (1e-50 + error))
        h_new = min(1800.0 , max( 0.1, h_new))
        
        matplotlib.pyplot.scatter(x[0], x[1], s = 1)
        current_time += h
        h = h_new
        
        matplotlib.pyplot.scatter(0.0, 0.0)
        axes = matplotlib.pyplot.gca()
        
        
    matplotlib.pyplot.show()


orbit()