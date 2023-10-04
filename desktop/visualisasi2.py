#import module from tkinter for UI
from tkinter import *
import os
from datetime import datetime;
#creating instance of TK
root=Tk()

root.configure(background="grey")                      
root.geometry('500x500')
# root.state('zoomed')

#root.geometry("300x300")

def function1():
    
    os.system("datavis2.py")
    
def function2():
    
    os.system("grafikvis2.py")

 
def function3():

    os.system("main.py")

#stting title for the window
root.title("Detections")

#creating a tex t label
Label(root, text="Traffic Analysist Visualization",font=("times new roman",26),fg="black",bg="grey",height=2).grid(row=0,rowspan=2,columnspan=2,sticky=N+E+W+S,padx=5,pady=5)
 
Label(root, text="Visualisasi",font=("times new roman",15),fg="black",bg="grey",height=2).grid(row=2,rowspan=2,columnspan=2,sticky=N+E+W+S,padx=5,pady=5)

#creating first button
Button(root,text="Data",font=("times new roman",20),bg="pink",fg='black',command=function1).grid(row=4,columnspan=2,sticky=W+E+N+S,padx=5,pady=5)

#creating second button
Button(root,text="Grafik",font=("times new roman",20),bg="pink",fg='black',command=function2).grid(row=5,columnspan=2,sticky=N+E+W+S,padx=5,pady=5)

#creating third button
# Button(root,text="Pedestrian Detection",font=('times new roman',20),bg="#000000",fg="green",command=function3).grid(row=6,columnspan=2,sticky=N+E+W+S,padx=5,pady=5)

# Button(root,text="Bus Detection",font=('times new roman',20),bg="#000000",fg="green",command=function4).grid(row=7,columnspan=2,sticky=N+E+W+S,padx=5,pady=5)

Button(root,text="Back",font=('times new roman',20),bg="pink",fg="red",command=function3).grid(row=9,columnspan=2,sticky=N+E+W+S,padx=5,pady=5)


root.mainloop()
 