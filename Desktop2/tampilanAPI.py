import tkinter as tk
from tkinter import ttk
import requests  # Import modul requests untuk membuat permintaan HTTP

# URL API server database (ganti dengan URL server Anda)
API_URL = 'https://wkf6l4sh-5000.asse.devtunnels.ms/datadesktop'

# Fungsi untuk mengambil data dari API server database 
def get_traffic_data(day, session): 
    # Membuat parameter permintaan HTTP
    params = {
        'day': day,
        'session': session
    }

    try:
        # Mengirim permintaan GET ke API server database
        response = requests.get(API_URL, params=params)

        # Mengecek apakah permintaan berhasil
        if response.status_code == 200:
            data = response.json()  # Mengambil data dari respons JSON
            return data
        else:
            return []  # Jika permintaan gagal, kembalikan daftar kosong
    except requests.exceptions.RequestException as e:
        print(f'Error: {e}')
        return []

def find_busiest_day(data):
    # Inisialisasi variabel untuk melacak hari terpadat dan jumlah kendaraan terbanyak
    busiest_day = ""
    max_vehicle_count = 0

    # Iterasi melalui data untuk mencari hari terpadat
    for item in data['trafficgate']:
        jumlah_kendaraan = item['jumlah_kendaraan']
        if jumlah_kendaraan > max_vehicle_count:
            max_vehicle_count = jumlah_kendaraan
            busiest_day = item['hari']

    return busiest_day

def find_busiest_session(data):
    # Inisialisasi variabel untuk melacak hari terpadat dan jumlah kendaraan terbanyak
    busiest_ses = ""
    max_vehicle_count = 0

    # Iterasi melalui data untuk mencari hari terpadat
    for item in data['trafficgate']:
        jumlah_kendaraan = item['jumlah_kendaraan']
        if jumlah_kendaraan > max_vehicle_count:
            max_vehicle_count = jumlah_kendaraan
            busiest_ses = item['sesi']

    return busiest_ses
# Fungsi untuk menampilkan data pada tabel Tkinter
def display_traffic_data():
    selected_day = day_var.get()
    selected_session = session_var.get()

    # Ambil data dari API server database berdasarkan pilihan pengguna
    data = get_traffic_data(selected_day, selected_session)

    # Bersihkan tabel Tkinter sebelum menampilkan data baru
    # tree.delete(*tree.get_children())
    # tree.delete(tree)
    for row in tree.get_children():
         tree.delete(row)

    # Tampilkan data dalam tabel Tkinter
    
    for item in data['trafficgate']:
        tanggal = item['waktu']
        hari = item['hari']
        sesi = item['sesi']
        jumlah = item['jumlah_kendaraan']
        status = item['status_kendaraan']
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
day_dropdown = ttk.Combobox(frame, textvariable=day_var, values=("Senin", "Selasa", "Rabu", "Kamis", "Jumat"))
day_dropdown.grid(row=1, column=1, padx=10, pady=5)
day_dropdown.set("Senin")  # Set nilai default

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
busiest_ses_label.grid(row=5, column=0, columnspan=2, padx=10, pady=5) 

# Main loop Tkinter
root.mainloop() 