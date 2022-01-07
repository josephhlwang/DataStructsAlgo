def quick_sort(list):
    # start with 0 and last index
    quick_sort_helper(list, 0, len(list) - 1)


def quick_sort_helper(list, first, last):
    if first < last:
        # partition will create pivot where pivot is in the correct position
        # items to left of pivot, < pivot
        # items to right of pivor, > pivot
        split_point = partition(list, first, last)
        quick_sort_helper(list, first, split_point - 1)
        quick_sort_helper(list, split_point + 1, last)


def partition(list, first, last):
    # assume first val is pivot
    pivot_val = list[first]

    # left is index of item greater than pivot
    # right is index of item less than pivot
    # left and right will be swapped
    left = first + 1
    right = last

    done = False

    while not done:
        # find left val
        while left <= right and list[left] <= pivot_val:
            left += 1
        # find right val
        while list[right] >= pivot_val and left <= right:
            right -= 1

        # if list partitioned
        if right < left:
            done = True
        # otherwise swap
        else:
            list[left], list[right] = list[right], list[left]

    # we return swap and return right val since pivot_val on left side
    list[first], list[right] = list[right], list[first]
    return right


list = [5, 2, 4, 1, 3]
quick_sort(list)
print(list)
