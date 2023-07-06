import csv
import os

election_file = r"C:\Users\Tim\DataCourse\HW\Python-Challenge\PyPoll\Resources\election_data.csv"
with open (election_file) as csvfile:
    # create csv reader
    csvreader = csv.reader (csvfile, delimiter = ",")

    # init vars
    rowcount = 0
    can_list = 0

    # read header from first row
    header = next (csvreader)

    votes = {}  # key: candidate name, val: vote count
    name = "Charles Casper Stockham" 
    for a, b, name in csvreader:
        if name in votes:
            votes[name] +=1
        else:
            votes[name] = 1
        rowcount += 1

# print list of cannidates
print("Election Results")
print("-"*25)
print(f"Total Votes: {rowcount}")
print("-"*25)
max_votes = 0
for name, can_votes in votes.items():
    print(f"{name}: {can_votes/rowcount*100:.3f}% ({can_votes})")
    if can_votes > max_votes:
        max_votes = can_votes
        Winner = name
    
print("-"*25)
print(f"Winner: {Winner}")
print("-"*25)
# outputs

with open("PyPoll/Analysis/PyPollAnalysis.txt", 'w') as fout:
    fout.write("Election Results\n")
    fout.write("-"*25 + '\n')
    fout.write(f"Total Votes: {rowcount}\n")
    fout.write("-"*25 + '\n')
    max_votes = 0 
    for name, can_votes in votes.items():
        fout.write(f"{name}: {can_votes/rowcount*100:.3f}% ({can_votes})\n")
        if can_votes > max_votes:
            max_votes = can_votes
            Winner = name
    fout.write("-"*25 + '\n')
    fout.write(f"Winner: {Winner}\n")
    fout.write("-"*25 + '\n')

