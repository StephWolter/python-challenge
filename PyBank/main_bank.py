import os
import csv


# Path to collect data from the Resources folder
budget_csv = os.path.join('Resources', 'budget_data.csv')

#define lists
budget_data = []

# Read in the CSV file
with open(budget_csv) as csvfile:
    # Split the data on commas
    budget_data = csv.reader(csvfile, delimiter=',')

    # Label the header row first 
    budget_header = next(budget_data)

    #initialize counters
    last_month = 0    
    total = 0
    total_months = 0
    change = []

    #splitting columns into new lists
    for row_data in budget_data:
        date_info, balance_info = row_data[0], row_data[1]
        #spot check lists made of columns 
        #print(date_info)
    #calculate total number of balances
        total += int(balance_info) 
        #add to the counter for total months
        total_months += 1
    #The changes in "Profit/Losses" over the entire period, and then the average of those changes
        if last_month != 0:
            change.append(int(balance_info) - int(last_month))
        #set last_month to current month
        last_month = balance_info
    
    #find average
    average_change = sum(change) / int(total_months)

    greatest_increase = max(change)
    greatest_decrease = min(change)

    #Spot check balance total
    #print (total)

    #Spot Check The total number of months included in the dataset
    #print(total_months)

#The greatest increase in profits (date and amount) over the entire period

#The greatest decrease in profits (date and amount) over the entire period

#display output
print("Financial Analysis")
print("--------------------")
print(f"The total months is: {total_months}")
print(f"The total profit/loss: {total} ")
print(f"The average change is: {average_change} ")
print(f"The greatest increase over time is: {greatest_increase}")
print(f"The greatest decrease over time is: {greatest_decrease}")

with open("Analysis/Monthly_Budget_Results.txt", "w") as f:
    l1 = "Financial Analysis"
    l2 = "------------------"
    l3 = (f"The total months is: {total_months}")
    l4 = (f"The total profit/loss: {total} ")
    l5 = (f"The average change is: {average_change} ")
    l6 = (f"The greatest increase over time is: {greatest_increase}")
    l7 = (f"The greatest decrease over time is: {greatest_decrease}")
    f.writelines([l1,l2,l3,l4,l5,l6,l7])

