import os
import csv
import sys

total = 0
month = 0
csvpath = os.path.join("Resources", "budget_data.csv")

Date = []
Profit_losses = []

with open(csvpath) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    
    csv_header = next(csv_reader)
    previous_month = next(csv_reader)[1]
    total = int(previous_month)
    max_for_loop = 0
    max_month = ""
    min_for_loop = 0
    min_month = ""
    for row in csv_reader:
        Date.append(row[0])
        Profit_losses.append(int(row[1]) - (int(previous_month)))
        previous_month = row[1]
        total += int(row[1])
        if int(row[1]) >= 0:
            max_for_loop = int(row[1])
            max_month = row[0]
        if int(row[1]) <= 0:
            min_for_loop = int(row[1])
            min_month = row[0]
    month = len(Profit_losses) + 1     
    average_change = sum(Profit_losses)/len(Profit_losses)
    max_increase = max(Profit_losses)
    min_increase = min(Profit_losses)


   
    print('Financial Analysis')
    print("-------------------------------------")
    print("Total Months: " + str(month))
    print("Total:", ('${0}'.format(format(total))))
    print("Total Average Change:", ('${0}'.format(format(average_change, ',.2f'))))
    print("Greatest Monthly Increase in Profits " + max_month + " ($" + str(max_increase) + ")")
    print("Greatest Monthly Increase in Profits " + min_month + " ($" + str(min_increase) + ")")


sys.stdout = open("Pybank.txt", "w")

print('Financial Analysis')
print("-------------------------------------")
print("Total Months: " + str(month))
print("Total:", ('${0}'.format(format(total))))
print("Total Average Change:", ('${0}'.format(format(average_change, ',.2f'))))
print("Greatest Monthly Increase in Profits " + max_month + " ($" + str(max_increase) + ")")
print("Greatest Monthly Increase in Profits " + min_month + " ($" + str(min_increase) + ")")

sys.stdout.close()
