def countingSort(a):
    s = len(a)
    o = [0] * s
    c = [0] * 10
    for i in range(0, s):
        c[a[i]] += 1
    for i in range(1, 10):
        c[i] += c[i - 1]
    i = s - 1
    while i >= 0:
        o[c[a[i]] - 1] = a[i]
        c[a[i]] -= 1
        i -= 1
    for i in range(0, s):
        a[i] = o[i]

d = [4, 2, 2, 8, 3, 3, 1]
countingSort(d)
print(d)