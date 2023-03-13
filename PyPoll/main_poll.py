import os
import csv

election_csv = os.path.join("Resources", "election_data.csv")
election_data = []
# Open and read csv
with open(election_csv) as csvfile:
    election_data = csv.reader(csvfile, delimiter=",")

    # Label the header row first 
    election_header = next(election_data)

    #Spot check csv file is working
    #for row in election_data:
        #print(row)
    total_votes = 0
    candidate_list = []
    votes = {}

    for row_data in election_data:
        ballot_id, county, candidate_voted = row_data[0], row_data[1], row_data[2]
        #spot check those lists worked
        #print(candidate_voted)

        #The total number of votes cast
        total_votes += 1

        # A complete list of candidates who received votes
        if candidate_voted not in candidate_list:
            candidate_list.append(candidate_voted)
            votes[candidate_voted] = 0
        votes[candidate_voted] += 1

    
    #The total number of votes each candidate won
    CCS_votes = float(votes["Charles Casper Stockham"])
    DD_votes = float(votes["Diana DeGette"])
    RAD_votes = float(votes["Raymon Anthony Doane"])

    vote_display = [CCS_votes, DD_votes, RAD_votes]

#"{:.2f}".format(13.949999999999999)
    #The percentage of votes each candidate won 
    CCS_percent = (float(CCS_votes)/float(total_votes))*100
    DD_percent = (float(DD_votes)/float(total_votes))*100 
    RAD_percent = (float(RAD_votes)/float(total_votes))*100

    percent_display = [CCS_percent, DD_percent, RAD_percent]

display = zip(candidate_list, percent_display, vote_display)
vote_summary = list(display)


#* The winner of the election based on popular vote.

print("Election Results")
print("-------------------------")
print(f"Total Votes: {total_votes}")
print("-------------------------")
print(f"{vote_summary}")
print("-------------------------")
#print(f"Winner: {winner}") 
print("-------------------------")
