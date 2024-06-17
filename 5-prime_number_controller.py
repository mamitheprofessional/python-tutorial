sayi=int(input("sayiyi girin : "))

if sayi > 1:
   for i in range(2,sayi):
       if (sayi % i) == 0:
           print(f"{sayi} asal degildir")
           break
   else:
       print(f"{sayi} asaldir")


else:
   print(f"{sayi} asal degil")