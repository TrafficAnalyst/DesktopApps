#import module from tkinter for UI
from tkinter import ttk
from tkinter import *
import os
from datetime import datetime;
#creating instance of TK
root=Tk()

root.configure(background="grey")
# root.geometry('500x500')
# root.state('zoomed')

#root.geometry("300x300")
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

# button
    Button(root,text="Analisis Hari",font=("times new roman",20),bg="pink",fg='black',command=function2).grid(row=4,columnspan=2,sticky=W+E+N+S,padx=5,pady=5)

    Button(root,text="Analisis Sesi",font=("times new roman",20),bg="pink",fg='black',command=function3).grid(row=5,columnspan=2,sticky=N+E+W+S,padx=5,pady=5)

# Button(root,text="Input Data",font=("times new roman",20),bg="pink",fg='black',command=function3).grid(row=5,columnspan=2,sticky=N+E+W+S,padx=5,pady=5)

    Button(root,text="Exit",font=('times new roman',20),bg="pink",fg="red",command=function4).grid(row=9,columnspan=2,sticky=N+E+W+S,padx=5,pady=5)
    # os.system("visualisasi1.py")
    
    
def function2():
    global lblframe2, page_check
    page_check = 2
    lblframe2 = LabelFrame(root)
    lblframe2.grid()

    Label(root, text="Traffic Analysist Visualization",font=("times new roman",26),fg="black",bg="grey",height=2).grid(row=0,rowspan=2,columnspan=2,sticky=N+E+W+S,padx=5,pady=5)

    Label(root, text="Visualisasi",font=("times new roman",15),fg="black",bg="grey",height=2).grid(row=2,rowspan=2,columnspan=2,sticky=N+E+W+S,padx=5,pady=5)

#creating first button
    Button(root,text="Data",font=("times new roman",20),bg="pink",fg='black',command=function4).grid(row=4,columnspan=2,sticky=W+E+N+S,padx=5,pady=5)

#creating second button
    Button(root,text="Grafik",font=("times new roman",20),bg="pink",fg='black',command=function4).grid(row=5,columnspan=2,sticky=N+E+W+S,padx=5,pady=5)

#creating third button
# Button(root,text="Pedestrian Detection",font=('times new roman',20),bg="#000000",fg="green",command=function3).grid(row=6,columnspan=2,sticky=N+E+W+S,padx=5,pady=5)

# Button(root,text="Bus Detection",font=('times new roman',20),bg="#000000",fg="green",command=function4).grid(row=7,columnspan=2,sticky=N+E+W+S,padx=5,pady=5)

    Button(root,text="Back",font=('times new roman',20),bg="pink",fg="red",command=function1).grid(row=9,columnspan=2,sticky=N+E+W+S,padx=5,pady=5)

    # os.system("visualisasi2.py")
    
def function3():
    global lblframe3, page_check
    page_check = 3
    lblframe3 = LabelFrame(root)
    lblframe3.grid()

    Label(root, text="Traffic Analysist Visualization",font=("times new roman",26),fg="black",bg="grey",height=2).grid(row=0,rowspan=2,columnspan=2,sticky=N+E+W+S,padx=5,pady=5)

    Label(root, text="Visualisasi",font=("times new roman",15),fg="black",bg="grey",height=2).grid(row=2,rowspan=2,columnspan=2,sticky=N+E+W+S,padx=5,pady=5)

#creating first button
    Button(root,text="Data",font=("times new roman",20),bg="pink",fg='black',command=function1).grid(row=4,columnspan=2,sticky=W+E+N+S,padx=5,pady=5)

#creating second button
    Button(root,text="Grafik",font=("times new roman",20),bg="pink",fg='black',command=function1).grid(row=5,columnspan=2,sticky=N+E+W+S,padx=5,pady=5)

#creating third button
# Button(root,text="Pedestrian Detection",font=('times new roman',20),bg="#000000",fg="green",command=function3).grid(row=6,columnspan=2,sticky=N+E+W+S,padx=5,pady=5)

# Button(root,text="Bus Detection",font=('times new roman',20),bg="#000000",fg="green",command=function4).grid(row=7,columnspan=2,sticky=N+E+W+S,padx=5,pady=5)

    Button(root,text="Back",font=('times new roman',20),bg="pink",fg="red",command=function1).grid(row=9,columnspan=2,sticky=N+E+W+S,padx=5,pady=5)

    # os.system("inputdata.py")


def function4():
    global lblframe3, page_check
    page_check = 3
    lblframe3 = LabelFrame(root)
    lblframe3.grid()

    density = density_entry.get()

    if density.isdigit():
        density = int(density)
        if density < 10:
            status = "Lalu lintas lancar"
        elif density < 20:
            status = "Lalu lintas padat"
        else:
            status = "Kemacetan"

        # Memasukkan data ke dalam tabel
        treeview.insert("", "end", values=(density, status))
    else:
        messagebox.showerror("Error", "Masukkan angka yang valid")

# Membuat jendela utama
root = Tk()
root.title("Aplikasi Pemeriksaan Kepadatan Kendaraan")

# Membuat label dan entri untuk input kepadatan kendaraan
density_label = ttk.Label(root, text="Masukkan kepadatan kendaraan:")
density_label.pack(padx=10, pady=5)

density_entry = ttk.Entry(root)
density_entry.pack(padx=10, pady=5)

# Membuat tombol untuk memeriksa kepadatan kendaraan
check_button = ttk.Button(root, text="Periksa", command=function4)
check_button.pack(pady=10)

# Membuat tabel
treeview = ttk.Treeview(root, columns=("Kepadatan", "Status"))
treeview.heading("Kepadatan", text="Kepadatan")
treeview.heading("Status", text="Status")
treeview.pack(padx=10, pady=10)


# Menampilkan jendela utama
def function5():
    root.destroy()
    

#stting title for the window
root.title("Detections")

#creating a tex t label
Label(root, text="Traffic Analysist Visualization",font=("times new roman",26),fg="black",bg="grey",height=2).grid(row=0,rowspan=2,columnspan=2,sticky=N+E+W+S,padx=5,pady=5)

Label(root, text="Dashboard",font=("times new roman",15),fg="black",bg="grey",height=2).grid(row=2,rowspan=2,columnspan=2,sticky=N+E+W+S,padx=5,pady=5)

# button
Button(root,text="Analisis Hari",font=("times new roman",20),bg="pink",fg='black',command=function1).grid(row=4,columnspan=2,sticky=W+E+N+S,padx=5,pady=5)

Button(root,text="Analisis Sesi",font=("times new roman",20),bg="pink",fg='black',command=function2).grid(row=5,columnspan=2,sticky=N+E+W+S,padx=5,pady=5)

# Button(root,text="Input Data",font=("times new roman",20),bg="pink",fg='black',command=function3).grid(row=5,columnspan=2,sticky=N+E+W+S,padx=5,pady=5)

Button(root,text="Exit",font=('times new roman',20),bg="pink",fg="red",command=function4).grid(row=9,columnspan=2,sticky=N+E+W+S,padx=5,pady=5)

root.mainloop()
