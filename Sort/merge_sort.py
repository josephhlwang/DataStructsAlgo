def merge_sort(list):
    # split list into two sublists, sort those, then merge them
    # merge sublists by iterating through both lists
    if len(list) > 1:
        mid = len(list) // 2
        l = list[:mid]
        r = list[mid:]
        merge_sort(l)
        merge_sort(r)

        # merge
        # i tracks left
        # j track right
        # k tracks main array
        i = j = k = 0

        while i < len(l) and j < len(r):
            # l smaller
            if l[i] < r[j]:
                list[k] = l[i]
                i += 1
            # r smaller
            else:
                list[k] = r[j]
                j += 1
            k += 1

        while i < len(l):
            # l array leftover
            list[k] = l[i]
            i += 1
            k += 1

        while j < len(r):
            # r array leftover
            list[k] = r[j]
            j += 1
            k += 1


list = [5, 2, 4, 1, 3]
merge_sort(list)
print(list)
