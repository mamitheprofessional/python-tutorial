import dis_cephe
import ic_cephe

bina_maliyet_ortalama = []

while True:
    devam = ' ' 

    while devam.lower() == ' ':
        print("Binanın konumunu belirtiniz")
        konum = int(input("Deniz kenarı ise '1', şehir merkezi ise '2', taşra ise '3' tuşuna basınız: "))

        print("Binanın dış cephe stilini belirtiniz") 
        dis_cephe_stil = int(input("Modern için '1', geleneksel için '2', eski tip için '3' tuşuna basınız: "))

        puan = int(input("Binanın dış cephesini 1-10 arasında puanlayınız: "))

        print("binanin en ve boy unu metre cinsinden giriniz")
        en=int(input("en: "))
        boy=int(input("boy: "))
        print("ic mekan tasarimi nasil olsun ?")
        ic_mekan_tasarimi=int(input("luks icin '1' guzel icin '2' idare eder icin '3' tusuna basiniz: "))


        ic_mekan_fiyat = ic_cephe.ic_mekan_fiyat_hesabi(en,boy,ic_mekan_tasarimi)
        dis_cephe_fiyat = dis_cephe.puanlama(puan, konum, dis_cephe_stil)

        print() 

        bina_maliyeti = dis_cephe_fiyat * 40 + ic_mekan_fiyat * 60 
        bina_maliyet_ortalama.append(bina_maliyeti)
        print(bina_maliyet_ortalama)

        print(f"binanın maliyeti: {round(bina_maliyeti, 2)}")

         

        devam = input("Çıkış yapmak için 'H/h' tuşuna basınız veya tekrar hesaplama için herhangi bir tuşa basınız: ")
        if devam.lower() == ' ':
            break

    toplam = sum(bina_maliyet_ortalama) 
    ortalama = toplam / len(bina_maliyet_ortalama)
    print(f"Ortalama bina maliyeti: {round(ortalama, 2)}")

    if devam.lower() == 'h':
            break