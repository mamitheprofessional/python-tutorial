import tkinter as tk
from tkinter import filedialog 


class Notepad:
    def __init__(self,pencere):
        self.pencere=pencere
        self.pencere.title("Not Defteri")
        self.pencere.geometry("600x600")

        self.text_bolumu=tk.Text(self.pencere, wrap="word")
        self.text_bolumu.pack(expand="yes", fill="both")
        self.menu=tk.Menu(self.pencere) 
        self.pencere.config(menu=self.menu) 
        self.file_set=tk.Menu(self.menu, tearoff=0) 
        self.menu.add_cascade(label="Ayarlar", menu=self.file_set)

        self.file_set.add_command(label="Temizle", command=self.temizle)
        self.file_set.add_command(label="Aç", command=self.dosya_ac)
        self.file_set.add_command(label="Kaydet", command=self.dosya_kaydet)
        
        
    def temizle(self):
        self.text_bolumu.delete(1.0, tk.END)


    def dosya_ac(self):
        self.dosyayi_ac = filedialog.askopenfilename(defaultextension=".txt", filetypes=[("Text Dosyası", "dosya_adı.txt")])
        with open(self.dosyayi_ac, "r") as file:
            self.text_bolumu.delete(1.0, tk.END)
            self.text_bolumu.insert(tk.END, file.read())

    def dosya_kaydet(self):
        self.dosyayi_kaydet = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text Dosyası", "dosya_adı.txt")])
        with open(self.dosyayi_kaydet, "w") as file:
            file.write(self.text_bolumu.get(1.0, tk.END))
        


if __name__ == "__main__":
    pencere=tk.Tk()
    notepad=Notepad(pencere)
    pencere.mainloop()