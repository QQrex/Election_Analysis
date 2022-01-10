#The data we need to retrieve.
#1. The total number of votes cast
#2. A complete list of candidates who received votes
#3. The Percentage of votes each candidate won
#4. The total number of votes each candidate won
#5. The winner of the lection based on popular vote

import csv
import os

# Assign a variable to load a file from a path
file_to_load = os.path.join("Resources", "election_results.csv")

#Assign a variable to save the file to a path
file_to_save = os.path.join("analysis", "election_analysis.txt")

#1. Initialize a total vote counter
total_votes = 0

#Candidate Options
candidate_options = []

#Declare the empty dictionary
candidate_votes = {}

#Winning Candidate and Winning Count Tracker
winning_candidate = ""
winning_count = 0
winning_percentage = 0

#Open the election results and  read the file.
with open(file_to_load) as election_data:
    file_reader = csv.reader(election_data)

    #Read and print the header row
    header = next(file_reader)
    print(header)

    #Print each row in the CSV file.
    for row in file_reader:
        #2. Add to the total vote count.
        total_votes +=1

        #print the canadidate name for each row
        candidate_name = row[2]

        # If the candidate does not match any existing candidate...
        if candidate_name not in candidate_options:

            # Add it to the list of candidates.
            candidate_options.append(candidate_name)

            #Begin tracking that candidate's vote count
            candidate_votes[candidate_name] = 0

        #Add a vote to the that candidate's count.
        candidate_votes[candidate_name] +=1
    
#Determine the percentage of votes for each candidate by looping through the counts
# Iterate through the candidate list
for candidate_name in candidate_votes:
    #retrieve vote count of a candidate
    votes = candidate_votes[candidate_name]
    #Calculate the percentage of votes.
    vote_percentage = float(votes) / float(total_votes) * 100
    #print the candidate name and percentage of votes
 
    #to do: print out each candidates's name, vote count and percentage of votes to the terminal
    
    #Determine winning vote count and candidate
    #Determin if the votes is greater than the winning count

    if (votes > winning_count) and (vote_percentage > winning_percentage):
        #If true then set winning_count = votes and winning_percent = vote_percentage.
        winning_count = votes
        winning_percentage = vote_percentage
        #And, set the winning_candidate equal to the candidate's name
        winning_candidate = candidate_name

    #print out the winning candidate, vote count and percentage
    print(f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")
Winning_candidate_summary = (
    f"----------------------\n"
    f"winner: {winning_candidate}\n"
    f"Winning Vote Count: {winning_count:,}\n"
    f"Winning Percentage: {winning_percentage:.1f}%\n"
    f"----------------------\n")
print(Winning_candidate_summary)