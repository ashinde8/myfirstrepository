#!/usr/bin/env python
# coding: utf-8





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




