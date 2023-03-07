import os
import csv

budget_data = os.path.join("Resources", "budget_data.csv")
# Open and read csv
with open(budget_data) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=",")
