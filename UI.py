from ast import Delete
from multiprocessing.connection import wait
import tkinter as tk
from turtle import width
from PIL import Image, ImageTk

cur_room = "start_room"

# root window
root = tk.Tk()
root.title('Labyrinth')

text_box = tk.Text(root, height=1, width=50)
text_box.grid(row=2, column=0, columnspan=3, pady=5)
text_box.insert("end", "Welcome to the Labyrinth.")
#text_box.delete(0.0, "end")
text_box.config(state="disabled")

testImg2 = Image.open("images/test2.png")
testImg2 = testImg2.resize((500, 500), Image.Resampling.LANCZOS)
testImgTk2 = ImageTk.PhotoImage(testImg2)

testImg = Image.open("images/test.png")
testImg = testImg.resize((500, 500), Image.Resampling.LANCZOS)
testImgTk = ImageTk.PhotoImage(testImg)
panel = tk.Label(root, image = testImgTk)
panel.grid(row = 0, column=0, columnspan=3)


upImg = Image.open("images/actions/up.jpeg")
upImg = upImg.resize((40, 40))
leftImg = upImg.rotate(90)
rightImg = upImg.rotate(270)

upImgTK = ImageTk.PhotoImage(upImg)
leftImgTK = ImageTk.PhotoImage(leftImg)
rightImgTK = ImageTk.PhotoImage(rightImg)

def forward():
    global panel
    global img_num
    if img_num == 0:
        panel.grid_forget()
        panel = tk.Label(root, image=testImgTk2)
        panel.grid(row=0,column=0,columnspan=3)
        img_num+=1
    else:
        panel.grid_forget()
        panel = tk.Label(root, image=testImgTk)
        panel.grid(row=0,column=0,columnspan=3)
        img_num=0
        
# exit button
forward_button = tk.Button(root, image=upImgTK, command=lambda: root.quit())
forward_button.grid(row=1, column=1, padx=5, pady=5)

left_button = tk.Button(root, image=leftImgTK, command=lambda: root.quit())
left_button.grid(row=1, column=0, padx=5, pady=5)

right_button = tk.Button(root, image=rightImgTK, command=forward)
right_button.grid(row=1, column=2, padx=5, pady=5)

root.mainloop()