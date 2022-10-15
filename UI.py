from multiprocessing.connection import wait
import tkinter as tk
from PIL import Image, ImageTk
if not hasattr(Image, 'Resampling'):  # Pillow<9.0
    Image.Resampling = Image
from rooms_dict import rooms

# Add None room to display image for rooms with no left/right path
rooms[None] = {"name": "eyes"}
# Add END room to display image for winning :)
rooms["END"] = {"name": "eyes"}

#image crop functions
def getfilename(name):
    return "images/rooms/" + name + ".jpg"

def resize(filename):
    return Image.open(filename).resize((500, 500),Image.Resampling.LANCZOS)

def leftcrop(filename):
    return resize(filename).crop([400,0,500,500])

def rightcrop(filename):
    return resize(filename).crop([0,0,100,500])

# update images to show for currrent room function
def updateimgs(cur_room):
    imgCentre = resize(getfilename( rooms[cur_room]["name"] ))
    imgCentreTk = ImageTk.PhotoImage(imgCentre)

    imgLeft = leftcrop(getfilename( rooms[rooms[cur_room]["left"]]["name"] ))
    imgLeftTk = ImageTk.PhotoImage(imgLeft)

    imgRight = rightcrop(getfilename( rooms[rooms[cur_room]["right"]]["name"] ))
    imgRightTk = ImageTk.PhotoImage(imgRight)

    return imgCentreTk, imgLeftTk, imgRightTk

#print(rooms)
#name behind next left right items mobs

cur_room = 0

# root window
root = tk.Tk()
root.title('Labyrinth')
root["bg"] = "#333"

text_box = tk.Text(root, height=1, width=50)
text_box.grid(row=3, column=0, columnspan=3, pady=5)
text_box.insert("end", "Welcome to the Labyrinth.")
text_box.config(state="disabled")

# initial panels
imgCentreTk, imgLeftTk, imgRightTk = updateimgs(cur_room)

panel = tk.Label(root, image = imgCentreTk, borderwidth=0)
panel.grid(row = 0, column=1, columnspan=1)

leftPanel = tk.Label(root, image = imgLeftTk, borderwidth=0)
leftPanel.grid(row = 0, column=0, columnspan=1)

rightPanel = tk.Label(root, image = imgRightTk, borderwidth=0)
rightPanel.grid(row = 0, column=2, columnspan=1)

# button images
upImg = Image.open("images/actions/up.jpeg")
upImg = upImg.resize((40, 40))
downImg = upImg.rotate(180)
leftImg = upImg.rotate(90)
rightImg = upImg.rotate(270)

upImgTK = ImageTk.PhotoImage(upImg)
downImgTK = ImageTk.PhotoImage(downImg)
leftImgTK = ImageTk.PhotoImage(leftImg)
rightImgTK = ImageTk.PhotoImage(rightImg)

imgTest = Image.open(getfilename( rooms[cur_room]["name"] ))
imgTest = imgTest.resize((500, 500), Image.Resampling.LANCZOS)
imgTestTk = ImageTk.PhotoImage(imgTest)

#pass through variable here to change image
def newArea(cur_room):
    updateimgs(cur_room)

    panel = tk.Label(root, image = imgCentreTk, borderwidth=0)
    panel.grid(row = 0, column=1, columnspan=1)
    leftPanel = tk.Label(root, image = imgLeftTk, borderwidth=0)
    leftPanel.grid(row = 0, column=0, columnspan=1)
    rightPanel = tk.Label(root, image = imgRightTk, borderwidth=0)
    rightPanel.grid(row = 0, column=2, columnspan=1)

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
    global panel, leftPanel, rightPanel
    global cur_room
    if rooms[cur_room][direction] != None:
        cur_room = rooms[cur_room][direction]
        panel.grid_forget()
        leftPanel.grid_forget()
        rightPanel.grid_forget()
        newArea(cur_room)
    else:
        nothingHere()




# exit button
forward_button = tk.Button(root, image=upImgTK, command=lambda:move("next"))
forward_button.grid(row=1, column=1, padx=5, pady=5)

down_button = tk.Button(root, image=downImgTK, command=lambda:move("behind"))
down_button.grid(row=2, column=1, padx=5, pady=5)

left_button = tk.Button(root, image=leftImgTK, command=lambda:move("left"))
left_button.grid(row=1, column=0, padx=5, pady=5)

right_button = tk.Button(root, image=rightImgTK, command=lambda:move("right"))
right_button.grid(row=1, column=2, padx=5, pady=5)

root.mainloop()