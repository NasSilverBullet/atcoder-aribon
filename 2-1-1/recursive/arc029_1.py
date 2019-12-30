def f(arr):
    a, b = 0, 0

    for t in arr:
        if a > b:
            b += t
        else:
            a += t

    return max(a, b)


N = int(input())
ts = sorted([int(input()) for i in range(N)], reverse=True)
print(f(ts))
