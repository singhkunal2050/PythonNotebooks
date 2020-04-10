#!/usr/bin/env python
# coding: utf-8

# In[2]:


# day5 Letsupgrade


# In[16]:


# print X pattern using nested loop

for i in range(10):
    for j in range(10):
        if(i==j or i== 10-j-1 ):
            print('*',end=" ")
        else:
            print(' ',end=" ")
    print()


# In[22]:


# if no of arguments is unknown then we can use this
def my_function(*kids):
    print("The youngest child is ", kids[1])

my_function("Emil", "Tobias", "Linus",23232)


# In[24]:


# You can also send arguments with the key = value syntax. This way the order of the arguments does not matter

def my_function(child3, child2, child1):
    print("The youngest child is " + child3)

my_function(child1 = "Emil", child2 = "Tobias", child3 = "Linus")


# In[25]:


# another way

def my_function(**kid):
    print("His last name is " + kid["lname"])

my_function(fname = "Tobias", lname = "Refsnes")


# In[5]:


#default parameter

def my_function(country = "Norway"):
    print("I am from " + country)

my_function("Sweden")
my_function("India")
my_function()
my_function("Brazil")


# In[13]:


# Recursion
# factorial of a no

def fact(no):
    if(no==0):
        return 1
    elif(no>0):
        return no*fact(no-1)
    else: 
        return -1

for i in range(10):
    print(fact(i))

for i in range(10,0,-1):
    print(fact(i))


# # Lamda Functions in py
#     >A lambda function is a small anonymous function.
#         >lambda arguments : expression
# 

# In[111]:


x = lambda a : a + 10
print(x(5))


# In[116]:


x = lambda a, b, c : a + b + c
print(x(5, 6, 2))


# In[ ]:





# In[ ]:





# In[4]:


# Taking User Input

num= int(input('enter a number'))
print(num)

str1= input('enter a str')
print(str1)

li= list(input('enter a str'))
print(li)


# In[6]:


# input eg
a = int (input('Enter a number'))
b = int (input('Enter another number'))
print('Sum is {0:d}'.format(a+b))


# In[17]:


# String Slcing 

str1= 'ThisWasTheString'

print(str1[1:5])  # from 1 to 5 char 
print(str1[:5])   # from start to 5
print(str1[5:])   # from 5 to end
print(str1[::-1])  # print in reverse
print(str1[-8:-5])  # from 8th last to fifth last


# In[18]:


# STring library functions

s1 = 'MyNameisKunal'
s2 = 'IamTryingPython'

help('str')


# In[42]:


print(s1+s2)
print(s1.capitalize())  # only first char of word becomes capital
print(s1.casefold())   # Return a version of the string suitable for caseless comparisons.
print(s1.count('a'))  # count of char
print(s1.swapcase())
print(s1.isalpha())
print(s1.isdigit())
print(len(s1))
print(s1.replace('a','|'))
print(max(s1))  # returns the char which has biggest ascii value
print(min(s1))  # returns the char which has lowe ascii value


# In[44]:


# Membership OPerators 
# in and not in operators
li = list('Kunal is my name')
print('K' in li)


# In[64]:


# strings are immutable  

st ='Kunal'
print(st[0])
st[0]='Y'
print(st[0])


# but replace function can be used to replace a char it internally 
# creates a copy of the string with modification and dels the old one


# In[52]:


# find char in str 
st='eNewStringe'
print(st.find('e',0,5))  #  returns first occ b|W the range
print(st.find('e',1))  #  returns first occ b|W 1 to end
 


# # LIST TUPLE AND DICTONIARY
# 

# In[63]:


li = list('132cv,32')
print(li)   # list are mutable

li[2] = '|'
print(li)


# In[95]:


# list of lists 

# l1 = [1,2,3,4,5,6,7]    better for int list
l1 =list('1234567')     # str list
l2 =list('5446446')
l3 =list('8754467')
l4 =list('0054549')

l = [l1,l2,l3,l4]

for i in l:
    for j in i:
        print(j,end=" ")
    print()

print('---------------can access through posn-------------')
print(l[1][4])


# In[87]:


# remmve from list 
l2.remove('4')
l2


# In[94]:


# pop : removes last 
# pop(n) :: removes index n

l1.pop(1)
l1


# In[97]:


# all list functions

help('list')


# In[110]:


# sort 
l3.sort()
l3


# In[115]:


# tuple 

# single valued tuple 
t = (1,)
t2 = (1)

print(type(t))
print(type(t2))


# In[119]:


# most methods like list wotk on tuple

t3 =(1,2,3)
t3=t3*4
print(t3)
print(1 in t3)


# # Variable len arguments

# In[124]:


def add(*nos):
    print(nos)
    
add(1,2,3,4,5,6)


# # Dictionary / Associative Array

# In[151]:


# values in dict are mutable 
# keys are immutable

dict1 = {
    1:'Kunal',
    2:'Atharv',
    3:'Shree'
}

dict2 = {
    'Cname':'Modern',
    'Caddr': 'Pune',
    'Cfees':'10000'
}


print(dict1)


# In[152]:


print(dict1[1])
print(dict1.keys())
print(dict1.values())
print(dict1.get(2))
#print(dict1.pop(3))
dict1.update({'54':'Anish'})
print(dict1)
dict1.update(dict2)
print(dict1)


# In[156]:


# Dictoniary with key value where values can be another data structure

dict3 = {
    1:[1,2,3],
    2:[2,5,7],
    3:[7,443,1]
}


dict4 = {
    1:(1,2,3),
    2:[2,5,7],
    3:{7,443,1}
}

print(dict3)
print(dict4)


# In[158]:


# nested Dictoniary

D = { {dict1 : dict2 }, dict3 : dict4}


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




