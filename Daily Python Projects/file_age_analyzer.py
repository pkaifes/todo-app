# -*- coding: utf-8 -*-
"""
Created on Fri Dec  6 22:20:52 2024

@author: frost
"""
from datetime import datetime, date, timedelta
import os, time

print("Welcome to File Age Analyzer!")
user_dir = input("Enter the FULL path of the folder to analyze: ")
#user_dir = "C:/Users/frost/OneDrive/Desktop/software creations/python/"
print("Analyzing file ages. Please wait...")


current_date = datetime.now()
weekPast_date = datetime.now() - timedelta(days=7)
monthPast_date = datetime.now() - timedelta(days=30)

lessThanWeekOld = 0
lessThanMonthOld = 0
olderThanMonthOld = 0

oldestFile = ""
oldestFileDate = current_date
newestFile = ""
newestFileDate = current_date

first_file = True

for root, dirs, files in os.walk(user_dir):
    for filename in files:
        f = os.path.join(root, filename)
        f_time = datetime.fromtimestamp(os.path.getctime(f))
        
        #counter for each date category
        if f_time > weekPast_date:
            lessThanWeekOld += 1
        elif f_time > monthPast_date:
            lessThanMonthOld += 1
        else:
            olderThanMonthOld += 1
            
        #check for oldest file in set
        if f_time < oldestFileDate:
            oldestFile = f
            oldestFileDate = f_time
            
        if first_file:
            first_file = False
            newestFile = f
            newestFileDate = f_time
        
        #check for newest file in set
        if f_time > newestFileDate:
            newestFile = f
            newestFileDate = f_time

print("\n--- File Age Anlysis Report ---")
print(f"Files created less than 1 week ago: {lessThanWeekOld}")
print(f"Files created more than 1 week and less than 1 month ago: {lessThanMonthOld}")
print(f"Files created more than 1 month ago: {olderThanMonthOld}")
print("\n")
print(f"Oldest File, made on {oldestFileDate}:")
print(oldestFile)
print("\n")
print(f"Newest File, made on {newestFileDate}:")
print(newestFile)
print("\n")
print("--- Complete! ---")


