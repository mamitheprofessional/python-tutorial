def max_min_bul(lst):
    maxValue=lst[0]
    minValue=lst[0]
    for num in lst[1:]:
        if num>maxValue:
            maxValue=num
        elif num<minValue:
            minValue=num
    return maxValue,minValue

liste = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
maxValue,minValue=max_min_bul(liste)
print(f"max deger:{maxValue}")
print(f"min deger:{minValue}")


# or

liste = [1,2,3,4,5]

print(max(liste))

print(min(liste))