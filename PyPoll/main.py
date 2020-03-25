# First we'll import the os module
# This will allow us to create file paths across operating systems
import os
from collections import Counter

# Module for reading CSV files
import csv

# declare variables
candidates = []
total_votes = 0
winning_candidate_vote_count = 0
winning_candidate = ""


# os independent function to get path of Resources
csvpath = os.path.join('', 'Resources', 'election_data.csv')

# Open the CSV
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    # Read the header row first (skip this step if there is now header)
    csv_header = next(csvreader)
    # print(f"CSV Header: {csv_header}")

    # Loop through looking 
    for row in csvreader:
        total_votes = total_votes + 1
        # voter_id.append(row[0])
        # county.append(row[1])
        candidates.append(row[2])


print("\nElection Results")
print("-------------------------")
print(f"Total Votes: {total_votes}")
print("-------------------------")

# used Counter library to build frequency of candidates in a list
number_of_votes_per_candidate = Counter(candidates)

for candidate in number_of_votes_per_candidate:
    vote_percentage = round(((int(number_of_votes_per_candidate[candidate])/int(total_votes))*100), 2)
    print(f"{candidate}: {vote_percentage}% ({number_of_votes_per_candidate[candidate]})")
    if number_of_votes_per_candidate[candidate] > winning_candidate_vote_count:
        winning_candidate_vote_count = number_of_votes_per_candidate[candidate]
        winning_candidate = candidate

print("-------------------------")
print(f"Winner: {winning_candidate}")
print("-------------------------\n")




# os independent function to get path of Resources
text_path = os.path.join('', 'Resources', 'textFile.txt')

# write data in a file. 
text_file = open(text_path,"w") 
text  = "Election Results\n"
text += "-------------------------\n"
text += "Total Votes: " + str(total_votes) + "\n"
text += "-------------------------\n"

for candidate in number_of_votes_per_candidate:
    vote_percentage = round(((int(number_of_votes_per_candidate[candidate])/int(total_votes))*100), 2)
    text += str(candidate) + ": " + str(vote_percentage) + "% (" + str(number_of_votes_per_candidate[candidate]) + ")\n"
    if number_of_votes_per_candidate[candidate] > winning_candidate_vote_count:
        winning_candidate_vote_count = number_of_votes_per_candidate[candidate]
        winning_candidate = candidate

text += "-------------------------\n"
text += "Winner: " + str(winning_candidate) + "\n"
text += "-------------------------"
  
text_file.writelines(text) 
text_file.close() #to change file access modes 