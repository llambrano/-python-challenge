# import os and csv modules
# help https://bit.ly/2Ncs6Hl
import os
import csv

file = os.path.join('resources', 'budget_data.csv')

with open(file) as f:
    reader = csv.reader(f, delimiter=',')
    header_row = next(reader)
    
    for index, column_header in enumerate(header_row):
        print(index, column_header) # to match index with header
    
    #create lists from columns 
    months = [] # empty list to store months = []
    profit_loss = [] # empty list to store profit/loss = []
    change = []
    c = 1 # counter start

    for row in reader: # loop to append rows to lists
        months.append(row[0]) # add all months column 0 
        profit_loss.append(int(row[1])) # add all prof/loss column 1
    
    for c in range(len(profit_loss)-1):
        change.append(profit_loss[c+1]-profit_loss[c])

# calculations 
total_months = len(months)
total_profit_loss = sum(profit_loss) # https://bit.ly/3fPiiiC
avg = round(sum(change)/(len(profit_loss)-1),2)


    # Profit & Loss 
    # avg_profit_loss = []
    # pl_1 = []
        
        
        # Avg change 
        # for i in range(len(profit)-1):
        #     pl_1.append()

# print results 

print('Financial Analysis')
print('----------------------------')
print(f'Total Months: {(total_months)}') # or print('Total Months: ' + str(len(months))) 
print(f"Total: ${(total_profit_loss)}")
print(f"Average  Change: ${(avg)}")