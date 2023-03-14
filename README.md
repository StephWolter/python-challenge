## Setup

* Created a new repository for this project called `python-challenge`. 
* Cloned 'python-challenge' to my computer.
* Created a directory for each Python challenge. Used folder names: **PyBank** and  **PyPoll**, respectively.
* Inside of each folder added the following:

  * A new file called `main_bank.py` and 'main_poll.py' respectively as the main script file.
  * A `Resources` folder that contains the CSV files used. 
  * An `analysis` folder that contains the text file that has the results from my analysis.


## PyBank Challenge
* Using the financial data in "budget_data.csv"
* Defined lists
* Split the csv by commas and skipped the header row
* Initialized my variables
* Split the csv into two lists, one for each column
* Calculated the total number of months included in the dataset with a loop
* Calculated the net total amount of "Profit/Losses" over the entire period with a sum function
* Calculated the changes in "Profit/Losses" over the entire period with a loop subtracting each month from the previous
* Calculated the the average of those changes
* Calculated the greatest increase in profits (date and amount) over the entire period using a max() function
* Calculated the greatest decrease in profits (date and amount) over the entire period using a min() function
* Printed out a summary
* Print analysis to terminal and exported a text file with results
* I ADMIT I HAD DIFFICULTY WITH FORMATTING HERE

## PyPoll Challenge
* Using the election data in "election_data.csv"
* Defined lists and variables
* Read in csv file as "election_data" using deliminater ","
* Skip past the header
* Initialize vote counter
* Split the csv data into three lists by columns
* Add 1 to the total for each row (finding total votes per candidate)
* Create an append() loop to compile a complete list of candidates
* Define variables for the votes of each individual candidate by index 
* Create a list of all the total votes
* Find the index of the maximum vote quantity and use that index to find the winning candidate
* Calculate the percentage of votes each candidate won
* Create a formatted list of the percentage of votes each candidate won
* Print requested information using f strings when appropriate
* Print analysis to terminal and exported a text file with results
* I ADMIT I HAD DIFFICULTY WITH FORMATTING HERE
