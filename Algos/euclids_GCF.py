def euclid_efficient(a, b):
    if b == 0:
        return a

    r = a % b

    return euclid_efficient(b, r)


def euclid(a, b):
    if a == b:
        return a

    m = max(a, b)
    s = min(a, b)

    return euclid(s, m - s)


print(euclid(30, 50))
