import csv

row = [
    {'nama': 'jacklee', 'skill': 'tendangan beracun', 'power': 100},
    {'nama': 'yip', 'skill': 'wingchun', 'power': 1000},
    {'nama': 'songoku', 'skill': 'kamehameha', 'power': 1000}]

with open('data.csv', 'a') as csvfile:
    fields = ['nama', 'skill', 'power']
    writer = csv.DictWriter(csvfile, fieldnames=fields)

    writer.writeheader()
    writer.writerows(row)