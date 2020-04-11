#!/usr/bin/env python
# coding: utf-8

# In[6]:


# day 5 assignment 


# In[15]:


def generateDict():
    d={}
    n = int(input('Please enter Range'))
    for i in range(1,n+1):
        temp = {i:i*i}
        d.update(temp)
    print('Dictoniray of size {0:d} generated'.format(n))
    print(d)
    
generateDict()


# In[20]:


def createList():
    list1 = []
    no = int(input('Plese enter Size of list'))
    
    for i in range(1,no+1):
        list1.append(i)
    print(list1)
    return list1
    
def giveSlice(l,n1,n2):
    if(n1<0 or n2<1 or n2>len(l) or n1>len(l)):
        print('Out of Range to slice')
        return -1
    elif(n1>=n2):
        print('n1 greater than n2 Invalid argument')
        return -1
    else:
        for i in range(n1,n2+1):
            print(l[i],end=" ")
    
l = createList()
giveSlice(l,2,8)


# In[13]:


help('range')

