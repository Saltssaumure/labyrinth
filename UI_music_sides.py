from multiprocessing.connection import wait
import tkinter as tk
from PIL import Image, ImageTk, ImageEnhance
if not hasattr(Image, 'Resampling'):  # Pillow<9.0
    Image.Resampling = Image
from rooms_dict import rooms
import pygame

#image crop functions
def resize(filename):
    return Image.open(filename).resize((500, 500),Image.Resampling.LANCZOS)

def leftcrop(filename):
    return resize(filename).crop([400,0,500,500])

def rightcrop(filename):
    return resize(filename).crop([0,0,100,500])

#initialise pygame
pygame.mixer.init()

#name behind next left right items mobs

cur_room = 0

# root window
root = tk.Tk()
root.title('Labyrinth')
root["bg"] = "#333"

text_box = tk.Text(root, height=1, width=50)
text_box.grid(row=2, column=0, columnspan=3, pady=5)
text_box.insert("end", "Welcome to the Labyrinth.")
text_box.config(state="disabled")

testImg2 = Image.open("images/rooms/" + rooms[cur_room]["name"] + ".jpeg")
testImg2 = testImg2.resize((500, 500), Image.Resampling.LANCZOS)
testImgTk2 = ImageTk.PhotoImage(testImg2)

# imgLeft = testImg2.crop([500, 0, 100, 500])
imgLeft = leftcrop("images/rooms/keyRoom3.jpg") # placeholder image
imgLeftTk = ImageTk.PhotoImage(imgLeft)

imgRight = rightcrop("images/rooms/keyRoom.jpg") # placeholder image
imgRightTk = ImageTk.PhotoImage(imgRight)

"""
testImg = Image.open("images/test.png")
testImg = testImg.resize((500, 500), Image.Resampling.LANCZOS)
testImgTk = ImageTk.PhotoImage(testImg)
"""
panel = tk.Label(root, image = testImgTk2, borderwidth=0)
panel.grid(row = 0, column=1, columnspan=1)

leftPanel = tk.Label(root, image = imgLeftTk, borderwidth=0)
leftPanel.grid(row = 0, column=0, columnspan=1)

rightPanel = tk.Label(root, image = imgRightTk, borderwidth=0)
rightPanel.grid(row = 0, column=2, columnspan=1)


upImg = Image.open("images/actions/up.jpeg")
upImg = upImg.resize((40, 40))
leftImg = upImg.rotate(90)
rightImg = upImg.rotate(270)

upImgTK = ImageTk.PhotoImage(upImg)
leftImgTK = ImageTk.PhotoImage(leftImg)
rightImgTK = ImageTk.PhotoImage(rightImg)

imgTest = Image.open("images/rooms/" + rooms[cur_room]["name"] + ".jpeg")
imgTest = imgTest.resize((500, 500), Image.Resampling.LANCZOS)
imgTestTk = ImageTk.PhotoImage(imgTest)

# imgTest = Image.open("images/rooms/" + rooms[cur_room]["name"] + ".jpeg")
# imgTest = imgTest.resize((500, 500), Image.Resampling.LANCZOS)
# imgTestTk = ImageTk.PhotoImage(imgTest)

#music functions
def background():
    pygame.mixer.music.load('audio/Background_music.mp3')
    pygame.mixer.music.play()

def scream():
    pygame.mixer.music.load('audio/Scream_1.mp3')
    pygame.mixer.music.play()

def get_item():
    pygame.mixer.music.load('audio/.mp3')
    pygame.mixer.music.play()
    
def stop_song():
    pygame.mixer.music.stop()
    pygame.mixer.music.unload()

def forward():
    global panel
    global cur_room

    if rooms[cur_room]["next"] != None:
        cur_room = rooms[cur_room]["next"]
        panel.grid_forget()
        panel = tk.Label(root, image=imgTestTk)
        panel.grid(row=0,column=0,columnspan=3)

        text_box.config(state="normal")
        text_box.delete(0.0, "end")
        text_box.insert("end", "You move to a new area.")
        text_box.config(state="disabled")
    else:
        text_box.config(state="normal")
        text_box.delete(0.0, "end")
        text_box.insert("end", "There is nothing here.")
        text_box.config(state="disabled")

        
# exit button
forward_button = tk.Button(root, image=upImgTK, command=forward)
forward_button.grid(row=1, column=1, padx=5, pady=5)

left_button = tk.Button(root, image=leftImgTK, command=lambda: root.quit())
left_button.grid(row=1, column=0, padx=5, pady=5)

right_button = tk.Button(root, image=rightImgTK, command=lambda: root.quit())
right_button.grid(row=1, column=2, padx=5, pady=5)

background()

root.mainloop()