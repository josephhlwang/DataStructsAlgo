def quick_select(arr, k):
    # quick select selects the kth smallest element
    return quick_select_helper(arr, 0, len(arr) - 1, k)


def quick_select_helper(arr, first, last, k):
    if last > first:
        # partially sort arr
        # returned pivot is in sorted position
        pivot = partition(arr, first, last)

        # return val if pivot is k
        if pivot == k:
            return arr[pivot]
        # k on lower side
        elif k < pivot:
            return quick_select_helper(arr, first, pivot - 1, k)
        # k on upper side
        else:
            return quick_select_helper(arr, pivot + 1, last, k)


def partition(arr, first, last):
    pivot = arr[first]

    left = first + 1
    right = last

    done = False

    while not done:
        while left <= right and arr[left] <= pivot:
            left += 1
        while arr[right] >= pivot and left <= right:
            right -= 1

        if left > right:
            done = True
        else:
            arr[right], arr[left] = arr[left], arr[right]

    arr[first], arr[right] = arr[right], arr[first]
    return right


nums = [7, 4, 6, 3, 9, 1]
k = 2

print(quick_select(nums, k))
print(nums)
