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


from polygon.inheritenseClass import Square

square = Square(50, 'blue', 20)
print(square.name, square.sides)

square.draw()

