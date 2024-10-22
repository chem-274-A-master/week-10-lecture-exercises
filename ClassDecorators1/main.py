"""
Class Decorators - Static Methods

Add a static method to the class that takes in a list of elements and returns True 
if the list represents a diatomic molecule and False otherwise. 
The method should be called `is_diatomic`

"""

class Molecule:
    def __init__(self, atoms):
        self.atoms = atoms

        
    

if __name__ == "__main__":

  atom_list_1 = ["H", "H"]
  
  # returns True
  print(Molecule.is_diatomic(atom_list_1))

  atom_list_2 = ["H", "O", "O"]

  # returns False
  print(Molecule.is_diatomic(atom_list_2))


