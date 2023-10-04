import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

def check_density():
    # Kode untuk memeriksa kepadatan kendaraan dan menampilkan hasil status
    density = density_entry.get()

    if density.isdigit():
        density = int(density)
        if density < 10:
            status = "Arus lancar"
        elif density < 20:
            status = "Arus padat"
        else:
            status = "Arus macet"

        # Memasukkan data ke dalam tabel
        treeview.insert("", "end", values=(density, status))
    else:
        messagebox.showerror("Error", "Masukkan angka yang valid")

# Membuat jendela utama
root = tk.Tk()
root.title("Aplikasi Pemeriksaan Kepadatan Kendaraan")

# Membuat label dan entri untuk input kepadatan kendaraan

density_label = tk.Label(root, text="Masukkan Hari:")
density_label.pack(padx=10, pady=5)

density_entry = tk.Entry(root)
density_entry.pack(padx=10, pady=5)

density_label = tk.Label(root, text="Masukkan Sesi:")
density_label.pack(padx=10, pady=5)

density_entry = tk.Entry(root)
density_entry.pack(padx=10, pady=5)

density_label = tk.Label(root, text="Masukkan kepadatan kendaraan:")
density_label.pack(padx=10, pady=5)

density_entry = tk.Entry(root)
density_entry.pack(padx=10, pady=5)


# Membuat tombol untuk memeriksa kepadatan kendaraan
check_button = tk.Button(root, text="Periksa", command=check_density)
check_button.pack(pady=10)

# Membuat tabel
treeview = ttk.Treeview(root, columns=("Hari", "Sesi", "Kepadatan", "Status"))
treeview.heading("Hari", text="Hari")
treeview.heading("Sesi", text="Sesi")
treeview.heading("Kepadatan", text="Kepadatan")
treeview.heading("Status", text="Status")
treeview.pack(padx=10, pady=10)


# Menampilkan jendela utama
root.mainloop()