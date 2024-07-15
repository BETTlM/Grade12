import tkinter as tk
from tkinter import ttk, filedialog, messagebox
from ttkthemes import ThemedStyle
import os
import pygame
import pdfminer.high_level as pdfminer
from modules import writer
import time
from modules import audiorecorder
class AudioConverterApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Audio Converter App")
        self.root.geometry("1440x900")
        self.root.configure(bg="#333")

      
        self.style = ThemedStyle(self.root)
        self.style.set_theme("equilux")  
      
        self.login_frame = ttk.Frame(self.root, style="TFrame")
        self.login_frame.pack(pady=200) 


        self.username_label = ttk.Label(self.login_frame, text="Username:")
        self.username_label.grid(row=0, column=0, padx=10, pady=5, sticky=tk.E)
        self.username_entry = ttk.Entry(self.login_frame)
        self.username_entry.grid(row=0, column=1, padx=10, pady=5)

        self.password_label = ttk.Label(self.login_frame, text="Password:")
        self.password_label.grid(row=1, column=0, padx=10, pady=5, sticky=tk.E)
        self.password_entry = ttk.Entry(self.login_frame, show="*")
        self.password_entry.grid(row=1, column=1, padx=10, pady=5)

        self.login_button = ttk.Button(self.login_frame, text="Login", command=self.login)
        self.login_button.grid(row=2, column=0, columnspan=2, pady=10, padx=10, sticky=tk.EW)


        self.greet_label = ttk.Label(self.root, text="")
        self.greet_label.pack(pady=20)


        button_width = 20
        button_height = 2

 
        self.upload_button = ttk.Button(self.root, text="Upload PDF", command=self.upload_pdf, width=button_width)
        self.upload_button.pack_forget()

   
        self.converter_button = ttk.Button(self.root, text="Convert PDF to Audio", command=self.convert_to_audio, width=button_width)
        self.converter_button.pack_forget()

        self.play_button = ttk.Button(self.root, text="Play Audio", command=self.play_audio, width=button_width)
        self.play_button.pack_forget()

      
        pygame.init()



    loc = ''
    def login(self):
        username = self.username_entry.get()
        password = self.password_entry.get()

   
        if username == "bettim" and password == "1":
            self.greet_label.config(text=f"Hello, {username}!", font=("Arial", 16))
            self.animate_login()
        else:
            messagebox.showerror("Login Failed", "Invalid username or password")

    def animate_login(self):
  
        self.login_frame.destroy()

    
        self.upload_button.pack(pady=10)

        self.converter_button.pack(pady=10)

       
        self.play_button.pack(pady=10)

    def upload_pdf(self):
        pdf_file = filedialog.askopenfilename(filetypes=[("PDF Files", "*.pdf")])
        if pdf_file:
            self.pdf_file = pdf_file
            global loc 
            loc = pdf_file
            messagebox.showinfo("File Uploaded", f"PDF file '{os.path.basename(pdf_file)}' uploaded successfully.")

    def convert_to_audio(self):
       
        try:
            content = pdfminer.extract_text(loc)
            writer.writenow(content)
            audiorecorder.record('/home/bettim/Documents/Kishoore/book.txt','/home/bettim/Documents/Kishoore/recordedaudio.mp3')
            time.sleep(4)
            print('PASSES')
        except Exception as error:
            return None, error
        messagebox.showinfo("AUDIO CONVERTED","Audio can be played now.")

    def play_audio(self):
        audio_file = "/home/bettim/Documents/Kishoore/recordedaudio.mp3"
        if os.path.exists(audio_file):
            pygame.mixer.music.load(audio_file)
            pygame.mixer.music.play()
        else:
            messagebox.showerror("File Not Found", "Please convert a PDF to audio first.")

if __name__ == "__main__":
    root = tk.Tk()
    app = AudioConverterApp(root)
    root.mainloop()
