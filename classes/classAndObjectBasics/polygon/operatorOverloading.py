__version__ = 1.0
__author__ = "Sourav Raj"
__author_email__ = "souravraj.iitbbs@gmail.com"

import matplotlib.pyplot as plt

class Point:
    def __init__(self, x, y):
        self.x=x
        self.y=y

    def plot(self):
        plt.scatter(self.x, self.y)
        plt.show()

    def __repr__(self) -> str:
        return f'({self.x}, {self.y})'

    def __add__(self, other):
        if isinstance(other, Point):
            x=self.x+other.x
            y=self.y+other.y
        else:
            x=self.x+other
            y=self.y+other
        return Point(x, y)

