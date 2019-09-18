
import os
import csv

total_months = 0
net_total_amount = 0
monthly_change = []
month_count = []
greatest_increase = 0
greatest_increase_month = 0
greatest_decrease = 0
greatest_decrease_month = 0

bank=os.path.join(".","resources","budget_data.csv")
with open(bank,"r",encoding="UTF-8") as csvfile:
    
    csvreader = csv.reader(csvfile, delimiter=',')
    csv_header = next(csvreader)
    x = next(csvreader)
    
    prev_ = int(x[1])
    total_months += 1
    net_total_amount += int(x[1])
    greatest_increase = int(x[1])
    greatest_increase_month = x[0]
    
    for x in csvreader:
        
        total_months += 1
        net_total_amount += int(x[1])

        revenue_change = int(x[1]) - prev_
        monthly_change.append(revenue_change)
        prev_ = int(x[1])
        month_count.append(x[0])
        
        if int(x[1]) > greatest_increase:
            greatest_increase = int(x[1])
            greatest_increase_month = x[0]
            
        if int(x[1]) < greatest_decrease:
            greatest_decrease = int(x[1])
            greatest_decrease_month = x[0]  
        
    average_change = sum(monthly_change)/ len(monthly_change)
    
    highest = max(monthly_change)
    lowest = min(monthly_change)

print(f"Financial Analysis")
print(f"---------------------------")
print(f"Total Months: {total_months}")
print(f"Total: ${net_total_amount}")
print(f"Average Change: ${average_change:.2f}")
print(f"Greatest Increase in Profits:, {greatest_increase_month}, (${highest})")
print(f"Greatest Decrease in Profits:, {greatest_decrease_month}, (${lowest})")

output_file = os.path.join('.', 'resources', 'budget_data_output.txt')
with open(output_file, 'w',) as txtfile:

    txtfile.write(f"Financial Analysis\n")
    txtfile.write(f"---------------------------\n")
    txtfile.write(f"Total Months: {total_months}\n")
    txtfile.write(f"Total: ${net_total_amount}\n")
    txtfile.write(f"Average Change: ${average_change}\n")
    txtfile.write(f"Greatest Increase in Profits:, {greatest_increase_month}, (${highest})\n")
    txtfile.write(f"Greatest Decrease in Profits:, {greatest_decrease_month}, (${lowest})\n")