# -*- coding: utf-8 -*-
# Indentation: Visual Studio

'''
ddsd
'''

__version__ = 1.0
__author__ = "Sourav Raj"
__author_email__ = "souravraj.iitbbs@gmail.com"

import turtle

class Polygon:
    def __init__(self, sides, name, size=10, color='red', lineWidth=10):
        self.sides=sides
        self.name=name
        self.size=size
        self.color=color
        self.linewidth=lineWidth
        self.interior_angle=(self.sides-2)*180
        self.angle=self.interior_angle/self.sides

    def draw(self):
        for i in range(self.size):
            turtle.color(self.color)
            turtle.pensize(self.linewidth)
            turtle.forward(100)
            turtle.right(180-self.angle)
        turtle.done()


