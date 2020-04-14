#!/usr/bin/env python
# coding: utf-8

# # Classes and Objects 

# In[1]:


class Person:
    def __init__(self,fname,lname):
        print('Constructor of person')
        self.fname=fname
        self.lname=lname
        
    def __del__ (self):
        print('Memory freed')
        
    def setName(self,fname,lname):
        self.fname=fname
        self.lname=lname
        
    def show(self):
        print(self.fname, "" ,self.lname)


# In[2]:


p = Person("kunal","singh")
p.show()


# In[5]:


# default argument
# only one type of  constructor can be used in python at a time

# inheritance

class Employee(Person):
    def __init__(self,fname,sname,sal):
        print('Constructor of Employee')
        super().__init__(fname,sname)
        self.sal =sal
        
    def setAll(self,fname,sname,sal):
        super().setName(fname,sname)
        self.sal = sal
        
    def show(self):
        super().show()
        print("sal :",self.sal)
        
class Owner(Person):
    def __init__(self,fname,sname,revenue):
        print('Constructor of Owner')
        super().__init__(fname,sname)
        self.revenue =revenue
        
    def setAll(self,fname,sname,revenue):
        super().setName(fname,sname)
        self.revenue = revenue
        
    def show(self):
        super().show()
        print("Revenue :",self.revenue)

        
p = Person("Kunal","Singh")
e = Employee("Om","Prakash",213123)
o = Employee("Sai","KIran",42343244523445)

p.show()
e.show()
o.show()


# # Generators
# > generators are functions which give output acording to requirment
# 
# > returns traversable objects
# 
# > returns only one o|p at a time
# 
# > generators are run with a loop
# 
# > they return using 'yield' statement
# 
# > generators are called using next() method
# 
# > if the body of a func has yield it automatically becomes a generator

# In[9]:


# generator eg

def myGen():
    yield 1
    yield 7
    yield 14
    
for i in myGen():
    print(i)
    


# In[15]:


# storing the result of a generator

a = myGen()
print(a)
print(a.__next__())
print(a.__next__())
print(a.__next__())
# print(a.__next__())  # error on exyta iterations


# In[17]:


# amother generator

def myGen2():
    yield [1,2,3,4,5]
    yield "Kunal"
    yield 12.424
    
for i in myGen2():
    print(i)              # objects


# In[23]:


# dictoniary 

def myGen3(d):
    for i in d.items():
        yield i
D = {
    "name" : "kunal",
    "age" : "21",
    "height" : "5.59",
    "class": "TY"
}
 
a = myGen3(D)
print(a)
print(a.__next__())
print(a.__next__())
print(a.__next__())
print(a.__next__())
# print(a.__next__())    # end of itr error


# # Decorators 
# > Nested Functions
# 
# > Functions are 1st class obj
# 
# > Closure
# 
# > Functions are Parameters

# In[28]:


def outter():
    print("inside outer")
    def inner():
        print("inside inner")
        x =232
        print(x)
        print("leaving inner")
    inner()
    print('Leaving outter')
    
outter()
# inner()              generates an error coz inner function is declared within outter function


# In[33]:


# functions are objects

def myfun():
    print('Heyy')
    
print(type(myfun))
print(myfun)
myfun


# In[40]:


#  functions can be treated as var we can use a ref var to call fun

a = myfun


# In[41]:


a()
a


# In[47]:


# value returning function

def out():
    print('inside out')
    x=34
    def within():
        print('inside within')
        y=232
        s = x + y
        print('Leaving within')
        return s
    print('Leaving out')
    return within      #  returning the obj of fun

a= out()
print(a)
a.__name__    


# In[49]:


# closure 

def out():
    x=34
    def within():
        y=232
        s = x + y
        return s
    return within      #  ret

r = out()
r()                           # it remembers the value of x


# In[52]:


# another eg of closure

def out():
    msg = "hello ksr"
    def inner():
        print(msg)
    return  inner

r = out()
r()
r.__name__


# In[55]:


# Functions are PArameters

# eg 

def fun1():
    print('In fun1')
        
def fun2(func):
    print('In fun2')
    func()

fun2(fun1)
    


# In[57]:


# Decorators

def abc_upper(func):
    def inner():
        str1 = func()
        return str1.upper()
    return inner

def abc_lowwer():
    return "learning decorators"

print(abc_lowwer())

d = abc_upper(abc_lowwer)
print(d())


# In[58]:


# real use case

def abc_upper(func):
    def inner():
        str1 = func()
        return str1.upper()
    return inner

@abc_upper
def abc_lowwer():
    return 'learning decorators'

print(abc_lowwer())


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




