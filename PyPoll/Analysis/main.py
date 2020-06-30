import os
import csv

poll_csv = os.path.join("PyPoll", "Resources", "election_data.csv")

with open(poll_csv) as csvfile:
    csvreader = csv.reader(cvsfile, delimiter=",")

    csv_header = next(csvfile)
    print(f"Header: {csv_header}")