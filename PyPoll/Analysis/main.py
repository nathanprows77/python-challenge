import os
import csv

total = 0
candidate = 0
votes = 0
Vote_percent = 0

#Import csv file
poll_csv = os.path.join("PyPoll", "Resources", "election_data.csv")

#Define columns as lists
Voter_ID = []
County = []
Candidate = []
Unique_Candidate_List = []
Vote_percent = {}
Vote_percent = dict()
#Open csv file with csvreader
with open(poll_csv) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    csv_header = next(csvfile)
    # previous_candidates = next(csvreader)[2]
    Total_Votes = 0
    Vote_count = {}
    Vote_count = dict()

    for row in csvreader:
        Voter_ID.append(row[0])
        County.append(row[1])
        Candidate.append(row[2])
        # previous_candidates = row[2]
        Total_Votes = total + len(Candidate)
        
         
        if row[2] not in Unique_Candidate_List:
            Unique_Candidate_List.append(row[2])

        if row[2] not in Vote_count.keys():
            Vote_count[row[2]] = 1
        else:
            Vote_count[row[2]] += 1

  
print("Election Results")
print("------------------------------------------------------")
print("Total Votes: ", Total_Votes)
print("------------------------------------------------------")
high_score = 0
winner = ""
for candidate in Unique_Candidate_List:
    Vote_percent[candidate] = (Vote_count[candidate] / Total_Votes) * 100
    print(candidate + ": " + str(round(Vote_percent[candidate], 3)) + "% (" + str(Vote_count[candidate]) + ")")
    if Vote_count[candidate] > high_score:
        high_score = Vote_count[candidate]
        winner = candidate
print("------------------------------------------------------")
print("Winner: " + winner)
print("------------------------------------------------------")

# Set variable for output file
output_file = os.path.join("Pypoll_main.csv")

#  Open the output file
with open(output_file, "w") as datafile:
    writer = csv.writer(datafile)
# python /PyPoll/Analysis/main.py > Pypol_main.txt