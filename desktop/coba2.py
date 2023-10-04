import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

def check_density():
     # Kamus untuk memetakan angka ke huruf
    day_mapping = {
        "1": "Senin",
        "2": "Selasa",
        "3": "Rabu",
        "4": "Kamis",
        "5": "Jumat",
        "6": "Sabtu",
        "7": "Minggu"
    }

    session_mapping = {
        "1": "Pagi",
        "2": "Siang",
        "3": "Sore"
    }

    # Kode untuk memeriksa kepadatan kendaraan dan menampilkan hasil status
    day = day_entry.get()
    session = session_entry.get()
    density = density_entry.get()

    if day in day_mapping and session in session_mapping and density.isdigit():
        day = day_mapping[day]
        session = session_mapping[session]
        density = int(density)

        if density < 10:
            status = "Arus lancar"
        elif density < 20:
            status = "Arus padat"
        else:
            status = "Arus macet"

        # Memasukkan data ke dalam tabel
        treeview.insert("", "end", values=(day, session, density, status))

        # Memperbarui kesimpulan hari terpadat
        update_busiest_day()
    else:
        messagebox.showerror("Error", "Masukkan input yang valid")

def update_busiest_day():
    # Menghitung hari terpadat
    busiest_day = ""
    max_density = 0

    for child in treeview.get_children():
        density = int(treeview.item(child, "values")[2])
        if density > max_density:
            busiest_day = treeview.item(child, "values")[0]
            max_density = density

    busiest_day_label.config(text="Hari Terpadat: " + busiest_day)

# Membuat jendela utama
root = tk.Tk()
root.title("Aplikasi Pemeriksaan Kepadatan Kendaraan")

# Membuat label dan entri untuk input hari
day_label = tk.Label(root, text="Hari:")
day_label.grid(row=0, column=0, padx=10, pady=5)
day_entry = tk.Entry(root)
day_entry.grid(row=0, column=1, padx=10, pady=5)

# Membuat label dan entri untuk input sesi jumlah
session_label = tk.Label(root, text="Sesi :")
session_label.grid(row=1, column=0, padx=10, pady=5)
session_entry = tk.Entry(root)
session_entry.grid(row=1, column=1, padx=10, pady=5)

# Membuat label dan entri untuk input kepadatan kendaraan
density_label = tk.Label(root, text="Jumlah :")
density_label.grid(row=2, column=0, padx=10, pady=5)
density_entry = tk.Entry(root)
density_entry.grid(row=2, column=1, padx=10, pady=5)

# Membuat tombol untuk memeriksa kepadatan kendaraan
check_button = tk.Button(root, text="Periksa", command=check_density)
check_button.grid(row=3, column=0, columnspan=2, padx=10, pady=10)

# Membuat tabel
treeview = ttk.Treeview(root, columns=("Hari", "Sesi Jumlah", "Kepadatan", "Status"))
treeview.heading("Hari", text="Hari")
treeview.heading("Sesi Jumlah", text="Sesi Jumlah")
treeview.heading("Kepadatan", text="Kepadatan")
treeview.heading("Status", text="Status")
treeview.grid(row=4, column=0, columnspan=2, padx=10, pady=10)

# Membuat label untuk kesimpulan hari terpadat
busiest_day_label = tk.Label(root, text="Hari Terpadat: ")
busiest_day_label.grid(row=5, column=0, columnspan=2, padx=10, pady=5)

# Menampilkan jendela utama
root.mainloop()