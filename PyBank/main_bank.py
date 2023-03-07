import os
import csv
#point to correct resource csv file
budget_data = os.path.join("Resources", "budget_data.csv")
# Open and read csv
with open(budget_data) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=",")

#define list and variables within
def budget_csv(month_data):
 
    month = str(month_data[0])
    prof_loss = int(month_data[1])

total_months = len('prof_loss')

    

print("Financial Analysis")
print("--------------------")
print(f"The number of months is ", total_months)
