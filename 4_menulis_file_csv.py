from asyncore import write
import csv

rows = [
    {'nama': 'Naruto','skill': 'punch','power': 100,},
    {'nama': 'Lee','skill': 'kick','power': 100,},
    {'nama': 'Narto','skill': 'kick','power': 100,}
]

with open('newDate.csv', 'a') as csvfile:
    fields = ['nama', 'skill', 'power']
    writer = csv.DictWriter(csvfile, fieldnames= fields)


    writer.writeheader()
    # writer.writeheader({
    #     'nama': 'tes',
    #     'skill': 'kick',
    #     'power': 100,
    # })
    writer.writerows(rows)