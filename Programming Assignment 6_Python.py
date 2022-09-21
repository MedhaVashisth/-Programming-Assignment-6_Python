#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Python program to display the Fibonacci sequence

def recur_fibo(n):
   if n <= 1:
       return n
   else:
       return(recur_fibo(n-1) + recur_fibo(n-2))

nterms = 10

# check if the number of terms is valid
if nterms <= 0:
   print("Plese enter a positive integer")
else:
   print("Fibonacci sequence:")
   for i in range(nterms):
       print(recur_fibo(i))


# In[2]:


# Factorial of a number using recursion

def recur_factorial(n):
   if n == 1:
       return n
   else:
       return n*recur_factorial(n-1)

num = 7

# check if the number is negative
if num < 0:
   print("Sorry, factorial does not exist for negative numbers")
elif num == 0:
   print("The factorial of 0 is 1")
else:
   print("The factorial of", num, "is", recur_factorial(num))


# In[6]:


#Python program to illustrate
# how to calculate BMI
def BMI(height, weight):
	bmi = weight/(height**2)
	return bmi

# Driver code
height = 1.79832
weight = 70

# calling the BMI function
bmi = BMI(height, weight)
print("The BMI is", format(bmi), "so ", end='')

# Conditions to find out BMI category
if (bmi < 18.5):
	print("underweight")

elif ( bmi >= 18.5 and bmi < 24.9):
	print("Healthy")

elif ( bmi >= 24.9 and bmi < 30):
	print("overweight")

elif ( bmi >=30):
	print("Suffering from Obesity")


# In[7]:


# Python code to demonstrate the working of
# log(a,Base)

import math

# Printing the log base e of 14
print ("Natural logarithm of 14 is : ", end="")
print (math.log(14))

# Printing the log base 5 of 14
print ("Logarithm base 5 of 14 is : ", end="")
print (math.log(14,5))


# In[9]:


# Simple Python program to find sum of series
# with cubes of first n natural numbers

# Returns the sum of series
def sumOfSeries(n):
	sum = 0
	for i in range(1, n+1):
		sum +=i*i*i
		
	return sum


# Driver Function
n = 5
print(sumOfSeries(n))

# Code Contributed by Mohit Gupta_OMG <(0_o)>


# In[ ]:




