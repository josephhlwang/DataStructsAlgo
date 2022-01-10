def kadane(arr):
    # kadanes algo finds the max sum of a subarray

    # if list has all negative values, return greatest
    maximum = max(arr)
    if maximum <= 0:
        return maximum

    # max so far keeps track of the global max
    max_so_far = 0
    # max here keeps track of the non-negative max of current iteration
    max_here = 0

    for num in arr:
        # add num to current max
        max_here += num
        # if negative, set to 0, other wise it can be added to next num
        max_here = max(max_here, 0)
        # check if its greater than global
        max_so_far = max(max_so_far, max_here)

    return max_so_far


arr = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
print(kadane(arr))
