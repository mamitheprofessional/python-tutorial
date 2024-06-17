original_list = [5, 2, 7, 14, 76, 34, 1, 64, 26, 15, 3, 4]
list = original_list.copy()

n = len(list)

def bubble_sort(list):
    for _ in range(n): 
        for j in range(0, n-1): 
            if list[j] < list[j+1]: 
                temp = list[j]
                list[j] = list[j+1]
                list[j+1] = temp

bubble_sort(list) 

print("Sıralanmış liste:", list) 
print("Orijinal liste:", original_list)