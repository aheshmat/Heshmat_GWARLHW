#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun 24 18:19:14 2019

@author: Aya
"""

import os 
import csv

pybank_csv = os.path.join('budget_data.csv')

numMonths = []
netTotal = []
monthlyChange = []

with open(pybank_csv, "r", newline="") as budget:
   csvreader = csv.reader(budget,delimiter=",")
   header = next(csvreader)
   
   for row in csvreader:
       numMonths.append(row[0])
       netTotal.append(int(row[1]))
    
   for i in range(len(netTotal)-1):
       monthlyChange.append(netTotal[i+1]-netTotal[i])

maxIncrease = max(monthlyChange)
maxDecrease = min(monthlyChange)

maxIncreaseMonth = monthlyChange.index(max(monthlyChange))+1
maxDecreaseMonth = monthlyChange.index(min(monthlyChange))+1

analysis = f'''
Financial Summary Analysis
--------------------------
Total Months: {len(numMonths)}
Total: ${sum((netTotal))}
Average Change: {round(sum(monthlyChange)/len(monthlyChange),2)}
Greatest Increase in Profits: {numMonths[maxIncreaseMonth]}(${(str(maxIncrease))})
Greatest Decrease in Profits: {numMonths[maxDecreaseMonth]}(${(str(maxDecrease))})

'''

output_file = os.path.join("analysis.txt")

with open(output_file, "w") as file:
    file.write(analysis)

