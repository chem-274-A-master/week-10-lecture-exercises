"""
Decorators - class method exercise

One common use of class methods is as an alternate constructor. 
Write a class method for the provided diatomic class called `from_parameters`

It should take in a reduced mass, amplitude, omega, and phi (in that order) 
and create a diatomic instance with appropriate force constant, separation, and velocity.

You can calculate force constant, k, initial separation, and initial velocity from amplitude, 
phi, and omega using the following expressions:

k = reduced_mass * omega ** 2
separation = amplitude * math.cos(phi)
velocity = -amplitude * omega * math.sin(phi)

"""

import math

class Diatomic:
    def __init__(self, reduced_mass, force_constant, separation, velocity):
         
        self.k = force_constant
        self.mass = reduced_mass
        self.separation = separation
        self.velocity = velocity

        self.omega = math.sqrt(self.k / self.mass)
        self.amplitude = math.sqrt( 2 * (self.potential_energy() + self.kinetic_energy()) / self.k)
        self.phi = math.acos(self.separation / (self.amplitude) ) 
    
    def potential_energy(self):
      return 0.5 * self.k * self.separation ** 2
    
    def kinetic_energy(self):
      return 0.5 * self.mass * self.velocity ** 2
