#!/usr/bin/env python
# coding: utf-8

# In[32]:


grid1 = [
    [5,8,6,6,1,9],
    [1,3,9,7,6,9],
    [2,7,9,8,2,7],
    [7,2,6,4,5,6],
    [3,5,8,9,3,8],
    [5,4,3,5,1,5]
]
grid2 = [
    [0,0,0,0,0,0],
    [0,0,0,0,0,0],
    [0,0,0,0,0,0],
    [0,0,0,0,0,0],
    [0,0,0,0,0,0],
    [0,0,0,0,0,0]
]

import numpy as np


# In[33]:


def ispossible(x,y):

    sumx=0
    sumy=0
    count = 0
    grid2[x][y] = grid1[x][y]
    for i in range(0,6):
        sumx = sumx + grid2[i][y]
        sumy = sumy + grid2[x][i]
    if sumx > 9 or sumy > 9:
        grid2[x][y] = 0
        return False
    
    for i in range(0,6):
        for j in range(0,6):
            if grid2[x][y] == grid2[i][j]:
                count = count+1
    if count == 2:
        grid2[x][y] = 0
        return False #se o numero aparece 2x, então ele não pode aparecer
    return True


# In[34]:


ispossible(5,5)


# In[35]:


def solve(init):
    global grid1
    global grid2
    
    for n in range(init,10):
        for i in range(0,6):
            for j in range(0,6):
                if n == grid1[i][j]:
                    if ispossible(i,j):
                        grid2[i][j] = n
                        solve(init+1)
                        grid2[i][j] = 0
        return
    
    print(np.matrix(grid2))
    print()


# In[36]:


grid2 = [
    [0,0,0,0,0,0],
    [0,0,0,0,0,0],
    [0,0,0,0,0,0],
    [0,0,0,0,0,0],
    [0,0,0,0,0,0],
    [0,0,0,0,0,0]
]


solve(1)


# In[ ]:




