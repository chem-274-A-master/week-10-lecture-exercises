"""
Write a method for Point2D so that two points can be compared using ==

For this, two points should considered to be equivalent if the magnitude of their vectors 
is the same.
"""

import math

class Point2D:
  def __init__(self, x, y):
    self.x = x
    self.y = y


if __name__ == "__main__":

  p1 = Point2D(1.0, 2.0)
  p2 = Point2D(2.0, 1.0)

  #assert p1 == p2

  p1 = Point2D(1.0, 2.0)
  p2 = Point2D(0, math.sqrt(5.0))

  #assert p1 == p2

  p1 = Point2D(1.5, 2.0)
  p2 = Point2D(2.0, 1.0)

  assert not p1 == p2

