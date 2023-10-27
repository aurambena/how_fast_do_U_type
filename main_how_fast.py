"""This script measures how fast you can type a sentense given by the program in a random way,
also, it tells the user how many letters can you type in 1 second. When the user has finished
the sentense it has to press enter to send the result. It uses the GUI interface and time 
library"""

#import standar modules
from essential_generators import DocumentGenerator
import time
from tkinter import *
import tkinter as tk 

#--- Create the window widget ---
root = Tk()
#set the dimensions
root.geometry('1000x400')
#set the title
root.title('How fast can U type!!!')
#set the background color
root.configure(bg='forest green')

# --- Generate a random sentence using the library DocumentGenerator ---
gen = DocumentGenerator()
phrase = gen.sentence()
#calculate how many keys the user has to press to complete the challenge
keys_number = len(phrase)+1

#create a label to show on screen the sentence to copy
label = tk.Label(root, text=phrase, font=("Arial", 15))
#shoving it onto screen
label.pack(pady=40)

# --- In order to measure the time, this script use the library time ---
#start counting in this part of the code
start_time = time.perf_counter()

def typing(event):
    """this method gets the input typed by the user and compare if it is the same phrase
    to copy"""
    #gets the input as an event
    value = event.widget.get()
    #compare the input with the random sentense
    if value == phrase:
        #if they are the same, te time stops 
        end_time = time.perf_counter()
        #measures how many keys do you press per second
        speed = keys_number/(end_time-start_time)
        #changes the label text to show the total time on screen
        label.config(text = 'Your total time was: '+str(end_time-start_time)+\
        '\nYou typed: '+str(speed)+ ' keys per second')

# --- Create the input on the screen ---
entry = Entry(root, width=100, background= 'yellow', foreground='black', borderwidth=5)
#shoving it onto the screen
entry.pack(pady=50) 
entry.focus()
#send the input string to the method typing 
entry.bind("<Return>", typing)

#Create exit button
exit_button = Button(root, text="Exit", command=root.destroy) 
exit_button.pack(pady=20) 

#infinitive bucle to show the screen
root.mainloop()