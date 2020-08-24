# -*- coding: utf-8 -*-
# Indentation: Jupyter Notebook

'''
Neclace Problem
'''

__version__ = 1.0
__author__ = "Sourav Raj"
__author_email__ = "souravraj.iitbbs@gmail.com"

def main(B, R, Y, G):
    if(R == 0):
        if(B!=0):
            return(B)
        if(Y == 0):
            return(G)
        else:
            return (G + 1)        
    else:
        if(Y == 0):
            return (B + G + 1)
        elif(G ==0 and B!=0):
            return(B+ R+ min(R, Y))
        elif(B==0 and G!=0):
            return(2+G+ 2* min(R-1, Y))
        elif(R>Y):
            return(2*min(R, Y) + B + G+1)
        elif(R<=Y):
            return(2*min(R, Y) + B + G)
            
B=input()
R=input()
Y=input()
G=input()
if __name__ == "__main__":
    print main(B,R,Y,G)