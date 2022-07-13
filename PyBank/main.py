# Creating the file
import os
import csv

filepath = os.path.join('.', 'Resources', 'budget_data.csv')

# Creating list to store data 
budgetdata = []

# Opening the CSV
with open(filepath) as csvfile:
    reader = csv.DictReader(csvfile)

    for row in reader:
        budgetdata.append({"month": row["Date"], "amount": int(row["Profit/Losses"]),"change": 0})

# Calculating the total months
totalmonths = len(budgetdata)

previousamount = budgetdata[0]["amount"]
for i in range(totalmonths):
    budgetdata[i]["change"] = budgetdata[i]["amount"] - previousamount
    prevamount = budgetdata[i]["amount"]

# Calculating the total amount
totalamount = sum(row['amount'] for row in budgetdata) 

# Calculating the average of amount changes
totalchange = sum(row['change'] for row in budgetdata)
average = round(totalchange / (totalmonths-1), 2)

# Getting the  Greatest Increase and Decrease from the changes
getincrease = max(budgetdata, key=lambda x:x['change'])
getdecrease = min(budgetdata, key=lambda x:x['change'])


# Printing the Final Analysis
print('Financial Analysis')
print('----------------------------')
print(f'Total Months: {totalmonths}')
print(f'Total: ${totalamount}')
print(f'Average Change: ${average}')
print(f'Greatest Increase in Profits: {getincrease["month"]} (${getincrease["change"]})')
print(f'Greatest Decrease in Profits: {getdecrease["month"]} (${getdecrease["change"]})')


# Printting  the Final analysis and exporting to a text file 
# Set path for file
filepath = os.path.join('.', 'analysis', 'PyBank_Results.txt')
with open(filepath, "w") as text_file:
    print('Financial Analysis', file=text_file)
    print('----------------------------', file=text_file)
    print(f'Total Months: {totalmonths}', file=text_file)
    print(f'Total: ${totalamount}', file=text_file)
    print(f'Average Change: ${average}', file=text_file)
    print(f'Greatest Increase in Profits: {getincrease["month"]} (${getincrease["change"]})', file=text_file)
    print(f'Greatest Decrease in Profits: {getdecrease["month"]} (${getdecrease["change"]})', file=text_file)