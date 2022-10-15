import random

mobs = ["mob1", "mob2", "mob3", "mob4", "mob5", "mob6", "mob7", "mob8"] # mob names set to change

with open("rooms.csv", encoding='utf-8-sig') as file:
    rooms_list = [line.split(",") for line in file.readlines()]

rooms = {}
for idx,room in enumerate(rooms_list):
    rooms[idx] = {
        "name": room[0],
        "behind": int(room[1]),
        "next": int(room[2]) if room[2] != "None"  and room[2] != "END" else None,
        "left": int(room[3]) if room[3] != "None" else None,
        "right": int(room[4]) if room[4] != "None" else None,
        "items": room[5] if room[5] != "None" else None,
        "mobs": [mobs[random.randint(0,7)] for x in range(random.randint(int(room[6].strip().split("/")[0]), int(room[6].strip().split("/")[1])))]
    }