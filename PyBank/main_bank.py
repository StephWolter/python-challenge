import os
import csv
#point to correct resource csv file
budget_data = os.path.join("Resources", "budget_data.csv")
# Open and read csv
with open(budget_data) as csvfile:
    csv_reader = csv.reader(csvfile, delimiter=",")
    
    csv_header = next(csv_reader)
    #print out the csv file
    #print(f"CSV Header: {csv_header}")

    # Read each row of data after the header
    for row in csv_reader:
        print(row)

#define list and variables within
    def monthly_statements(budget_data):
        month = csv_reader[0]
        prof_loss = csv_reader[1]

#calculate total months
    total_months = len[month]
    print(total_months)
    
#display output
#print("Financial Analysis")
#print("--------------------")
#print(f"The number of months is ", total_months)
