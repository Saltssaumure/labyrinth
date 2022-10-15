import csv
import random

with open('rooms.csv', newline='') as csvfile:
    rooms = list(csv.reader(csvfile))
rooms[0][0] = rooms[0][0].replace("\ufeff", '')

mobs = ["mob1", "mob2", "mob3", "mob4", "mob5", "mob6", "mob7", "mob8"] # mob names set to change

for room in rooms:
    mob_count = room[-1]
    
    if '/' in mob_count:
        mob_number = mob_count.split("/")
        for i in range(len(mob_number)):
            mob_number[i] = int(mob_number[i])
        mob_count = random.choice(mob_number)
    else:
        mob_count = int(mob_count)
    room[-1] = mob_count
    room[1] = int(room[1])
    room[-2] = int(room[-2])
    if room[-1]>0:
        room += [random.sample(mobs, room[-1])]

#print(rooms)

current_room = rooms[0]