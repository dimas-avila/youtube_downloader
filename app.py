import downloader
import tkinter as tk
import pathlib


class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.master.geometry("500x250") 
        self.grid()
        self.row = 0
        self.quality = tk.StringVar(self, value="480p")
        self.isAudio = tk.BooleanVar(self)
        self.create_widgets()
        

    def create_widgets(self):
        self.link_label = tk.Label(self)
        self.link_label["text"] = "Introduce el link del vídeo"
        self.link_label.grid(row=self.row, column=0)
        self.link_entry = tk.Entry(self)
        self.link_entry.grid(row=self.row, column=1)
        self.updaterow()
        media = {"Solo Audio": True, "Audio y Vídeo": False}
        qualities = ["480p", "720p", "1080p"]

        tk.Label(self, text="¿Quieres solo Audio o Vídeo+Audio?").grid(row=self.row, column=0)
        self.updaterow()

        for (text, value) in media.items():
            tk.Radiobutton(self, text=text, value=value, variable=self.isAudio).grid(row=self.row, column=0)
            self.updaterow()

        tk.Label(self, text="¿Qué calidad deseas?").grid(row=self.row, column=0)
        self.updaterow()

        for quality in qualities: 
            tk.Radiobutton(self, text=quality, value=quality, variable=self.quality).grid(row=self.row, column=0)
            self.updaterow()
        
        self.descarga = tk.Button(self)
        self.descarga["text"] = "Descargar"
        self.descarga["command"] = self.descargar
        self.descarga.grid(row=self.row, column=0)

    def say_hi(self):
        print("hi there, everyone!")

    def updaterow(self):
        self.row +=1

    def descargar(self):
        print(f'El link del vídeo es: {self.link_entry.get()} y la calidad {self.quality.get()}')
        descargador = downloader.Downloader(pathlib.Path().absolute().joinpath('descargas'))
        descargador.download(self.link_entry.get(), self.isAudio.get(), quality=self.quality.get())

root = tk.Tk()
app = Application(master=root)
app.mainloop()
