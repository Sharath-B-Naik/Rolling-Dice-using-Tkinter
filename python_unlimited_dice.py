
from tkinter import *
from PIL import Image, ImageTk
import random

root = Tk()
root.geometry('400x400')
root.title('Data Flair Roll the Dice')
l0 = Label(root, text="")
l0.pack()
l1 = Label(root, text="Roll Dice from Python Unlimited",  font = "times 16 bold")
l1.pack()
dice = ['die1.png', 'die2.png', 'die3.png', 'die4.png', 'die5.png', 'die6.png']
image1 = ImageTk.PhotoImage(Image.open(random.choice(dice)))
label1 = Label(root, image=image1)
label1.pack( expand=True)

def rolling_dice():
    image1 = ImageTk.PhotoImage(Image.open(random.choice(dice)))
    label1.configure(image=image1)
    label1.image = image1

label2 = Label(text = "Made by @Python_Unlimited", font = ("times", 10, "bold"))
label2.pack(expand = 1)

btn = Button(root, text='Roll the Dice', fg='blue', command=rolling_dice)
btn.pack( expand=True)
root.mainloop()

