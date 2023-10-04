from tkinter import *
import os
from datetime import datetime;
#creating instance of TK
root=Tk()

root.configure(background="grey")

page_check = 0
def function1():
    global lblframe1, page_check
    if page_check == 0:
        pass
    elif page_check == 2:
        lblframe2
    
    page_check = 1
    lblframe1 = LabelFrame(root)
    lblframe1.grid()
    Label(root, text="Traffic Analysist Visualization",font=("times new roman",26),fg="black",bg="grey",height=2).grid(row=0,rowspan=2,columnspan=2,sticky=N+E+W+S,padx=5,pady=5)

    Label(root, text="Dashboard",font=("times new roman",15),fg="black",bg="grey",height=2).grid(row=2,rowspan=2,columnspan=2,sticky=N+E+W+S,padx=5,pady=5)

    Button(root, text="Analisis Hari",font=("times new roman",20),bg="pink",fg='black',command=function2).grid(row=4,columnspan=2,sticky=W+E+N+S,padx=5,pady=5)
    Button(root, text="Analisis Waktu",font=("times new roman",20),bg="pink",fg='black',command=function2).grid(row=4,columnspan=2,sticky=W+E+N+S,padx=5,pady=5)
    # Button(root, text="Exit",font=("times new roman",20),bg="pink",fg='red',command=function2).grid(row=4,columnspan=2,sticky=W+E+N+S,padx=5,pady=5)

def function2():
    global lblframe2, page_check
    page_check = 2
    lblframe2 = LabelFrame(root)
    lblframe2.grid()
    Label(root, text="Traffic Analysist Visualization",font=("times new roman",26),fg="black",bg="grey",height=2).grid(row=0,rowspan=2,columnspan=2,sticky=N+E+W+S,padx=5,pady=5)

    Label(root, text="Visualisasi",font=("times new roman",15),fg="black",bg="grey",height=2).grid(row=2,rowspan=2,columnspan=2,sticky=N+E+W+S,padx=5,pady=5)

    Button(root, text="Data",font=("times new roman",20),bg="pink",fg='black',command=function2).grid(row=4,columnspan=2,sticky=W+E+N+S,padx=5,pady=5)
    # Button(root, text="Grafik",font=("times new roman",20),bg="pink",fg='black',command=function2).grid(row=4,columnspan=2,sticky=W+E+N+S,padx=5,pady=5)


def function3():
    global lblframe3, page_check
    page_check = 3
    lblframe3 = LabelFrame(root)
    lblframe3.grid()
    Label(root, text="Traffic Analysist Visualization",font=("times new roman",26),fg="black",bg="grey",height=2).grid(row=0,rowspan=2,columnspan=2,sticky=N+E+W+S,padx=5,pady=5)

    Label(root, text="Visualisasi",font=("times new roman",15),fg="black",bg="grey",height=2).grid(row=2,rowspan=2,columnspan=2,sticky=N+E+W+S,padx=5,pady=5)

    # Button(root, text="Data",font=("times new roman",20),bg="pink",fg='black',command=function2).grid(row=4,columnspan=2,sticky=W+E+N+S,padx=5,pady=5)
    Button(root, text="Grafik",font=("times new roman",20),bg="pink",fg='black',command=function2).grid(row=4,columnspan=2,sticky=W+E+N+S,padx=5,pady=5)

function1()

root.mainloop()
