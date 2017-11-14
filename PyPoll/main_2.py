#Each dataset has three columns: `Voter ID`, `County`, and `Candidate'
#allow os to run across different systems
import os

# importing csv module
import csv
 
# csv file name
filename = "election_data_1.csv"

#Declaring empty dictionary
candidates = {}

# reading csv file
with open("election_data_1.csv", 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    next (csvreader, None)
    for row in csvreader:
        if row[2] not in candidates:
            candidates[row[2]] = 0

        candidates[row[2]] += 1

    print(candidates)

#The total number of votes cast
        #total = "Total Votes: "
       # total_votes = len(voter_id)
   # print (total + str(total_votes))
    
#A complete list of candidates who received votes
    #used = set()
    #candidate_list = [x for x in col_3 if x not in used and (used.add(x) or True)]
    #print(candidate_list)

#The total number of votes each candidate won

#The winner of the election based on popular vote.

#Winner equals the largest number from the total number of votes
