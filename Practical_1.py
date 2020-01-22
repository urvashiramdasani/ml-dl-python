#!/usr/bin/env python
# coding: utf-8

# In[31]:


#Modify string
def modify():
    str = input('Enter a string: ')
    l1 = list(str)
    l1.reverse()
    for i in range(0,len(l1)-1):
        if l1[i] == l1[i+1]:
            l1[i] = '*'
    l1.reverse()
    str = ''.join(l1)
    print(str)
modify()           


# In[34]:


#use dictionary
def numTostring():
    values = {1:'One',2:'Two',3:'Three',4:'Four',5:'Five',6:'Six',7:'Seven',8:'Eight',9:'Nine',0:'Zero'}
   # n = int(input('Enter the length: '))
    num = int(input('Enter a number: '))
    #l1 = list(num)
    #l1
    list1 = []
    if 
    while num>0:
        d = num%10
        num = int(num/10)
        list1.append(values[d])
   # list1.sort()
    list1.reverse()
    for i in list1:
        print(i)
numTostring()


# In[ ]:


def func(x):
    n = x
    if(n==0):
        return
    else:
        print(x)
        x = x+1
        n = n-1
    
x = int(input('Enter a number : '))
func(x)

