# import os and csv modules
# help https://bit.ly/2Ncs6Hl
import os
import csv

file = os.path.join('resources', 'budget_data.csv')

with open(file) as f:
    
    reader = csv.reader(f, delimiter=',')
    header_row = next(reader)
        # print(header_row) if want to review what my headers are
    
    for index, column_header in enumerate(header_row):
        print(index, column_header)

    # empty function total_months = []
    months = []
    for row in reader: 
        months.append(row[0]) # add months column 0 

    # empty function profit/loss = []
    # profit_loss = []
    # for row in reader:
    #     profit_loss.

# def pybank(bankdata):

# data reading 
# date = str(f[0])
# profit_loss = int(f[1])


# total months 
# total_months = len(rows)

# profit loss 
    #total profit loss from column 2 = index(1)

# greatest increase vs previous month

    # - get previous time period 
    # - calculate p(n) - p(n-1)
    # loop holding to highest value 
    # list = numbers 
    # last_row =  next (csvfile)
    # max = 0
    # for x in l:
    #     if x > max: 
    #         max = x

    #     last_row = row 

# greatest decrease 

# 

# loading variables as list 


# The total number of months included in the dataset


# The net total amount of "Profit/Losses" over the entire period


# The average of the changes in "Profit/Losses" over the entire period

    # def average(numbers):
    #     lenght = len(numbers)
    #     total = 0.0
    #     for number in numbers:


# The greatest increase in profits (date and amount) over the entire period


# The greatest decrease in losses (date and amount) over the entire period

# As an example, your analysis should look similar to the one below:

# Financial Analysis
# ----------------------------
# Total Months: 86
# Total: $38382578
# Average  Change: $-2315.12
# Greatest Increase in Profits: Feb-2012 ($1926159)
# Greatest Decrease in Profits: Sep-2013 ($-2196167)

# print results 
print('Financial Analysis')
print('----------------------------')
print('Total Months: ' + str(len(months)))
