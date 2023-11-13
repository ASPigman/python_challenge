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

# creating empty lists to append
months = []
profits_losses = []
changes = []

# Opening the csv file
with open(csvpath, 'r') as csvfile:

    #This splits each item by the comma
    csvreader = csv.reader(csvfile, delimiter=",")

    # Read the header row first - skip if no header!
    csv_header = next(csvreader)

    # Setting the line count variable to integer 0 so we can count number of months.
    line_count = 0
    
    # Calculating the number of months
    for row in csvreader:
        months.append(row[0])
        profits_losses.append(int(row[1]))

        if line_count == 0:
            line_count += 1
        else:
            line_count += 1
print(" ")
print("Financial Analysis")
print("-----------------------------------")
print(f'Total Months: {line_count}')
print(" ")

# Calculating the net change over the number of months.
def csv_total(something):
    total = 0
    with open(something) as a:
        csvreader = csv.reader(a)
        csv_header = next(csvreader)

        for line in csvreader:
            total += int(line[1])
            
    return total
total = csv_total(csvpath)
print(f"Total: $ {total}")
print(" ")

    
# Calculating the average change over time and identifying the amounts and dates of greatest increases and decreases in profits.
for i in range (1, len(months)):
        change = profits_losses[i]-profits_losses[i-1]
        changes.append(change)
        
        average_change = sum(changes)/len(changes)
        increase = max(changes)
        increase_date = months[changes.index(increase) + 1]
        decrease = min(changes)
        decrease_date = months[changes.index(decrease) + 1]

# the :.2f allows for two decimal places
print(f"Average Change: $ {average_change:.2f}")
print(" ")
print(f"Greatest increase in Profits: $ {increase} on {increase_date}")
print(" ")
print(f"Greatest decrease in Profits: $ {decrease} on {decrease_date}")
print(" ")