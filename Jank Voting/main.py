# Imports

import webbrowser
from tkinter import *
import tkinter
from PIL import Image, ImageTk
from datetime import datetime


# Functions

# This stuff executes when you click the continue button


def start():
    continue_button.destroy()
    main.destroy()

    vote = Canvas(root, width=screen_width / 2, height=screen_height / 15, bg='#1c1c26')
    vote.pack()

    vote.create_text(screen_width / 4, screen_height / 30, text='Who will you vote?', fill='white',
                     font=('San Francisco', int(screen_height / 30)))

    cat = tkinter.Button(root, image=img1,
                         command=lambda: [vote_event('Cat'), cat.pack_forget(), dog.pack_forget(), vote.pack_forget()])

    cat.pack(side=tkinter.LEFT)

    dog = tkinter.Button(root, image=img2,
                         command=lambda: [vote_event('Dog'), cat.pack_forget(), dog.pack_forget(), vote.pack_forget()])

    dog.pack(side=tkinter.RIGHT)


# This stuff executes when someone votes


def vote_event(var):
    file = open("votes.txt", "r")
    with open('votes.txt', 'a') as f:
        pvar = f'Vote for {var} at {datetime.now()}. \n'
        f.write(pvar)
    read_data = file.read()
    cat_count = read_data.count("Cat")
    dog_count = read_data.count("Dog")

    end = Canvas(root, width=screen_width / 2, height=screen_height / 7.5, bg='#1c1c26')
    end.pack()

    end.create_text(screen_width / 4, screen_height / 30, text=f'You voted for {var}. ', fill='white',
                    font=('San Francisco', int(screen_height / 30)))

    end.create_text(screen_width / 4, screen_height / 10,
                    text=f'There are {cat_count} votes for Cat and {dog_count} votes for Dog. ', fill='white',
                    font=('San Francisco', int(screen_height / 30)))

    tkinter.Button(root, text='Exit', command=lambda: exit(), font=('San Francisco', int(screen_height / 45))
                   ).pack(side=tkinter.BOTTOM)


# Advertising

print('Made by ElectricS01(Thomas B) electrics01.itch.io ')
# Do Not Redistribute without permission

# create and customize the root

root = tkinter.Tk()
root.title('Jank voting')
root.configure(bg='#1c1c26')
root.geometry()

# Get screen dimensions for scaling(I don't know if the scaling is correct on non 16:10 displays)

screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

if screen_width / 16 > screen_height / 9:
    screen_width = screen_width / 2

screen_geo_x = screen_width / 2
screen_geo_y = screen_height / 2

screen_geo_x = str(screen_geo_x).removesuffix('.0')
screen_geo_y = str(screen_geo_y).removesuffix('.0')

# Set root size/scaling

root.geometry(f'{screen_geo_x}x{screen_geo_y}')

# More advertising

link1 = Label(root, text='Made by ElectricS01(Thomas B)', bg='#282828', fg='white', cursor='hand',
              font=('San Francisco', int(screen_height / 70)))

link1.pack()
link1.bind('<Button-1>', lambda e: webbrowser.open_new('https://electrics01.itch.io'))

# Make the canvas

main = Canvas(root, width=screen_width / 2, height=screen_height / 2.35, bg='#1c1c26')
main.pack()

# Add text to canvas

main.create_text(screen_width / 4, screen_height / 30, text='Wellcome to Jank voting', fill='white',
                 font=('San Francisco', int(screen_height / 30)))

# Make a button to move to the voting

continue_button = Button(root, text='Click to continue', fg='black', cursor='hand',
                         font=('San Francisco', int(screen_height / 35)), command=start)
continue_button.pack()

# Gets the images to vote on

img1 = (Image.open('Cat.png'))
img2 = (Image.open('Dog.png'))

img1 = img1.resize((int(screen_width / 4 - 10), int(screen_width / 4)))
img1 = ImageTk.PhotoImage(img1)

img2 = img2.resize((int(screen_width / 4 - 10), int(screen_width / 4)))
img2 = ImageTk.PhotoImage(img2)

# Puts the images on the home screen

pho1 = main.create_image(screen_width / 3, screen_height / 4, image=img1)
pho2 = main.create_image(screen_width / 5, screen_width / 4, image=img2)

root.mainloop()
