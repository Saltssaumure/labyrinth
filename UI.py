import tkinter as tk
from tkinter import ttk, PhotoImage
from PIL import Image, ImageTk


# root window
root = tk.Tk()
root.geometry('900x900')
root.resizable(False, False)
root.title('Labyrinth')


upImg = Image.open("up.png")

upImg = upImg.resize((20, 20))

leftImg = upImg.rotate(90)

rightImg = upImg.rotate(270)

upImgTK = ImageTk.PhotoImage(upImg)
leftImgTK = ImageTk.PhotoImage(leftImg)
rightImgTK = ImageTk.PhotoImage(rightImg)

# exit button
forward_button = ttk.Button(
    root,
    image=upImgTK,
    command=lambda: root.quit()
)

left_button = ttk.Button(
    root,
    image=leftImgTK,
    command=lambda: root.quit()
)

right_button = ttk.Button(
    root,
    image=rightImgTK,
    command=lambda: root.quit()
)

forward_button.place(x=400,y=800, width=50, height=50)
left_button.place(x=100,y=800, width=50, height=50)
right_button.place(x=700,y=800, width=50, height=50)

root.mainloop()