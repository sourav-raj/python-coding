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

from polygon.operatorOverloading import Point

a=Point(1,1)

a.plot()

b=Point(2,3)


c= a+b
print(str(c))

d=a+5
print(str(d))