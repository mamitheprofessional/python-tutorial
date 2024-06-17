satis_list=[]
finans_list=[]
insan_kaynaklari_list=[]
pazarlama_list=[]
#maaşlar
maas_topla_s=0
maas_topla_f=0
maas_topla_i=0
maas_topla_p=0
#kişi sayısı için sayaç
satis_sayac = 0
finans_sayac = 0
insan_kaynaklari_sayac = 0
pazarlama_sayac = 0

class Kimlik:
    def __init__(self, ad, soyad, tc, dogum_tarihi):
        self.ad = ad
        self.soyad = soyad
        self.tc = tc
        self.dogum_tarihi = dogum_tarihi

class Personel(Kimlik):
    def __init__(self, ad, soyad, tc, dogum_tarihi, departman, giris_tarihi, maas):
        super().__init__(ad, soyad, tc, dogum_tarihi)
        self.__departman = departman
        self.__giris_tarihi = giris_tarihi
        self.__maas = maas
        self.personel_id = f"{self.ad[0]}{self.ad[1]}{self.__departman[-1]}{self.__departman[-2]}{self.__giris_tarihi.split('.')[0]}{self.__giris_tarihi.split('.')[1]}"

    # bunlar accesor
    def get_departman(self):
        return self.__departman
    
    def get_giris_gunu(self):
        return self.__giris_gunu
    
    def get_giris_ay(self):
        return self.__giris_ay
    
    def get_maas(self):
        return self.__maas
    

    # bunlarda mutator
    def set_departman(self, yeni_departman):
        self.__departman = yeni_departman

    def set_giris_tarihi(self, yeni_tarih):
        self.__giris_tarihi = yeni_tarih

    def set_maas(self,yeni_maas):
        self.__maas = yeni_maas

    def __str__(self): 
        return f"Personel Adı: {self.ad} {self.soyad}, Çalıştığı Departman: {self.__departman}, Giriş Tarihi: {self.__giris_tarihi}, Maaşı: {self.__maas}"
    
personel_sozlugu={}

def main():
    global maas_topla_s, maas_topla_f, maas_topla_i, maas_topla_p
    global satis_sayac, finans_sayac, insan_kaynaklari_sayac, pazarlama_sayac

    while True:
        ad = input("Personelin adını girin (Çıkmak için 'h' basın): ")
        if ad.lower() == 'h':
            print(f"Satış departmanı toplam maaş: {maas_topla_s}")
            print(f"Finans departmanı toplam maaş: {maas_topla_f}")
            print(f"Insan kaynakları toplam maaş: {maas_topla_i}")
            print(f"Pazarlama toplam maaş: {maas_topla_p}")

            toplam_maas=maas_topla_s + maas_topla_f + maas_topla_i + maas_topla_p
            print(f"tüm departmanlara ödenecek toplam maaş: {toplam_maas}")

            tum_maaslar = satis_list + finans_list + insan_kaynaklari_list + pazarlama_list
            en_dusuk_maas = min(tum_maaslar)
            en_yuksek_maas = max(tum_maaslar)
            print(f"En düşük maaş: {en_dusuk_maas}")
            print(f"En yüksek maaş: {en_yuksek_maas}")
            print(f"Maaş ortalaması: {toplam_maas / len(tum_maaslar)}")

            print(f"Satış Departmanında Çalışan Sayısı: {satis_sayac}")
            print(f"Finans Departmanında Çalışan Sayısı: {finans_sayac}")
            print(f"İnsan Kaynakları Departmanında Çalışan Sayısı: {insan_kaynaklari_sayac}")
            print(f"Pazarlama Departmanında Çalışan Sayısı: {pazarlama_sayac}")
            break

        soyad = input("Personelin soyadını girin: ")
        tc = input("Personelin TC kimlik numarasını girin: ")
        tarih = input("Doğum tarihini girin: ")
        giris_tarihi = input("Personel giriş tarihini gün.ay formatında girin: ")
        departman = input("Bulunduğu departman(satış, finans, insan kaynakları, pazarlama): ")
        maas = input("Personelin maaşını girin: ")
        if departman.lower() == 'satış':
            satis_list.append(int(maas))
            maas_topla_s = sum(satis_list)
            satis_sayac += 1
        elif departman.lower() == 'finans':
            finans_list.append(int(maas))
            maas_topla_f = sum(finans_list)
            finans_sayac += 1
        elif departman.lower() == 'insan kaynakları':
            insan_kaynaklari_list.append(int(maas))
            maas_topla_i = sum(insan_kaynaklari_list)
            insan_kaynaklari_sayac += 1
        elif departman.lower() == 'pazarlama':
            pazarlama_list.append(int(maas))
            maas_topla_p = sum(pazarlama_list)
            pazarlama_sayac += 1
        else:
            print("Geçersiz giriş. Lütfen tüm bilgileri tekrar giriniz.")

        

        yeni_personel = Personel(ad, soyad, tc, tarih, departman, giris_tarihi, maas) #özellikleri değişkene atadım
        personel_sozlugu[yeni_personel.personel_id] = yeni_personel #atadığım değişkenden personel id yi çekip key olarak atadım sonrada geri kalan herşeyi value olarak sözlüğe yazdım

main()

for personel_id, personel in personel_sozlugu.items():
    print(personel)
    print(personel_id)