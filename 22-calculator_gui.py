import tkinter as tk
from tkinter import messagebox

class HesapMakinesi:
    def __init__(self, master):
        self.master = master
        master.title("Hesap Makinesi")

        self.label = tk.Label(master, text="İşlemi seçiniz:")
        self.label.grid(row=0, columnspan=2)

        self.toplama_button = tk.Button(master, text="Toplama", command=self.toplama)
        self.toplama_button.grid(row=1, column=0)

        self.cikarma_button = tk.Button(master, text="Çıkarma", command=self.cikarma)
        self.cikarma_button.grid(row=1, column=1)

        self.carpma_button = tk.Button(master, text="Çarpma", command=self.carpma)
        self.carpma_button.grid(row=2, column=0)

        self.bolme_button = tk.Button(master, text="Bölme", command=self.bolme)
        self.bolme_button.grid(row=2, column=1)

        self.sayi1_label = tk.Label(master, text="Birinci sayı:")
        self.sayi1_label.grid(row=3, column=0)

        self.sayi1_entry = tk.Entry(master)
        self.sayi1_entry.grid(row=3, column=1)

        self.sayi2_label = tk.Label(master, text="İkinci sayı:")
        self.sayi2_label.grid(row=4, column=0)

        self.sayi2_entry = tk.Entry(master)
        self.sayi2_entry.grid(row=4, column=1)

        self.sonuc_label = tk.Label(master, text="Sonuç:")
        self.sonuc_label.grid(row=5, column=0)

        self.sonuc_value = tk.Label(master, text="")
        self.sonuc_value.grid(row=5, column=1)

    def topla(self, x, y):
        return x + y

    def cikart(self, x, y):
        return x - y

    def carp(self, x, y):
        return x * y

    def bol(self, x, y):
        if y == 0:
            messagebox.showerror("Hata", "Bölme işleminde ikinci sayı sıfır olamaz!")
            return None
        return x / y

    def toplama(self):
        self.hesapla(self.topla)

    def cikarma(self):
        self.hesapla(self.cikart)

    def carpma(self):
        self.hesapla(self.carp)

    def bolme(self):
        self.hesapla(self.bol)

    def hesapla(self, islem):
        try:
            x = float(self.sayi1_entry.get())
            y = float(self.sayi2_entry.get())
            sonuc = islem(x, y)
            if sonuc is not None:
                self.sonuc_value.config(text=str(sonuc))
        except ValueError:
            messagebox.showerror("Hata", "Lütfen geçerli sayılar girin!")

root = tk.Tk()

hesap_makinesi = HesapMakinesi(root)

root.mainloop()
