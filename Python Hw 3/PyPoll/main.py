#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun 24 18:19:14 2019

@author: Aya
"""

import os
import csv

election_csv = os.path.join("election_data.csv")

totalVotes = 0
khanVotes = 0
correyVotes = 0
liVotes = 0
otooleyVotes = 0

with open(election_csv, "r", newline="") as elections:
    csvreader = csv.reader(elections, delimiter=",")
    header = next(csvreader)
    
    for row in csvreader:
        totalVotes +=1
        
        if row[2] == "Khan":
            khanVotes +=1
            
        elif row[2] == "Correy":
            correyVotes +=1
        
        elif row[2] == "Li":
            liVotes +=1
        
        elif row[2] == "O'Tooley":
            otooleyVotes +=1

candidates = ["Khan","Correy","Li","O'Tooley"]
votes = [khanVotes, correyVotes, liVotes, otooleyVotes]

candNvotes = dict(zip(candidates,votes))

key = max(candNvotes, key=candNvotes.get)

#summary of analysis
khanPercent = (khanVotes/totalVotes)*100
correyPercent = (correyVotes/totalVotes)*100
liPercent = (liVotes/totalVotes)*100
otooleyPercent = (otooleyVotes/totalVotes)*100

#SUMMARY TABLE
analysis = f'''
Election Results
----------------
Total Votes: {totalVotes}
----------------
Khan: {khanPercent:.3f}% ({khanVotes})
Correy: {correyPercent:.3f}% ({correyVotes})
Li: {liPercent:.3f}% ({liVotes})
O'Tooley: {otooleyPercent:.3f}% ({otooleyVotes})
----------------
Winner: {key}
----------------
'''
print(analysis)

#OUTPUT FILES
outputFile = os.path.join("election_results.csv")

with open(outputFile, "w") as file:
    file.write(analysis)

