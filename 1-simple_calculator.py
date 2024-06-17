def topla(x,y):
    return x+y

def cikart(x,y):
    return x-y

def carp(x,y):
    return x*y

def bol(x,y):
    return x/y

  

print("yapilacak islemi seciniz: ")

print("1.toplama")

print("2.cikarma")

print("3.carpma")

print("4.bolme")

secim=input("birini seciniz: ")


if secim=="1":
    sonuc=topla(float(input("birinci sayi: ")), float(input("ikinci sayi: ")))
    print(sonuc)

if secim=="2":
    sonuc=cikart(float(input("birinci sayi: ")), float(input("ikinci sayi: ")))
    print(sonuc)

if secim=="3":
    sonuc=carp(float(input("birinci sayi: ")), float(input("ikinci sayi: ")))
    print(sonuc)

if secim=="4":
    sonuc=bol(float(input("birinci sayi: ")), float(input("ikinci sayi: ")))
    print(sonuc)