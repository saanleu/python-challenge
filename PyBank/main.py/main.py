import os
import csv

budget__csv = os.path.join("..","Resources", "budget_data.csv")

with open(budget__csv, encoding ="utf-8") as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=",")

    csv_header = next(csv_reader)
    csv_first = next(csv_reader)

    months = 1
    netTotal = int(csv_first[1])
    bevalue = int(csv_first[1])

    
    valChanges = []
    gIncr = 0 
    gDecr = 0

    for row in csv_reader:
        months = months + 1
        netTotal = netTotal + int(row[1])
    
        change = int(row[1]) - bevalue 
        valChanges.append(change)
        bevalue = int(row[1])

        if change < gDecr:
            gDecr = change 
            gD_month = row[0]
        
        if change > gIncr:
            gIncr = change
            gI_month = row[0]
    
    def avg(list):
        return sum(list)/len(list)
    average = avg(valChanges)
    roundedavg = round(average, 2)

    finance_file = os.path.join("..","analysis", "finance.txt")
    fin_out = (
        f"Financial Analysis\n"
        f"----------------------------\n"
        f"Total Months: {months}\n"
        f"Total: ${netTotal}\n"
        f"Average Change: ${roundedavg}\n"
        f"Greatest Increase in Profits: {gI_month} (${gIncr})\n"
        f"Greatest Decrease in Profits: {gD_month} (${gDecr})\n"

    )
    print(fin_out)

    with open(finance_file, "w") as txt_file:
        txt_file.write(fin_out)