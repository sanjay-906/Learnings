import tkinter as tk
from tkinter import ttk
import time

commands= ['Initializing...', 'Searching data...', 'Pre-processing data...', 'Building ML model...', 'Prediction on input...']

def get_input():
    user_input= input_entry.get()

def open_progress_window():
    progress_window= tk.Toplevel(root)
    progress_window.title("Predicting...")
    new_text= tk.StringVar()
    text_label= tk.Label(progress_window, textvariable= new_text)
    text_label.pack(pady= 20)

    bar= ttk.Progressbar(progress_window, orient= tk.HORIZONTAL, length= 300)
    bar.pack(pady= 10)

    n= 200
    i= 0
    speed= 1
    try:
        while(i<n):
            time.sleep(0.05)
            bar['value']+= (speed/n)*100
            i+= speed
            new_text.set(commands[int(i/40)])
            progress_window.update_idletasks()
    except:
        pass

    open_text_window()

def open_text_window():
    text_window= tk.Toplevel(root)
    text_window.wm_geometry("150x100")
    text_window.title("Output")

    text_label= tk.Label(text_window, text= "idk, just look outside.")
    text_label.pack(pady= 20)

root= tk.Tk()
root.title("AI-weather app")

heading_label= tk.Label(root, text= "State-of-the-art Weather Prediction",  font=('TkDefaultFont', 12))
heading_label.pack()

heading_label2= tk.Label(root, text= "using Deep Generative Adversarial Networks",  font=('TkDefaultFont', 12))
heading_label2.pack()

question_label= tk.Label(root, text= "Enter Location:", pady= 30)
question_label.pack()

input_entry= tk.Entry(root)
input_entry.pack()

open_button= tk.Button(root, text= "Check weather", command= open_progress_window)
open_button.pack(pady= 20)

heading_label= tk.Label(root, text= "© Copyright 2023. All Rights Reserved.")
heading_label.pack()


root.wm_geometry("400x250")

root.mainloop()
