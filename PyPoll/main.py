import csv
import os

from collections import Counter

file = os.path.join('resources', 'election_data.csv')

# create lists from columns 
voter_id = []
country = []
candidate = []
c = 1 #counter start

with open(file) as f:
    reader = csv.reader(f, delimiter=',')
    header_row = next(reader)

    # for index, column_header in enumerate(header_row):
    #     print(index, column_header)

    # storage data
    for row in reader: # loop to append rows to lists
        voter_id.append(row[0])
        country.append(row[1])
        candidate.append(row[2])

# calculations 
total_votes = len(voter_id)

candidates = Counter(candidate).keys()
votes = Counter(candidate)

# print results 
print('Election Results')
print('----------------------------')
print(f'Total Votes : {(total_votes)}')
print('----------------------------')
for key,value in votes.items():
    print(f'{key}, {value/total_votes:.1%} ({value})')
print('----------------------------')
print(f'Winner: {max(votes, key=votes.get)}')
print('----------------------------')

# export results 
output_file = os.path.join('resources', 'election_results.txt')

with open(output_file, 'w') as datafile: 
    datafile.write('Election Results\n')
    datafile.write('----------------------------\n')
    datafile.write(f'Total Votes : {(total_votes)}\n')
    datafile.write('----------------------------\n')
    for key,value in votes.items():
        datafile.write(f'{key}, {value/total_votes:.1%} ({value})\n')
    datafile.write('----------------------------\n')
    datafile.write(f'Winner: {max(votes, key=votes.get)}\n')
    datafile.write('----------------------------\n')

    # Write in zipped rows
    # writer.writerows(cleaned_csv)



