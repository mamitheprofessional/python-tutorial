liste = [8, 5, 2, 9, 5, 6, 3]
n=len(liste)

def insertion_sort(liste):
    for i in range(1, n):
        anahtar = liste[i]
        j = i-1
        while j >=0 and anahtar < liste[j] :
            liste[j+1] = liste[j]
            j -= 1

        liste[j+1] = anahtar


insertion_sort(liste)
print(liste)