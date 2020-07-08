# Modules
import os
import csv


# Set path for file 
csvpath = os.path.join("..", "Pybank", "budget_data.csv")

#Open the CSV
with open(csvpath, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    # Loop through the budget to find the total months
    months = len(list(csvreader))-1 

# --------------------------------------------------------------------

#Find net total amount of "Profit/Losses" over the entire period

import csv
with open('budget_data.csv', 'r') as f:
    next(f)
    total = 0
    previous = 0
    change = 0 
    average_list = []
    increase_list = ["", 0]
    decrease_list = ["", 9999]

    for row in csv.reader(f):
        total += int(row[1])
        change = int(row[1])-previous
        average_list.append(change)
        previous = int(row[1])
        if change > increase_list[1]:
            increase_list[0] = row[0]
            increase_list[1] = change 
            # print(increase_list)

        if change < decrease_list[1]:
            decrease_list[0] = row[0]
            decrease_list[1] = change 
            # print(decrease_list)

    average = sum(average_list[1:]) / (len(average_list)-1)
    print("Financial Analysis")
    print("--------------------")
    print("Total Months: " + str(months))
    print('The total is ${}'.format(total))
    print('The average is ${}'.format(round(average, 2)))
    print(f'Greatest Increase in Profits: {increase_list[0]} ${increase_list[1]}')
    print(f'Greatest Decrease in Profits: {decrease_list[0]} ${decrease_list[1]}')
   
   
    outF = open("pybank.txt", "w")
    outF.writelines("Financial Analysis")
    outF.writelines("\n")
    outF.writelines("--------------------")
    outF.writelines("\n")
    outF.writelines("Total Months: " + str(months))
    outF.writelines("\n")
    outF.writelines('The total is ${}'.format(total))
    outF.writelines("\n")
    outF.writelines('The average is ${}'.format(round(average, 2)))
    outF.writelines("\n")
    outF.writelines(f'Greatest Increase in Profits: {increase_list[0]} ${increase_list[1]}')
    outF.writelines("\n")
    outF.writelines(f'Greatest Decrease in Profits: {decrease_list[0]} ${decrease_list[1]}')
    outF.writelines("\n")
    outF.writelines("--------------------")
    outF.close()