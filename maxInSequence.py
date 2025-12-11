# -*- coding: utf-8 -*-
"""
Created on Tue Sep 11 01:05:11 2018

@author: louay
"""

n = int(input("Enter number n of  integers:"))
if n==0:
    print("Empty sequence")
else:
    maximum = int(input("Enter an integer:")) 
    i = 2  
    while i<=n:
         x = int(input("Enter an integer:"))
         if x>maximum:
            maximum = x
         i=i+1
    print("Maximum:", maximum)


