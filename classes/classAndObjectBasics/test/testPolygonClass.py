# -*- coding: utf-8 -*-
# Indentation: Visual Studio

'''
Polygon class


'''

__version__ = 1.0
__author__ = "Sourav Raj"
__author_email__ = "souravraj.iitbbs@gmail.com"

import sys

sys.path.append(r'G:\PythonProjects\python\classes\classAndObjectBasics')


from polygon.polygon import Polygon

square = Polygon(4, 'square')
print(square.name, square.sides)

square.draw()