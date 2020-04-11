#!/usr/bin/env python
# coding: utf-8

# In[17]:


# ass1 
# count the total nos of holes in the given string 
for i in range(65,91,1):
    print("{0:c}".format(i),end=" ")
print()
for i in range(97,123,1):
    print("{0:c}".format(i),end=" ")


# In[1]:


def countHoles(str):
    holes=0
    indexes = []
    
    for i in range(len(str)):
        if(str[i]=="A" or str[i]=="a" or str[i]=="b" or str[i]=="D" or str[i]=="d" or str[i]=="e" or str[i]=="g" or str[i]=="O" or str[i]=="o" or str[i]=="P" or str[i]=="p" or str[i]=="Q" or str[i]=="q" or str[i]=="R"):
            holes=holes+1;
            indexes.append(i)
        elif(str[i]=="B"):
            holes=holes+2;
            indexes.append(i) 
    print("The Total no of holes are {0:d}\n".format(holes));
    print('The characters are::')
    for i in indexes:
        print(str[i] , end = " ")
        
flag = 1 

while(flag==1):
    str = input('Please enter a String :: ')
    countHoles(str)
    flag = int(input('Want to try again =>1 else=>0'))


# In[ ]:


# ass 2 
# notebook of map and lambda


# # MAP 

# In[ ]:


# map(function, iterable)

# without map

def sqr(a):
    return a*a

print(sqr(4))


# In[ ]:


# with map

x = map(sqr , [1,2,3,4,5])
print(list(x))


# In[ ]:


import random 
def subtract(m,n):
    return m-n

result = map(subtract , [5,4,3,2,1],[1,2,3,4,5])
print(list(result))


# # LAmda Function

# In[ ]:


# single line function which do not have a name 

a = lambda x,y : x + y

print(a(5,9))


# In[ ]:


# combo of def and lambda

def myfun(x):
    return lambda y:x+y

result = myfun(4)
print(result)
print(result(99))


# In[ ]:





# In[ ]:





# In[ ]:




