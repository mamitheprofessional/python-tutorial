liste = [8, 5, 2, 9, 5, 6, 3]

def quick_sort(liste):
    if len(liste) <= 1: 
        return liste
    else:
        pivot = liste[0]
        less_than_pivot = [x for x in liste[1:] if x <= pivot] #list compherension
        greater_than_pivot = [x for x in liste[1:] if x > pivot]
        return quick_sort(less_than_pivot) + [pivot] + quick_sort(greater_than_pivot)

sirala = quick_sort(liste)

print("Sıralanmış dizi:", sirala)


# or just call .sort() function
deneme = [2,45,25,89,3,67,43,1]
deneme.sort()
print(deneme)