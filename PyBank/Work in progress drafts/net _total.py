import os
import csv

file_name = "PyBank/Resources/budget_data.csv"
csv_file = open(file_name)
csv_reader = csv.DictReader(csv_file)

#next(csv_reader) #skipping header

# setting variables

month_count = 0
sum_total_profitlosses = 0

# counting the total months

for line in csv_reader:
####month_count = month_count +1
####counting the total months
####print(f'Total Months: {month_count}')

    #sum of profit/losses
    sum_total_profitlosses = sum_total_profitlosses + int(line["Profit/Losses"])
    
print(f'Total: ${sum_total_profitlosses}')
