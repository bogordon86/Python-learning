#Each dataset has three columns: `Voter ID`, `County`, and `Candidate'
#allow os to run across different systems
import os

# importing csv module
import csv
 
# csv file name
files = "election_data_1.csv"

#Declaring Dictionary
candidates = {}

# reading csv file
with open("election_data_1.csv", 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    next (csvreader, None)

#Calculate Total Votes for each Candidate and Print
    total = "Total Votes: "
    count = (len(open("election_data_1.csv").readlines())-1)
    print(total + str(count))

    candidates = {}
    candidates_2 = {}
    for row in csvreader:

        if row[2] not in candidates:
            candidates[row[2]] = 0

        candidates[row[2]] += 1
    print(candidates)
        # The winner of the election based on popular vote.
    for row in csvreader:
        county = row[1]
        candidate = row[2]

        # Find the Candidates Values and Number of Votes
        if candidate not in candidates_2:
            candidates_2[candidate] = 0

        candidates_2[candidate] += 1

        # Divide count by total items, make percent
        # aka accessing everything in the dictionary
        for key, candidate in candidates_2.items():
            # declare percent as a int
            percent = 0
        # Divide value by the total
        percent = value / count
        # Format as percent
        percent = '{0:.0f}%'.format(percent * 100)
        # key = candidate, value = vote count for candidate, percent
    print(str(candidate) + str(value) + str(percent))

winner = 0
winner_name = ''

for name, votes in candidates.items():
    if votes > winner:
        winner = votes
        winner_name = name

    print("Winner: " + winner_name + " (" + str(winner) + ")")
