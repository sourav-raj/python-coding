# -*- coding: utf-8 -*-
# Indentation: Visual Studio

'''
create square class using Polygon class


'''

__version__ = 1.0
__author__ = "Sourav Raj"
__author_email__ = "souravraj.iitbbs@gmail.com"

import sys
import turtle

sys.path.append(r'G:\PythonProjects\python\classes\classAndObjectBasics')

from polygon.polygon import Polygon

class Square(Polygon):

    def __init__(self, size=10, color='red', lineWidth=10):
        super(Square, self).__init__( 4, 'square', size, color, lineWidth)

    def draw(self):
        turtle.begin_fill()
        super().draw()
        turtle.end_fill()


