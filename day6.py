#!/usr/bin/env python
# coding: utf-8

# In[4]:


# file handling
# modes of opening 
# r => read
# w => write
# a => append
# r+ => read & write


# In[31]:


f = open('t1.txt' , 'w')

# some file object attributes
print(f.closed)
print(f.name)
print(f.mode)

for i in range(10):
    f.write("Line {0:d} \n".format(i))
f.close()


# In[33]:


f = open('t1.txt','r')
# print(f.read())   # entire file text
# f.read(15)          # first 15 character

for i in range(5):
    print(f.readline())           # reads one line at a time
    
f.seek(0)          # jumps to a particular line
l = f.readlines()  # returns a list with all the lines of file
print(l)
f.tell()  # no of characters


# In[34]:


# append mode

f = open('t1.txt' ,'a')
for i in range(5):
    f.write('Appended {0:d}\n'.format(i))
    
f = open('t1.txt','r')
print(f.read())

f.close()


# In[35]:


# rename a file

import os 

os.rename('t1.txt','kunal.txt')


# # Directory / Folder

# In[40]:


import os 
os.rmdir('demo')  # remove 
os.mkdir('demo')  # create
os.listdir()      # list


# In[41]:


os.rename('demo','newdemo')
os.listdir()      # list


# In[44]:


# list the files of a directory
os.listdir('pyVersions')


# # Exception Handling

# In[45]:


a =1 
b =2 
c = ab
print(c)


# In[46]:


a = int(input('No 1:'))
b = int(input('No 2:'))
c = a/b
print(c)


# In[52]:


# exceptions are runtime errors
# they can be avoided using try except and finally

try:
    a = int(input('No 1:'))
    b = int(input('No 2:'))
    c = a/b
    print(c)
    
# except Exception:   common for all 
except ZeroDivisionError:
    print('Something is wrong' ,ZeroDivisionError)
finally :
    print('I\'ll print no matter what ill always run before the termaination of program ')


# In[1]:


# on try many except

try:
    a = int(input('No 1:'))
    b = int(input('No 2:'))
    c = a/b
    print(c)
    
except ZeroDivisionError:
    print('Something is wrong' ,ZeroDivisionError)
except ValueError:
    print('Something is wrong with value' ,ValueError)
finally :
    print('I\'ll print no matter what ill always run before the termaination of program ')


# In[3]:


# on try many except

try:
    a = int(input('No 1:'))
    b = int(input('No 2:'))
    c = a/b
    print(c)
    
except (ValueError,ZeroDivisionError):
    print('Something is wrong')
finally :
    print('I\'ll print no matter what ill always run before the termaination of program ')


# In[2]:


# menu for accepting a number with handling exception
flag=True
while flag==True:
    try:
        no = int(input('Enter a no'))
        print(no)
    except Exception:
        print(Exception)
        flag=False


# In[1]:


# on try many except

try:
    a = int(input('No 1:'))
    b = int(input('No 2:'))
    c = a/b
    print(c)
    
except ZeroDivisionError:
    print('Something is wrong' ,ZeroDivisionError)
except ValueError:
    print('Something is wrong with value' ,ValueError)
else :
    print('No exception next lines will execute')
finally :
    print('I\'ll print no matter what ill always run before the termaination of program ')


# In[2]:


try:
    f = open("demofile.txt","w")
    f.write("Lorum Ipsum")
except Exception:
    print("Something went wrong when writing to the file")
finally:
    f.close()


# In[ ]:


# user defined exception

try:
    no = int(input('Enter a no '))
    if no < 0:
        raise Exception("Sorry, no numbers below zero") 
# except Exception:
#     print(Exception)
finally:
    print('End')
    


# # MAP 

# In[9]:


# map(function, iterable)

# without map

def sqr(a):
    return a*a

print(sqr(4))


# In[11]:


# with map

x = map(sqr , [1,2,3,4,5])
print(list(x))


# In[13]:


import random 
def subtract(m,n):
    return m-n

result = map(subtract , [5,4,3,2,1],[1,2,3,4,5])
print(list(result))


# # LAmda Function

# In[18]:


# single line function which do not have a name 

a = lambda x,y : x + y

print(a(5,9))


# In[23]:


# combo of def and lambda

def myfun(x):
    return lambda y:x+y

result = myfun(4)
print(result)
print(result(99))


# In[ ]:





# In[ ]:




