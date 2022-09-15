from math import sqrt

class Point:
    """A class to draw, move, and manage a 2D point"""

    def __init__(self, x=0, y=0):
        """Set values of both x and y, if no value given defaults to 0,0"""
        self.x = x
        self.y = y

    def move(self, x, y):
        """Simulates movement of a point in x and  y"""
        self.x += x
        self.y += y

    def reset(self):
        """Reset co-ordinates of a point to 0,0"""
        self.x = 0
        self.y = 0

    def calculate_distance(self, other_point):
        """Calculates distance between two points using pathagoras theorm"""
        return sqrt(((self.x - other_point.x)**2)+
                    ((self.y - other_point.y)**2))
    