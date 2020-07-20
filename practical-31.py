#!/usr/bin/env python
# coding: utf-8

# In[1]:


import mysql.connector


# In[2]:


pip install mysql-connector


# In[3]:


import mysql.connector


# In[7]:


import mysql.connector
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="",
  database="jenish"
)

mycursor = mydb.cursor()
mycursor.execute("CREATE TABLE personal (name VARCHAR(255))")

file = open('a2.txt','r')
file_content = file.read()
file.close()

query = "INSERT INTO personal(name) VALUES (%s)"
mycursor.execute(query,(file_content,))
mydb.commit()
mydb.close()


# In[ ]:




