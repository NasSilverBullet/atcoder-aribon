N, M = map(int, input().split())
reach = [[] for _ in range(N)]
for i in range(M):
    u, v = map(lambda x: int(x) - 1, input().split())
    reach[u].append(v)
    reach[v].append(u)

check = [False] * N
pre = [False] * N
ans = 0
for i in range(N):
    flag = True
    if not check[i]:
        continue
    check[i] = True
    stack = [i]
    while len(stack) > 0:
        tmp = stack.pop()
        tmp_list = reach[tmp]
        for j in tmp_list:
            if j == pre[tmp]:
                continue
            if not check[j]:
                flag = False
                stack = []
                break
            check[j] = True
            pre[j] = tmp
            stack.append(j)

    if flag:
        ans += 1

print(ans)
