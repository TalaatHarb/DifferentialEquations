import numpy

earth_mass = 5.97e24
moon_mass = 7.35e22
gravitational_constant = 6.67e-11

def acceleration(moon_position, spaceship_position):
    global earth_mass, moon_mass, gravitational_constant
    
    distance_to_earth = numpy.linalg.norm(spaceship_position)
    distance_to_moon = numpy.linalg.norm(moon_position-spaceship_position)
    
    result = gravitational_constant * (earth_mass/distance_to_earth**3*spaceship_position) 
    + (monn_mass/distance_to_moon**3*(moon_position-spaceship_position))
    
    return result