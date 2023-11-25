import tkinter as tk
from tkinter import ttk

from mainAnalisis import open_analys
from mainLogin import open_login

# Create the main window
main = tk.Tk()
main.title("Home")
main.geometry("200x200")
# style = Style(theme="journal")

# create label
label_day = ttk.Label(main, text="Jenis akun")
label_day.pack(pady=(10, 0))

# Create a button in the main window
buttonRecom = tk.Button(main, text="Petugas", command=lambda: open_login(main), width=15, height=2)
buttonRecom.pack(pady=(10, 0))
# buttonRecap = tk.Button(main, text="Satpam", command=lambda: open_analys(main), width=15, height=2)
# buttonRecap.pack(pady=(10, 0))

# Start the main loop
main.mainloop()