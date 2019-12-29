from itertools import combinations

N, M = map(int, input().split())
xy = [[] for _ in range(N)]
for _ in range(M):
    x, y = map(int, input().split())
    xy[x - 1].append(y - 1)
    xy[y - 1].append(x - 1)

ans = 0

for bit in range(1 << N):
    members = []
    for i in range(N):
        if bit & (1 << i):
            members.append(i)

    for a, b in combinations(members, 2):
        if not b in xy[a]:
            break
    else:
        ans = max(ans, bin(bit)[2:].count("1"))

print(ans)
