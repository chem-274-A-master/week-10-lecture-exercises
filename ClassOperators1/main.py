"""
Write a method for the class Point2D to achieve the behavior described in main
"""

class Point2D:
    def __init__(self, x, y):
        self.x = x
        self.y = y


if __name__ == "__main__":

    p1 = Point2D(1, 2)
    p2 = Point2D(1, 4.5)
    
    # val is a point with x=2 and y=6.5
    val = p1 + p2
    
    # val2 is a point with x=0 and y =-2.5
    val2 = p1 - p2