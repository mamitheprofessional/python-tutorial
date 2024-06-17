# mukemmel sayilar dene ---> 6,28,496,8128

while True:
    sec = 1
    while sec == 1:
        sayi = int(input("Bir sayi giriniz: "))
        adet = 0
        for i in range(1, sayi):
            if sayi % i == 0:
                adet += i
        if adet == sayi:
            print(f"{sayi} mukemmel sayidir")
        else:
            print(f"{sayi} sayisi mukemmel sayi degildir")
        sec=int(input("devam etmek icin bir sayi girin yada cikmak icin 0 a basiniz: "))

    if sec == 0:
            break
