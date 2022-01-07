def selection_sort(list):
    for i in range(len(list)):
        max = i
        for j in range(i, len(list)):
            if list[j] > list[max]:
                max = j
        list[i], list[max] = list[max], list[i]


list = [5, 2, 4, 1, 3]
selection_sort(list)
print(list)
