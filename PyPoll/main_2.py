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
    total = "Total Votes: "
    count = (len(open("election_data_1.csv").readlines())-1)
    print(total + str(count))
    for row in csvreader:

#Print out the total number of votes

#Find the Candidates Values and Number of Votes
        if row[2] not in candidates:
            candidates[row[2]] = 0

        candidates[row[2]] += 1

    print(candidates)


    
#A complete list of candidates who received votes
    #used = set()
    #candidate_list = [x for x in col_3 if x not in used and (used.add(x) or True)]
    #print(candidate_list)

#The total number of votes each candidate won

#The winner of the election based on popular vote.
#nner = 0
   #winner_name = ''

   #for name, votes in candidates.items() :
       #if votes > winner:
          # winner = votes
           #winner_name = name

   #print("Winner: " + winner_name + " (" + str(winner) +")")
#Winner equals the largest number from the total number of votes
