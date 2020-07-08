# Modules
import os
import csv
import collections
# Set path for file 

csvpath = os.path.join("..", "PyPoll", "election_data.csv")

#Open the CSV

with open(csvpath, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

# The total number of votes cast

    next(csvreader)

# A complete list of candidates who received votes

    candidates = []
    total_votes = 0 
    candidate_dict = {}
    for row in csvreader:
        total_votes = total_votes +1
        
        if row[2] not in candidates:
          candidates.append(row[2])
          candidate_dict[row[2]] = 0 
        candidate_dict[row[2]] = candidate_dict[row[2]] +1 

    percent_dict = {}
    max_votes = 0 
    winner = ""

    print("Election Results")
    print("-------------------")
    print("Total Votes: " + str(total_votes))
    print("-------------------")
# The percentage of votes each candidate won
    for x in candidate_dict:
        percent_dict[x] = round((candidate_dict[x] / total_votes) * 100, 2)

# The winner of the election based on popular vote.
        votes = candidate_dict.get(x)
        if votes > max_votes:
            max_votes = votes
            winner = x  
        output = f"{x} : {percent_dict[x]}% , {votes} \n "
        print(output)

    print("-------------------")
    print("Winner: " + (winner))
    print("-------------------")
    outF = open("pypoll.txt", "w")
    outF.writelines("Election Results")
    outF.writelines("\n")
    outF.writelines("-------------------")
    outF.writelines("\n")
    outF.writelines("Total Votes: " + str(total_votes))
    outF.writelines("\n")
    outF.writelines("-------------------")
    outF.writelines("\n")
    outF.writelines(output) # output won't display all names in the election outside of the for loop. WHOOPSIE! 
    outF.writelines("\n")
    outF.writelines("-------------------")
    outF.writelines("\n")
    outF.writelines("Winner: " + (winner))
    outF.writelines("\n")
    outF.writelines("-------------------")
    outF.writelines("\n")
    outF.close()
