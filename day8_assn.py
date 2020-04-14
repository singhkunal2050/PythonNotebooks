#!/usr/bin/env python
# coding: utf-8

# In[8]:


# make a number have same dig by flipping just one dig 1|0

def check(no):
    n = list(str(no))
    l = len(n)
    if(n.count('0') + n.count('1') != l):
        print('Number cannot contain anything other than 1|0')
    elif(n.count('0')==1 or n.count('1')==1):
        print("YES WE CAN")
    else :
        print('Nooooooooooo!')
    
check(121232)
check(100000)
check(111110)
check(111101111)
check(1000001)
check(2650001)


# In[ ]:




