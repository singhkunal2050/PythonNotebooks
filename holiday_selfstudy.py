#!/usr/bin/env python
# coding: utf-8

# # Classes and Objects
# >Python is an object oriented programming language.
# 
# >Almost everything in Python is an object, with its properties and methods.
# 
# >A Class is like an object constructor, or a "blueprint" for creating objects.
# 
# 

# In[1]:


# create a basic class wnd initialize it 

class MyClass:
    x=-2            # class member variable

c = MyClass()
print(c.x)    


# In[2]:


# constructor 

class Person:
    def __init__(self,fname,lname):
        self.fname=fname
        self.lname=lname
    
    def setValues(self):
        self.fname=input('Enter First Name :: ')
        self.lname=input('Enter Last Name :: ')
        
    def Display(self):
        print("The Name :: " + self.fname + " " + self.lname)
        
p = Person("kunal" ,"singh")
print(p.fname + " " + p.lname)

p.setValues()
p.Display()


# In[3]:


# The __init__() function is called automatically every time the class is being used to create a new object.
# The self parameter is a reference to the current instance of the class, and is used to access variables that belongs to the class.
# It does not have to be named self , you can call it whatever you like, but it has to be the first parameter of any function in the class:
# We can also use 'this' instead of self


# In[4]:


# eg of stack class with this instead of self

class Stk:
    def __init__(this):
        this.top = -1   # empty stk
        this.s = []  
        this.l = 0      # length = 0
        
    def push(this,no):
        this.s.insert(0,no)
        this.top=this.top+1
        this.l= this.l+1
        print('Pushed!')
        
    def pop(this):
        if (s.top==-1):
            print('Underflow')
        else:
            print('\nPopping {0:d}'.format(this.s[0]))
            this.s.pop(0)
            this.top=this.top-1
            this.l= this.l-1
            print('Popped!')

    def show(this):
        print('Stack is')
        for i in this.s:
            print(i,end=" ")
            
s = Stk()
for i in range(88,109,3):
    s.push(i)
s.show()

for i in range(9):
    s.pop()


# In[5]:


li = [2,34,4]
li.insert(0,555)
li.pop(0)
li


# In[6]:


# func and class definitions cannot be empty, but if you for some reason
# have a class definition with no content, put in the pass statement to avoid getting an error.

def mySillyFunction():
    pass

class SillyClass:
    pass


# # Python Inheritance
# >Inheritance allows us to define a class that inherits all the methods and properties from another class.
# 
# >Parent class is the class being inherited from, also called base class.
# 
# >Child class is the class that inherits from another class, also called derived class.

# In[7]:


# person class is created above we'll inherit it


# # Create a Child Class
# >To create a class that inherits the functionality from another class, send the parent class as a parameter when creating the child class:
# 

# In[8]:


class Student(Person):
    pass

s = Student("Mohan" , "Sehgal")
s.setValues()
s.Display()


# In[9]:


class Student(Person):
    def __init__(this,fname,lname,roll,age):
        Person.__init__(this,fname,lname)
        this.roll=roll
        this.age=age
        
    def setValues(this):
        Person.setValues(this)
        this.roll = input('Please enter roll no : ')
        this.age = input('Please enter age no : ')

    def Display(this):
        Person.Display(this)
        print('The ROll is : ',this.roll)
        print('The Age is : ',this.age)
        
s = Student("Mohan" , "Sehgal",223,25)
s.setValues()
s.Display()


# # Use the super() Function
# >Python also has a super() function that will make the child class inherit all the methods and properties from its parent
# 
# > When using super() func for calling base class functions u dont need to pass the self/this object
# 

# In[10]:


class Student(Person):
    def __init__(this,fname,lname,roll,age):
        super().__init__(fname,lname)
        this.roll=roll
        this.age=age
        
    def setValues(this):
        super().setValues()
        this.roll = input('Please enter roll no : ')
        this.age = input('Please enter age no : ')

    def Display(this):
        super().Display()
        print('The ROll is : ',this.roll)
        print('The Age is : ',this.age)
        
s = Student("Mohan" , "Sehgal",223,25)
s.setValues()
s.Display()


#    # Global Keyword
#    >If you need to create a global variable, but are stuck in the local scope, you can use the global keyword.
#    
#    >The global keyword makes the variable global.
#    

# In[11]:


def myfunc():
    global x
    x = 300

myfunc()
print(x)


# # Modules
# >Consider a module to be the same as a code library.A file containing a set of functions you want to include in your application.
# 
# >To create a module just save the code you want in a file with the file extension .py:
# 
# > Modules can have functions and objects in it

# In[12]:


# lets create a module using file handling

code ="""

li = [1,2,34,5,3,3,'Kunal',"anos",243.444]

def greetKunal(name):
    print("Hello " + name + "! How are You!!!")   

"""

f = open('ksrModule.py','w')
f.write(code)
f.close()


# In[13]:


# lets see if our file is created

