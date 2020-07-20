#!/usr/bin/env python
# coding: utf-8

# In[10]:


#Name = Dhruv_Gandhi
#Enrollment_Number = 17SE02CE017
#Assginment = 33->Show the use of inheritance
#Using Pass-Keyword

class Vehicle:
  def __init__(self, Vehicle_Name,Vehicle_type,Vehicle_Price):
    self.VehicleName = Vehicle_Name
    self.VehicleType = Vehicle_type
    self.VehiclePrice= Vehicle_Price
  def print(self):
    print("VehicleName =",self.VehicleName, "---->VehicleType =", self.VehicleType ,"---->VechiclePrice =", self.VehiclePrice)
class Car(Vehicle):
  pass
x = Car("Hyundai_I_20", "Family_Car","7,50,000 TO 15,00,000")
x.print()


# In[11]:


#Using-__init__() Function
class Vehicle:
  def __init__(self, Vehicle_Name,Vehicle_type,Vehicle_Price):
    self.VehicleName = Vehicle_Name
    self.VehicleType = Vehicle_type
    self.VehiclePrice= Vehicle_Price
  def print(self):
    print("VehicleName =",self.VehicleName, "---->VehicleType =", self.VehicleType ,"---->VechiclePrice =", self.VehiclePrice)
class Car(Vehicle):
  def __init__(self, Vehicle_Name,Vehicle_type,Vehicle_Price):
    Vehicle.__init__(self, Vehicle_Name,Vehicle_type,Vehicle_Price)
  
x = Car("Hyundai_I_20", "Family_Car","7,50,000 TO 15,00,000")
x.print()


# In[12]:


#Using-super() Function
class Vehicle:
  def __init__(self, Vehicle_Name,Vehicle_type,Vehicle_Price):
    self.VehicleName = Vehicle_Name
    self.VehicleType = Vehicle_type
    self.VehiclePrice= Vehicle_Price
  def print(self):
    print("VehicleName =",self.VehicleName, "---->VehicleType =", self.VehicleType ,"---->VechiclePrice =", self.VehiclePrice)
class Car(Vehicle):
  def __init__(self, Vehicle_Name,Vehicle_type,Vehicle_Price):
    super().__init__(Vehicle_Name,Vehicle_type,Vehicle_Price)
  
x = Car("Hyundai_I_20", "Family_Car","7,50,000 TO 15,00,000")
x.print()


# In[ ]:




