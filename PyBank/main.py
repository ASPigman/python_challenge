#  I would like the code to be as reusable as possible!

#In this Challenge, you are tasked with creating a Python script to analyze the financial records of your company. 
# You will be given a financial dataset called budget_data.csv. The dataset is composed of two columns: "Date" and "Profit/Losses".
# Your task is to create a Python script that analyzes the records to calculate each of the following values:
# - The total number of months included in the dataset
#       -Create a variable that counts rows since each represents a different month. Make sure to skip first row!
# - The net total amount of "Profit/Losses" over the entire period
#       - Need to subtract first and last or add one row to the next?
# - The changes in "Profit/Losses" over the entire period, and then the average of those changes
#       - Average change in profit_loss = (Amount of last row - Amount of first row) / (months - 1)
# - The greatest increase in profits (date and amount) over the entire period
#       -Is there a fin max function? Maybe using a loop like the VBA challenge?
# - The greatest decrease in profits (date and amount) over the entire period
#       - Is there a min function?
# ---------------------------------------------------------------------------------
# Your final script should both print the analysis to the terminal and export a text file with the results.

# Modules
import os
import csv

# set path for file
csvpath = os.path.join("Resources", "budget_data.csv")

# Opening the csv file
with open(csvpath, 'r') as csvfile:

    #This splits each item by the comma
    csvreader = csv.reader(csvfile, delimiter=",")

    # Read the header row first - skip if no header!
    csv_header = next(csvreader)
    # retain the header by 
    # print(f"Header: {csv_header}")

    date = []

    # An attempt at using list.count() to calculate number of months (not working)
    # for row in csvreader:

        #date.append(row[0])

        #list.count(date)

    # Calculate # of months by counting rows (this works)
    #months = sum(1 for row in csvreader)
    #print("Financial Analysis")
    #print("----------------------------")
    #print(f"Months: {months}")