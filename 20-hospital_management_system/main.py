from personel import Personel
from doktor import Doktor
from hemsire import Hemsire
from hasta import Hasta
import pandas as pd

#pd.set_option('display.max_columns', None)

personeller = [
            Personel(1,"ali", "velioglu", "hasta bakıcı", 6000),
            Personel(2, "ayşe", "fatmaoglu", "aşcı", 8000)
    ]

doktorlar = [
            Doktor(3, "mucize", "doktoroglu", "gözcü", 7000, "göz doktoru", 10, "new york devlet hastanesi"),
            Doktor(4, "hekim", "hekimoglu", "kardiyolog", 6000, "kalp doktoru", 15, "bakırçay üniversite hastanesi"),
            Doktor(5, "fikret", "tıpçıoğlu", "kbb", 8000, "kbb doktoru", 20, "bakırköy hastanesi")
]

hemsireler = [
            Hemsire(6, "Zeynep", "Kara", "Pediatri", 7500, 40, "Çocuk Sağlığı", "City Hospital"),
            Hemsire(7, "Hülya", "Çelik", "Acil", 6500, 35, "Acil Durumlar", "State Hospital"),
            Hemsire(8, "Selin", "Kaya", "Dahiliye", 6000, 45, "Genel Sağlık", "State Hospital")
]

hastalar = [
            Hasta(1, "Berk", "Koç", 1990, "Gribal Enfeksiyon", "İlaç Tedavisi"),
            Hasta(2, "Selma", "Şahin", 1988, "Kırık", "Alçı ve Dinlenme"),
            Hasta(3, "Okan", "Yılmaz", 2000, "Migren", "İlaç Tedavisi")
]

for doktor in doktorlar:
    doktor.maas_arttir(0.10)

for hemsire in hemsireler:
    hemsire.maas_arttir(0.07)

personel_data = []

for person in personeller + doktorlar + hemsireler:
    person_data = {
        "ID": person.get_personel_no(),
        "Ad": person.get_ad(),
        "Soyad": person.get_soyad(),
        "Tür": "Personel",
        "Departman": person.get_departman(),
        "Maaş": person.get_maas(),
        "Hastane": None,
        "Uzmanlık": None,
        "Çalışma Saati": None,
        "Sertifika": None,
        "Deneyim Yılı": None
    }

    if isinstance(person, Doktor):
        person_data["Tür"] = "Doktor"
        person_data["Uzmanlık"] = person.get_uzmanlik()
        person_data["Hastane"] = person.get_hastane()
        person_data["Deneyim Yılı"] = person.get_deneyim_yili()
    elif isinstance(person, Hemsire):
        person_data["Tür"] = "Hemşire"
        person_data["Çalışma Saati"] = person.get_calisma_saati()
        person_data["Sertifika"] = person.get_sertifika()
        person_data["Hastane"] = person.get_hastane()
    
    personel_data.append(person_data)

df_personel_data = pd.DataFrame(personel_data)
df_personel_data.fillna(0, inplace=True)

# Hasta verilerini oluşturma
hasta_data = []

for hasta_kisi in hastalar:
    hasta_bilgileri = {
        "ID": hasta_kisi.get_hasta_no(),
        "Ad": hasta_kisi.get_ad(),
        "Soyad": hasta_kisi.get_soyad(),
        "Tür": "Hasta",
        "Doğum Tarihi": hasta_kisi.get_dogum_tarihi(),
        "Hastalık": hasta_kisi.get_hastalik(),
        "Tedavi": hasta_kisi.tedavi_suresi()
    }
    hasta_data.append(hasta_bilgileri)

df_hasta_data = pd.DataFrame(hasta_data)
df_hasta_data.fillna(0, inplace=True)


print("\n\nPersonel DataFrame:")
print(df_personel_data)

print("\n\nHasta DataFrame:")
print(df_hasta_data)

# Uzmanlık alanına göre doktor sayısı
uzman_hekim_sayisi = df_personel_data[df_personel_data["Uzmanlık"] != 0].groupby("Uzmanlık").size()
print("\nUzmanlık alanına göre doktor sayısı: ")
print(uzman_hekim_sayisi)

# 5 yıldan fazla deneyimi olan doktorlar
df_deneyim_filtresi = df_personel_data[df_personel_data["Deneyim Yılı"] > 5]
print("\n5 yıldan fazla deneyimi olan doktorlar: ")
print(df_deneyim_filtresi)

# Hasta adına göre alfabetik sırala
df_hasta_adı_sırala = df_hasta_data.sort_values(by="Ad")
print("\nHasta adına göre alfabetik sıra: ")
print(df_hasta_adı_sırala)

# Maaşı 7000 üzeri olan personeller
df_personel_maas_filtresi = df_personel_data[df_personel_data["Maaş"] >= 7000]
print("\nMaaşı 7000 üzeri olan personeller: ")
print(df_personel_maas_filtresi)

# 1990 ve sonrası doğan hastalar
df_hasta_yas_filtresi = df_hasta_data[df_hasta_data["Doğum Tarihi"] >= 1990]
print("\n1990 ve sonrasında doğan hastalar: ")
print(df_hasta_yas_filtresi)


df_yeni = pd.concat([df_personel_data[["Ad", "Soyad", "Departman", "Maaş", "Uzmanlık", "Deneyim Yılı"]],
                     df_hasta_data[["Ad", "Soyad", "Hastalık", "Tedavi"]]])


print("\nYeni DataFrame:")
print(df_yeni)



df_yeni.to_excel('birlesik_data.xlsx')


