import random 
import time 

class QuickSort:
    def __init__(self):
        self.liste = []

    def quick_sort(self, liste):
        if len(liste) <= 1:
            return liste
        pivot = liste[0] 
        left = [x for x in liste if x < pivot] 
        middle = [x for x in liste if x == pivot] 
        right = [x for x in liste if x > pivot]
        return self.quick_sort(left) + middle + self.quick_sort(right)

    def girdi_al(self):
        secim = input("Listeyi girmek için 'g', rastgele oluşturmak için 'r' tuşlayınız: ")
        if secim == 'r':
            n = int(input("Liste boyutunu girin: "))
            min_value = int(input("En küçük eleman değerini girin: "))
            max_value = int(input("En büyük eleman değerini girin: "))
            self.liste = [random.randint(min_value, max_value) for _ in range(n)]
        elif secim == 'g':
            self.liste = input("Listeyi virgülle ayırarak girin: ").split(',')
            self.liste = [int(x.strip()) for x in self.liste]
        else:
            print("Geçersiz giriş.")
            return

    def sirala_ve_yazdir(self):
        print("Girilen Liste:", self.liste)

        baslangic_zamani = time.time()
        siralanmis_liste = self.quick_sort(self.liste) 
        bitis_zamani = time.time()

        gecen_zaman = bitis_zamani - baslangic_zamani 
        print("Sıralandıktan Sonra:", siralanmis_liste)
        print("Sıralama işlemi {} saniye sürdü.".format(gecen_zaman))

def main():
    qs = QuickSort() 
    qs.girdi_al() 
    qs.sirala_ve_yazdir()

if __name__ == "__main__": 
    main()