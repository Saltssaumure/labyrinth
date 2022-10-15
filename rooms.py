import csv
import random

with open('rooms.csv', newline='') as csvfile:
    rooms = list(csv.reader(csvfile))
rooms[0][0] = rooms[0][0].replace("\ufeff", '')

for room in rooms:
    print(room)
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
    print(room)
    print()

current_room = rooms[0]