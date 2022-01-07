def counting_sort(list, max):
    count = (max + 1) * [0]
    for num in list:
        count[num] += 1

    index = 0
    for i in range(max, -1, -1):
        for times in range(count[i]):
            list[index] = i
            index += 1


list = [5, 2, 4, 1, 3]
counting_sort(list, 6)
print(list)
