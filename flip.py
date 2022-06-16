import tkinter as tk
import random
import time


choices = ['Head', 'Tail']

flips =[]

def plot():
    pass

def start(event):
    flip_range = int(entry.get())
    for x in range(flip_range):
        result = random.choice(choices)
        flips.append(result)

        

        head_percentage = round(flips.count("Head")/len(flips)*100,5)
        tail_percentage = round(flips.count("Tail")/len(flips)*100,5)

        heads['text'] = "Head Percentage is " + str(head_percentage)+"%"
        tails['text'] = "Tail Percentage is " + str(tail_percentage) +"%" 
    
    

    

root = tk.Tk()
root.title("COIN FLIPPER")
root.resizable(0,0)
root.bind('<Return>',start)
frame = tk.Frame(root)
frame.pack()

entry = tk.Entry(frame)
button = tk.Button(frame,
                    text= "start",
                    fg='blue',
                    command= start)


heads = tk.Label(frame)
tails = tk.Label(frame)


button.grid(row=1,column=0)
entry.grid(row=1, column=1)

heads.grid(row=2,column=0,columnspan=2)
tails.grid(row=3,column=0,columnspan=2)

root.mainloop()