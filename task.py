import csv
from beautifultable import BeautifulTable
table = BeautifulTable()
file = "task.csv"

with open(file,'r') as csvfile:
    csvreader = csv.reader(csvfile)
    table.column_headers=(next(csvreader))
    # extracting each data row one by one
    for row in csvreader:
        row[2]=("$"+row[2])
        table.append_row(row)

    print(table)
    
