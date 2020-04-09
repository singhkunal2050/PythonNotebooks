#!/usr/bin/env python
# coding: utf-8

# # Range
# 

# In[7]:


range(1,5)


# In[11]:


for i in range(4):
    print(i)


# In[9]:


for i in range(3,24):
    print(i)


# In[10]:


for i in range(2,72,12):
    print(i)


# In[14]:


for i in range(25,33,7):
    print(i,end=" ")


# In[20]:


sum=0
for i in range(10):
    sum=sum+i
    print(sum,end="\t")  
print()
print('final Sum',sum)


# # Nested for

# In[23]:


for i in range(5):
    for j in range(i):
        print('*',end=" ")
    print()
print("Star Printed")    


# In[24]:


# jump Statements 
# break      escapes current loop
# continue   skips the current iteratiion and iterates to next
# pass       does noting 


# In[28]:


for i  in range(5):
    if(i==3):
        print('gonna break')
        break
    else:
        print(i)


# In[32]:


for i  in range(5):
    if(i==3):
        print('gonna continue')
        continue
        print('after continue')
    else:
        print(i)


# In[31]:


for i  in range(5):
    if(i==3):
        print('gonna pass')
        pass
        print('after pass')
    else:
        print(i)


# # Function

# In[37]:


# Some built in functions 

print(int(2))
print(str('s3dasd'))


# In[40]:


# Some math library built in functions
import math

print(math.cos(23))


# In[62]:


# list all modules
help('modules')


# In[64]:


# list all functions from a module
import os
import turtle

print (dir(os))
print('==================OR====================')
#help('modulename') 

help('random')


# In[60]:


# alias name for module
import math as m
print(m.ceil(4.56))
print(m.pow(2,3))
print(m.log10(2))
print(m.log2(2))
print(m.factorial(5))
print(abs(-4))


# In[61]:


# function composition 
# a function within another function


#    # User Defined Function
#     

# In[74]:


import math

def myfunction():
    print('This is my funtion')
    #num1=int(input('Please enter a number'))
    num1 = random.randint(1,199)
    print('The Square of', num1 ,':: ',math.pow(num1,2) , "!!" )
    
for i in range(5):
    myfunction()


# In[9]:


def calculateBonus(sal,exp,tier):
   bonus=0
   bonus = sal+bonus
   if(tier=='A'):
       bonus= bonus + 1000
   elif(tier=='B'):
       bonus= bonus + 500
   elif(tier=='C'):
       bonus= bonus + 300
   elif(tier=='D'):
       bonus= bonus + 100   
   return bonus
       
def processCandidate():
   name = input('Enter your name::')
   eid = int(input('ENter your ID::'))
   exp = int(input('Enter your Experice::'))
   sal = int(input('Enter your Salary::'))
   tier = input('Enter your Tier /(A ,B,C,D/)::')
   b=calculateBonus(sal,exp,tier)
   print('Your bonus is :: ',b)
   
processCandidate()
   


# In[ ]:




