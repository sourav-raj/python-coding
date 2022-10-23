# -*- coding: utf-8 -*-
# Indentation: Jupyter Notebook

'''
Race problem
'''

__version__ = 1.0
__author__ = "Sourav Raj"
__author_email__ = "souravraj.iitbbs@gmail.com"

c=int(input())
x, y, v=[], [], []
rows=[]
for row in range(c):
    rows.append(input())
for row in rows:
    x.append(int(row.split()[0]))
    y.append(int(row.split()[1]))
    v.append(int(row.split()[2]))

time=[]
for i in range(len(x)):
    time.append(pow(pow(x[i], 2) + pow(y[i], 2), 0.5)/v[i])

def nCr(n,r):
    return int(n*(n-1)/r)
    
from itertools import groupby
cnt=0
for val in [len(list(group)) for key, group in groupby(time)]:
    if val>=2:
        cnt=cnt+nCr(val,2)
print(cnt)


-------------------------------------------------------

c=int(input())
t=int(input())

rows=[]
for row in range(c):
    rows.append(input().split())
for i in range(len(rows)):
    rows[i][:]=[int(val)*int(rows[i][-1]) for val in rows[i]] 
    
rows_add=[]
if t%2==0:
    for j in range(len(rows)):
        row_add=[]
        for i in range(int((len(rows[j])-1)/2)):
            row_add.append(rows[j][2*i]+rows[j][2*i+1])
        rows_add.append(row_add)
else:
    for j in range(len(rows)):
        row_add=[]
        for i in range(int((len(rows[j])-2)/2)):
            row_add.append(rows[j][2*i]+rows[j][2*i+1])
        rows_add.append(row_add)
output=[]
for row in [list(i) for i in zip(*rows_add)]:
    output.append(row.index(max(row)))

if __name__ == "__main__": 
    print(max(output,key=output.count))