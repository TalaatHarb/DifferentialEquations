import numpy
import matplotlib.pyplot

earth_mass = 5.97e24
gravitational_constant = 6.67e-11
spaceship_mass = 30000.0
total_time = 24 * 60 * 60

def acceleration(spaceship_position):
    global earth_mass, gravitational_constant
    
    vector_to_earth = -spaceship_position
    return gravitational_constant * earth_mass / numpy.linalg.norm(vector_to_earth)**3 * vector_to_earth

def euler_symplectic(num_steps):

    h = total_time / num_steps
    x = numpy.zeros([num_steps + 1, 2])
    v = numpy.zeros([num_steps + 1, 2])
    energy = numpy.zeros(num_steps + 1)
    
    x[0, 0] = 15e6
    x[0, 1] = 1e6
    v[0, 0] = 2e3
    v[0, 1] = 4e3
        
    for step in range(num_steps):
        x[step + 1] = x[step] + h * v[step]
        v[step + 1] = v[step] + h * acceleration(x[step+1])
        
    for step in range(num_steps + 1):
        energy[step] = 0.5 * spaceship_mass * numpy.linalg.norm(v[step])**2 - gravitational_constant * earth_mass * spaceship_mass / numpy.linalg.norm(x[step])
        
    
    return x, energy
    
x, energy = euler_symplectic(20000)

axes_height = matplotlib.pyplot.subplot(211)
matplotlib.pyplot.plot(x[:, 0] , x[:, 1])
matplotlib.pyplot.scatter(0.0, 0.0)
axes_velocity = matplotlib.pyplot.subplot(212)
matplotlib.pyplot.plot(energy)
matplotlib.pyplot.show()