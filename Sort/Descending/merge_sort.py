def merge_sort(list):
    if len(list) > 1:
        split = len(list) // 2

        l = list[:split]
        r = list[split:]
        merge_sort(l)
        merge_sort(r)

        i = j = k = 0

        while i < len(l) and j < len(r):
            if l[i] > r[j]:
                list[k] = l[i]
                i += 1
            else:
                list[k] = r[j]
                j += 1
            k += 1

        while i < len(l):
            list[k] = l[i]
            i += 1
            k += 1

        while j < len(r):
            list[k] = r[j]
            j += 1
            k += 1


list = [5, 2, 1, 5, 4, 1, 3]
merge_sort(list)
print(list)
