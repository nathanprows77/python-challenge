import os
import csv

csvpath = os.path.join('..', 'Resources', 'budget_data.csv')



with open(csvpath) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    print(csv_reader)
