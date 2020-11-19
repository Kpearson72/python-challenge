import os
import csv

file_name = "Pyroll/Resources/election_data.csv"
csv_file = open(file_name)
#using a dictionary reader to read the csv and signing it to a variable
csv_reader = csv.DictReader(csv_file)
print(csv_reader)