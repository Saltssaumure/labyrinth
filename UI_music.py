from multiprocessing.connection import wait
import tkinter as tk
from PIL import Image, ImageTk
if not hasattr(Image, 'Resampling'):  # Pillow<9.0
    Image.Resampling = Image
from rooms_dict import rooms
from imgs_dict import read_images
import random
import pygame

#initialise pygame
pygame.mixer.init()

inventory = []

jumpscares = ["images/jumpscares/clown.jpg", "images/jumpscares/ghost.jpg", 
              "images/jumpscares/ghost2.jpg", "images/jumpscares/undead.jpg", "images/jumpscares/undead2.jpg"]

#music functions
def background():
    if pygame.mixer.music.get_busy()==True:
        stop_song()
    pygame.mixer.music.load('audio/Background_music.mp3')
    pygame.mixer.music.play(-1)
    

def scream():
    if pygame.mixer.music.get_busy()==True:
        stop_song()
    pygame.mixer.music.load('audio/Scream_1.mp3')
    pygame.mixer.music.play()
    text_box.config(state="normal")
    text_box.delete(0.0, "end")
    text_box.insert("end", "You will die here.")
    text_box.config(state="disabled")
    pygame.mixer.music.queue('audio/Background_music.mp3', loops=-1)

def get_key():
    if pygame.mixer.music.get_busy()==True:
        stop_song()
    pygame.mixer.music.load('audio/Getting_Item.mp3')
    pygame.mixer.music.play()
    text_box.config(state="normal")
    text_box.delete(0.0, "end")
    text_box.insert("end", "You picked up a key.")
    text_box.config(state="disabled")
    pygame.mixer.music.queue('audio/Background_music.mp3', loops=-1)

def win_audio():
    if pygame.mixer.music.get_busy()==True:
        stop_song()
    pygame.mixer.music.load('audio/Winning_music.mp3')
    pygame.mixer.music.play()
    text_box.config(state="normal")
    text_box.delete(0.0, "end")
    text_box.insert("end", "You escaped the dungeon! You win! :)")
    text_box.config(state="disabled")
    pygame.mixer.music.queue('audio/Ending_Music.mp3', loops=-1)

def boss_music():
    if pygame.mixer.music.get_busy()==True:
        stop_song()
    pygame.mixer.music.load('audio/Boss_music.mp3')
    pygame.mixer.music.play(-1)

def stop_song():
    pygame.mixer.music.stop()
    pygame.mixer.music.unload()

#name behind next left right items mobs

cur_room = 34
dir = "R"

# root window
root = tk.Tk()
root.title('Labyrinth')
root["bg"] = "#333"

# Add None room to display image for rooms with no left/right path
rooms[None] = {"name": "eyes"}

imgs_dictionary_full = read_images(rooms, "name", "images/rooms/", ".jpg")
imgs_dictionary_left = read_images(rooms, "name", "images/rooms/", ".jpg", "left")
imgs_dictionary_right = read_images(rooms, "name", "images/rooms/", ".jpg", "right")

text_box = tk.Text(root, height=1, width=50)
text_box.grid(row=3, column=0, columnspan=3, pady=5)
text_box.insert("end", "Welcome to the Labyrinth.")
text_box.config(state="disabled")

panel = tk.Label(root, image = imgs_dictionary_full[cur_room], borderwidth=0)
panel.grid(row = 0, column=1, columnspan=1)
panelleft = tk.Label(root, image = imgs_dictionary_left[None], borderwidth=0)
panelleft.grid(row = 0, column=0, columnspan=1)
panelright = tk.Label(root, image = imgs_dictionary_right[None], borderwidth=0)
panelright.grid(row = 0, column=2, columnspan=1)


upCompass = Image.open("images/icons/compass.jpg")
upCompass = upCompass.resize((60, 60))
downCompass = upCompass.rotate(180)
leftCompass = upCompass.rotate(90)
rightCompass = upCompass.rotate(270)

compass = {}
compass["U"] = ImageTk.PhotoImage(upCompass)
compass["D"] = ImageTk.PhotoImage(downCompass)
compass["L"] = ImageTk.PhotoImage(leftCompass)
compass["R"] = ImageTk.PhotoImage(rightCompass)

panelCompass = tk.Label(root, image=compass[dir])
panelCompass.grid(row=2, column=2)

