def counting_sort(list, max):
    # create arr of max+1 indices, fill arr with how many times each index comes up in list-to-be-sorted
    # replace and sort list-to-be-sorted by iteration through arr
    index = [0] * (max + 1)
    for num in list:
        index[num] += 1

    count = 0
    for i, num in enumerate(index):
        for j in range(num):
            list[count] = i
            count += 1


list = [5, 2, 4, 1, 3]
counting_sort(list, 6)
print(list)
