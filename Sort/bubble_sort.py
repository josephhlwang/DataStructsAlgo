def bubble_sort(list):
    # for each element, swap with next element if current element bigger than next element
    for i in range(len(list)):  # -1 since last element is already sorted
        for j in range(0, len(list) - i - 1):
            if list[j] > list[j + 1]:
                list[j], list[j + 1] = list[j + 1], list[j]


list = [5, 2, 4, 1, 3]
bubble_sort(list)
print(list)
