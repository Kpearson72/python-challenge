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

for line in csv_reader:
# CALCULATING THE NUMBER OF MONTHS
    month_count = month_count +1

# CALCULATING NET TOTAL SUM OF PROFIT/LOSSES
    sum_total_profitlosses = sum_total_profitlosses + int(line["Profit/Losses"])

print(f'Financial Analysis')
print(f'-----------------------------')
print(f'Total Months: {month_count}')
print(f'Total: ${sum_total_profitlosses}')
print(f'Average Change: $')
print(f'Greatest Increase in Profits: ')
print(f'Greatest Decrease in Profits: ')





