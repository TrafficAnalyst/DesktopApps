import tkinter as tk
from tkinter import ttk

from mainAnalisis import open_analys

def open_login(main):
    main.withdraw()
    mainLogin = tk.Tk()
    mainLogin.title("Login")
    mainLogin.geometry("200x200")
    
    def close_login():
        mainLogin.destroy()
        main.deiconify()
    
    # input
    label_user = ttk.Label(mainLogin, text="Username")
    label_user.pack(pady=(10, 0))
    input_user = tk.Entry(mainLogin)
    input_user.pack(pady=(10, 0))

    label_pass = ttk.Label(mainLogin, text="Password")
    label_pass.pack(pady=(10, 0))
    input_pass = tk.Entry(mainLogin)
    input_pass.pack(pady=(10, 0))

    # button
    login_button = tk.Button(mainLogin, text="Login", command=lambda: open_analys(mainLogin))
    login_button.pack(pady=(10, 0))

    close_button = tk.Button(mainLogin, text="Back to Home", command=close_login)
    close_button.pack(pady=(10, 0))