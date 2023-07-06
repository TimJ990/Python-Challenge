import csv
import os

budget_file = r"C:\Users\Tim\DataCourse\HW\Python-Challenge\PyBank\Resources\budget_data.csv"
with open (budget_file) as csvfile :
    # create csv reader
    csvreader = csv.reader (csvfile, delimiter = ",")

    # init vars
    rowcount = 0
    monthlyoutcome = 0
    diff_list = []

    # greatest incr and decr vars (value and month)
    greatest_incr = 0
    greatest_decr = 0
    greatest_incr_month = None
    greatest_decr_month = None
    
    # read header from first row
    header = next (csvreader)

    # read first month data -> prev_pnl
    first_row = next (csvreader)  # ["month", "pnl"]
    rowcount = rowcount + 1
    prev_pnl = float(first_row [1])
    monthlyoutcome = prev_pnl
  
    # loop through the csv file row by row
    for row in csvreader :
        rowcount = rowcount + 1
        curr_pnl = float(row[1])
        monthlyoutcome =  monthlyoutcome + curr_pnl 

        # find diff between current and prev pnl
        diff_pnl = curr_pnl - prev_pnl 
        prev_pnl = curr_pnl

        # add diff to diff list
        diff_list.append (diff_pnl)
    
        # if diff pnl > 0 update greatest incr if nec
        if diff_pnl > greatest_incr: 
            greatest_incr = diff_pnl
            greatest_incr_month = row[0]
        # if diff pnl < 0 update greatest decr if nec
        if diff_pnl < greatest_decr: 
            greatest_decr = diff_pnl
            greatest_decr_month = row[0]

# outputs
out = f"Total Months: {rowcount}\n" +\
    f"Total: ${monthlyoutcome:,}\n" +\
    f"Average Change: ${sum(diff_list)/len(diff_list):,.2f}\n" +\
    f"Greatest Increase: {greatest_incr_month} (${greatest_incr:,})\n" +\
    f"Greatest Decrease: {greatest_decr_month} (${greatest_decr:,})\n"

print(out)

# Export to analysis
with open("PyBank/Analysis/PyBankAnalysis.txt", 'w') as fout:
    fout.write(out)
