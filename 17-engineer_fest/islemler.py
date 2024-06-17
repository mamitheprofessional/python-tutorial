katilimci_isim=[]
katilimci_soyisim=[]
katilimci_dogum_tarihi=[]
festivale_katilim_tarihi=[]
katilimcinin_sehri=[]
katilimci_id=[]

def yeni_katilimci():
    try:
        print("Yeni katılımcının bilgilerini giriniz:")
        isim = input("Katılımcı isim: ")
        soyisim=input("Katılımcı soyisim: ")
        dogum_tarihi_ayi = int(input("Doğduğunuz ayı giriniz(1-12): "))  # String olarak alıyoruz, çünkü dosyaya yazarken string olarak yazacağız
        katilim_tarihi = input("Katılım tarihi: ")  # Aynı nedenle string olarak alıyoruz
        sehir = input("Katılımcının şehri: ")
        id = input("id giriniz: ")

        if not id:
            raise ValueError("ID boş olamaz") #özellikle id girilmemiş ise raise
        
        if dogum_tarihi_ayi < 1 or dogum_tarihi_ayi > 12:
            raise ValueError
        dogum_tarihi_ayi = str(dogum_tarihi_ayi)
        with open("MuhendisFest2024-katılımcılar.txt", "a") as dosya:  
            dosya.write(f"{isim}, {soyisim}, {dogum_tarihi_ayi}, {katilim_tarihi}, {sehir}, {id}\n")

        # Diğer listelere bilgileri ekliyoruz
        katilimci_isim.append(isim)
        katilimci_soyisim.append(soyisim)
        katilimci_dogum_tarihi.append(dogum_tarihi_ayi)
        festivale_katilim_tarihi.append(katilim_tarihi)
        katilimcinin_sehri.append(sehir)
        katilimci_id.append(id)

        # Katılımcının bilgilerini bir listede toplayıp döndürme
        return [isim, soyisim, dogum_tarihi_ayi, katilim_tarihi, sehir, id]

    except :  
        print("Hatalı giriş yaptınız.")  
        return None 
    

def katilimci_getir():
    try:
        id_al = input("Katılımcı ID'sini giriniz: ")
        with open("MuhendisFest2024-katılımcılar.txt", "r") as dosya:
            for satir in dosya:
                bilgi = satir.lower().strip().split(", ")
                if bilgi[-1] == id_al:
                    print(f"ID={bilgi[-1]}, İsim={bilgi[0]}, Soyisim={bilgi[1]} Doğum tarihi={bilgi[2]}, Festival katılım tarihi={bilgi[3]}, Şehir={bilgi[4]}")

    except FileNotFoundError:
        print("Dosya bulunamadı.")



def girisKodu_sifre_uret():
    try:
        with open("MuhendisFest2024-katılımcılar.txt", "r") as dosya:
            for satir in dosya:
                bilgi = satir.strip().split(", ")
                isim_ilk_harf = bilgi[0][0]  # İsimin ilk harfi
                soyisim_son_harf = bilgi[1][-1]  # Soyismin son harfi
                katilimci_id_ilk = bilgi[-1][0]  # Katılımcı ID'si
                katilimci_id_ikinci=bilgi[-1][1]
                islem = int(bilgi[-1]) * int(bilgi[2])  # Doğum tarihi ile ID çarpımı
                # Giriş kodunu oluştur
                giris_kodu = isim_ilk_harf + soyisim_son_harf + katilimci_id_ilk +katilimci_id_ikinci +str(islem) #Islemi str olarak bastırıcaz
                print(f"Giriş Kodu/Sifre: {giris_kodu}")

    except FileNotFoundError:
        print("Dosya bulunamadı.")