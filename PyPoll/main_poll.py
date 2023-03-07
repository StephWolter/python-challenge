import os
import csv

election_data = os.path.join("Resources", "election_data.csv")
# Open and read csv
with open(election_data) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=",")