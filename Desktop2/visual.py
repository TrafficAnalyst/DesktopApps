import tkinter as tk
from tkinter import ttk
from tkinter import filedialog
from matplotlib.figure import Figure
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import pandas as pd
import numpy as np
import cv2
from PIL import Image, ImageTk

# Untuk chart visualisasi trend kendaraan
class ChartPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        label = tk.Label(self, text="First Chart Page", font=("Helvetica", 16))
        label.pack(pady=10, padx=10)

        button_back = ttk.Button(self, text="Back to Home", command=lambda: controller.show_frame('HomePage'))
        button_back.pack(fill="x", padx=10, pady=10)

        # Create a button to load and display the chart
        button_chart = ttk.Button(self, text="Show Chart", command=self.show_chart)
        button_chart.pack(fill="x", padx=10, pady=10)

        # Placeholder for the chart
        self.chart_placeholder = ttk.Label(self, text="Chart will be displayed here")
        self.chart_placeholder.pack(pady=20)

    def show_chart(self):
        try:
            file_path = 'dummyanalisis.csv'  # Ganti dengan path sesuai lokasi file Anda
            data = pd.read_csv(file_path)

            # Menghitung jumlah kendaraan per sesi
            sesi_counts = data.groupby('sesi')['jumlah_kendaraan'].sum()

            # Membuat bar chart
            
            fig, ax = plt.subplots(figsize=(10, 6))
            sesi_counts.plot(kind='bar', color='skyblue', ax=ax)
            ax.set_title('Jumlah Kendaraan per Sesi')
            ax.set_xlabel('Sesi')
            ax.set_ylabel('Jumlah Kendaraan')
            ax.tick_params(axis='x', rotation=45)
            plt.show()

            # # Embed the chart in Tkinter
            canvas = FigureCanvasTkAgg(fig, master=self)
            canvas_widget = canvas.get_tk_widget()
            canvas_widget.pack()

        except Exception as e:
            self.chart_placeholder.config(text="Error creating chart: {}".format(str(e)))


         # Create a Notebook (tabbed interface)
        notebook = ttk.Notebook(self)
        chart_tab = ttk.Frame(notebook)
        notebook.add(chart_tab, text="Charts")
        self.create_chart_tab(chart_tab)

       
    def create_chart_tab(self, tab):
        # Create a button to load and display the chart
        button_chart = ttk.Button(tab, text="Show Chart", command=self.show_chart)
        button_chart.pack(fill="x", padx=10, pady=10)

        # Create a canvas for chart display
        self.chart_canvas = tk.Canvas(tab)
        self.chart_canvas.pack()

    


        # Create a Notebook (tabbed interface)
        notebook = ttk.Notebook(self)

        # Create tabs
        
        video_tab = ttk.Frame(notebook)

        # Add tabs to the Notebook
      
        notebook.add(video_tab, text="Video")

        # Pack the Notebook widget
        notebook.pack(expand=True, fill="both")

        # Content for the 'Charts' tab
       

        # Content for the 'Video' tab
        self.create_video_tab(video_tab)


    def create_video_tab(self, tab):
        # Create a button to start video
        button_start_video = ttk.Button(tab, text="Start Video", command=self.start_video)
        button_start_video.pack(fill="x", padx=10, pady=10)

        # Placeholder for video canvas
        self.video_canvas = tk.Canvas(tab)
        self.video_canvas.pack()

    def start_video(self):
        # Use a predefined video path
        video_path = 'coba.mp4'

        # Start video playback
        self.play_video(video_path)

    def play_video(self, video_path):
        # Open the video file
        cap = cv2.VideoCapture(video_path)

        # Get video properties
        width = int(cap.get(3))
        height = int(cap.get(4))

        # Create a canvas for video display
        video_canvas = tk.Canvas(self.video_canvas, width=width, height=height)
        video_canvas.pack()

        while True:
            # Read a frame from the video
            ret, frame = cap.read()

            if not ret:
                break

            # Convert the frame from BGR to RGB
            rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

            # Convert the frame to ImageTk format
            img = ImageTk.PhotoImage(Image.fromarray(rgb_frame))

            # Update the canvas with the new frame
            video_canvas.create_image(0, 0, anchor=tk.NW, image=img)
            video_canvas.update()

            # Pause for a short duration to control the video playback speed
            video_canvas.after(30)

            # Remove the previous frame
            video_canvas.delete("all")

        # Release the video capture object
        cap.release()

