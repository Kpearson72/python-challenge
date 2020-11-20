import os
import csv

file_name = "PyBank/Resources/budget_data.csv"
csv_file = open(file_name)
#using a dictionary reader to read the csv and signing it to a variable
csv_reader = csv.DictReader(csv_file)

#setting variables 
month_count = 0
sum_total_profitlosses = 0
previous_profitlosses = 0
change_profitloss = 0
change_list_profitlosses = []
change_month = []
greatest_inc = 0
greatest_dec = 0

#creating an index to know list position
index = 0

#looping through the data

for line in csv_reader:
    #going through the list with index
    if(index==0):
        month_count+=1
        sum_total_profitlosses = sum_total_profitlosses + int(line["Profit/Losses"])
        previous_profitlosses = int(line["Profit/Losses"])
        change_month = change_month + [line["Date"]]
        index +=1
        continue

# CALCULATING THE NUMBER OF MONTHS
    month_count = month_count +1

# CALCULATING NET TOTAL SUM OF PROFIT/LOSSES
    sum_total_profitlosses = sum_total_profitlosses + int(line["Profit/Losses"])

# CALCULATING CHANGES IN PROFIT/LOSSES FOR ENTIRE TIME - THEN FINDING AVERAGE OF CHANGES
    #subtracts the integer number of profit/loss to the one previous to it
    change_profitloss = int(line["Profit/Losses"]) - previous_profitlosses
    #adds to list of profitlosses
    change_list_profitlosses.append(change_profitloss)
    #overrides the previous profit/loss
    previous_profitlosses = int(line["Profit/Losses"])
   
# CALCULATING GREATEST INCREASE AND DECREASE
    #variable to find out location of month in a list to be created
    change_month = change_month + [line["Date"]]
#max and minimum used to find out amounts for greatest decrease and increase of profit/loss using previously created list (change_list_profitlosses)
greatest_inc = max(change_list_profitlosses)
greatest_dec = min(change_list_profitlosses)
#associating a vairable to the previously created list (change_list_profitlosses) to determine what months have greatest increase/decrease
# +1 shows the "next" month that has the greatest inc/dec
greatest_inc_month = change_list_profitlosses.index(greatest_inc)+1
greatest_dec_month = change_list_profitlosses.index(greatest_dec)+1



print(f'Financial Analysis')
print(f'-----------------------------')
print(f'Total Months: {month_count}')
print(f'Total: ${sum_total_profitlosses}')
#prints the average change profit loss by rounding the number and leaving to digits to the right of decimal
# divides new list created by number of items in the list of change_list_profitlosses
print(f'Average Change: ${round(sum(change_list_profitlosses)/len(change_list_profitlosses),2)}')
print(f'Greatest Increase in Profits: {change_month[greatest_inc_month]} (${(str(greatest_inc))})')
print(f'Greatest Decrease in Profits: {change_month[greatest_dec_month]} (${(str(greatest_dec))})')

#write a text file named analysis.txt

g = open('analysis.txt', 'w+')
g.write(f'Financial Analysis \n')
g.write(f'----------------------------- \n')
g.write(f'Total Months: {month_count} \n')
g.write(f'Total: ${sum_total_profitlosses} \n')
g.write(f'Average Change: ${round(sum(change_list_profitlosses)/len(change_list_profitlosses),2)}) \n')
g.write(f'Greatest Increase in Profits: {change_month[greatest_inc_month]} (${(str(greatest_inc))}) \n')
g.write(f'Greatest Decrease in Profits: {change_month[greatest_dec_month]} (${(str(greatest_dec))}) \n')
g.close()



