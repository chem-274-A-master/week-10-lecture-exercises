"""
Using the provided diatomic class, use the property decorator to make the kinetic,
 potential, and total energy methods appear as non-writable attributes.

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
        self._total_energy = self.total_energy() 
    
    def potential_energy(self):
      return 0.5 * self.k * self.separation ** 2

    def kinetic_energy(self):
      return 0.5 * self.mass * self.velocity ** 2

    def total_energy(self):
      return self.potential_energy() + self.kinetic_energy()