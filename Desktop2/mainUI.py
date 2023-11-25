import tkinter as tk
from tkinter import ttk
import pandas as pd


def open_ui(main):
    main.withdraw()
    mainAnalisis = tk.Tk()
    mainAnalisis.title("Aplikasi Kepadatan Arus Kendaraan")
    mainAnalisis.geometry("200x200")

# Path to the CSV file (replace with your CSV file path)
CSV_FILE_PATH = 'dummyanalisis.csv'

# Function to read data from CSV
def read_csv_data():
    try:
        # Read data from CSV using pandas
        data = pd.read_csv(CSV_FILE_PATH)
        return data
    except Exception as e:
        print(f'Error: {e}')
        return pd.DataFrame()

# Function to find busiest day
def find_busiest_day(data):
    busiest_day = ""
    max_vehicle_count = 0

    for index, row in data.iterrows():
        jumlah_kendaraan = int(row['jumlah_kendaraan'])  # Convert to integer
        if jumlah_kendaraan > max_vehicle_count:
            max_vehicle_count = jumlah_kendaraan
            busiest_day = row['hari']

    return busiest_day

def find_busiest_session(data):
    busiest_ses = ""
    max_vehicle_count = 0

    for index, row in data.iterrows():
        jumlah_kendaraan = int(row['jumlah_kendaraan'])  # Convert to integer
        if jumlah_kendaraan > max_vehicle_count:
            max_vehicle_count = jumlah_kendaraan
            busiest_ses = row['sesi']

    return busiest_ses


# Function to display data in the Tkinter treeview
# Function to display data in the Tkinter treeview
def display_traffic_data():
    data = read_csv_data()

    for row in tree.get_children():
        tree.delete(row)

    for index, row in data.iterrows():
        tanggal = row['waktu']
        hari = row['hari']
        sesi = row['sesi']
        jumlah = row['jumlah_kendaraan']
        status = row['status_arus']
        tree.insert("", "end", values=(tanggal, hari, sesi, jumlah, status))

    busiest_day = find_busiest_day(data)
    busiest_day_label.config(text=f"Hari Terpadat: {busiest_day}")

    busiest_ses = find_busiest_session(data)
    busiest_ses_label.config(text=f"Sesi Terpadat: {busiest_ses}")
    

# Membuat GUI
root = tk.Tk()
root.title("Aplikasi Kepadatan Arus Kendaraan")

frame = ttk.Frame(root)
frame.pack(padx=20, pady=20)

# Menambahkan judul di tengah frame
label_judul = ttk.Label(frame, text="Analisis Kepadatan Arus Kendaraan", font=("times new roman", 20), foreground="black")
label_judul.grid(row=0, column=0, columnspan=2, padx=10, pady=20)

# Pilihan hari
day_label = ttk.Label(frame, text="Pilih Hari:")
day_label.grid(row=1, column=0, padx=10, pady=5)
day_var = tk.StringVar()
day_dropdown = ttk.Combobox(frame, textvariable=day_var, values=("Monday", "Tuesday", "Wednesday", "Thursday", "Friday"))
day_dropdown.grid(row=1, column=1, padx=10, pady=5)
day_dropdown.set("Monday")  # Set nilai default

# Pilihan sesi
session_label = ttk.Label(frame, text="Pilih Sesi:")
session_label.grid(row=2, column=0, padx=10, pady=5)
session_var = tk.StringVar()
session_dropdown = ttk.Combobox(frame, textvariable=session_var, values=("Pagi", "Siang", "Sore"))
session_dropdown.grid(row=2, column=1, padx=10, pady=5)
session_dropdown.set("Pagi")  # Set nilai default

# Tombol Tampilkan Data dengan warna pink
show_button = ttk.Button(frame, text="Tampilkan Data", command=display_traffic_data, style="Pink.TButton")
show_button.grid(row=3, columnspan=2, padx=10, pady=10)

# Membuat tabel untuk menampilkan data
tree = ttk.Treeview(frame, columns=("Tanggal", "Hari", "Sesi", "Jumlah", "Status"))
tree.grid(row=4, columnspan=2, padx=10, pady=5)

# Konfigurasi kolom-kolom tabel
tree.heading("#1", text="Tanggal")
tree.heading("#2", text="Hari")
tree.heading("#3", text="Sesi")
tree.heading("#4", text="Jumlah")
tree.heading("#5", text="Status")
tree.column("#1", width=100)
tree.column("#2", width=100)
tree.column("#3", width=100)
tree.column("#4", width=100)
tree.column("#5", width=100)

busiest_day_label = ttk.Label(frame, text="Hari Terpadat: ")
busiest_day_label.grid(row=5, column=0, columnspan=2, padx=10, pady=5)

busiest_ses_label = ttk.Label(frame, text="Sesi Terpadat: ")
busiest_ses_label.grid(row=6, column=0, columnspan=2, padx=10, pady=5) 

# Main loop Tkinter
root.mainloop()
