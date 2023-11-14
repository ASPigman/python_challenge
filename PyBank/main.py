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

        # Using conditional to total the number of lines, starting with the first one on the if line, then adding each additon one with the else.
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
    
    # setting the total variable to 0
    total = 0
    with open(something) as word:

        # making sure we're reading the csv file and skipping header
        csvreader = csv.reader(word)
        csv_header = next(csvreader)
        
        # looping through the rows to add the values together.
        for row in csvreader:
            total += int(row[1])
            
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