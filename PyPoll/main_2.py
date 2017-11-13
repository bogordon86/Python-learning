#Each dataset has three columns: `Voter ID`, `County`, and `Candidate'
#allow os to run across different systems
import os

# importing csv module
import csv
 
# csv file name
filename = "election_data_1.csv"
 
# reading csv file
with open("election_data_1.csv", 'r') as csvfile:
    # creating a csv reader object
    csvreader = csv.reader(csvfile)

#declare columns
    col_1 = [x[0] for x in csvreader]
    col_2 = [x[1] for x in csvreader]
    col_3 = [x[2] for x in csvreader]

#The total number of votes cast
    total = "Total Votes: "
    total_col1 = (len(col_1) -1)
    print ((total)+ str(total_col1))
    
#A complete list of candidates who received votes

#The percentage of votes each candidate won
#

#The total number of votes each candidate won

#The winner of the election based on popular vote.

#Winner equals the largest number from the total number of votes
