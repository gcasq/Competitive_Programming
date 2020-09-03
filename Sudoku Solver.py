#!/usr/bin/env python
# coding: utf-8

# In[28]:


import numpy as np


# In[1]:


grid = [
    [0,0,6,8,0,0,0,0,0],
    [2,0,0,0,3,0,7,0,0],
    [0,9,0,0,0,2,0,1,0],
    [0,1,0,0,0,0,0,4,0],
    [0,0,5,0,0,0,0,0,6],
    [0,0,0,0,0,5,2,0,0],
    [5,0,0,0,6,0,0,0,9],
    [0,0,0,0,8,0,1,0,0],
    [7,4,0,0,0,0,5,0,0]
]


# In[17]:


def isvalid(x,y,n):
    global grid
    for i in range(0,9):
        if grid[i][y]==n:
            return False
    for i in range(0,9):
        if grid[x][i]==n:
            return False
    x0 = x//3
    y0 = y//3
    x0 = x0*3
    y0 = y0*3
    for i in range(0,3):
        for j in range(0,3):
            if grid[x0+i][y0+j]==n:
                return False
    return True


# In[16]:


isvalid(0,7,7)


# In[29]:


def solve():
    global grid
    for x in range(0,9):
        for y in range(0,9):
            if grid[x][y]==0:
                for n in range(1,10):
                    if isvalid(x,y,n):
                        grid[x][y] = n
                        solve()
                        grid[x][y] = 0 #se a solve() do valor seguinte retornou, foi porque nenhum outro valor
                                       #conseguiu ser encaixado, e então zera este valor e tenta-se novamente o seguinte
                                       #porque prossegue no for
                return #Se nenhum número foi válido, então chega aqui. Ele retorna a função, e o valor anterior vai a 0
    print(np.matrix(grid))


# In[30]:


solve()


# In[31]:


grid


# In[ ]:




