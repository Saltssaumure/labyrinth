import tkinter as tk
from tkinter import ttk, PhotoImage
from PIL import Image, ImageTk
import os

dir_path = os.path.dirname(os.path.realpath(__file__))

img_num = 0

# root window
root = tk.Tk()
root.title('Labyrinth')

testImg2 = Image.open("test2.png")
testImg2 = testImg2.resize((500, 500), Image.ANTIALIAS)
testImgTk2 = ImageTk.PhotoImage(testImg2)

testImg = Image.open("test.png")
testImg = testImg.resize((500, 500), Image.ANTIALIAS)
testImgTk = ImageTk.PhotoImage(testImg)
panel = tk.Label(root, image = testImgTk)
panel.grid(row = 0, column=0, columnspan=3)


upImg = Image.open(dir_path+"/images/actions/up.jpeg")
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