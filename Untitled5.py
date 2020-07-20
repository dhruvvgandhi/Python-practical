#!/usr/bin/env python
# coding: utf-8

# In[7]:


#default constructor :
class dhruv: 
    d1 = "" 
  
    # default constructor 
    def __init__(self): 
        self.d1 = "dhruv"
  
    # a method for printing data members 
    def print_sumit(self): 
        print(self.d1) 
  
  
# creating object of the class 
obj = dhruv() 
  
# calling the instance method using the object obj 
obj.print_sumit() 


# In[8]:


#parameterized constructor :

class Add: 
    first = 0
    second = 0
    answer = 0
      
    # parameterized constructor 
    def __init__(self, f, s): 
        self.first = f 
        self.second = s 
      
    def display(self): 
        print("First number = " + str(self.first)) 
        print("Second number = " + str(self.second)) 
        print("Addition of two numbers = " + str(self.answer)) 
  
    def calculate(self): 
        self.answer = self.first + self.second 
  
# creating object of the class 
# this will invoke parameterized constructor 
obj = Add(1000, 2000) 
  
# perform Addition 
obj.calculate() 
  
# display result 
obj.display() 


# In[6]:


#Destructors
class Employee: 
  
    # Initializing 
    def __init__(self): 
        print('Employee created.') 
  
    # Deleting (Calling destructor) 
    def __del__(self): 
        print('Destructor called, Employee deleted.') 
  
obj = Employee() 
del obj 


# In[11]:





# In[ ]:




