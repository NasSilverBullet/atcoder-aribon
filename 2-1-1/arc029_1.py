N = int(input())
ts = []
for i in range(N):
    ts.append(int(input()))

ts.sort(reverse=True)

a, b = 0, 0

for i in range(N):
    if a > b:
        b += ts[i]
    else:
        a += ts[i]


print(max(a, b))