f = open('ksrModule.py','r')
print(f.read())
f.close()


# In[14]:


# now lets use the module after all this

import ksrModule
ksrModule.greetKunal("Anjali")
ksrModule.li


# In[15]:


import funmodule
funmodule.fun('Kunal','Singh')
funmodule.getnos(11)


# In[16]:


import funmodule
funmodule.getnos(20)


# In[17]:


import mod3
dir(mod3)
mod3.randoms(50)


# # Import From Module
# > we can choose only specific function or object to import 
# 
# > this improves perfomance
# 

# In[18]:


from ksrModule import li
li


# # Python Dates

# In[29]:


import datetime

obj= datetime.datetime.now()

print(obj)
print(obj.day)
print(obj.month)
print(obj.hour)
print(obj.microsecond)
print(obj.min)
print(obj.second)
print(obj.timestamp)


# In[21]:


help('datetime.datetime')


# In[33]:


# creating a date obj with our vals
# The datetime() class also takes parameters for time and timezone (hour, minute, 
# second, microsecond, tzone), but they are optional, and has a default value of 0, (None for timezone).

x = datetime.datetime(2010, 5, 17)
print(x)


# # The strftime() Method
# > The datetime object has a method for formatting date objects into readable strings.
# 
# >The method is called strftime(), and takes one parameter, format, to specify the format of the returned string:
# 

# In[34]:


# Display the name of the month
import datetime
x = datetime.datetime(2018, 6, 1)
print(x.strftime("%B"))    

%a	Weekday, short version	Wed	
%A	Weekday, full version	Wednesday	
%w	Weekday as a number 0-6, 0 is Sunday	3	
%d	Day of month 01-31	31	
%b	Month name, short version	Dec	
%B	Month name, full version	December	
%m	Month as a number 01-12	12	
%y	Year, short version, without century	18	
%Y	Year, full version	2018	
%H	Hour 00-23	17	
%I	Hour 00-12	05	
%p	AM/PM	PM	
%M	Minute 00-59	41	
%S	Second 00-59	08	
%f	Microsecond 000000-999999	548513	
%z	UTC offset	+0100	
%Z	Timezone	CST	
%j	Day number of year 001-366	365	
%U	Week number of year, Sunday as the first day of week, 00-53	52	
%W	Week number of year, Monday as the first day of week, 00-53	52	
%c	Local version of date and time	Mon Dec 31 17:41:00 2018	
%x	Local version of date	12/31/18	
%X	Local version of time	17:41:00	
%%	A % character	%
# # JSON
# >JSON is a syntax for storing and exchanging data.
# 
# >JSON is text, written with JavaScript object notation.
# 

# In[35]:


import json

# some JSON:
x =  '{ "name":"John", "age":30, "city":"New York"}'

# parse x:
y = json.loads(x)

# the result is a Python dictionary:
print(y["age"])

# works like dictniory to me


# # Converting Python Object (Dict) to JSON

# In[73]:


import json 

# create a dict
dict = {
    "name":"Kunal",
    "age":"21",
    "gender":"M",
    "country":"India"
}

y = json.dumps(dict ,indent = 2 )
print(dict)
print(y)


# In[54]:


# can we dump this obj into a file

f  = open("rawjson.txt","w")
json.dump(dict,f)
f.close()

f  = open("rawjson2.txt","w")
json.dump(y,f)
f.close()


# In[55]:


f = open("rawjson.txt","r")
print(f.read())
f.close()

f = open("rawjson2.txt","r")
print(f.read())
f.close()


# In[61]:


# You can convert Python objects of the following types, into JSON strings:

print(json.dumps({"name": "John", "age": 30}))
print(json.dumps(["apple", "bananas"]))
print(json.dumps(("apple", "bananas")))
print(json.dumps("hello"))
print(json.dumps(42))
print(json.dumps(31.76))
print(json.dumps(True))
print(json.dumps(False))
print(json.dumps(None))


# In[68]:


# lets dump all these as json
a = json.dumps({"name": "John", "age": 30}) 
b = json.dumps(["apple", "bananas"])
c = json.dumps(("apple", "bananas")) 
d = json.dumps("hello") 
e = json.dumps(42)
f = json.dumps(31.76)
g = json.dumps(True) 
h = json.dumps(None)

s = a+b+c+d+e+f+g+h

f  = open("rawjson3.txt","w")
json.dump(s,f)
f.close()


# In[69]:


f = open("rawjson3.txt","r")
print(f.read())
f.close()


# In[76]:


import json

x = {
  "name": "John",
  "age": 30,
  "married": True,
  "divorced": False,
  "children": ("Ann","Billy"),
  "pets": None,
  "cars": [
    {"model": "BMW 230", "mpg": 27.5},
    {"model": "Ford Edge", "mpg": 24.1}
  ]
}

print(json.dumps(x, indent=4))
print('***************************************************')
print(json.dumps(x, indent=4 ,sort_keys= True))   # sorted on keys


# In[ ]:




