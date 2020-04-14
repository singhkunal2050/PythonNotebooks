#!/usr/bin/env python
# coding: utf-8

# # Advance Functions
# > Map 
# 
# > filter 
# 
# > lambda 
# 
# > reduce

# In[1]:


# map 
# used to call a function with a chunk of values

def addtill(n):
    s=0
    for i in range(n+1):
        s = s + i
    return s

li = [4,52,2,1,151,512,53]
tu = 5,6,3443,121,4267,7

result = map(addtill,li)
result2 = map(addtill,tu)

print(list(result))
print(list(result2))


# In[2]:


# using map with lambda function 
# anonymous function
# used when function is only needed only 
# inside as input to other function

x = lambda x,y:x+y
print(x(3,45))

li=[2,4,5,67,2,1]
li2=[12,34,55,767,82,10]

result = map(x,li,li2)
print(list(result))
print(result)


# In[3]:


# assigning a labda function to a variabke using a normal function

def thisfun(x):
    return lambda y:x+y

r = thisfun(12)
print(r)
print(r(11))


# In[4]:


# defining lamda within map 

li = [243,234,34,21,3,2,23]
result = map( lambda x:x+3 , li)
print(list(result))


# # filter
# >Getting some elements out of an existing array and creating a new array out of them is called filtering.

# In[5]:


li = [-4,-85,4,534,432,2,3,32,23,5656]

def isEven(n):
    if(n%2==0):
        return n
r = filter(isEven,li)
print(r)
print(list(r))              # only even results stored in array


# In[6]:


r = filter(lambda x:x>=3 , x*x ,[1,2,3,4,])
print(list(r))


# # reduce
# > reduce ( function , iterable)
# 
# > does a cumulative opearion on the list 

# In[7]:


from  functools import reduce

li = [1,2,3,4,5]

def sqr(a,b):
    return a+b 

x = reduce(sqr,li)
print(x)


# In[8]:


r = reduce(lambda x,y:x/y,li)
print(r)
print((((1/2)/3)/4)/5)                 # cumulative results simulation results


# In[10]:


r = filter(lambda x,y: x%2==0,x+y,li)
r = list(r)
print(r)
# (lambda x,y:x+y, filter(lambda x,y:x+y,li)) )


# In[9]:


li = [2,3,4,5,6,8,10]
# r = map(lambda x,y:if ()x/y)

reduce(lambda x,y:x/y , map (lambda x,y:x+y, filter(lambda x,y:x+y,li)) )


# > Write a Python program to add the digits of a positive integer repeatedly until the result has a
# single digit.
# Input Format:
# The first line of the input contains a number n.
# Output:
# Print the resultant number
# Example:
# Input:
# 48
# Output:
# 3
# Explanation: If you add digits 4 and 8, you will get 12. Again adding 1 and 2 will give 3
# which is a single digit and hence the answer.

# In[30]:


def addno(no):
    if(abs(no)>9):
        s = 0
        t = no
        while(t>0):
            s = s + t%10
            t = t // 10
        print('The Sum is ',s)
    else:
        print('The Sum is ',no)
        
print(addno(121))
print(addno(12))
print(addno(7))
print(addno(91312))
print(addno(-121))


# In[ ]:





# In[ ]:




