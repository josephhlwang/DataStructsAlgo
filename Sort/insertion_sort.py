def insertion_sort(list):
    # for each element, shuffle the list up until value bigger than next element, insert
    for i in range(1, len(list)):  # 1 because assume first sublist sorted
        val = list[i]
        j = i - 1
        while j >= 0 and list[j] > val:
            list[j + 1] = list[j]
            j -= 1
        list[j + 1] = val


list = [5, 2, 4, 1, 3]
insertion_sort(list)
print(list)
