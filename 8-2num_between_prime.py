print("iki sayı arasındaki asal sayı kontolcusu")

sayi1=int(input("birinci sayiyi giriniz: "))
sayi2=int(input("ikinci sayiyi giriniz: "))

asal_mi = True

for sayi in range(sayi1, sayi2 + 1):
    for i in range(2, sayi):
        if sayi % i == 0:
            asal_mi = False
            break
    if asal_mi:
        print(f"{sayi} sayısı asaldır")
    asal_mi = True