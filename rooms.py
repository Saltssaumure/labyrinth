import csv

with open('rooms.csv', newline='') as csvfile:
    rooms = list(csv.reader(csvfile))
rooms[0][0] = rooms[0][0].replace("\ufeff", '')
#print(rooms[int(rooms[10][1])])
print(rooms)

#room2 = {"next":None, "back":room1, "items":None, "name":2}
#start_room = {"next":None, "back":None, "items":None, "name":"start"}
#room1 = {"next":None, "back":start_room, "items":None, "name":1}
#room3 = {"next":None, "back":room2, "items":None, "name":3}
#room4 = {"next":None, "back":room3, "items":None, "name":4}
#room5 = {"next":None, "back":room4, "items":None, "name":5}
#room6 = {"next":None, "back":room5, "items":None, "name":6}
#room7 = {"next":None, "back":room6, "items":None, "name":7}
#room8 = {"next":None, "back":room7, "items":None, "name":8}
#room9 = {"next":None, "back":room8, "items":None, "name":9}
#room10 = {"next":None, "back":room9, "items":None, "name":10}
#bigger_room = {"next":None, "back":None, "items":None, "name":"big1"}
#bigger_room2 = {"next":None, "back":None, "items":"key", "name":"big2"}
#hidden_room = {"next":None, "back":None, "items":None, "name":"hidden"}
#end_room = {"next":"END", "back":None, "items":None, "name":"final"}
#rooms = [room1, room2, room3, room4, room5, room6, room7, room8, room9, room10, bigger_room, bigger_room2]

#start_room["next"] = room1
#room1["next"] = room2
#room2["next"] = room3
#room3["next"] = room4
#room4["next"] = room5
#room5["next"] = room6
#room6["next"] = room7
#room7["next"] = room8
#room8["next"] = room9
#room9["next"] = room10

current_room = rooms[0]

#print(current_room)