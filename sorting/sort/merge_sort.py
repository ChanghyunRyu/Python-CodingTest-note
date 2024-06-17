arr = [7, 5, 9, 0, 3, 1, 6, 2, 9, 1, 4, 8, 0, 5, 2]


def merge_list(left, right):
    result = []
    while left and right:
        if left[0] > right[0]:
            result.append(right[0])
            right = right[1:]
        else:
            result.append(left[0])
            left = left[1:]
    result.extend([*left, *right])
    return result


def merge_sort(arr_list):
    if len(arr_list) == 1:
        return arr_list
    mid = len(arr_list)//2
    left = merge_sort(arr_list[:mid])
    right = merge_sort(arr_list[mid:])
    return merge_list(left, right)


print(merge_sort(arr))
