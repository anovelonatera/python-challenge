# Unit 3 | Assignment - Py Me Up, Charlie (PyBank)

# Import Modules/Dependencies
import os
import csv

# Variables
total_months = 0
net_total_amount = 0
monthly_change = []
month_count = []
greatest_increase = 0
greatest_increase_month = 0
greatest_decrease = 0
greatest_decrease_month = 0

# Set Path For File

bank=os.path.join(".","resources","budget_data.csv")
with open(bank,"r",encoding="UTF-8") as csvfile:
    
    # CSV Reader Specifies Delimiter & Variable That Holds Contents
    csvreader = csv.reader(csvfile, delimiter=',')
    csv_header = next(csvreader)
    x = next(csvreader)
    
    # Calculate Total Number Of Months, Net Amount Of "Profit/Losses" & Set Variables For Rows
    prev_ = int(x[1])
    total_months += 1
    net_total_amount += int(x[1])
    greatest_increase = int(x[1])
    greatest_increase_month = x[0]
    
    # Read Each Row Of Data After The Header
    for x in csvreader:
        
        # Calculate Total Number Of Months Included In Dataset
        total_months += 1
        # Calculate Net Amount Of "Profit/Losses" Over The Entire Period
        net_total_amount += int(x[1])

        # Calculate Change From Current Month To Previous Month
        revenue_change = int(x[1]) - prev_
        monthly_change.append(revenue_change)
        prev_ = int(x[1])
        month_count.append(x[0])
        
        # Calculate The Greatest Increase
        if int(x[1]) > greatest_increase:
            greatest_increase = int(x[1])
            greatest_increase_month = x[0]
            
        # Calculate The Greatest Decrease
        if int(x[1]) < greatest_decrease:
            greatest_decrease = int(x[1])
            greatest_decrease_month = x[0]  
        
    # Calculate The Average & The Date
    average_change = sum(monthly_change)/ len(monthly_change)
    
    highest = max(monthly_change)
    lowest = min(monthly_change)

# Print Analysis
print(f"Financial Analysis")
print(f"---------------------------")
print(f"Total Months: {total_months}")
print(f"Total: ${net_total_amount}")
print(f"Average Change: ${average_change:.2f}")
print(f"Greatest Increase in Profits:, {greatest_increase_month}, (${highest})")
print(f"Greatest Decrease in Profits:, {greatest_decrease_month}, (${lowest})")

# Specify File To Write To
output_file = os.path.join('.', 'resources', 'budget_data_revised.text')

# Open File Using "Write" Mode. Specify The Variable To Hold The Contents
with open(output_file, 'w',) as txtfile:

# Write New Data
    txtfile.write(f"Financial Analysis\n")
    txtfile.write(f"---------------------------\n")
    txtfile.write(f"Total Months: {total_months}\n")
    txtfile.write(f"Total: ${net_total_amount}\n")
    txtfile.write(f"Average Change: ${average_change}\n")
    txtfile.write(f"Greatest Increase in Profits:, {greatest_increase_month}, (${highest})\n")
    txtfile.write(f"Greatest Decrease in Profits:, {greatest_decrease_month}, (${lowest})\n")