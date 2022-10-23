# -*- coding: utf-8 -*-
# Indentation: Jupyter Notebook

'''
Counting Leaves problem
'''

__version__ = 1.0
__author__ = "Sourav Raj"
__author_email__ = "souravraj.iitbbs@gmail.com"

N = input()
A = []
tempA = raw_input().split()
for x in tempA:
    A.append(int(x))
X = input()

def main(actual_N, original_A, nodeList_toDelete):
    original_N = range(actual_N)
    modified_N = [x for x in original_N if x not in nodeList_toDelete]
    new_treeStruct = []
    for x in modified_N:
        new_treeStruct.append(original_A[x])
    return(no_leafNode(new_treeStruct, modified_N))

def no_leafNode(new_treeStruct, modified_N):
    leafNode = [leafNode for leafNode in modified_N if leafNode not in new_treeStruct]
    return(len(leafNode))

def nodeList_toDelete(X):
    list_indexDel = [X]
    for x in list_indexDel:
        tempChildList = childIndex(x)
        for y in tempChildList:
            list_indexDel.append(y)
    return(list_indexDel)

def childIndex(nodeNum):
    child_indexList = []
    indexCounter = 0
    for x in A:
        if(x == nodeNum):
            child_indexList.append(indexCounter)
        indexCounter += 1
    return(child_indexList)

if __name__ == "__main__": 
    print main(N, A, nodeList_toDelete(X))