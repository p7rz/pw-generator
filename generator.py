import random
import pyperclip
from tkinter import *
from tkinter.ttk import *

def password():
    entry.delete(0, END)
    strength = strength_choice.get()
    oracle = oracle_choice.get()
    weak_len = random.randint(8,12)
    medium_len = random.randint(13,17)
    strong_len = random.randint(18,24)



    password = ''
    if oracle == 0:
        if strength == 1:
            for i in range(0, weak_len):
                lowercase_letter = chr(random.randint(97,122))
                number = chr(random.randint(48,57))
                choice = random.choice((lowercase_letter, number))
                password = password + choice
        elif strength == 2:
            for i in range(0, medium_len):
                lowercase_letter = chr(random.randint(97,122))
                number = chr(random.randint(48,57))
                uppercase_letter = chr(random.randint(65,90))
                choice = random.choice((lowercase_letter, number, uppercase_letter))
                password = password + choice
        else:
            for i in range(0, strong_len):
                lowercase_letter = chr(random.randint(97,122))
                number = chr(random.randint(48,57))
                uppercase_letter = chr(random.randint(65,90))                
                special_char = chr(random.randint(33,152))
                choice = random.choice((lowercase_letter, number, uppercase_letter, special_char))
                password = password + choice
    else:
            for i in range(0, strong_len):
                lowercase_letter = chr(random.randint(97,122))
                number = chr(random.randint(48,57))
                uppercase_letter = chr(random.randint(65,90))                
                special_char_oracle = random.choice(('@', '%', '+', '!', '#', '$', '?', ':', ',', '~', '_', '.'))
                choice = random.choice((lowercase_letter, number, uppercase_letter, special_char_oracle))
                password = password + choice
    return password
                

def generate():
     password1 = password()
     entry.insert(0,password1)

def copy1():
    random_password = entry.get()
    pyperclip.copy(random_password)

root = Tk()
root.title('Password generator')

strength_choice = IntVar()
oracle_choice = IntVar()

Random_password = Label(root, text="Password")
Random_password.grid(row=0)
entry = Entry(root)
entry.grid(row=0,column=1,columnspan=2,sticky=E)

copy_button = Button(root, text='Copy', command=copy1)
copy_button.grid(row=0,column=6)

generate_button = Button(root, text='Generate', command=generate)
generate_button.grid(row=0,column=5)

low_strength_button = Radiobutton(root, text='Weak', variable=strength_choice, value=1)
low_strength_button.grid(row=1,column=1,sticky=E)

medium_strength_button = Radiobutton(root, text='Medium', variable=strength_choice, value=2)
medium_strength_button.grid(row=1,column=2,sticky=E)

strong_strength_button = Radiobutton(root, text='Strong', variable=strength_choice, value=3)
strong_strength_button.grid(row=1,column=3)

oracle_checkbutton = Checkbutton(root, text='Oracle', variable=oracle_choice, onvalue=1, offvalue=0)
oracle_checkbutton.grid(row=1,column=0)


root.mainloop()