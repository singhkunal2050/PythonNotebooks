#!/usr/bin/env python
# coding: utf-8
# ass1

take a no as ip and categorize the person on the basis of the marks

# ass2

guessing team india score 
while loop ask 
randomly generate a score 
if right end loop with message
# In[3]:


end = False 

while(not end):
    marks = input('Please enter your marks')
    marks = int(marks)
    if(marks>100):
        print('Invalid Input')
        continue
    elif(marks>=95):
        print('Youre A+')
    elif(marks>=85):
            print('Youre A')
    elif(marks>=75):
            print('Youre B')
    elif(marks>=65):
            print('Youre C')
    elif(marks>=35):
            print('Youre D')
    elif(marks<35):
            print('Sorry Youre FF')
    end = int(input('Do you want to End?(1/0)'))
        
print('Thank yout for using')
    


# In[1]:


# ass 2 20 20

import random

end = False
score = random.randint(1,250)
print(score)

while(not end):
      guess = int (input('Please guess the score'))
      if(guess>250 or guess <1):
          print('Reduce your expectation for 20-20')
      else:
          if(abs(score-guess)==0):
              print('Bullseye!!! On spot')
          elif(abs(score-guess)<=10):
              print('Youre a true 29 20 fan')
          else:
              print('Close but not close enough')
      end = int(input('Do you want to End?(1/0)'))
        
print('Thank yout for using')
         

