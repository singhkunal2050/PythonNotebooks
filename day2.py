#!/usr/bin/env python
# coding: utf-8

# In[35]:


#two modes in python script and interpreter

a = 1
b = 2
c= a+b 
print(c)


# In[1]:


import os 
os.getcwd()


# In[19]:


# catenating string with dff types

x = 23
y = 42

print('Value os X:: ', x ,' and y::',y )
print("Value os X:: {0:2d} y:: {1:d} ".format(x,y))


# In[2]:


a
b
c


# In[3]:


print(a)
print(b)
print(c)


# In[30]:


str1  = "Kunal_is_good "
str2  = "anisha_is_bad "
str3 = str1 + str2
str3


# In[31]:


# slicing in python

print(str3[5:11])


# In[32]:


print(str3[4])


# In[35]:


print(str3[-2])


# In[39]:


# first index is always smaller for slicing 

print([str3[-10:-2]])


# # KEYWORS
# 

and	A logical operator
as	To create an alias
assert	For debugging
break	To break out of a loop
class	To define a class
continue	To continue to the next iteration of a loop
def	To define a function
del	To delete an object
elif	Used in conditional statements, same as else if
else	Used in conditional statements
except	Used with exceptions, what to do when an exception occurs
False	Boolean value, result of comparison operations
finally	Used with exceptions, a block of code that will be executed no matter if there is an exception or not
for	To create a for loop
from	To import specific parts of a module
global	To declare a global variable
if	To make a conditional statement
import	To import a module
in	To check if a value is present in a list, tuple, etc.
is	To test if two variables are equal
lambda	To create an anonymous function
None	Represents a null value
nonlocal	To declare a non-local variable
not	A logical operator
or	A logical operator
pass	A null statement, a statement that will do nothing
raise	To raise an exception
return	To exit a function and return a value
True	Boolean value, result of comparison operations
try	To make a try...except statement
while	To create a while loop
with	Used to simplify exception handling
yield	To end a function, returns a generator


# In[20]:


#ccomma separated numbers or data is considered as tuple

a = 'Kunal',23,2000,'Pune'
print(a)


# In[27]:


# Ttype Casting

i = 10  #int 
f = 12.2  #float 
s = 'Stirng sad'  #string
tup = (12,24,2452,'Kunla')        #tuple
li = [32,42,42,'Kdjkasdas']     #list
se = [23,321,4,42,22,44,22,44]   #set

print(i)
print(f)
print(s)
print(tup)
print(li)
print(se)

print("---------------------Lets do Type Casting-------------------------")

print(int(f))
print(float(i))
print(list(se))
print(set(li))
print(list(tup))
print(list(s))


# In[31]:


# ** is used for ^

a = 10
b = 3

print(a**b)


# In[34]:


# Precedence and Priority

"""
**
()
*
/
+
-
"""
print(1+(2**2)*23/4)


# In[ ]:




