import tkinter as tk
from tkinter import ttk
import requests
import matplotlib.pyplot as plt
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import json
import pandas as pd

# Fungsi untuk mendapatkan data dari API server database
def get_data_from_api():
    response = requests.get('https://wkf6l4sh-5000.asse.devtunnels.ms/dataanalisis')

    if response.status_code == 200:
        try:
            data = response.json()
            return data
        except json.decoder.JSONDecodeError as e:
            print(f"Error decoding JSON: {str(e)}")
            return None
    elif response.status_code == 404:
        print("Sumber daya tidak ditemukan. Periksa endpoint API Anda.")
        return None
    else:
        print(f"Permintaan API gagal dengan kode status: {response.status_code}")
        return None

# Fungsi untuk membuat bubble chart dari data
def create_bubble_chart(data):
    fig = Figure(figsize=(6, 6))
    axis = fig.add_subplot(111)

    x = [item['hari'] for item in data]
    y = [item['jumlah_kendaraan'] for item in data]
    sizes = [item['size'] for item in data]
    labels = [item['Line Chart'] for item in data]

    axis.scatter(x, y, s=sizes, alpha=0.5)

    for i, label in enumerate(labels):
        axis.annotate(label, (x[i], y[i]))

    return fig

# Fungsi untuk menggambar bubble chart di aplikasi Tkinter
def draw_bubble_chart():
    data = get_data_from_api()
    if data:
        fig = create_bubble_chart(data)
        canvas = FigureCanvasTkAgg(fig, master=chart_frame)
        canvas_widget = canvas.get_tk_widget()
        canvas_widget.pack()

# Fungsi untuk memperbarui grafik sesuai dengan pilihan dropdown
def update_chart():
    selected_option = dropdown.get()
    if selected_option == "Bubble Chart":
        draw_bubble_chart()
    else:
        data = get_data_from_api()
        if data:
            if selected_option == "Bar Chart":
                create_bar_chart(data)
            elif selected_option == "Line Chart":
                create_line_chart(data)
            elif selected_option == "Pie Chart":
                create_pie_chart(data)

# Fungsi untuk membuat bar chart dari data
def create_bar_chart(data):
    df = pd.DataFrame(data)
    df.plot(kind="bar")
    plt.xlabel("Hari")
    plt.ylabel("Jumlah_Kendaraan")
    plt.title("Bar Chart")
    plt.show()

# Fungsi untuk membuat line chart dari data
def create_line_chart(data):
    df = pd.DataFrame(data)
    df.plot()
    plt.xlabel("Hari")
    plt.ylabel("Jumlah_kendaraan")
    plt.title("Line Chart")
    plt.show()

# Fungsi untuk membuat pie chart dari data
def create_pie_chart(data):
    df = pd.DataFrame(data)
    df.plot(kind="pie", y="column_name")
    plt.xlabel("X Label")
    plt.ylabel("Y Label")
    plt.title("Pie Chart")
    plt.show()

# Membuat jendela utama Tkinter
window = tk.Tk()
window.title("Visualisasi Data")
window.geometry("800x600")

# Membuat dropdown
dropdown = ttk.Combobox(window, values=["Bubble Chart", "Bar Chart", "Line Chart", "Pie Chart"])
dropdown.set("Pilih Jenis Chart")
dropdown.pack()

# Tombol untuk memperbarui grafik
update_button = tk.Button(window, text="Perbarui", command=update_chart)
update_button.pack()

# Membuat frame untuk grafik
chart_frame = ttk.Frame(window)
chart_frame.pack()

# Menjalankan aplikasi Tkinter
window.mainloop()
