import random

while True:
    minDeger = 50
    maxDeger = 250
    sayiTahmin = random.randint(minDeger, maxDeger)
    denemeHakki = 10
    hamle_sayisi=0
    hamle_sayisi+=1
    

    while denemeHakki > 0:
        skor=10-denemeHakki
        oyun = int(input("50 ile 250 arasindaki sayiyi tahmin edin: "))
        if oyun == sayiTahmin:
            print("Tebrikler, cevabi buldunuz!")
            print(f"{skor}. hamlede cevabi yakaladiniz")
            break
        elif oyun < 50 or oyun > 250:
            print("50 ile 250 araliginda kalin!!!")
        elif oyun < sayiTahmin:
            print("Yukari...")
        elif oyun > sayiTahmin:
            print("Asagi...")
        denemeHakki -= 1
        if denemeHakki == 0:
            print("Deneme hakkiniz bitti.")
            print("Dogru cevap:", sayiTahmin)
            break
        print("Kalan deneme hakki:", denemeHakki)

    devam_et = input("Oyun bitti. Tekrar oynamak istiyor musunuz? (Evet için 'e', Hayır için başka bir tuşa basın): ")
    if devam_et.lower() != 'e':
        print("Oyun bitti. İyi günler!")
        break