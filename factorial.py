# -*- coding: utf-8 -*-
"""
Created on Tue Sep 11 00:39:14 2018

@author: louay
"""

n = int(input("Enter an integer n:"))
if n<0:
     print("Negative number!")
else:
     fact=1;
     i=1
     while i<=n:
         fact = fact*i
         i=i+1
     print("Factorial of n:", fact)
     print( " Finished" ) 
     
