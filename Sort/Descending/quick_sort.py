def quick_sort(list):
    quick_sort_helper(list, 0, len(list) - 1)


def quick_sort_helper(list, start, end):
    if start < end:
        pivot = partition(list, start, end)
        quick_sort_helper(list, start, pivot - 1)
        quick_sort_helper(list, pivot + 1, end)


def partition(list, start, end):
    # choose last element as pivot

    pivot = list[end]

    left = start
    right = end - 1

    done = False

    while not done:
        while left <= right and list[left] >= pivot:
            left += 1

        while list[right] <= pivot and left <= right:
            right -= 1

        if left > right:
            done = True
        else:
            list[left], list[right] = list[right], list[left]

    list[left], list[end] = list[end], list[left]

    return left


list = [5, 2, 4, 1, 3]
quick_sort(list)
print(list)
