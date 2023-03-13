import os
import csv

election_csv = os.path.join("Resources", "election_data.csv")
election_data = []
candidate_list = {}
vote_candidates = ()

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

        #The total number of votes cast
        total_votes += 1

        # A complete list of candidates who received votes and the running total
        if candidate_voted not in candidate_list:
            candidate_list.append(candidate_voted)
            votes[candidate_voted] = 0
        votes[candidate_voted] += 1
        #print(candidate_list)
    
    
    #The total number of votes each candidate won
    CCS_votes = int(votes[candidate_list[0]])
    DD_votes = int(votes[candidate_list[1]])
    RAD_votes = int(votes[candidate_list[2]])

    vote_candidates = (CCS_votes, DD_votes, RAD_votes)
    winner_votes = max(vote_candidates)

    #The percentage of votes each candidate won 
    CCS_percent = ((int(CCS_votes)/int(total_votes))*100)
    DD_percent = (int(DD_votes)/int(total_votes))*100 
    RAD_percent = (int(RAD_votes)/int(total_votes))*100
    percents = (CCS_percent, DD_percent, RAD_percent)
    #format the percents by reducing decimals and adding percent symbol
    percent_candidates = list(map("{:.3f}%".format, percents))
    #spot check percents
    #print(percent_candidates)
#create summary with everything together
numbers_display = zip(candidate_list, percent_candidates, vote_candidates)
vote_summary = list(numbers_display)
       
print("Election Results")
print("-------------------------")
print(f"Total Votes: {total_votes}")
print("-------------------------")
print(*vote_summary,sep='\n')
print("-------------------------")
#print(f"Winner: {winner}") 
print("-------------------------")
