def shell_sort(list):
    # k sort list with k = gap
    # implemented with insertion sort algo.
    # cut gap in half until gap = 1
    gap = len(list) // 2

    # gap is what optimizes shell sort, gap allows swapping of father spread indexes
    while gap > 0:
        for start in range(gap):
            gap_insertion_sort(list, start, gap)

        gap //= 2


def gap_insertion_sort(list, start, gap):
    for i in range(start + gap, len(list), gap):
        val = list[i]
        j = i - gap
        while j >= 0 and list[j] > val:
            list[j + gap] = list[j]
            j -= gap
        list[j + gap] = val


list = [5, 2, 4, 1, 3]
shell_sort(list)
print(list)
