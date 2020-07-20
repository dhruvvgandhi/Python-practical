#!/usr/bin/env python
# coding: utf-8

# In[1]:


#Name = Dhruv_Gandhi
#Enrollment_Number = 17SE02CE017
#Assginment = 35->Show the inner join
#Connection and create database
import mysql.connector
mydb = mysql.connector.connect(
 host="localhost",
 user="root",
 passwd=""
)
mycursor = mydb.cursor()
mycursor.execute("CREATE DATABASE Assignment35")
#print(mydb)
mycursor = mydb.cursor()
mycursor.execute("SHOW DATABASES")
for x in mycursor:
 print(x)


# In[7]:


#Name = Dhruv_Gandhi
#Enrollment_Number = 17SE02CE017
#Assginment = 35->Show the inner join
#create_table_1
import mysql.connector
mydb = mysql.connector.connect(
 host="localhost",
 user="root",
 passwd="",
 database="Assignment35"
)
mycursor = mydb.cursor()
mycursor.execute("CREATE TABLE t1 (id INT AUTO_INCREMENT PRIMARY KEY,name VARCHAR(255),address VARCHAR(255))")


# In[9]:


#Name = Dhruv_Gandhi
#Enrollment_Number = 17SE02CE017
#Assginment = 35->Show the inner join
#create_table_2
import mysql.connector
mydb = mysql.connector.connect(
 host="localhost",
 user="root",
 passwd="",
 database="assignment35"
)
mycursor = mydb.cursor()
mycursor.execute("CREATE TABLE t2 (id INT AUTO_INCREMENT PRIMARY KEY, enrollment_number VARCHAR(255), Semester VARCHAR(255))")


# In[10]:


#Name = Dhruv_Gandhi
#Enrollment_Number = 17SE02CE017
#Assginment = 35->Show the inner join
#insert_vale_in_table_1
import mysql.connector
mydb = mysql.connector.connect(
 host="localhost",
 user="root",
 passwd="",
 database="assignment35"
)
mycursor = mydb.cursor()
sql = "INSERT INTO t1 (name, address) VALUES (%s, %s)"
val = [
 ('Peter', 'Lowstreet 4'),
 ('Amy', 'Apple st 652'),
 ('Hannah', 'Mountain 21'),
 ('Michael', 'Valley 345'),
 ('Sandy', 'Ocean blvd 2'),
 ('Betty', 'Green Grass 1'),
 ('Richard', 'Sky st 331'),
 ('Susan', 'One way 98'),
 ('Vicky', 'Yellow Garden 2'),
 ('Ben', 'Park Lane 38'),
 ('William', 'Central st 954'),
 ('Chuck', 'Main Road 989'),
 ('Viola', 'Sideway 1633')
]
mycursor.executemany(sql, val)
mydb.commit()
print(mycursor.rowcount, "was inserted.")


# In[12]:


#Name = Dhruv_Gandhi
#Enrollment_Number = 17SE02CE017
#Assginment = 35->Show the inner join
#insert_vale_in_table_2
import mysql.connector
mydb = mysql.connector.connect(
 host="localhost",
 user="root",
 passwd="",
 database="assignment35"
)
mycursor = mydb.cursor()
sql = "INSERT INTO t2 (enrollment_number, Semester) VALUES (%s,%s)"
val = [
 ('17SE02CE010', '6'),
 ('17SE02CE011', '7'),
 ('17SE02CE012', '5'),
 ('17SE02CE013', '4'),
 ('17SE02CE014', '3'),
 ('17SE02CE015', '2'),
 ('17SE02CE016', '1'),
 ('17SE02CE017', '8'),
 ('17SE02CE018', '5'),
 ('17SE02CE019', '6'),
 ('17SE02CE020', '4'),
 ('17SE02CE021', '3'),
 ('17SE02CE022', '2')
]
mycursor.executemany(sql, val)
mydb.commit()
print(mycursor.rowcount, "was inserted.")


# In[13]:


#Name = Dhruv_Gandhi
#Enrollment_Number = 17SE02CE017
#Assginment = 35->Show the inner join
#inner_join
import mysql.connector
mydb = mysql.connector.connect(
 host="localhost",
 user="root",
 passwd="",
 database="assignment35"
)
mycursor = mydb.cursor()
sql = "SELECT t1.name AS user, t2.enrollment_number AS favorite FROM t1 INNER JOIN t2 ON t1.id =t2.id"
mycursor.execute(sql)
myresult = mycursor.fetchall()
for x in myresult:
 print(x)


# In[ ]:




