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
#Calculate Total Votes for each Candidate and Print
    total = "Total Votes: "
    count = (len(open("election_data_1.csv").readlines())-1)
    print(total + str(count))



    for row in csvreader:
        if row[2] not in candidates:
            candidates[row[2]] = 0

        candidates[row[2]] += 1

        print(candidates)

        candidate_name = row[2]

#Find the Candidates Values and Number of Votes
        if candidate_name not in candidates:

        # Add it to the list of candidates in the running
            candidates.append(candidate_name)
        # And begin tracking that candidate's voter count
            candidate_votes[candidate_name] = 0
    # Then add a vote to that candidate's count
            candidate_votes[candidate_name] = candidate_votes[candidate_name] + 1

            votes = candidate_votes.get(candidate_name)
            vote_percentage = (votes / count) * 100
        print (vote_percentage)
#The winner of the election based on popular vote.

Winning_candidate = 0
WC_name = ''

for name, votes in candidates.items() :
    if votes > Winning_candidate:
        Winning_candidate = votes
        WC_name = name

    print("Winner: " + WC_name + " (" + str(Winning_candidate) +")")


