import csv
import os

file = os.path.join('resources', 'election_data.csv')

with open(file) as f:
    reader = csv.reader(f, delimiter=',')
    header_row = next(reader)

    for index, column_header in enumerate(header_row):
        print(index, column_header)

    # create lists from columns 
    voter_id = []
    country = []
    candidate = []
    c = 1 #counter start

    # storage data
    for row in reader: # loop to append rows to lists
        voter_id.append(row[0])
        country.append(row[1])
        candidate.append(row[2])

# calculations 
total_votes = len(voter_id)

# print results 
print('Election Results')
print('----------------------------')
print(f'Total Votes : {(total_votes)}')



