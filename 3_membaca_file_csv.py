import csv


rows =[]

with open('MOCK_DATA.csv', 'r') as csvfile:
    csvreader = csv.DictReader(csvfile)
    # for row in csvreader:
    #     rows.append(row)
    #bisajuga pake list
    rows = list(csvreader)
    print('total baris : ', csvreader.line_num)


for row in rows[:10]:
    print(row['id'] + " - " + row['first_name'] + " - " + row['email'])

# print(rows)