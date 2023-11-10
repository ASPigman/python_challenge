# In this Challenge, you are tasked with helping a small, rural town modernize its vote-counting process.
# You will be given a set of poll data called election_data.csv. The dataset is composed of three columns: "Voter ID", "County", and "Candidate". 
# Your task is to create a Python script that analyzes the votes and calculates each of the following values:
#  - The total number of votes cast
#  - A complete list of candidates who received votes
#  - The percentage of votes each candidate won
#  - The total number of votes each candidate won
#  - The winner of the election based on popular vote
# Your final script should both print the analysis to the terminal and export a text file with the results.

# Modules
import os
import csv

# set path for file
csvpath = os.path.join("Resources", "election_data.csv")

#Opening the csv file
with open(csvpath, encoding='UTF-8') as csvfile:

    #This splits each item by the comma
    csvreader = csv.reader(csvfile, delimiter=",")

    # Read the header row first - skip if no header!
    csv_header = next(csvreader)

    # Calculate # of months by counting rows
    votes = sum(1 for row in csvreader)
    print("Election Analysis")
    print("----------------------------")
    print(f"Months: {votes}")

    
