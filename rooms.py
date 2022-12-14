import random


rooms = []

with open("rooms.csv", encoding='utf-8-sig') as file:
    lines = file.readlines()
file.close()

for line in lines:
    rooms.append(line.split(","))

mobs = ["mob1", "mob2", "mob3", "mob4", "mob5", "mob6", "mob7", "mob8"] # mob names set to change

# what each index is:
# room name, room behind, room ahead (Empty is nothing ahead), [room to left, room to right] (0 for no rooms in hallway, list of one element means one room to left, no room to right), Items, Number of mobs in room, list of mobs in room (randomly selected from list of mobs)

for room in rooms:
    mob_count = room[-1]
    corridor_rooms = room[3]
    
    if '/' in mob_count:
        mob_number = mob_count.split("/")
        for i in range(len(mob_number)):
            mob_number[i] = int(mob_number[i])
        mob_count = random.choice(mob_number)
    else:
        mob_count = int(mob_count)
      
    if '|' in corridor_rooms:
        corridor_rooms = corridor_rooms.split("|")
        for i in range(len(corridor_rooms)):
            corridor_rooms[i] = int(corridor_rooms[i])
    else:
        try:
            corridor_rooms = int(corridor_rooms)
            if corridor_rooms > 0:
                corridor_rooms = [corridor_rooms]
        except:
            pass
    room[3] = corridor_rooms
    room[-1] = mob_count
    room[1] = int(room[1])
    try:
        room[2] = int(room[2])
    except:
        pass
    if room[-1]>0:
        room_mobs = random.sample(mobs, room[-1])
        if len(room_mobs)==1:
            room_mobs = room_mobs[0]
        room += [room_mobs]

print(rooms)