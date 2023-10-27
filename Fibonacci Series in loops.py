#!/usr/bin/env python
# coding: utf-8

# In[3]:


#list with first two items in the Fibonacci series 
list_1 = [0,1]
#use the input function 
n = int(input("Enter the number of term: "))
if n == 1: 
    print('0')
elif n == 2:
    print('1')
else: 
    while(len(list_1) < n):
        list_1.append(0)
    if (n == 0 or n == 1):
        print (1)
    else: 
        list_1[0] = 0 
        list_1[1] = 1
        for i in range(2,n):
            list_1[i] = list_1[i-1] + list_1[i-2]
        print(f'First {n} terms of Fibonacci series {list_1}')          
    


# In[ ]:




