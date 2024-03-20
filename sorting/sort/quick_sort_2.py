def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr)//2]
    low_arr, equal_arr, high_arr = [], [], []
    for num in arr:
        if num < pivot:
            low_arr.append(num)
        elif num == pivot:
            equal_arr.append(num)
        else:
            high_arr.append(num)
    return quick_sort(low_arr) + equal_arr + quick_sort(high_arr)


array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]
print(quick_sort(array))
