D, G = map(int, input().split())
arr = []
n = 0
for i in range(D):
    arr.append([int(c) for c in input().split()])
    n += arr[i][0]

ans = 1e9

for bit in range(1 << D):
    sum = 0
    num = 0
    rest_max = -1
    for i in range(D):
        if bit & 1 << i:
            sum += 100 * (i + 1) * arr[i][0] + arr[i][1]
            num += arr[i][0]
        else:
            rest_max = i

    if sum < G:
        p = 100 * (rest_max + 1)
        need = (G - sum + p - 1) // p
        if need >= arr[rest_max][0]:
            continue
        num += need
    ans = min(ans, num)

print(ans)
