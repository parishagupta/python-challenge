# Define and link csv
import os
import csv
election_data = os.path.join(os.path.dirname(__file__), "Resources", "election_data.csv") # Navigate to cwd and search for Resourcess\election_data.csv

# Open and read csv
with open(election_data) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    csv_data = list(csvreader)[1:]

# Define variables as lists
ballot_id=[]
county=[]
candidate=[]
unique_candidates=[]
votes_per_candidate=[]
result_display_candidate=[]
percent_per_candidate=[]
winner_votes=0
loser_votes=0

# Read ballot ID, county, and candidate as list; ballot ID as integer list
ballot_id = [int(row[0]) for row in csv_data]
county = [(row[1]) for row in csv_data]
candidate= [(row[2]) for row in csv_data]

# Calculate total votes
total_votes=len(ballot_id)
loser_votes=total_votes

# Store unique candidate records
for x in candidate:
    if x not in unique_candidates:
        unique_candidates.append(x)
for x in unique_candidates:
    num_candidates=len(unique_candidates)

# Store votes per candidate
for v in range(num_candidates):
    votes_per_candidate.append(candidate.count(unique_candidates[v]))

# Calculate votes per candidate as winner and loser 
for c in range(num_candidates):
    percent_per_candidate.append(f"{round((votes_per_candidate[c]/total_votes*100),3)}%")
    if votes_per_candidate[c]>winner_votes:
        winner=unique_candidates[c]
        winner_votes=votes_per_candidate[c]
    if votes_per_candidate[c]<loser_votes:
        loser=unique_candidates[c]
        loser_votes=votes_per_candidate[c]

for l in range(num_candidates):
    result_display_candidate.append(f"{unique_candidates[l]}: {percent_per_candidate[l]} ({votes_per_candidate[l]})")

result_lines="\n".join(result_display_candidate)

# Check calc
# print(ballot_id[:4])
# print(county[:4])
# print(candidate[:4])
# print(total_votes)
# print(f"Names of candidates: {unique_candidates}")
# print(f"Number of unique candidates: {num_candidates}")
# print(F"Number of votes per candidate: {votes_per_candidate}")
# print(f"Winner: {winner}; {winner_votes}")
# print(f"Loser: {loser}; {loser_votes}")
# print(result_lines)

# Display analysis report using f strings over rows of 48 characters
report = (
    f"{' Election Results ':-^48}\n" 
    f"{'Total Votes: '}{total_votes}\n"
    f"{'--':-^48}\n"
    f"{result_lines}\n"
    f"{'--':-^48}\n"
    f"{'Winner: '}{winner}\n"
    f"{'--':-^48}\n"
)
print(report)

# # Assemble the output text file path, starting from the cwd
textfile_path = os.path.join(
    os.path.dirname(__file__), "Analysis", "election_analysis.txt"
)

# # Open the election_analysis text file and write the report in it
with open(textfile_path, "w", encoding="utf-8") as textfile:
    textfile.write(report)