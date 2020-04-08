#!/usr/bin/env python
# coding: utf-8

# # Operators 
# 
# >Arithmetic operators
# 
# >Assignment operators
# 
# >Relational operators
# 
# >Logical operators
# 
# >Identity operators
# 
# >Membership operators
# 
# >Bitwise operators
# 

# In[1]:


# Arithematic Opeartors 
#  / // % ** * + - 

print(35/2)
print(35//2)
print(35%2)
print(35**2)
print(35*2)
print(35+2)
print(35-2)

# Assignment Opearators

# short hands

Operator	Example	Same As	Try it
=             x = 5           x = 5
+=            x += 3           x = x + 3
-=            x -= 3           x = x - 3
*=            x *= 3           x = x * 3
/=            x /= 3           x = x / 3
%=            x %= 3           x = x % 3
//=           x //= 3          x = x // 3
**=           x **= 3          x = x ** 3
&=            x &= 3           x = x & 3
|=            x |= 3           x = x | 3
^=            x ^= 3           x = x ^ 3
>>=           x >>= 3         x = x >> 3
<<=           x <<= 3         x = x << 3
# In[3]:


# Relational Operator
# < > <= >= != ==

print(5<4)
print(5<=4)
print(5>4)
print(5>=4)
print(5!=4)
print(5==4)


# In[10]:


# Logical Operators
# and or not 
# True ~ -n..1..n
# False ~ 0

print(not(-99))
print(not(0))


# In[11]:


a = True
b = True

print(a and b)
print(a or b)
print(not a and b)
print(not(a and b))
print(a and not b)
print(not not a and b)


# In[16]:


# Bitwise Operators

a=2  # 0010 
b=4  # 0100

print(a&b)
print(a|b)
print(a^b)  # xor
print(~b)  # not 
print(a<<b) # left shift Shift left by pushing zeros in from the right and let the leftmost bits fall off
print(a>>b) # right shift Shift right by pushing copies of the leftmost bit in from the left, and let the rightmost bits fall off


# In[19]:


# Identity operator
# is ::Returns True if both variables are the same object
# is not :: Returns True if both variables are not the same object

x = 4
y = 4
z =66

print(x is y)
print(z is y)
print(x is not y)
print(x is z)


# In[22]:


# Membership Operators
# in :: Returns True if a sequence with the specified value is present in the object
# not in ::Returns True if a sequence with the specified value is not present in the object

x = [11,22,33,44,5,66,787,997]
z= 111
xs= 22

print(xs in x)
print(z in x)
print(xs not in x)
print(z  not in x)


# In[1]:


thislist = ["apple", "banana", "cherry"]
if "apple" in thislist:
  print("Yes, 'apple' is in the fruits list")


# # Conditional Execution 
# 
# >if else
# 
# > if elif elif ...
# 

# In[24]:


a=True
if(a):
    print('Hello there')
    print('Howw are you')


# In[23]:


a=20
if(a==11):
    print('Condition met')
else:
    print('Condition not met')    


# In[30]:


a=20
if(a<=11):
    print('Your are underage')
elif(a<=12):
    print('your still underage')
elif(a<=16):
    print('just 2 more years')
else:
    print('Yayy youre an adult')
print('This part is beyond if else scope')    
    


# In[34]:


# nested if else

train_catched = False
have_money = True


if(train_catched):
    print('Going by train')
else:
    if(have_money):
        print('Can afford Taxi now')
    else:
        print('Dont even have money now ill walk')


# # Loops
# 
# > for 
# 
# > while
# 
# 

# In[2]:


a = 1,'Kunal','Pune',456  # immutable tuple
print(a)


# In[5]:


for x in a:
    print(x)


# In[7]:


l=[]

for i in range(10):
    l.append(i)
    
for i in range(10):
    print(l[i])


# In[13]:


str = "Kunal is my name"
for c in str:
    print(c)


# In[15]:


# from 2 to 10 increment by 2

for i in range(2,10,2):
    print(i)


# In[16]:


i=1 
while i<=5:
    print(i)
    i=i+1


# In[ ]:





# In[31]:


ll = [[1,2,3,4,5],[1,2,3,4,5],[1,2,3,4,5],[1,2,3,4,5],[1,2,3,4,5]]

for x in ll:
    for y in x:
        print(y)


# In[35]:


for x in ll:
    for y in x:
        print(y,end=" ")      # overwrite the last char of y to " " from "\n"
    print()   # newline


# In[ ]:


# ass1

take a no as ip and categorize the person on the basis of the marks

# ass2

guessing team india score 
while loop ask 
randomly generate a score 
if right end loop with message

