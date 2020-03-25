# First we'll import the os module
# This will allow us to create file paths across operating systems
import os

# Module for reading CSV files
import csv

# declare variables
total_number_months = 0
sum_profit_loss = 0
my_profit_loss_list = []
sum_profit_loss_changed = 0
count_profit_loss_changes = 0


# os independent function to get path of Resources
csvpath = os.path.join('', 'Resources', 'budget_data.csv')

# Open the CSV
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    # Read the header row first (skip this step if there is now header)
    csv_header = next(csvreader)
    print(f"CSV Header: {csv_header}")

    # Loop through looking 
    for row in csvreader:
        total_number_months = total_number_months  + 1   
        sum_profit_loss += int(row[1])
        my_profit_loss_list.append(row[1])

        
for i in range(len(my_profit_loss_list) -1):
    sum_profit_loss_changed += int(my_profit_loss_list[i+1]) - int(my_profit_loss_list[i])
    count_profit_loss_changes = count_profit_loss_changes + 1


print(f"Number of Months: {total_number_months}")
print(f"Sum of Profit & Loss: {sum_profit_loss}")

print(f"{sum_profit_loss_changed} / {count_profit_loss_changes}")

print(f"Average Change: {round(sum_profit_loss_changed/count_profit_loss_changes, 2)}\n")
    
 
