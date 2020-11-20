import os
import csv

file_name = "PyPoll/Resources/election_data.csv"
csv_file = open(file_name)
#using a dictionary reader to read the csv and assigning it to a variable
csv_reader = csv.DictReader(csv_file)

#setting vairables
total_votes = 0
unique_candidates = []
total_votes_percandidate = []

#looping through the data
for line in csv_reader:
    #calculate total votes
    total_votes = total_votes +1
    #creating a list from the csv
    list_candidates = (line["Candidate"])
    #going through the list with index - if name = same name then add to total votes per candidate
    if list_candidates in unique_candidates:
        index_candidate = unique_candidates.index(list_candidates)
        # +1 shows the "next" candidate
        total_votes_percandidate[index_candidate] = total_votes_percandidate[index_candidate] +1
    else:
        #else add to the list of candidates 
        unique_candidates.append(list_candidates)
        #else add total number of votes each candidate had in a list
        total_votes_percandidate.append(1)
#variables-vote percentage for each candidate, number of greatest vote count, 

#variable - 1)number of top votes/candidate 2)percentage/candidate 3)which candidate = greatest # votes
vpct = []
number_greatest_votes = 0
top_votes = total_votes_percandidate[0]

#CALCULATING PERCENTAGE VOTES AND VOTES PER CANDIDATE USING A LIST
for v in range(len(unique_candidates)):
    vote_percent = round(total_votes_percandidate[v]/total_votes *100,2)
    vpct.append(vote_percent)
   
    if total_votes_percandidate[v] > top_votes:
        top_votes = total_votes_percandidate[v]
        number_greatest_votes = v

who_won = unique_candidates[number_greatest_votes]


print(f'Election Results')
print(f'-----------------------------')
print(f'Total Votes: {total_votes}')
print(f'-----------------------------')
for i in range(len(unique_candidates)):
    #added f-string formatting to add more zeros to percentage
    print(f'{unique_candidates[i]}: {vpct[i]:.3f}% ({total_votes_percandidate[i]}) ')
print(f'-----------------------------')
print(f'Winner: {who_won}')
print(f'-----------------------------')

#write a text file named analysis.txt

g = open('analysis.txt', 'w+')
g.write(f'Election Results \n')
g.write(f'----------------------------- \n')
g.write(f'Total Votes: {total_votes} \n')
g.write(f'----------------------------- \n')
for i in range(len(unique_candidates)):
    #added f-string formatting to add more zeros to percentage
    g.write(f'{unique_candidates[i]}: {vpct[i]:.3f}% ({total_votes_percandidate[i]}) \n')
g.write(f'----------------------------- \n')
g.write(f'Winner: {who_won} \n')
g.write(f'----------------------------- \n')
g.close()

