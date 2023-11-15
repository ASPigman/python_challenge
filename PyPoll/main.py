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
with open(csvpath, 'r') as csvfile:

    #This splits each item by the comma
    csvreader = csv.reader(csvfile, delimiter=",")

    # Read the header row first - skip if no header!
    csvheader = next(csvreader)

    # Calculating total number of votes by counting number of rows after the header.
    rows = list(csvreader)
    vote_number = len(rows)

    print(" ")
    print("Election Results")
    print("----------------------------")
    print(" ")
    # The :, allows for a place separator
    print(f"Total Votes: {vote_number:,}")
    print(" ")
    print("----------------------------")
    print(" ")

    # Determining the names of the candidates by looping through and 
    candidates = []
    totals = []
    for i in range (0,vote_number):
        candidate = rows[i][2]
        totals.append(candidate)
        if candidate not in candidates: 
            candidates.append(candidate)

    #The number of candidates to use for finding percentage votes.
    candidate_number = len(candidates)

    # The total number of votes each candidate won & the percentage of votes each candidate won
    votes = []
    percent_votes = []
    for j in range (0,candidate_number):
        name = candidates[j]
        votes.append(totals.count(name))
        percentage = votes[j]/vote_number
        percent_votes.append(percentage)

    # Loop to print info for each candidate
    for k in range (0,candidate_number): 
        print(f"{candidates[k]}: {percent_votes[k]:%} ({votes[k]:,})")
        print(" ")
    print("----------------------------")
    print(" ")

    # The winner of the election based on popular vote.
    winner = votes.index(max(votes)) 


    # prints the winner at the end
    print(f"Winner: {candidates[winner]}")
    print(" ")
    print("----------------------------")


    # Print the results to text file
    file = open(os.path.join("Analysis", "election_analysis.txt"), "w")

    file.write(" ")
    file.write("Election Results")
    file.write("----------------------------")
    file.write(f"Total Votes: {vote_number:,}")
    file.write(" ")
    file.write("----------------------------")
    file.write(" ")
    for k in range (0,candidate_number): 
            file.write(f"{candidates[k]}: {percent_votes[k]:%} ({votes[k]:,})")
            file.write(" ")
    file.write("----------------------------")
    file.write(" ")
    file.write(f"Winner: {candidates[winner]}")
    file.write(" ")
    file.write("----------------------------")