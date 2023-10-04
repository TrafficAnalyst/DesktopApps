import tkinter as tk
from tkinter import ttk
from ttkbootstrap import Style

def update_status():
    # Kode untuk memperbarui status kepadatan kendaraan
    status_label.config(text="Status: Terjadi kemacetan")

# Membuat instance dari kelas Style pada ttkbootstrap
style = Style()

# Membuat jendela utama
root = style.master
root.title("Aplikasi Status Kepadatan Kendaraan")

# Membuat frame utama
main_frame = ttk.Frame(root, padding="20")
main_frame.grid(row=0, column=0, sticky="nsew")

# Membuat label judul
title_label = ttk.Label(main_frame, text="Status Kepadatan Kendaraan", style="primary.TLabel")
title_label.grid(row=0, column=0, columnspan=2, pady=10)

# Membuat label status
status_label = ttk.Label(main_frame, text="Status: Lalu lintas lancar")
status_label.grid(row=1, column=0, columnspan=2, pady=10)

# Membuat tombol perbarui status
update_button = ttk.Button(main_frame, text="Perbarui Status", style="success.TButton", command=update_status)
update_button.grid(row=2, column=0, columnspan=2, pady=10)

# Menampilkan jendela utama
root.mainloop()