# Untuk chart visualisasi kedua
class SecondChart(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        label = tk.Label(self, text="Second Chart Page", font=("Helvetica", 16))
        label.pack(pady=10, padx=10)

        button_back = ttk.Button(self, text="Back to Home", command=lambda: controller.show_frame('HomePage'))
        button_back.pack(fill="x", padx=10, pady=10)

        # Create a button to load and display the chart
        button_chart = ttk.Button(self, text="Show Chart", command=self.show_second_chart)
        button_chart.pack(fill="x", padx=10, pady=10)

        # Placeholder for the chart
        self.chart_placeholder = ttk.Label(self, text="Chart will be displayed here")
        self.chart_placeholder.pack(pady=20)

    def show_second_chart(self):
        try:
            # Membaca file CSV
            file_path = 'dummyanalisis.csv'  # Ganti dengan path sesuai lokasi file Anda
            data = pd.read_csv(file_path)

            # Menghitung jumlah kendaraan per waktu
            waktu_counts = data.groupby('hari')['jumlah_kendaraan'].sum()

            # Menggunakan figure yang sudah ada
            fig, ax = plt.subplots(figsize=(12, 6))
            waktu_counts.plot(kind='bar', color='skyblue', ax=ax)
            ax.set_title('Jumlah Kendaraan per Waktu')
            ax.set_xlabel('Hari')
            ax.set_ylabel('Jumlah Kendaraan')
            ax.tick_params(axis='x', rotation=45)
            plt.show()

             # Embed the chart in Tkinter
            canvas = FigureCanvasTkAgg(fig, master=self)
            canvas_widget = canvas.get_tk_widget()
            canvas_widget.pack()

        except Exception as e:
            self.chart_placeholder.config(text="Error creating chart: {}".format(str(e)))

        # Create a Notebook (tabbed interface)
        notebook = ttk.Notebook(self)
        chart_tab = ttk.Frame(notebook)
        notebook.add(chart_tab, text="Charts")
        self.create_chart_tab(chart_tab)

       
    def create_chart_tab(self, tab):
        # Create a button to load and display the chart
        button_chart = ttk.Button(tab, text="Show Chart", command=self.show_second_chart)
        button_chart.pack(fill="x", padx=10, pady=10)

        # Create a canvas for chart display
        self.chart_canvas = tk.Canvas(tab)
        self.chart_canvas.pack()

class ThirdChart(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        label = tk.Label(self, text="Third Chart Page", font=("Helvetica", 16))
        label.pack(pady=10, padx=10)

        button_back = ttk.Button(self, text="Back to Home", command=lambda: controller.show_frame('HomePage'))
        button_back.pack(fill="x", padx=10, pady=10)

        # Create a button to load and display the chart
        button_chart = ttk.Button(self, text="Show Chart", command=self.show_three_chart)
        button_chart.pack(fill="x", padx=10, pady=10)

        # Placeholder for the chart
        self.chart_placeholder = ttk.Label(self, text="Chart will be displayed here")
        self.chart_placeholder.pack(pady=20)

    def show_three_chart(self):
        try:
            # Membaca file CSV
            file_path = 'dummyanalisis.csv'  # Ganti dengan path sesuai lokasi file Anda
            data = pd.read_csv(file_path)

            # Menghitung jumlah kendaraan per sesi
            sesi_counts = data.groupby('sesi')['jumlah_kendaraan'].sum()

            # Menggunakan figure yang sudah ada
            fig, ax = plt.subplots(figsize=(8, 8))
            ax.pie(sesi_counts, labels=sesi_counts.index, autopct='%1.1f%%', startangle=140, colors=plt.cm.Paired.colors)
            ax.set_title('Proporsi Jumlah Kendaraan per Sesi')
            plt.show()

             # Embed the chart in Tkinter
            canvas = FigureCanvasTkAgg(fig, master=self)
            canvas_widget = canvas.get_tk_widget()
            canvas_widget.pack()

        except Exception as e:
            self.chart_placeholder.config(text="Error creating chart: {}".format(str(e)))

        # Create a Notebook (tabbed interface)
        notebook = ttk.Notebook(self)
        chart_tab = ttk.Frame(notebook)
        notebook.add(chart_tab, text="Charts")
        self.create_chart_tab(chart_tab)

       
    def create_chart_tab(self, tab):
        # Create a button to load and display the chart
        button_chart = ttk.Button(tab, text="Show Chart", command=self.show_three_chart)
        button_chart.pack(fill="x", padx=10, pady=10)

        # Create a canvas for chart display
        self.chart_canvas = tk.Canvas(tab)
        self.chart_canvas.pack()


# Untuk tampilan halaman utama
class HomePage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        label = tk.Label(self, text="Halaman Utama", font=("Helvetica", 16))
        label.pack(pady=10, padx=10)

        style = ttk.Style()
        style.configure("TButton", font=("Helvetica", 16))  # Ganti ukuran font sesuai kebutuhan

        # first button
        button_first_chart_page = ttk.Button(self, text="Visualisasi BarChart Berdasarkan Sesi", command=lambda: controller.show_frame('ChartPage'))
        button_first_chart_page.pack(fill="x", padx=10, pady=10)

        # second button
        button_second_chart_page = ttk.Button(self, text="Visualisasi BarChart Berdasarkan Hari", command=lambda: controller.show_frame('SecondChart'))
        button_second_chart_page.pack(fill="x", padx=10, pady=10)


          # fourth button
        button_fourth_chart_page = ttk.Button(self, text="Visualisasi PieChart Berdasarkan Sesi", command=lambda: controller.show_frame('ThirdChart'))
        button_fourth_chart_page.pack(fill="x", padx=10, pady=10)

        # third button
        button_third_chart_page = ttk.Button(self, text="Tabel Analisis", command=lambda: controller.show_frame('FourthChartPage'))
        button_third_chart_page.pack(fill="x", padx=10, pady=10)

      
        # Button to show videos on the home page
        button_vid = ttk.Button(self, text="Show Videos", command=self.show_videos_on_homepage)
        button_vid.pack(fill="x", padx=10, pady=10)

        # Create a frame to hold video canvases
        self.video_frame = tk.Frame(self)
        self.video_frame.pack(side="top", fill="both", expand=True)

        # Canvas for video display
        self.video_canvases = []

    def show_videos_on_homepage(self):
        # Use predefined video paths, bisa diganti sesuai keinginan
        video_paths = ['coba.mp4','coba.mp4']

        # Create a Canvas for each video and embed it in the video_frame
        for video_path in video_paths:
            video_canvas = tk.Canvas(self.video_frame, width=320, height=240)
            video_canvas.pack(side="left", padx=10)
            self.video_canvases.append(video_canvas)

            # Start video playback
            self.controller.play_video(video_path, video_canvas)
        
# Main application
class SampleApp(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        # Set window title
        self.title("Chart Visualization")

        # Create container to hold different frames/pages
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}
        for F in (HomePage, ChartPage, SecondChart, ThirdChart):
            page_name = F.__name__
            frame = F(parent=container, controller=self)
            self.frames[page_name] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        # Show the home page by default
        self.show_frame('HomePage')  

    def show_frame(self, page_name):
        frame = self.frames[page_name]
        frame.tkraise()

    def play_video(self, video_path, canvas):
        # Video playback logic using cv2.VideoCapture
        cap = cv2.VideoCapture(video_path)

        def update_frame():
            nonlocal self
            ret, frame = cap.read()
            if ret:
                # Convert the frame to RGB format
                rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

                # Convert the frame to ImageTk format
                image = Image.fromarray(rgb_frame)
                self.imgtk = ImageTk.PhotoImage(image=image)

                # Update the canvas with the new frame
                canvas.imgtk = self.imgtk
                canvas.create_image(0, 0, anchor='nw', image=self.imgtk)

                # Schedule the next update
                canvas.after(30, update_frame)
            else:
                # Video has ended, release the capture
                cap.release()


        # Start the first update
        update_frame()

# Untuk menjalankan aplikasi
if __name__ == "__main__":
    app = SampleApp()
    app.geometry("800x600")
    app.mainloop()