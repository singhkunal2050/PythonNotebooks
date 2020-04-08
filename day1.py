#!/usr/bin/env python
# coding: utf-8

# In[2]:


print ('Kunalds adsa')


# # Data Types
# 

# In[7]:


#integer 

no1= 1219
no2= 2342
no3 = no1+no2
print(no3)


# In[9]:


#float

no1= 12.19
no2= 2.342
no33 = no1+no2
print(no33)


# In[10]:


#String  
    
no1= 'laskdsal das '
no2= 'DJkah shdk ahk'
no333 = no1+no2
print(no333)


# In[12]:


type(no3)


# In[11]:


type(no33)


# In[13]:


type(no333)


# In[19]:


#list

list = ['sajdk',32 ,'dsadlksa' , "adsajkfkas" , 2482.32 ,[387, 213,372,312,32]]


# In[20]:


print(list)


# In[21]:


for i in list:
    print(i)
    print('\n')


# In[27]:


# Dictonary
dict = {"ksr":"Sai Krupa" , "atharva":"abc" , "dasda":"uiwueia"}


# In[28]:


dict


# In[29]:


dict.get('ksr')


# In[30]:


#SET


set1 = [22,33,12,32,22,541,51,21,12]


# In[31]:


set1


# In[32]:


#tuple

# completely similar to list except its immutable 

tup1 = (1,"lauinda" , "sai kripa" ,420)


# In[33]:


tup1


# In[38]:


tup1.count(2)


# In[39]:


tup1.count(1)


# In[40]:


tup1.index('sai kripa')


# In[41]:


# Boolean True / False 

a= True


# In[42]:


a


# In[43]:


get_ipython().system('a')


# In[44]:


not a


# In[45]:


a.bit_length()


# ## Home Work

# In[47]:


# list dictonary and set

list2 = ["Kunak ", 23 , 'D3' , 32.32 , True ]


# In[48]:


list2


# In[49]:


list2.append(2344)


# In[52]:


list32 = list2.copy()


# In[53]:


list32


# In[55]:


list2.count(23)


# In[56]:


list2.pop()


# In[57]:


list2.reverse()


# In[58]:


list2


# In[59]:


list2.remove(True)


# In[60]:


list2


# In[61]:



# Dictonary 


# In[62]:


dict1  =  {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}


# In[63]:


dict1.get('brand')


# In[67]:


dict1.values()


# In[69]:


dict1.keys()


# In[70]:


# Sets


# In[71]:


set1 = [1 ,3 ,3 ,44,44,323,32,12,234,11,11,22,33,11]


# In[72]:


set1


# In[74]:





# In[75]:


set1.append(222)


# In[76]:


set1.insert(23,0)


# In[77]:


set1


# In[78]:


set1.insert(1,888)


# In[79]:


set1


# In[80]:


set2 = [99,23,424,124]


# In[81]:


set1.extend(set2)


# In[83]:


print(set1)


# In[84]:


set1.sort()


# In[85]:


print(set1)


# In[ ]:




