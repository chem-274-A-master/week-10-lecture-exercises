"""
Tests for Python exercises.
"""

import os
import sys

import math
import pytest

def test_ClassDecorators1():

    exercise_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "ClassDecorators1"))
    sys.path.append(exercise_dir)
    
    from main import Molecule
    
    assert Molecule.is_diatomic(["H", "H"]) is True, "Expected True for diatomic molecule ['H', 'H']"
    assert Molecule.is_diatomic(["H", "O", "O"]) is False, "Expected False for molecule with more than two atoms ['H', 'O', 'O']"
    assert Molecule.is_diatomic(["O", "O"]) is True, "Expected True for diatomic molecule ['O', 'O']"
    assert Molecule.is_diatomic(["N"]) is False, "Expected False for molecule with only one atom ['N']"

def test_ClassDecorators2():

    exercise_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "ClassDecorators2"))
    sys.path.append(exercise_dir)
    
    from main import Diatomic

    reduced_mass = 2.0
    amplitude = 1.0
    omega = 1.5
    phi = math.pi / 4  # 45 degrees

    # Expected calculations
    k = reduced_mass * omega ** 2
    separation = amplitude * math.cos(phi)
    velocity = -amplitude * omega * math.sin(phi)
    
    # Create instance using from_parameters
    molecule = Diatomic.from_parameters(reduced_mass, amplitude, omega, phi)
    
    # Assertions to verify correctness
    assert math.isclose(molecule.k, k), f"Expected force constant {k}, got {molecule.k}"
    assert math.isclose(molecule.separation, separation), f"Expected separation {separation}, got {molecule.separation}"
    assert math.isclose(molecule.velocity, velocity), f"Expected velocity {velocity}, got {molecule.velocity}"
    assert math.isclose(molecule.mass, reduced_mass), f"Expected mass {reduced_mass}, got {molecule.mass}"

def test_ClassDecorators3():
    # add exercise directory to the path
    exercise_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "ClassDecorators3"))
    sys.path.append(exercise_dir)
    
    from main import Diatomic
    
    # Create an instance of Diatomic
    molecule = Diatomic(reduced_mass=2.0, force_constant=3.0, separation=1.0, velocity=2.0)
    
    # Check that the properties exist
    assert hasattr(molecule, "potential_energy"), "Expected attribute 'potential_energy' to exist"
    assert hasattr(molecule, "kinetic_energy"), "Expected attribute 'kinetic_energy' to exist"
    assert hasattr(molecule, "total_energy"), "Expected attribute 'total_energy' to exist"
    
    # Check that properties are read-only
    with pytest.raises(AttributeError):
        molecule.potential_energy = 10

    with pytest.raises(AttributeError):
        molecule.kinetic_energy = 10

    with pytest.raises(AttributeError):
        molecule.total_energy = 10

def test_ClassOperators1():
    exercise_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "ClassOperators1"))
    sys.path.append(exercise_dir)
    
    from main import Point2D
    
    p1 = Point2D(1, 2)
    p2 = Point2D(1, 4.5)
    
    # Test addition
    val = p1 + p2
    assert val.x == 2, f"Expected x=2, got {val.x}"
    assert val.y == 6.5, f"Expected y=6.5, got {val.y}"
    
    # Test subtraction
    val2 = p1 - p2
    assert val2.x == 0, f"Expected x=0, got {val2.x}"
    assert val2.y == -2.5, f"Expected y=-2.5, got {val2.y}"

def test_ClassOperators2():
    # add exercise directory to the path
    exercise_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "ClassOperators2"))
    sys.path.append(exercise_dir)
    
    # import the Point2D class
    from main import Point2D
    
    # Test cases for equality based on magnitude
    p1 = Point2D(1.0, 2.0)
    p2 = Point2D(2.0, 1.0)
    assert p1 == p2, "Expected p1 == p2 based on magnitude"

    p1 = Point2D(1.0, 2.0)
    p2 = Point2D(0, math.sqrt(5.0))
    assert p1 == p2, "Expected p1 == p2 based on magnitude"
    
    p1 = Point2D(1.5, 2.0)
    p2 = Point2D(2.0, 1.0)
    assert p1 != p2, "Expected p1 != p2 based on magnitude"

def test_ClassOperators3():
    # add exercise directory to the path
    exercise_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "ClassOperators3"))
    sys.path.append(exercise_dir)
    
    # import
    from main import Sentence
    
    # Test cases for length based on word count
    sentence = Sentence("This is a sentence.")
    assert len(sentence) == 4, "Expected 4 words for sentence 'This is a sentence.'"

    sentence = Sentence("Hello world!")
    assert len(sentence) == 2, "Expected 2 words for sentence 'Hello world!'"
    
    sentence = Sentence("Multiple punctuation marks!")
    assert len(sentence) == 3, "Expected 3 words for sentence 'Multiple punctuation marks!'"

def test_CustomDecorators1(capfd):
    # add exercise directory to the path
    exercise_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "CustomDecorators1"))
    sys.path.append(exercise_dir)
    
    # import the timer decorator and my_function
    from main import my_function

    # Call the function to trigger the timer decorator
    my_function(100000)

    # Capture the printed output
    captured = capfd.readouterr()

    # Check if "elapsed time:" is in the output
    assert "elapsed time:" in captured.out.lower(), "Expected 'elapsed time:' in the print output of the timer decorator"


