import tkinter as tk
from tkinter import ttk
import sqlite3

def fetch_data():
    # Mengambil data dari database
    conn = sqlite3.connect('trafficAnalyst.db')
    c = conn.cursor()
    c.execute("SELECT * FROM jumlahkendaraan")
    data = c.fetchall()
    conn.close()
    return data

def update_table():
    # Memperbarui tabel dengan data dari database
    records = treeview.get_children()
    for item in records:
        treeview.delete(item)

    data = fetch_data()
    for row in data:
        treeview.insert("", "end", values=row)

    update_busiest_day(data)

def update_busiest_day(data):
    # Menghitung hari terpadat dari data
    busiest_day = ""
    max_density = 0

    for row in data:
        density = row[2]
        if density > max_density:
            busiest_day = row[0]
            max_density = density

    busiest_day_label.config(text="Hari Terpadat: " + busiest_day)

# Membuat jendela utama
root = tk.Tk()
root.title("Aplikasi Pemeriksaan Kepadatan Kendaraan")

# Membuat tabel
treeview = ttk.Treeview(root, columns=("Hari", "Sesi", "Jumlah", "Status"))
treeview.heading("Hari", text="Hari")
treeview.heading("Sesi", text="Sesi")
treeview.heading("Jumlah", text="Jumlah")
treeview.heading("Status", text="Status")
treeview.grid(row=0, column=0, columnspan=2, padx=10, pady=10)

# Membuat tombol untuk memperbarui tabel
update_button = tk.Button(root, text="Perbarui", command=update_table)
update_button.grid(row=1, column=0, padx=10, pady=5)

# Membuat label untuk kesimpulan hari terpadat
busiest_day_label = tk.Label(root, text="Hari Terpadat: ")
busiest_day_label.grid(row=1, column=1, padx=10, pady=5)

# Memperbarui tabel saat aplikasi dimulai
update_table()

# Menampilkan jendela utama
root.mainloop()