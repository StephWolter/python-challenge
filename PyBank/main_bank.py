import os
import csv
#point to correct resource csv file
budget_data = os.path.join("Resources", "budget_data.csv")
# Open and read csv
with open(budget_data) as csvfile:
    monthly_statements = csv.reader(budget_data, delimiter=",")
    #identify and move past the header row
    csv_header = next(monthly_statements)
    date_info = [i.split(',')[0] for i in csvfile.readlines()]
    balance_info =  [i.split(',')[1] for i in csvfile.readlines()]

date_total = len(date_info)
print(date_total)


   
#display output
print("Financial Analysis")
print("--------------------")
print(f"The number of months is: {date_total}")
#print(f"The total profit/loss: {total_prof_loss} ")
#print(f"The average change is: {average_change} ")
#print(f"The greatest increase over time is: {greatest_increase}")
#print(f"The greatest decrease over time is: {greatest_decrease}")
