def faktoriyel(n):
    if n==0:
        return 1
    else:
        return n*faktoriyel(n-1)
    

print("faktoriyel hesaplayici")
print()
sayi=int(input("hesaplanacak sayiyi giriniz: "))
print(faktoriyel(sayi))