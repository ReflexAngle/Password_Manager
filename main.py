import random
from tkinter import *
import os

Window = Tk(className='manager')
Window.geometry('800x400')

# a series of strings that the program can use to randomly generate a password
lower = 'abcdefghijklmnopqrstuvwxyz'
upper = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
number = '1234567890'
symbol = '!@#$%^&*()_-+='

# A slider that allows to se the length of the password
# starts at 16 because anything lower in my opinion is to short to 50 be cause anything larger is too big
def gen():
    global password
    string = lower + upper + number + symbol
    length = entropy.get()
    password = "".join(random.sample(string, length))

    print(password)
    password_label = Label(Window, text=password)
    password_label.grid(row=0, column=0)

    return password


entropy = Scale(Window, orient='horizontal', from_=16, to=50, command=gen)
generate_Button = Button(Window, text='Generate', command=gen)

entropy.grid(row=1, column=0)
generate_Button.grid(row=2, column=3)

# function to save a password to a file
def save(password):
    print('save')


# passes the password into the save function
password = gen()
save(password)

# button used to save a password to your computer
save_Button = Button(Window, text='save', command=save)

Window.mainloop()
