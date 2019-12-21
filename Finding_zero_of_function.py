#!/usr/bin/env python
# coding: utf-8

# # QN. 1) Loop Condition Practice
#     

# In[142]:


def free_fall(org_hgt, num_landing=5): # Defining a function named 'free_fall' with arguments 'org_hgt' and 'num_landing'
                                       # 'num_landing' has been assigned a default value of 5
    dist = org_hgt                     
    
    for i in range(num_landing):          # 'for' loop runs for num_landing no of times
        
        if i!=(num_landing-1):
            org_hgt = 0.25*org_hgt      # as the ball bounces to 0.5 times the previous bounce we store org_hgt as 0.25*org_hgt
            bounce = 2*org_hgt          # bounce is twice of org_hgt as the ball goes up and down 
            dist = dist + bounce        # and we add the bounce to the total distance
        else:
            org_hgt = 0.25*org_hgt        
            bounce = org_hgt            # In the else statement we only add org_hgt once as we only we need it for the last part
            dist = dist + bounce
    return dist, bounce        # the function returns the values 'dist' and 'bounce' 


dist,bounce = free_fall(1000)   # 'dist' variable stores the value of the total distance travelled by the ball after 5 bounces

print("The distance travelled by the ball is {} meters ".format(dist))
print("The meters the ball travels after 5 no of landing {} meters".format(bounce))


# # QN. 2.) String Practice

# In[136]:


import re
import string
String = '‘” ”He has indicated he is prepared to sign the bill. He will also be issuing a national emergency declaration at the same time,” McConnell said. ”I’ve indicated to him that I’m going to support the national emergency declaration. So for all of my colleagues, the President will sign the bill. We will be voting on it shortly.” ‘” '

def clean_text():   # defining function clean_text

    Token = {}
    puncti=str(list(string.punctuation))   # stroing all the punctuations in the variable puncti
    string_clean=String.split('.')    # splitiing the string by fullstop
 
    for x in string_clean: 

        x = x.lower().strip() 
        x = x.replace('’', '')   # removing the different font symbols using replace() function
        x = x.replace('”', '')  
        x = x.replace('‘', '')   
        x = x.replace(puncti,' ')

        clean_text = x.split(' ') # split to get the words in the sentence 
        
        for i in clean_text: # for each word in the sentence 
            if i == "":
                pass
            else:
                Token[i]=Token.get(i,0)+1

    most_freq = max(Token.values())  # finding the maximum valuein the token
    for key,value in Token.items():   # finding the key 
        if value == most_freq:
            val = key
        else:
            pass
    

    return Token, most_freq, val

token, freq, word_ = clean_text()
print("The Dictionary is : ", token)
print("\n")
print("The Frequency of the most frequent word is :", freq)
print("The most frequent word is : ", word_)


# # QN. 3.) Find Zero of Function

# In[143]:


#Here we need to find a zero point of a function, x* i.e. where the function becomes zero, f(x*)=0           

fx = lambda x: 2*x + 4     # We use the lambda function to create the function f(x) = 2x + 4 

def zero_point(lambda_func,x0,epi,sig):   # We define a function 'zero_point' to find the zero point of the function
    
    lambda_func = lambda x: 2*x + 4    
    w0 = lambda_func(x0)
    w1 = w0 - sig*lambda_func(w0)  
    w_old = w0            
    w_new = w1
    i = 0
    run = 0
    zero_values = []
    while abs(w_new - w_old) > epi:    # we use the while loop to find out when wn converges by using the condition  " abs(w_new - w_old) > epi"
        
        if i == 0:
            w_old = w1
            i += 1
            
        else:
            w_old = w_new    # we save the wn+1 in wn
                
        zero_values.append(w_old)    # Zero_values list is appended with the value w_old
    
        w_new = w_old - sig*lambda_func(w_old)   # here we find the new value of w i.e. w(n+1) using the old value of w(n)
        run += 1
    
    return w_old, w_new, run, zero_values # w_old value is the zero point of the function

# Then we call the function as above with the initial value x0 as -5 and passing values fx and epi, sig as 0.001 and 0.01

zero_point_old,zero_point_new,run,zero_value = zero_point(fx,-5,0.001,0.01)   

# x* is what we need to find, which is w_n that is w_old for the last iteration of the while loop

print("No of times the while loop runs is : ", run)
print("Zero point of the given function fx using forward euler method is(zero point of the function):", zero_point_old)


# In[138]:



# Here we call the same function as above with the initial value x0 as 0 with same fx , epi and sig
zero_point_old,zero_point_new,run,zero_value = zero_point(fx,0,0.001,0.01)   

# x* is what we need to find, which is w_n that is w_old for the last iteration of the while loop

print("No of times the while loop runs is : ", run)
print("Zero point of the given function fx using forward euler method is(zero point of the function):", zero_point_old)


# # 3.) B)

# In[144]:


3.) B) 1

import math

gx = lambda x: x*(math.sin(x)) - 1

def zero_point(lambda_func,x0,epi,sig): # Here we use the same function as above with function gx and x0 values ranging from -4 to 4.
    
    w0 = 0
    lambda_func = lambda x: x*(math.sin(x)) - 1   
    w0 = lambda_func(x0)
    w1 = w0 - sig*lambda_func(w0)
    w__old = w0            
    w__new = w1
    i = 0
    run_ = 0
    zero__values = []
    
    while abs(w__new - w__old) > epi:
        
        if i == 0:
            w__old = w1
            i += 1
        else:
            w__old = w__new
                
        zero__values.append(w__old)
    
        w__new = w__old - sig*lambda_func(w__old)
        run_ += 1
     # w__old stores the value wn
                                                        # w__new stores the value wn+1
                                                        # zero__values stores all the wn values
    return w__old, w__new, run_ ,zero__values # run_ gives the no of times the loop runs
                                                      
    
x_list = [-4,-3,-2,-1,0,1,2,3,4]
graph_list = []

for i in range(len(x_list)):
    
    zero_point__old,zero_point__new,run_,zero__values = zero_point(gx,x_list[i],0.001,0.01)      
    # x* is what we need to find, which is w_n that is w_old for the last iteration of the while loop
    print('The value of x is :', x_list[i])
    print("No of times the while loop runs is : ", run_) 
    print("Zero point of the given function fx using forward euler method i.e. w_old is(zero point of the function):", zero_point__old)
    print("\n")
    graph_list.append(zero_point__old)

# the list graph_list stores all the zero points of the function for x0 values -4 to 4
print("All the zero points of the function are : ",graph_list)


# In[151]:


#3. B) 2.)

import matplotlib.pyplot as plt
import numpy as np
get_ipython().run_line_magic('matplotlib', 'inline')

x = np.arange(-4,4,0.1) 
y1 = np.sin(x)
y = x*y1 - 1

#fe.plot(x,y,marker = 's', label = "g(x)")
plt.plot(y,x,graph_list, marker = 's')
#fe.legend()
plt.show()
    
#As seen in the graph , we have plotted the function xsin(x)-1. Along with that we have also plotted the zero points of the 
#function g(x) ranging from the points -4 to 4. Orange line shows the Zero points of the function while the blue curve shows the 
# graph for the function xsin(x) - 1


# In[ ]:




