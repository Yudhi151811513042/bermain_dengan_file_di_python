import csv

rows = []

with open('MOCK_DATA.csv', 'r') as csvfile:
    csvreader = csv.reader(csvfile)
    """for row in csvreader:
        rows.append(row)"""
    rows = list(csvreader)
    print('total baris : ' , csvreader.line_num)

for row in rows:
    print(row[0] + ' - ' + row[1])