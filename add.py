#Name = Dhruv_Gandhi
#Enrollment_Number = 17SE02CE017
#Assginment = 37->User defined modules (RecursiveFuntion)in python 
#create a module in which you have a recursive function.
def recur_sum(n):
   if n <= 1:
       return n
   else:
       return n + recur_sum(n-1)