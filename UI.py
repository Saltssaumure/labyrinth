from multiprocessing.connection import wait
import tkinter as tk
from PIL import Image, ImageTk
if not hasattr(Image, 'Resampling'):  # Pillow<9.0
    Image.Resampling = Image
from rooms_dict import rooms

#print(rooms)
#name behind next left right items mobs

cur_room = 0

# root window
root = tk.Tk()
root.title('Labyrinth')

text_box = tk.Text(root, height=1, width=50)
text_box.grid(row=3, column=0, columnspan=3, pady=5)
text_box.insert("end", "Welcome to the Labyrinth.")
text_box.config(state="disabled")

testImg2 = Image.open("images/rooms/" + rooms[cur_room]["name"] + ".jpeg")
testImg2 = testImg2.resize((500, 500), Image.Resampling.LANCZOS)
testImgTk2 = ImageTk.PhotoImage(testImg2)

"""
testImg = Image.open("images/test.png")
testImg = testImg.resize((500, 500), Image.Resampling.LANCZOS)
testImgTk = ImageTk.PhotoImage(testImg)
"""
panel = tk.Label(root, image = testImgTk2)
panel.grid(row = 0, column=0, columnspan=3)


upImg = Image.open("images/actions/up.jpeg")
upImg = upImg.resize((40, 40))
downImg = upImg.rotate(180)
leftImg = upImg.rotate(90)
rightImg = upImg.rotate(270)

upImgTK = ImageTk.PhotoImage(upImg)
downImgTK = ImageTk.PhotoImage(downImg)
leftImgTK = ImageTk.PhotoImage(leftImg)
rightImgTK = ImageTk.PhotoImage(rightImg)

imgTest = Image.open("images/rooms/" + rooms[cur_room]["name"] + ".jpeg")
imgTest = imgTest.resize((500, 500), Image.Resampling.LANCZOS)
imgTestTk = ImageTk.PhotoImage(imgTest)

imgTest = Image.open("images/rooms/" + rooms[cur_room]["name"] + ".jpeg")
imgTest = imgTest.resize((500, 500), Image.Resampling.LANCZOS)
imgTestTk = ImageTk.PhotoImage(imgTest)

#pass through variable here to change image
def newArea():
    panel = tk.Label(root, image=imgTestTk)
    panel.grid(row=0,column=0,columnspan=3)

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
    if rooms[cur_room][direction] != None:
        cur_room = rooms[cur_room][direction]
        panel.grid_forget()
        newArea()
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