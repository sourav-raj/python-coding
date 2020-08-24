# -*- coding: utf-8 -*-
# Indentation: Jupyter Notebook

'''
Statistics module
'''

__version__ = 1.0
__author__ = "Sourav Raj"
__author_email__ = "souravraj.iitbbs@gmail.com"


def main():
    N_C = [x for x in input().split()]
    if 1<= int(N_C[0])<=200:
        N = int(N_C[0])
    if 0 <= float(N_C[1]) <= 100000:
        C = float(N_C[1])
    
    tree_list_orig=[]
    for i in range(N):
        tree_list_orig.append([int(x) for x in input().split()])
    tree_list = []
    for i in range(N):
        if -10000 <=tree_list_orig[i][0]<=10000 and -10000 <=tree_list_orig[i][0]<=10000
    final_tree=[]
    for i in range(N):
        move_flag = True
        for j in range(N):
            if j!=i:
                if not(math.sqrt(pow(tree_list[i][0]-tree_list[j][0], 2) + pow(tree_list[i][1]-tree_list[j][1], 2)) <= C 
                    and tree_list[j][2] <= tree_list[j][3] ) :
                    move_flag=False
        if move_flag == True:
            final_tree.append(i)
    if len(final_tree) == 0:
        return str(-1)
    else:
        return ' '.join([str(i) for i in final_tree])

if __name__ == "__main__":
    print(main())