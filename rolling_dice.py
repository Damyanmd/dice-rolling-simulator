from tkinter import *
from PIL import Image, ImageTk
import random

#creating the window
root = Tk()
root.geometry('400x400')
root.title('Dice Rolling Simulator')
root.resizable(0, 0)

#function for the button
def rolling_dice():
    image1 = ImageTk.PhotoImage(Image.open(random.choice(dice)))
    shown_image.configure(image=image1)
    shown_image.image = image1

#choosing and importing images
#IMPORTANT IMAGES SHOULD BE IN THE THE SAME FOLDER WITH THE CODE FOR IT TO WORK
dice = ['dice1.png', 'dice2.png', 'dice3.png', 'dice4.png', 'dice5.png', 'dice6.png']
random_image = ImageTk.PhotoImage(Image.open(random.choice(dice)))

shown_image = Label(root, image=random_image)
shown_image.image = random_image
shown_image.pack(expand=True)

button = Button(root, text='Roll the Dice',  font='arial 15 bold', bg='white smoke', fg='red2', command=rolling_dice).pack(expand=True)

root.mainloop()
