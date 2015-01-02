import numpy
import matplotlib.pyplot

earth_mass = 5.97e24
gravitational_constant = 6.67e-11
spaceship_mass = 7000.0
total_time = 6 * 60 * 60.0

def acceleration(spaceship_position):
    global earth_mass, gravitational_constant
    
    vector_to_earth = -spaceship_position
    return gravitational_constant * earth_mass / numpy.linalg.norm(vector_to_earth)**3 * vector_to_earth

def heun_boost(num_steps):

    h = total_time / num_steps
    x = numpy.zeros([num_steps + 1, 2])
    v = numpy.zeros([num_steps + 1, 2])
    energy = numpy.zeros(num_steps + 1)
    
    x[0, 0] = 15e6
    x[0, 1] = 1e6
    v[0, 0] = 2e3
    v[0, 1] = 4e3
    
    boost_done = False
    boost_time = 2.0 * 60 * 60.0
    boost_step = 0
        
    for step in range(num_steps):
        if (h * step >= boost_time) and not boost_done:
            v[step] += 300 * v[step, :] / numpy.linalg.norm(v[step])
            boost_step = step
            boost_done = True

        initial_acceleration = acceleration(x[step, :])
        xe = x[step, :] + h * v[step, :]
        ve = v[step, :] + h * initial_acceleration
        
        x[step + 1, :] = x[step, :] + 0.5 * h * (v[step, :] + ve)
        v[step + 1, :] = v[step, :] + 0.5 * h * (initial_acceleration + acceleration(xe))
        
    for step in range(num_steps + 1):
        energy[step] = 0.5 * spaceship_mass * numpy.linalg.norm(v[step])**2 - gravitational_constant * earth_mass * spaceship_mass / numpy.linalg.norm(x[step])
        
    
    return x, energy
    
x, energy = heun_boost(20000)

axes_orbit = matplotlib.pyplot.subplot(211)
matplotlib.pyplot.plot(x[:, 0] , x[:, 1])
matplotlib.pyplot.scatter(0.0, 0.0)
# matplotlib.pyplot.scatter(x[boost_step, 0] , x[boost_step, 1])
axes_energy = matplotlib.pyplot.subplot(212)
matplotlib.pyplot.plot(energy)
matplotlib.pyplot.show()
