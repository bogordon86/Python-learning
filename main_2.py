#allow os to run across different systems
import os

# importing csv module
import csv
 
# csv file name
filename = "election_data_1.csv"
 
# initializing the titles and rows list
fields = []
rows = []
 
# reading csv file
with open(filename, 'r') as csvfile:
    # creating a csv reader object
    csvreader = csv.reader(csvfile)
     

 
#declare columns

#The total number of votes cast
#len()column 1
#total_votes = len[]

#A complete list of candidates who received votes

#The percentage of votes each candidate won

#The total number of votes each candidate won

#The winner of the election based on popular vote.


