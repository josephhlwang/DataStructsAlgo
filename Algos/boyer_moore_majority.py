def boyer_moore(arr):

    # boyer_moore finds the majority element in arr
    # maj element appears more than n/2
    # thus the number of maj elements will always make count positive

    count = 0

    for num in arr:
        if count == 0:
            maj = num
            count = 1
        elif num == maj:
            count += 1
        else:
            count -= 1

    return maj


nums = [1, 8, 7, 4, 1, 2, 2, 2, 2, 2, 2]
print(boyer_moore(nums))
