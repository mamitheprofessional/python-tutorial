from islemler import yeni_katilimci, katilimci_getir, girisKodu_sifre_uret

bilgi=[]

def menu_goruntule():
    

    while True:
        secim = input("Seçiminizi yapınız: ")
        if secim.lower() == 'e':
            yeni_katilimci()
            break
        elif secim.lower() == 'l':
            katilimci_getir()
            break
        elif secim.lower() == 'g':
            girisKodu_sifre_uret()
            break
        elif secim.lower() == 'ç':
            print("Iyi günler")
            return
        else:
            print("Geçersiz seçim. Lütfen 'e', 'l', 'g' veya 'ç' tuşlarından birini seçiniz.")

def main():
    print("Festival kayıt programında hoşgeldiniz.")
    print("Yeni biri eklemek için 'e' tuşuna basınız.")
    print("Listeyi görüntülemek için 'l' tuşuna basınız.")
    print("giriş kodu görüntülemek için 'g' tuşuna basınız.")
    print("Çıkış yapmak için 'ç' tuşuna basınız")
    menu_goruntule()
    
main()