pickUpImg = Image.open("images/actions/pick_up.jpg")
pickUpImg = pickUpImg.resize((40, 40))

upImg = Image.open("images/actions/up.jpeg")
upImg = upImg.resize((40, 40))
downImg = upImg.rotate(180)
leftImg = upImg.rotate(90)
rightImg = upImg.rotate(270)

pickUpImgTK = ImageTk.PhotoImage(pickUpImg)

upImgTK = ImageTk.PhotoImage(upImg)
downImgTK = ImageTk.PhotoImage(downImg)
leftImgTK = ImageTk.PhotoImage(leftImg)
rightImgTK = ImageTk.PhotoImage(rightImg)

imgTest = Image.open("images/rooms/" + rooms[cur_room]["name"] + ".jpg")
imgTest = imgTest.resize((500, 500), Image.Resampling.LANCZOS)
imgTestTk = ImageTk.PhotoImage(imgTest)

#pass through variable here to change image
def newArea(room_index):
    global panel
    global panelleft
    global panelright
    global panelCompass
    global rooms
    print(rooms[room_index]["name"])

    if rooms[room_index]["name"]=="boss_room":
        boss_music()
    elif rooms[room_index]["name"]=="crdr_14" or rooms[room_index]["name"]=="escape":
        background()
    panel = tk.Label(root, image=imgTestTk)

    panelCompass.grid_forget()
    panelCompass = tk.Label(root,image=compass[rooms[room_index]["dir"]])
    panelCompass.grid(row=2,column=2)

    panel.grid_forget()
    panel = tk.Label(root,image=imgs_dictionary_full[room_index], borderwidth=0)
    panel.grid(row=0,column=1,columnspan=1)
    panelleft.grid_forget()
    panelleft = tk.Label(root,image=imgs_dictionary_left[rooms[room_index]["left"]], borderwidth=0)
    panelleft.grid(row=0,column=0,columnspan=1)
    panelright.grid_forget()
    panelright = tk.Label(root,image=imgs_dictionary_right[rooms[room_index]["right"]], borderwidth=0)
    panelright.grid(row=0,column=2,columnspan=1)

    text_box.config(state="normal")
    text_box.delete(0.0, "end")
    text_box.insert("end", "You move to a new area.")
    text_box.config(state="disabled")

def nothingHere():
    text_box.config(state="normal")
    text_box.delete(0.0, "end")
    text_box.insert("end", "There is nothing here.")
    text_box.config(state="disabled")

def move(direction):
    global panel
    global cur_room
    scream_time = random.randrange(1,30)
    if rooms[cur_room]["name"]=="escape" and direction=="next":
        win()
    else:
        if rooms[cur_room][direction] != None:
            panel.grid_forget()
            newArea(rooms[cur_room][direction])
            cur_room = rooms[cur_room][direction]
        else:
            nothingHere()
        if rooms[cur_room]["name"]=="boss_room" or rooms[cur_room]["name"]=="escape":
            pass
        else:
            if scream_time%15==0:
                scream()

def pick_up():
    if rooms[cur_room]["items"]==None:
        text_box.config(state="normal")
        text_box.delete(0.0, "end")
        text_box.insert("end", "There are no items here.")
        text_box.config(state="disabled")
    else:
        rooms[cur_room]["items"] = None
        get_key()
        inventory += ["key"]

def win():
    forward_button.configure(command=None)
    down_button.configure(command=None)
    left_button.configure(command=None)
    right_button.configure(command=None)
    pick_up_button.configure(command=None)
    win_audio()

# exit button
forward_button = tk.Button(root, image=upImgTK, command=lambda:move("next"))
forward_button.grid(row=1, column=1, padx=5, pady=5)

down_button = tk.Button(root, image=downImgTK, command=lambda:move("behind"))
down_button.grid(row=2, column=1, padx=5, pady=5)

left_button = tk.Button(root, image=leftImgTK, command=lambda:move("left"))
left_button.grid(row=1, column=0, padx=5, pady=5)

right_button = tk.Button(root, image=rightImgTK, command=lambda:move("right"))
right_button.grid(row=1, column=2, padx=5, pady=5)

pick_up_button = tk.Button(root, image=pickUpImgTK, command=lambda:pick_up())
pick_up_button.grid(row=2, column=0, padx=5, pady=5)

background()

root.mainloop()

pygame.quit()