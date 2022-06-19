import tkinter as tk
import random
import time
from turtle import color
import matplotlib
matplotlib.use("TkAgg")
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

import matplotlib.pyplot as plt


root = tk.Tk()
root.title("COIN FLIPPER")

root.resizable(0,0)
root.geometry('500x550')
frame = tk.Frame(root)
frame.pack()



choices = ['Head', 'Tail']



def plot():
    pass

def start():
    flips =[]
   
    flip_range = int(entry.get())
    for x in range(flip_range):
        result = random.choice(choices)
        flips.append(result)

        

        

        head_percentage = round(flips.count("Head")/len(flips)*100,5)
        tail_percentage = round(flips.count("Tail")/len(flips)*100,5)

        heads['text'] = "Head Percentage is " + str(head_percentage)+"%"
        tails['text'] = "Tail Percentage is " + str(tail_percentage) +"%" 


        data = {
            'head': head_percentage,
            'tail': tail_percentage
        }
        
        titles = list(data.keys())
        probabilities = list(data.values())

        fig = plt.figure(figsize=(5,5))
        plt.bar(titles,probabilities,color='green',width=0.4)
        plt.title("turn: "+str(x+1))

        canvas = FigureCanvasTkAgg(fig,frame)
    
        canvas.get_tk_widget().grid(row=5,columnspan=10)

       
        root.update()

    
    
    
def enter_start(event):
    start()
    




root.bind('<Return>',enter_start)


entry = tk.Entry(frame)
button = tk.Button(frame,
                    text= "start",
                    fg='blue',
                    command= start)


heads = tk.Label(frame)
tails = tk.Label(frame)





button.grid(row=1,column=0)
entry.grid(row=1, column=1)

heads.grid(row=2,column=0,columnspan=4)
tails.grid(row=3,column=0,columnspan=4)



root.mainloop()
