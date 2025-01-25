def sort_descending(arr):
    for i in range(len(arr)):
        for j in range(0, len(arr) - i - 1):
            if arr[j] < arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr
my_list = [8, 3, 1, 6, 7, 2]
sorted_list = sort_descending(my_list)
print("Sorted List:", sorted_list)