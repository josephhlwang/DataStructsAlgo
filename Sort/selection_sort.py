def selection_sort(list):
    # for each index, p valuesselection minimum from rest of list and swa
    for i in range(len(list)):
        min = i
        for j in range(i + 1, len(list)):
            if list[j] < list[min]:
                min = j
        list[min], list[i] = list[i], list[min]


list = [5, 2, 4, 1, 3]
selection_sort(list)
print(list)
