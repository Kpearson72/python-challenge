import os
import csv

file_name = "PyBank/Resources/budget_data.csv"
csv_file = open(file_name)
#using a dictionary reader to read the csv and signing it a variable
csv_reader = csv.DictReader(csv_file)

#next(csv_reader) #skipping header

# COUNTING TOTAL MONTHS
#setting variable for month count, net total profit/loss

month_count = 0
sum_total_profitlosses = 0
previous_profitlosses = 0
change_profitloss = 0
change_list_profitlosses = []
change_month = []

#creating an index to know list position
index = 0

#looping through the data

for line in csv_reader:
    #going through the list with index
    if(index==0):
        month_count+=1
        sum_total_profitlosses = sum_total_profitlosses + int(line["Profit/Losses"])
        previous_profitlosses = int(line["Profit/Losses"])
        index +=1
        continue

# CALCULATING THE NUMBER OF MONTHS
    month_count = month_count +1

# CALCULATING NET TOTAL SUM OF PROFIT/LOSSES
    sum_total_profitlosses = sum_total_profitlosses + int(line["Profit/Losses"])

# CALCULATING CHANGES IN PROFIT/LOSSES FOR ENTIRE TIME - THEN FINDING AVERAGE OF CHANGES
    change_profitloss = int(line["Profit/Losses"]) - previous_profitlosses
    #creating a new list and adds to list of profitlosses
    change_list_profitlosses.append(change_profitloss)
    #overrides the previous profit loss
    previous_profitlosses = int(line["Profit/Losses"])


print(f'Financial Analysis')
print(f'-----------------------------')
print(f'Total Months: {month_count}')
print(f'Total: ${sum_total_profitlosses}')
#prints the average change profit loss by rounding the number and leaving to digits to the right of decimal
# divides new list created by 
print(f'Average Change: ${round(sum(change_list_profitlosses)/len(change_list_profitlosses),2)}')
print(f'Greatest Increase in Profits: ')
print(f'Greatest Decrease in Profits: ')





