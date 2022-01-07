def bubble_sort(list):
    for i in range(len(list)):
        for j in range(len(list) - i - 1):
            if list[j] < list[j + 1]:
                list[j], list[j + 1] = list[j + 1], list[j]


list = [5, 2, 4, 1, 3]
bubble_sort(list)
print(list)
