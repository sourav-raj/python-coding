# -*- coding: utf-8 -*-
# Indentation: Jupyter Notebook

'''
Hiding Christmas gifts problem
'''

__version__ = 1.0
__author__ = "Sourav Raj"
__author_email__ = "souravraj.iitbbs@gmail.com"

def testCase_input():
    '''
    This Function Takes the User Input or Command Line Inputs
        >> 1. initValues = takes raw_Input() for N and M Values
        >> 2. init_treeStruct: A List-of-List Containing Branches Information
                [to Edit init_treeStruct to Make a Dictionary in (K,[V]) Format]
                    (i)  K: House Number
                    (ii) V: List of Houses Connected to the K-House
        >> 3. santaVisit: List of Start & End House on Each Santa Visit (M)
    '''
    # Generated Test Case Inputs
    initValues = raw_input().split()
    N = int(initValues[0])
    M = int(initValues[1])

    init_treeStruct = []
    for i in range(N-1):
        tempRoad = raw_input().split()
        init_treeStruct.append([int(j) for j in tempRoad])
    
    santaVisit = []
    for i in range(M):
        tempVisit = raw_input().split()
        santaVisit.append([int(j) for j in tempVisit])
    
    return(N, M, init_treeStruct, santaVisit)

def defining_possiblePaths(N, original_treeStruct):
    # Function to Create a Dictionary of (K, V) Pairs of House & its Connected House in List
    housePath = {}
    for i in range(N):
        conValue = [x[1] for x in original_treeStruct if x[0] == i+1] + [x[0] for x in original_treeStruct if x[1] == i+1]
        housePath.update({i+1 : list(set(conValue))})
    return(housePath)

def generating_houseGiftDict(N):
    tempDict = {}
    for i in range(N):
        tempDict.update({i+1 : 0})
    return(tempDict)

def pathFinder(house_connectStruct, startHouse, endHouse, path=[]):
    path = path + [startHouse]
    if startHouse == endHouse:
        return(path)
    if not house_connectStruct.has_key(startHouse):
        return(None)
    for houseNode in house_connectStruct[startHouse]:
        if houseNode not in path:
            requiredPath = pathFinder(house_connectStruct, houseNode, endHouse, path)
            if requiredPath:
                return(requiredPath)
    return(None)

def house_maxGift(houseGiftStruct):
    '''
    Returns the Maximum No. of Gifts
    '''
    V_giftCount = list(houseGiftStruct.values())
    #K_houseNum = list(houseGiftStruct.keys())
    #return K_houseNum[V_giftCount.index(max(V_giftCount))]
    return(max(V_giftCount))

def main():
    # Generating User Input
    N, M, init_treeStruct, santaVisit = testCase_input()
    # Getting the New Graph Structure & Creating a New Dictionary in (K, V) - K: House, V: Gifts Count
    house_graphStruct = defining_possiblePaths(N, init_treeStruct)
    #print 'HOUSE GRAPH: ', house_graphStruct
    house_withGiftCount = generating_houseGiftDict(N)
    #print 'HOUSE GIFT COUNT: ', house_withGiftCount
    
    # Sart of Santa Visit
    #print '===== ===== ===== ===== ====='
    for visitInfo in santaVisit:
        #print 'Visit Info: ', visitInfo
        if(visitInfo[0] == visitInfo[1]):
            house_withGiftCount.update({visitInfo[0] : house_withGiftCount[visitInfo[0]] + 2})
        else:
            pathFound = pathFinder(house_graphStruct, visitInfo[0], visitInfo[1])
            #print '\tPath: ', pathFound
            for everyHouse in pathFound:
                #print '\t\t@innerFor - everyHouse: ', everyHouse
                # Increasing the Gift Count by One when there is a Visit by Santa!
                #print '\t\tUpdating: ', everyHouse
                house_withGiftCount.update({everyHouse : house_withGiftCount[everyHouse] + 1})
            
    #print 'Final House Gift Count: ', house_withGiftCount
    return(house_maxGift(house_withGiftCount))

if __name__ == "__main__":
    print main()