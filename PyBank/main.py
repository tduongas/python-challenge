# First we'll import the os module
# This will allow us to create file paths across operating systems
import os

# Module for reading CSV files
import csv

# declare variables
total_number_months = 0
sum_profit_loss = 0
month = []
profit_loss = []
change_per_month = 0
sum_profit_loss_changed = 0
count_profit_loss_changes = 0
max_increase_profit = 0
max_increase_profit_date = ""
greatest_loss_in_profit = 0
greatest_loss_in_profit_date = ""

# os independent function to get path of Resources
csvpath = os.path.join('', 'Resources', 'budget_data.csv')

# Open the CSV
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    # Read the header row first (skip this step if there is now header)
    csv_header = next(csvreader)
    # print(f"CSV Header: {csv_header}")

    # Loop through looking 
    for row in csvreader:
        total_number_months = total_number_months  + 1   
        sum_profit_loss += int(row[1])
        month.append(row[0])
        profit_loss.append(row[1])

for i in range(len(profit_loss) - 1):
    sum_profit_loss_changed += int(profit_loss[i+1]) - int(profit_loss[i])
    change_per_month = int(profit_loss[i+1]) - int(profit_loss[i])
    count_profit_loss_changes = count_profit_loss_changes + 1

    if change_per_month > max_increase_profit:    
        max_increase_profit = change_per_month
        max_increase_profit_date = month[i+1]
       
    if change_per_month < greatest_loss_in_profit:
        greatest_loss_in_profit = change_per_month
        greatest_loss_in_profit_date = month[i+1]


print("\nFinancial Analysis")
print("----------------------------")
print(f"Total Months: {total_number_months}")
print(f"Total: ${sum_profit_loss}")
print(f"Average Change: {round(sum_profit_loss_changed/count_profit_loss_changes, 2)}")
print(f"Greatest Increase in Profits: {max_increase_profit_date}: (${max_increase_profit})" )
print(f"Greatest Decrease in Profits: {greatest_loss_in_profit_date}: (${greatest_loss_in_profit})\n" )
    

# os independent function to get path of Resources
text_path = os.path.join('', 'Resources', 'textFile.txt')

# write data in a file. 
text_file = open(text_path,"w") 
text  = "Financial Analysis\n"
text += "----------------------------\n"
text += "Total Months: " + str(total_number_months) + "\n"
text += "Total: $" + str(sum_profit_loss) + "\n"
text += "Average Change: " + str(round(sum_profit_loss_changed/count_profit_loss_changes, 2)) + "\n"
text += "Greatest Increase in Profits: " + str(max_increase_profit_date) + ": ($" + str(max_increase_profit) + ")\n"
text += "Greatest Decrease in Profits: " + str(greatest_loss_in_profit_date) + ": ($" + str(greatest_loss_in_profit) + ")\n"
  
text_file.writelines(text) 
text_file.close() #to change file access modes 