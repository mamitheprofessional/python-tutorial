original_list = [5, 2, 7, 14, 76, 34, 1, 64, 26, 15, 3, 4]
list = original_list.copy()

n = len(list)

def selection_sort(list):
    for i in range(n):
        min_index = i
        for j in range(i + 1, n):
            if list[j] < list[min_index]:
                min_index = j
        temp = list[i]
        list[i] = list[min_index]
        list[min_index] = temp


selection_sort(list)

print("Sıralanmış liste:", list) 
print("Orijinal liste:", original_list)