import os
import csv

csvpath = os.path.join('PyBank', 'Resources', 'Unit_03_Python_Instructions_PyBank_Resources_budget_data (1).csv')



with open(csvpath) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    print(csv_reader)
