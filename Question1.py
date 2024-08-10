# -*- coding: utf-8 -*-
"""
Created on Sat Aug 10 12:40:32 2024

@author: sam17
"""
#Initialize an app using 
non_duplicate = []

#Prompt user to type the numbers 
input_list = list(map(int, input("Please input the numbers separated by a space: ").split()))

print("List before removing duplicates:", input_list)

# Remove duplicates by loooping through the list
for i in range(len(input_list)):
    if input_list[i] not in non_duplicate:
        non_duplicate.append(input_list[i]) 

print("List after removing duplicates:", non_duplicate)
