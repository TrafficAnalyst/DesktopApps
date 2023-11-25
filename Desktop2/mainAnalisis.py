import tkinter as tk
from tkinter import ttk
import requests

from mainUI import open_ui


def open_analys(main):
    main.withdraw()
    mainAnalisis = tk.Tk()
    mainAnalisis.title("Analisis")
    mainAnalisis.geometry("200x200")
    
    def open_ui():
        mainAnalisis.destroy()
        main.deiconify()
    
    label= ttk.Label(mainAnalisis, text="ANALISIS")
    label.pack(pady=(10, 0))

    tabel_button = tk.Button(mainAnalisis, text="Tabel Analisis", command=open_ui)
    tabel_button.pack(pady=(10, 0))

    visual_button = tk.Button(mainAnalisis, text="Tabel Analisis", command=open_ui)
    visual_button.pack(pady=(10, 0))

   

# # Main loop Tkinter
# root.mainloop() 