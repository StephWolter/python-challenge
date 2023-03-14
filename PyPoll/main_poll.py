import os
import csv

election_csv = os.path.join("Resources", "election_data.csv")
election_data = []
vote_candidates = []
votes = {}
candidate_list = []

# Open and read csv
with open(election_csv) as csvfile:
    election_data = csv.reader(csvfile, delimiter=",")
    
    # Label the header row first 
    election_header = next(election_data)
    #initialize variables and set lists/dictionaries
    total_votes = 0
    
    #Create three separate lists based on the columns from the csv file
    for row_data in election_data:
        ballot_id, county, candidate_voted = row_data[0], row_data[1], row_data[2]
       
        #The total number of votes cast
        total_votes += 1

        # A complete list of candidates who received votes and the running total
        if candidate_voted not in candidate_list:
            candidate_list.append(candidate_voted)
            votes[candidate_voted] = 1
        votes[candidate_voted] += 1
    
    
    #The total number of votes each candidate won
    CCS_votes = int(votes[candidate_list[0]])
    DD_votes = int(votes[candidate_list[1]])
    RAD_votes = int(votes[candidate_list[2]])

    vote_candidates = [CCS_votes, DD_votes, RAD_votes]
    
    #find winner based on max votes
    winner_votes = vote_candidates.index(max(vote_candidates))
    #print(winner_votes)
    winner = candidate_list[winner_votes]
 
    #The percentage of votes each candidate won 
    CCS_percent = ((int(CCS_votes)/int(total_votes))*100)
    DD_percent = (int(DD_votes)/int(total_votes))*100 
    RAD_percent = (int(RAD_votes)/int(total_votes))*100
    percents = (CCS_percent, DD_percent, RAD_percent)
    #format the percents by reducing decimals and adding percent symbol
    percent_candidates = list(map("{:.3f}%".format, percents))
 


       
print("Election Results")
print("-------------------------")
print(f"Total Votes: {total_votes}")
print("-------------------------")
for count in range(len(candidate_list)):
    print(f"{candidate_list[count]}: {percent_candidates[count]} ({vote_candidates[count]})")
print("-------------------------")
print(f"Winner: {winner}") 
print("-------------------------")

with open("Analysis/Election_Results.txt", "w") as f:
    l1 = "Election Results"
    l2 = "------------------"
    l3 = (f"Total Votes: {total_votes}")
    l4 = "Analysis"
    l5 = "------------------"
    l6 = (f"Winner: {winner}")
    l7 = "------------------"
    f.writelines([l1,l2,l3,l4,l5,l6,l7])
