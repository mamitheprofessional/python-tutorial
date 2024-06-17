
def merge_sort_part_1(listt):
    if len(listt)<=1:
        return listt
    else:
        middle=len(listt) // 2
        left_half=listt[:middle]
        right_half=listt[middle:]


        left_sorted = merge_sort_part_1(left_half)
        right_sorted = merge_sort_part_1(right_half)

        return merge_sort_part_2(left_sorted, right_sorted) #closure type


def merge_sort_part_2(left, right):
    result = []
    while left and right:
        if min(left) <= min(right):
            result.append(left.pop(left.index(min(left))))
        else:
            result.append(right.pop(right.index(min(right))))
    
    while left:
        result.append(left.pop(left.index(min(left))))
    while right:
        result.append(right.pop(right.index(min(right))))

    return result

listt = [24,45,12,34,7,65,98,4]
sorted_list = merge_sort_part_1(listt)
print("Sıralanmış dizi:", sorted_list)