def binary_search(sorted_list, key):
    # init left and right index
    l = 0
    r = len(sorted_list) - 1

    while l <= r:
        # find midpoint
        mid = (l + r) // 2
        val = sorted_list[mid]

        if val == key:
            return mid
        # key in upper array
        elif val < key:
            l = mid + 1
        # key in lower arr
        else:
            r = mid - 1

    return -1


# sorted_list = [1, 3, 5, 7, 9, 12]
# print(binary_search(sorted_list, -1))
