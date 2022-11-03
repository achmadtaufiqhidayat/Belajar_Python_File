import json
#menulis file json
# data ={}
# data['member'] = [
#     {'nama': 'Naruto','skill': 'punch','power': 100,},
#     {'nama': 'Lee','skill': 'kick','power': 100,},
#     {'nama': 'Narto','skill': 'kick','power': 100,}
# ]

# with open('memberfile.json', 'w') as memberfile:
#     json.dump(data,memberfile)


#membaca file json

with open('memberfile.json', 'r') as memberfile:
    data = json.load(memberfile)

    for member in data['member']:
        print("Namanya " + member['nama'] + " punya skill " + member['skill'] + " dengan power " + str(member['power']))